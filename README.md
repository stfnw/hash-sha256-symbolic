This repo implements the SHA256 hash algorithm symbolically using the z3 SMT solver python API and its propositional logic / bitvector theories.
This allows formulating constraints on the inputs and outputs.

Of course this does not make it possible to break strong hashes because we quickly run into the exponentials!
This is nothing serious, just playing around.
But it nonetheless allows us to interactively explore the topic and find interesting pairs of inputs/outputs, like e.g. specific values at positions, fixed prefixes, or fixed suffixes.

# Examples

Here are some example input/output pairs I got while experimenting with this topic.
Note: All data input and hash output is hex encoded for easier printability.
The examples can be easily checked against the typical implementations available on Linux e.g. as follows:

```
printf 65b78816d1e650da930363102e8bfaef10c4f4b4bdf957ccc9d1fa84128cffef3d | xxd -r -p | sha256sum
00f33fddf4aa689b77850e8b0702859dd1e983c82e7a15d9498d4baf34dab1b3  -
```

Some data where the i-th hash-byte is null:

```
Data hex:    65b78816d1e650da930363102e8bfaef10c4f4b4bdf957ccc9d1fa84128cffef3d
SHA256 hash: 00f33fddf4aa689b77850e8b0702859dd1e983c82e7a15d9498d4baf34dab1b3
             ||

Data hex:    ce04e13c61c7612af84bfd5a1d578f55721e2721ca14179dfb9fc90223206e2a4d
SHA256 hash: b700cfb51ca2ae66df87fb4e2ad4ab5e3c053a71f077a2ac408261c0c7943dba
               ||

Data hex:    235a5856d6fbb7f75c5ffc64a5d241e2a6705457caeec57defcf91c73acbc170d8
SHA256 hash: 30c800060837f64fb788ac5071c7151ad156fbe145f5c34006c5b2d1f559aa69
                 ||

Data hex:    bfa687379454aa8c5f9d980571dbf329bf3512e58d07d3aa85d086a57b85f5a9d7
SHA256 hash: 833834005167045d3afe98cd471c41d54ed6c809b3f3ff7ede6177529082f82e
                   ||

Data hex:    1035fae694e4842a4d7bcaf5d17383b1b6674c530ef5f0364100033aa16897bd02
SHA256 hash: ae81f7eb00b70019ab39c63ca720dbc4efc70987ce6a6b6411fcd43c1471fa9e
                     ||

Data hex:    8efd99955110300008c42992a3ce9efe342f3b1464f001abbcc4a1f463cd840a27
SHA256 hash: 7005c80386004c4ba8ef75eb4bc526940aec8b853d2b1700b254ecdc94218f7f
                       ||

Data hex:    dd1cad9452d10862281343189cec9513947a6d6cf984d3bb29bfa42c53627f20db
SHA256 hash: 454f3d1f04e800e39cf34641acd742540fc9f5a5f241ab3f6f7068aac3f1bd8c
                         ||

Data hex:    b4445e0381914106f285f9351cd029a4cd7ea9f8bc0b10758f33541da86958ba05
SHA256 hash: 72f2b10d806e1e004c17a7124a6b2b9c95c48ec4c48a0bac28cf4e4e429646d2
                           ||

Data hex:    ac0c87d9a4a39e8e75eea3e7b5cd1037b32498f98ddb7b3d26a31e70f03286da22
SHA256 hash: f183c800e2565d8f0057d558be1c8832a7582317764c897e32abaf915d165036
                             ||

Data hex:    94af0c21ef1b1d5d40284e9356fb34938342c06832086790aa8c8a426af0802dee
SHA256 hash: 23b72ba76ccdccd21b007048cb7227e3cfb8875b6fa2416c97f68d786ff7ec61
                               ||

Data hex:    259a40f52fb8c67e464c56661d58ebe672be38fe5f9cb48daa60c1f8ba7f8ff862
SHA256 hash: 0d160498a889233c883b0011a871d508100a2c97eb6a3945919aad16acb9decb
                                 ||

Data hex:    21f58b00808343375ec68074667c5e602dfe6867012fd7b7e8a77babfe79f97daa
SHA256 hash: fdd61e0760a8754069d6c900e510553dc5695c8abd9c035a1e0d364ebeda175d
                                   ||

Data hex:    4272ddae8b2fab887223859aac1edb693a99ef4b67eca9c1a42c8434a07d147888
SHA256 hash: 4b315d8a2f2dc26628155ee400a53c24fd313a2955c9893375d98dd6955befd1
                                     ||

Data hex:    72ddaaf19727cf1d6081e973f05da3ff1897642d81a4472e3f729a637939e8a5f4
SHA256 hash: 34cf446d92529070d488cd3149005221b607b50aa1f29fd052159fc837d03030
                                       ||

Data hex:    f86b26ef502b59420ed8912083df702cd61db0bb14ab884b130656459cb33a9a8f
SHA256 hash: e311c559e55607f386f09e062c5a00b62d813d3d0d4f8a7346da77004213f321
                                         ||

Data hex:    4086b2b9e8503629e572ef0400331edf46186c65c0c522465e9495c891662e4ac9
SHA256 hash: dd4529e18a1393cb42f0b7b781cdb3002d378cb6ff1daa1ba05c192460f57181
                                           ||

Data hex:    231d4fcbda715c7f70436285a9eef1656e92ce622d56d9c4f6af881bd4314781d3
SHA256 hash: c3af3a75759dca52ff8d7eaae76dda5400d6b24a21db2aa681bca7e477e38b39
                                             ||

Data hex:    0239ebcd5d27aa5d281c1b3dc004f0b66a3502ceb9c53873e0f202accf513fdd39
SHA256 hash: 6c4f526412ba6e2b11ee485768d2998ce1003550006bf4f4937a9c5418694c24
                                               ||

Data hex:    a864d52ae2044c373eee7f0faa29d26e970c85768143ec80b4a1ce0ef2e9a37e83
SHA256 hash: 2bd42fbc080b29e1fa912945b1d5c94e8dd30024a6ac02caff5968421b1cbdc1
                                                 ||

Data hex:    7841e3ddae56fcd7abfb6f8fddceb2296f37702ce12f270f2d582714e8471a0259
SHA256 hash: f7bc2a9a12b47673a2ca785a9cda54e09707aa00ea87a73ee46274f6c2076a86
                                                   ||

Data hex:    b30daee8a64051a4fa66001be4f6284bc043ff9d9b495c3a1ad37f3a50e959bc20
SHA256 hash: 8cbdcf0c5f837e4713f402fe06c6934eb4ccb9130095d68217501a8bc5581271
                                                     ||

Data hex:    065c453315b48d32fe5c17cf201d8eff5eb4fffc09fc66aefb3eba58cd587b4f4b
SHA256 hash: b99f354acd74547fdf6743fb291a364eadf233a1b400b798c60986120635c8ec
                                                       ||

Data hex:    ea58d601fd4ccdc38b420b9d9a62887bc0989d86c5c575d6fdf547a383fcdec7d9
SHA256 hash: 9256318683ba40a8df44323ddc140268b29be159440c0093ae1f779ff517327f
                                                         ||

Data hex:    b5af846ba4a390663bedfe9894a960f8490ea793c58317311d4680f74de7413967
SHA256 hash: bf5a8a8788144affaae08da9de6ebb5ff744d3dc75c726002c6188c505d75304
                                                           ||

Data hex:    8ed18dba374a57dc96e0133fcc1cad8a0b8691aa7783c4b0e94d527350034b5d16
SHA256 hash: 0c8babe7d72b9bf5564a24088e91e0e06cb63508652f13e40096d98a4615ece6
                                                             ||

Data hex:    cb642ef859cdf391793502d52a37df18c317ac4e8f9625d656e626612e62bed1fc
SHA256 hash: d91df12c3a9382ab8a76327c4dbdc84aa117693ab8e39436bb00901e603dfb87
                                                               ||

Data hex:    afd9d5fd7c41f8b6acba3496250f0ec22f5a8125d472ae586ad993040bd3eee86c
SHA256 hash: 498f83cb646b79e778f99bd76bbb09de23c5aa668bca5fc741040007350c4414
                                                                 ||

Data hex:    c0eea814e902fdffed43c22f87104261aaf5e91614f29c506c877c0e6fd4c40793
SHA256 hash: 16f2ec4182d42421ac2272b9b81db367bf05fc3e92c8f89878a0b6002c790041
                                                                   ||

Data hex:    ea0b2544718db61537e56d8f2d630c1d71ca929d423e194958bfd61ce9575075f7
SHA256 hash: 0453cc4876d88aa05bf4300332f9a26e05a0f184a077461ab886c50800b47341
                                                                     ||

Data hex:    61929ba26842cc5a7d7a230757b29d13b80f8bd6bcd42042b504b57b183effb7ac
SHA256 hash: 30b18b63d0aee3e9cb2ea3a7d4af8991294bfe968c70f77f006c80c4c600e9fb
                                                                       ||

Data hex:    2b8935cc83827210aea62b61904ea8682ce16b652186e9f0dfa829a8b3b7ee6f61
SHA256 hash: ebdc52791ce7637cd39fa1c11316993e482aab895711fbadbfac0b35431e003e
                                                                         ||

Data hex:    6338ddeea3fe5d491b9b0332a12865e190c081ff6eafe0afd5fabd290eded97d86
SHA256 hash: d3c60b9222dbc5b1b65e0d193b8f9fb145876c5fb6af89007321e409c1b5b700
                                                                           ||
```
