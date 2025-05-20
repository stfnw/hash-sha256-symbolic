#!/usr/bin/python3

# SPDX-FileCopyrightText: 2011 Original C code: IETF Trust and the persons identified as the document authors. All rights reserved.
# SPDX-FileCopyrightText: 2025 Rewrite in python: stfnw
#
# SPDX-License-Identifier: BSD-3-Clause


import z3  # type: ignore
from typing import TypeVar


def main() -> None:
    z3.set_param(verbose=2)

    # Sanity check that the symbolic implementation is correct by passing
    # fully determined input.
    # assert (
    #     "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
    #     == sha256hash_(b"Hello World")
    # )
    # assert (
    #     "d25f01257c9890622d78cf9cf3362457ef75712bd187ae33b383f80d618d0f06"
    #     == sha256hash_(b"1" * 10000)
    # )

    data = [z3.BitVec("data" + str(i), 8) for i in range(SHA256HashSize + 1)]
    print(
        f"[+] Constructing U8 array of {len(data)} symbolic bytes "
        + "and the symbolic hash computation for it"
    )
    hash = sha256hash(data)

    print("[+] Adding additional constraints to the solver")

    # for i in range(SHA256HashSize):
    #     s = z3.Solver()
    #
    #     # Find message whose i-th hash-byte is null.
    #     s.add(hash[i] == make_u8(0))
    #
    #     print("[+] Checking for boolean satisfiability")
    #     if s.check() == z3.sat:
    #         print("[+] Found valid model")
    #
    #         m = s.model()
    #         dataval = [m.evaluate(d) for d in data]
    #         hashval = [m.evaluate(h) for h in hash]
    #
    #         print(f"    Data hex:    {hex_from_bv(dataval)}")
    #         print(f"    SHA256 hash: {hex_from_bv(hashval)}")

    s = z3.Solver()

    i = 0

    # Find message whose i-th input and hash nibble have the same value.
    # s.add(z3.Extract(4 - 1, 0, hash[i]) == z3.Extract(4 - 1, 0, data[i]))  # Even
    # s.add(z3.Extract(8 - 1, 4, hash[i]) == z3.Extract(8 - 1, 4, data[i]))  # Odd

    # Find message whose i-th input and hash byte have the same value.
    # s.add(hash[i] == data[i])

    # Find message whose i-th and (i+1)-th hash byte have the same value.
    # s.add(hash[i] == hash[i+1])

    # Find message where i-th hash-byte and its mirror have the same value.
    s.add(hash[i] == hash[SHA256HashSize - 1 - i])

    print("[+] Checking for boolean satisfiability")
    if s.check() == z3.sat:
        print("[+] Found valid model")

        m = s.model()
        dataval = [m.evaluate(d) for d in data]
        hashval = [m.evaluate(h) for h in hash]

        print(f"    Data hex:    {hex_from_bv(dataval)}")
        print(f"    SHA256 hash: {hex_from_bv(hashval)}")


type U8 = z3.BitVecRef
type U32 = z3.BitVecRef


def make_u8(n: int) -> U8:
    return z3.BitVecVal(n, 8)


def make_u32(n: int) -> U32:
    return z3.BitVecVal(n, 32)


def sha256hash(val: list[U8]) -> list[U8]:
    m = SHA256()
    m.SHA256Input(val)
    digest = m.SHA256Result()
    return [z3.simplify(b) for b in digest]


# Use symbolic version with fixed fully determined input for checking that the
# implementation is correct.
def sha256hash_(val: bytes) -> str:
    m = SHA256()
    m.SHA256Input(bv_from_bytes(val))
    digest = m.SHA256Result()
    return hex_from_bv(digest)


def bv_from_bytes(data: bytes) -> list[U8]:
    return [make_u8(b) for b in data]


def bytes_from_bv(data: list[U8]) -> bytes:
    return bytes([z3.simplify(b).as_long() for b in data])


def hex_from_bv(data: list[U8]) -> str:
    bs = bytes_from_bv(data)
    return bytes.hex(bs)


SHA256_Message_Block_Size = 64
SHA256HashSize = 32
SHA256HashSizeBits = 256


def SHA256_SIGMA0(word: U32) -> U32:
    return (
        z3.RotateRight(word, make_u32(2))
        ^ z3.RotateRight(word, make_u32(13))
        ^ z3.RotateRight(word, make_u32(22))
    )


def SHA256_SIGMA1(word: U32) -> U32:
    return (
        z3.RotateRight(word, make_u32(6))
        ^ z3.RotateRight(word, make_u32(11))
        ^ z3.RotateRight(word, make_u32(25))
    )


def SHA256_sigma0(word: U32) -> U32:
    return (
        z3.RotateRight(word, make_u32(7))
        ^ z3.RotateRight(word, make_u32(18))
        ^ z3.LShR(word, make_u32(3))
    )


def SHA256_sigma1(word: U32) -> U32:
    return (
        z3.RotateRight(word, make_u32(17))
        ^ z3.RotateRight(word, make_u32(19))
        ^ z3.LShR(word, make_u32(10))
    )


def SHA_Ch(x: U32, y: U32, z: U32) -> U32:
    return (x & y) ^ ((~x) & z)


def SHA_Maj(x: U32, y: U32, z: U32) -> U32:
    return (x & y) ^ (x & z) ^ (y & z)


def SHA_Parity(x: U32, y: U32, z: U32) -> U32:
    return x ^ y ^ z


class SHA256:

    def __init__(self) -> None:
        self.Intermediate_Hash: list[U32] = [
            make_u32(0x6A09E667),
            make_u32(0xBB67AE85),
            make_u32(0x3C6EF372),
            make_u32(0xA54FF53A),
            make_u32(0x510E527F),
            make_u32(0x9B05688C),
            make_u32(0x1F83D9AB),
            make_u32(0x5BE0CD19),
        ]
        self.Length: int = 0
        self.Message_Block_Index: int = 0
        self.Message_Block: list[U8] = [
            make_u8(0) for _ in range(SHA256_Message_Block_Size)
        ]
        self.Computed: bool = False

    def SHA256ProcessMessageBlock(self) -> None:
        K: list[U32] = [
            make_u32(0x428A2F98),
            make_u32(0x71374491),
            make_u32(0xB5C0FBCF),
            make_u32(0xE9B5DBA5),
            make_u32(0x3956C25B),
            make_u32(0x59F111F1),
            make_u32(0x923F82A4),
            make_u32(0xAB1C5ED5),
            make_u32(0xD807AA98),
            make_u32(0x12835B01),
            make_u32(0x243185BE),
            make_u32(0x550C7DC3),
            make_u32(0x72BE5D74),
            make_u32(0x80DEB1FE),
            make_u32(0x9BDC06A7),
            make_u32(0xC19BF174),
            make_u32(0xE49B69C1),
            make_u32(0xEFBE4786),
            make_u32(0x0FC19DC6),
            make_u32(0x240CA1CC),
            make_u32(0x2DE92C6F),
            make_u32(0x4A7484AA),
            make_u32(0x5CB0A9DC),
            make_u32(0x76F988DA),
            make_u32(0x983E5152),
            make_u32(0xA831C66D),
            make_u32(0xB00327C8),
            make_u32(0xBF597FC7),
            make_u32(0xC6E00BF3),
            make_u32(0xD5A79147),
            make_u32(0x06CA6351),
            make_u32(0x14292967),
            make_u32(0x27B70A85),
            make_u32(0x2E1B2138),
            make_u32(0x4D2C6DFC),
            make_u32(0x53380D13),
            make_u32(0x650A7354),
            make_u32(0x766A0ABB),
            make_u32(0x81C2C92E),
            make_u32(0x92722C85),
            make_u32(0xA2BFE8A1),
            make_u32(0xA81A664B),
            make_u32(0xC24B8B70),
            make_u32(0xC76C51A3),
            make_u32(0xD192E819),
            make_u32(0xD6990624),
            make_u32(0xF40E3585),
            make_u32(0x106AA070),
            make_u32(0x19A4C116),
            make_u32(0x1E376C08),
            make_u32(0x2748774C),
            make_u32(0x34B0BCB5),
            make_u32(0x391C0CB3),
            make_u32(0x4ED8AA4A),
            make_u32(0x5B9CCA4F),
            make_u32(0x682E6FF3),
            make_u32(0x748F82EE),
            make_u32(0x78A5636F),
            make_u32(0x84C87814),
            make_u32(0x8CC70208),
            make_u32(0x90BEFFFA),
            make_u32(0xA4506CEB),
            make_u32(0xBEF9A3F7),
            make_u32(0xC67178F2),
        ]

        W: list[U32] = [make_u32(0) for _ in range(64)]

        for t in range(0, 16):
            W[t] |= z3.ZeroExt(24, self.Message_Block[t * 4 + 0]) << (3 * 8)
            W[t] |= z3.ZeroExt(24, self.Message_Block[t * 4 + 1]) << (2 * 8)
            W[t] |= z3.ZeroExt(24, self.Message_Block[t * 4 + 2]) << (1 * 8)
            W[t] |= z3.ZeroExt(24, self.Message_Block[t * 4 + 3]) << (0 * 8)

        for t in range(16, 64):
            W[t] = (
                SHA256_sigma1(W[t - 2])
                + W[t - 7]
                + SHA256_sigma0(W[t - 15])
                + W[t - 16]
            )

        A, B, C, D, E, F, G, H = self.Intermediate_Hash

        for t in range(64):
            temp1: U32 = H + SHA256_SIGMA1(E) + SHA_Ch(E, F, G) + K[t] + W[t]
            temp2: U32 = SHA256_SIGMA0(A) + SHA_Maj(A, B, C)
            H = G
            G = F
            F = E
            E = D + temp1
            D = C
            C = B
            B = A
            A = temp1 + temp2

        self.Intermediate_Hash[0] += A
        self.Intermediate_Hash[1] += B
        self.Intermediate_Hash[2] += C
        self.Intermediate_Hash[3] += D
        self.Intermediate_Hash[4] += E
        self.Intermediate_Hash[5] += F
        self.Intermediate_Hash[6] += G
        self.Intermediate_Hash[7] += H

        self.Intermediate_Hash = [z3.simplify(el) for el in self.Intermediate_Hash]

        self.Message_Block_Index = 0

    def SHA256Input(self, message_array: list[U8]) -> None:
        assert len(message_array) != 0
        assert not self.Computed

        for i in range(len(message_array)):
            self.Message_Block[self.Message_Block_Index] = message_array[i]
            self.Message_Block_Index += 1

            self.Length += 8
            if self.Message_Block_Index == SHA256_Message_Block_Size:
                self.SHA256ProcessMessageBlock()

    def SHA256PadMessage(self, Pad_Byte: U8) -> None:
        if self.Message_Block_Index >= (SHA256_Message_Block_Size - 8):
            self.Message_Block[self.Message_Block_Index] = Pad_Byte
            self.Message_Block_Index += 1

            while self.Message_Block_Index < SHA256_Message_Block_Size:
                self.Message_Block[self.Message_Block_Index] = make_u8(0)
                self.Message_Block_Index += 1

            self.SHA256ProcessMessageBlock()

        else:
            self.Message_Block[self.Message_Block_Index] = Pad_Byte
            self.Message_Block_Index += 1

        while self.Message_Block_Index < (SHA256_Message_Block_Size - 8):
            self.Message_Block[self.Message_Block_Index] = make_u8(0)
            self.Message_Block_Index += 1

        self.Message_Block[56] = make_u8(self.Length >> (8 * 7))
        self.Message_Block[57] = make_u8(self.Length >> (8 * 6))
        self.Message_Block[58] = make_u8(self.Length >> (8 * 5))
        self.Message_Block[59] = make_u8(self.Length >> (8 * 4))
        self.Message_Block[60] = make_u8(self.Length >> (8 * 3))
        self.Message_Block[61] = make_u8(self.Length >> (8 * 2))
        self.Message_Block[62] = make_u8(self.Length >> (8 * 1))
        self.Message_Block[63] = make_u8(self.Length >> (8 * 0))

        self.SHA256ProcessMessageBlock()

    def SHA256Finalize(self, Pad_Byte: U8) -> None:
        self.SHA256PadMessage(Pad_Byte)
        for i in range(SHA256_Message_Block_Size):
            self.Message_Block[i] = make_u8(0)
        self.Length = 0
        self.Computed = True

    def SHA256Result(self) -> list[U8]:
        if not self.Computed:
            self.SHA256Finalize(make_u8(0x80))

        digest = [make_u8(0) for _ in range(SHA256HashSize)]

        for i in range(SHA256HashSize):
            digest[i] = z3.Extract(
                8 - 1,
                0,
                z3.LShR(self.Intermediate_Hash[i >> 2], make_u32(8 * (3 - (i & 0x03)))),
            )

        return digest


if __name__ == "__main__":
    main()

# clear ; mypy --strict *py  ; pylint --disable=R0903,C0114,C0115,C0116,C0200,C0103 *py
