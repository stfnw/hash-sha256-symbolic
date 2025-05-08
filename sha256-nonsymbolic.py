#!/usr/bin/python3

from typing import TypeVar


def main() -> None:
    assert (
        "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
        == sha256hash(b"Hello World")
    )
    assert (
        "d25f01257c9890622d78cf9cf3362457ef75712bd187ae33b383f80d618d0f06"
        == sha256hash(b"1" * 10000)
    )


def sha256hash(val: bytes) -> str:
    m = SHA256()
    m.SHA256Input(frombytes(val))
    digest = m.SHA256Result()
    return bytes.hex(tobytes(digest))


# Proper parametric polymorphism (with type classes and checked at compile time
# and actually enforced like in Haskell) is kind of nicer than this bolted on
# mypy type system around dynamic subtyping...
T = TypeVar("T", bound="FixedWidthUInt")


class FixedWidthUInt:
    def __init__(self: T, val: int, width: int):
        self.width = width
        self.maxval = 2**width - 1
        self.val = self.maxval & val

    def __str__(self: T) -> str:
        return str(self.val)

    def __add__(self: T, other: T) -> T:
        assert self.width == other.width, f"{self.width} != {other.width}"
        return self.__class__(self.val + other.val)

    def __and__(self: T, other: T) -> T:
        assert self.width == other.width, f"{self.width} != {other.width}"
        return self.__class__(self.val & other.val)

    def __or__(self: T, other: T) -> T:
        assert self.width == other.width, f"{self.width} != {other.width}"
        return self.__class__(self.val | other.val)

    def __invert__(self: T) -> T:
        return self.__class__(~self.val)

    def __xor__(self: T, other: T) -> T:
        assert self.width == other.width, f"{self.width} != {other.width}"
        return self.__class__(self.val ^ other.val)

    def __lshift__(self: T, other: T) -> T:
        assert self.width == other.width, f"{self.width} != {other.width}"
        return self.__class__(self.val << other.val)

    def __rshift__(self: T, other: T) -> T:
        assert self.width == other.width, f"{self.width} != {other.width}"
        return self.__class__(self.val >> other.val)

    def rotate_left(self: T, other: T) -> T:
        assert self.width == other.width, f"{self.width} != {other.width}"
        return (self << other) | (self >> self.__class__(self.width - other.val))

    def rotate_right(self: T, other: T) -> T:
        assert self.width == other.width, f"{self.width} != {other.width}"
        return (self >> other) | (self << self.__class__(self.width - other.val))


# seems not easily possible
# def from_u8(val: "U8", width: int) -> T:


class U8(FixedWidthUInt):
    def __init__(self, val: int):
        super().__init__(val, 8)


class U32(FixedWidthUInt):
    def __init__(self, val: int):
        super().__init__(val, 32)


class U64(FixedWidthUInt):
    def __init__(self, val: int):
        super().__init__(val, 64)


def frombytes(data: bytes) -> list[U8]:
    return [U8(b) for b in data]


def tobytes(data: list[U8]) -> bytes:
    return bytes([b.val for b in data])


SHA256_Message_Block_Size = 64
SHA256HashSize = 32
SHA256HashSizeBits = 256


def SHA256_SIGMA0(word: U32) -> U32:
    return (
        word.rotate_right(U32(2))
        ^ word.rotate_right(U32(13))
        ^ word.rotate_right(U32(22))
    )


def SHA256_SIGMA1(word: U32) -> U32:
    return (
        word.rotate_right(U32(6))
        ^ word.rotate_right(U32(11))
        ^ word.rotate_right(U32(25))
    )


def SHA256_sigma0(word: U32) -> U32:
    return word.rotate_right(U32(7)) ^ word.rotate_right(U32(18)) ^ (word >> U32(3))


def SHA256_sigma1(word: U32) -> U32:
    return word.rotate_right(U32(17)) ^ word.rotate_right(U32(19)) ^ (word >> U32(10))


def SHA_Ch(x: U32, y: U32, z: U32) -> U32:
    return (x & y) ^ ((~x) & z)


def SHA_Maj(x: U32, y: U32, z: U32) -> U32:
    return (x & y) ^ (x & z) ^ (y & z)


def SHA_Parity(x: U32, y: U32, z: U32) -> U32:
    return x ^ y ^ z


class SHA256:

    def __init__(self) -> None:
        self.Intermediate_Hash: list[U32] = [
            U32(0x6A09E667),
            U32(0xBB67AE85),
            U32(0x3C6EF372),
            U32(0xA54FF53A),
            U32(0x510E527F),
            U32(0x9B05688C),
            U32(0x1F83D9AB),
            U32(0x5BE0CD19),
        ]
        self.Length: int = 0
        self.Message_Block_Index: int = 0
        self.Message_Block: list[U8] = [U8(0) for _ in range(SHA256_Message_Block_Size)]
        self.Computed: bool = False

    def SHA256ProcessMessageBlock(self) -> None:
        K: list[U32] = [
            U32(0x428A2F98),
            U32(0x71374491),
            U32(0xB5C0FBCF),
            U32(0xE9B5DBA5),
            U32(0x3956C25B),
            U32(0x59F111F1),
            U32(0x923F82A4),
            U32(0xAB1C5ED5),
            U32(0xD807AA98),
            U32(0x12835B01),
            U32(0x243185BE),
            U32(0x550C7DC3),
            U32(0x72BE5D74),
            U32(0x80DEB1FE),
            U32(0x9BDC06A7),
            U32(0xC19BF174),
            U32(0xE49B69C1),
            U32(0xEFBE4786),
            U32(0x0FC19DC6),
            U32(0x240CA1CC),
            U32(0x2DE92C6F),
            U32(0x4A7484AA),
            U32(0x5CB0A9DC),
            U32(0x76F988DA),
            U32(0x983E5152),
            U32(0xA831C66D),
            U32(0xB00327C8),
            U32(0xBF597FC7),
            U32(0xC6E00BF3),
            U32(0xD5A79147),
            U32(0x06CA6351),
            U32(0x14292967),
            U32(0x27B70A85),
            U32(0x2E1B2138),
            U32(0x4D2C6DFC),
            U32(0x53380D13),
            U32(0x650A7354),
            U32(0x766A0ABB),
            U32(0x81C2C92E),
            U32(0x92722C85),
            U32(0xA2BFE8A1),
            U32(0xA81A664B),
            U32(0xC24B8B70),
            U32(0xC76C51A3),
            U32(0xD192E819),
            U32(0xD6990624),
            U32(0xF40E3585),
            U32(0x106AA070),
            U32(0x19A4C116),
            U32(0x1E376C08),
            U32(0x2748774C),
            U32(0x34B0BCB5),
            U32(0x391C0CB3),
            U32(0x4ED8AA4A),
            U32(0x5B9CCA4F),
            U32(0x682E6FF3),
            U32(0x748F82EE),
            U32(0x78A5636F),
            U32(0x84C87814),
            U32(0x8CC70208),
            U32(0x90BEFFFA),
            U32(0xA4506CEB),
            U32(0xBEF9A3F7),
            U32(0xC67178F2),
        ]

        W: list[U32] = [U32(0) for _ in range(64)]

        for t in range(0, 16):
            W[t] |= U32(self.Message_Block[t * 4 + 0].val) << U32(3 * 8)
            W[t] |= U32(self.Message_Block[t * 4 + 1].val) << U32(2 * 8)
            W[t] |= U32(self.Message_Block[t * 4 + 2].val) << U32(1 * 8)
            W[t] |= U32(self.Message_Block[t * 4 + 3].val) << U32(0 * 8)

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
                self.Message_Block[self.Message_Block_Index] = U8(0)
                self.Message_Block_Index += 1

            self.SHA256ProcessMessageBlock()

        else:
            self.Message_Block[self.Message_Block_Index] = Pad_Byte
            self.Message_Block_Index += 1

        while self.Message_Block_Index < (SHA256_Message_Block_Size - 8):
            self.Message_Block[self.Message_Block_Index] = U8(0)
            self.Message_Block_Index += 1

        self.Message_Block[56] = U8(self.Length >> (8 * 7))
        self.Message_Block[57] = U8(self.Length >> (8 * 6))
        self.Message_Block[58] = U8(self.Length >> (8 * 5))
        self.Message_Block[59] = U8(self.Length >> (8 * 4))
        self.Message_Block[60] = U8(self.Length >> (8 * 3))
        self.Message_Block[61] = U8(self.Length >> (8 * 2))
        self.Message_Block[62] = U8(self.Length >> (8 * 1))
        self.Message_Block[63] = U8(self.Length >> (8 * 0))

        self.SHA256ProcessMessageBlock()

    def SHA256Finalize(self, Pad_Byte: U8) -> None:
        self.SHA256PadMessage(Pad_Byte)
        for i in range(SHA256_Message_Block_Size):
            self.Message_Block[i] = U8(0)
        self.Length = 0
        self.Computed = True

    def SHA256Result(self) -> list[U8]:
        if not self.Computed:
            self.SHA256Finalize(U8(0x80))

        digest = [U8(0) for _ in range(SHA256HashSize)]

        for i in range(SHA256HashSize):
            digest[i] = U8(
                (self.Intermediate_Hash[i >> 2] >> U32(8 * (3 - (i & 0x03)))).val
            )

        return digest


if __name__ == "__main__":
    main()

# clear ; mypy --strict *py  ; pylint --disable=R0903,C0114,C0115,C0116,C0200,C0103 *py
