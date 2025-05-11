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

Some data where the i-th hash-nibble is null:

```
Data hex:    12b9bb52ffda9e3f8572246ab6e0d938713cfcf9a181478092f04fc54a3ecedad6
SHA256 hash: 0de1d69b67674230bbd5504ceccfae5a86af22ec3b08ddd55d7d795b791cc539
             |

Data hex:    6e6c41ff2879f01dccb8ac45449e5375357e98fe3479cb368f809e9cb6a9f758ce
SHA256 hash: b01f1a4e98c90831793c42fe2db11f4d338b57bf90d61803ce6847ed47af2eb2
              |

Data hex:    361502873d8cb99c402455ea20a040ccff9c7521d968e422f4c60ec671967238ff
SHA256 hash: 280884928fddfc82bdc0710b2299886dcf08557a378ff95c1e8ce1113a30236b
               |

Data hex:    c63f77b1c948f2f275035176bb9d74c7c8badd699f3019171758dd432d5b112732
SHA256 hash: ed80ccc2b1c4dd59e990b12df6ff4dee6f64304a8c6ca0197738b3d72e72b59d
                |

Data hex:    39298af8614fdc5bf0025a488110ad5cdeabd5ecb2bace2b6d7916d3b21a5a1e2a
SHA256 hash: 16ec0b88a4b242a0445077b3dc4e6e0bf20f2b99ef56d6a1a795fb9cb1881257
                 |

Data hex:    77b82ca2e20075f3257cf27294a198a548032f24ef9bde3a281bbd05268fe0e8c1
SHA256 hash: de1a70d9e19343d1aaef0ee42aa166ec9e0812ccd025c8af2ca4e0cb91f71653
                  |

Data hex:    15d008ff90b2be7ffa8f20ea78ebcce9640f86534b463996701d5b730970cd6598
SHA256 hash: f5e57e00d00922b32e2b97115bbe174a06fd8a9f3fbc52cc9a87fab2ce7996a4
                   |

Data hex:    a577623f40ad0567f0f171708c08171160520935cc4b4f95b0a7bee40eb11fa553
SHA256 hash: 3d4cad40541554ddf1ba843e014fc826849bf05ce26a7f8aa7df7dcffeebed30
                    |

Data hex:    da768e685d54098747225cb9fdb50d59250a491a42cbff7a33b85158e75a7dc258
SHA256 hash: d48d4d700dce506555c41ca29c34a6adecfc6db2d17f2c5e2ac052735c6b22c4
                     |

Data hex:    bb9e538315e29df6b81f980c639e58e21f534c222f7c7412e093c973640e63c6f6
SHA256 hash: 17313147d0b1ded202513020cbe5197aa44760e184a867a069832eb8e0aa6966
                      |

Data hex:    e76269a6624b1482146fafb8b2c94e1b9c26ce2b9faeaa0b8967f31d984f863a43
SHA256 hash: 78522c312f037896c2f2e53af255119b0bac48e9f0d04563d5e8001720a50985
                       |

Data hex:    49ac9ab0bc4c0f883928cd6741722459b6b78b03606f3bb77d0c52e2eb9a536f28
SHA256 hash: ebe41ff42b60abfba2a18e7c7d82427020c614313351b1b005004dbeb912350b
                        |

Data hex:    9bbc27f3cfdbf5a2b0ee3799df9ffd4514d62dadedf41e40dee8c261c74031a9c6
SHA256 hash: 90eb71a0ec330f8add6c1d45f82b960e1a945aa96fc2fe13702dfc39f4e7ccfe
                         |

Data hex:    a5348a202fb45b6c234aa6399989bf00f249cde199abb5e474ffeba4095e5ba7fb
SHA256 hash: 7edb339d5bacb04dd0e8fc88cc5475a6b83b31c1c5f567afa2d3e18d5104fb99
                          |

Data hex:    7f499e2e7bc8e85bd1caad18fbeb3c9731a32bc3d5c623515d0d7f513dfbf176ff
SHA256 hash: a3d0496eafc5a1074b38a7a886cbd62547bae48232e9427940ea10efa06ed475
                           |

Data hex:    0eaa5064bf05bae540061be59bb3911d9040485f76f1a8bb0e63e3e1702663e7e5
SHA256 hash: a916abbc582d4cd0fcd5625af51992589f8091374ae63cca4e63ede7b703aa5a
                            |

Data hex:    c31ab04bd0f35af6d16229adb812ef8fa3f757ef39f9244d06fa4035db24b0c5ab
SHA256 hash: a96ac64660ea801f0bd42af0ed66b67e0347541280b935b5f96269b4d7b160d5
                             |

Data hex:    8d4eb94ff5c42a799dbf97e3f6ba2b15bc9894e971e3e7f831a2b313517ee15468
SHA256 hash: 616ff45d9ba7fa7a608c63bb060a10734fa2b296c4a30dbe6e817fbb99d9cc74
                              |

Data hex:    27d6a878adb5c9abb4d7e05af81562c38689bacc4de4a490316b0dcd12ebac4f71
SHA256 hash: 83c607c3c20bd103b406d9cdd2f4afa188e30c9deecd950be9c6c05718dbf321
                               |

Data hex:    411b31267462854ce2c66150d5eccf464febe10034a4703122f7f0156da64f8fa7
SHA256 hash: e1ff162270a840762ca038e702cc3c22309314eae3617ed360fa896137383b3b
                                |

Data hex:    d216aff391402ec426b4f8b6aa9842b44e8ba0fff9482f75bdb71ed28e398c0c0d
SHA256 hash: 7535ac318b4c62c7472b032fd1a5f3d9dc81630e09a09fb90237433ebf92e36f
                                 |

Data hex:    066a14b4559cd6515f53a1c20eaeced61d45ff6986b7b840724d26d9a54fb32a73
SHA256 hash: 26e88ddca40b5c1b9d4ad010cab425d46cad93b4aca1bac0a3533eb779880cc0
                                  |

Data hex:    acfcc9e9e0e3b66ccee226d6cf6d2e4ef1be117f8f40e53aeb5d415ac77f9592dd
SHA256 hash: 813c3ff793aa9eed2532790c0c96dd774c9f14871905b6d2e61b05d2ac807796
                                   |

Data hex:    c1bc7cd4e0c7aa2e02d7f973e368a9741f8f35077f6652d8d3b1e6fbfde7a4078d
SHA256 hash: 21b593fb369f27069bf00b8043f011c24bd2d488dc1a83ea209c0dd8531b52ac
                                    |

Data hex:    5396470fa977e5fff650ca4cd7c467bd42a44ce6bd04c91c1d5adb0fd9a2e56aa7
SHA256 hash: 035f1883074c96a92cc79e740f204c8d62be55065c28aeadbb119fa31e93a136
                                     |

Data hex:    b09139c7768ffbfdc25f5d3978c13c1945db627aea6b84f06ffe0e3901d6a30a3f
SHA256 hash: 866e474dd4092f3fa7a00519702acd273309813a1732db90ce5ce16cfd50d5a8
                                      |

Data hex:    2e3cef2a1eddc4dcae277bbfad59b0e03884b5fb40be9a27d0458f9a934748b5e9
SHA256 hash: 3d26e38432b87c835e48a21502013106f96a5fc9a77cd55e7c940ece34482116
                                       |

Data hex:    37c5e9a8766f57176f4f87fe4e26678ee9f60e842e9c3e819a97e9c1c31dbc7d11
SHA256 hash: 1b35d6b3cf7cfcb5732983813ec00f63cd53b2fda7330c4ca0804ead7cea811a
                                        |

Data hex:    8527f68bc9c467c01ec1c792b1e6fbf83f4399f9feefd75ec771294375963f22ac
SHA256 hash: 8555d2dba798ce4ca9dadc5bde2c060fc23f2511e72b3a11879879a60c467a38
                                         |

Data hex:    6bff295345472b3f8dd819afa67904a4cc7e32517c48c73be68cc8724ffc54e7ee
SHA256 hash: 4ba1a1a7042078f4cf8a999b12863008e51cdedc763274f1fff5f0a59f923965
                                          |

Data hex:    06adf146387f6b8ca83f0a7f68a36c06cc5273115ad0252be303f243f19fda7677
SHA256 hash: 6fdea9f08b426d8ce34a10e2b8639b0d98f0c222527d91a13b41fdff78b1e364
                                           |

Data hex:    f4cf18f2d0aa787b9fee6205abf8c10a743610f11fddff6aea52f77e1590cab703
SHA256 hash: 46a232dbf52bd9eb34cbe15075cc04e01ac53d0d8b4c74ea0f16746543c073e8
                                            |

Data hex:    bccc26b6debad931be0753ac984c91598785d96cf4df82b63e0730a8d6c6436208
SHA256 hash: 42806d421829e354089f701fa6df9495090a43510393a32ee15ece0025300985
                                             |

Data hex:    51ad27aa874c792e9c482d6c7170674c5f9551eff275424ab16538e195397552d3
SHA256 hash: 9e58fea44d9e1a85e520dd7ed0c527f04055dc0679dd080edf2bfa8ade606e36
                                              |

Data hex:    9a280c40c843786942790f326742dcf9f3065b872e63e0d261477ba9bf1ea4c183
SHA256 hash: f254eb01960e345709a0d73559ea69001f0e0f9ef8a4c123be9a3ffd2929d5ab
                                               |

Data hex:    742782942a8a6781c68d1bee0899bd1f8f026e8558030cf75efee1c17b9c14b1ae
SHA256 hash: 6af35dc05f284248f55fdacf891aee7835907ae3d724aef9cbdfffccc4a8a75c
                                                |

Data hex:    59379a64ee3e12ee55a0ffa74bd3a7e9f7a276331710d4f8524878564c085e5f62
SHA256 hash: e7d7f6f14e7aed0ec3a4e3c1580983061f280854c692b7479e95f24d0d3c10c2
                                                 |

Data hex:    d08a390899bd43d26d83dd58b2cd87d5bea9e3600effa50233f0ac965e9cc86021
SHA256 hash: 1ff9d63d9d9fdb1203c7634731f616ae7c2bc0e7d33dd610491b2313051999e4
                                                  |

Data hex:    f47af00f3e469d98fdce3c849128e097d5adcdfaa2c35b3908248f1008c5b4dff6
SHA256 hash: d0f87377b1c5630b5df5d700f0e3baa504dac90dac9d07311e6a321dd3c5b9e2
                                                   |

Data hex:    4c4d9ca379d558dc273ec8f0cf22695e9c9991fab61e78c53e9a409f4242f04c28
SHA256 hash: ad23f436b93738a947c5d9e811cba70a25f0a050998aa3af76701569f9e187d8
                                                    |

Data hex:    064f7dd808e0dc2c504c7c5b9e446139351552d578478fca3cffbdc7f7c31aaead
SHA256 hash: 9e9c6bcbc85b75170d1450d15c95b0cece98a82006b02edc9a99d762e8a41e9b
                                                     |

Data hex:    4e5884ca91beb60f0fd7a4d238c3b91364dd883ff994b220039414156e4d5b218b
SHA256 hash: 35d7da1c06d9612006a04d99cece5e1d64b4ea0a6001487fc0091995e6df89ec
                                                      |

Data hex:    aa5af4bac9a3dae2ef90c0b34f2f0ba800046214c95e551ef6e55ddf51db298301
SHA256 hash: aa9b92f6467526dfa0028a1eda62c573b6e6c94a750a0ffcc4764c2d0886cb77
                                                       |

Data hex:    32180c6e701f70b22c921e95501419cecf32bad9598061ab56981d972354b9705f
SHA256 hash: a3c9ac33306318b9d1a6f168833d93ac5a5665407250d6428f18f8d900903cce
                                                        |

Data hex:    7f626b169fd6c86df574f72ad4f9df4c80a4e65024c92602f8c0e1886ae6f0c39b
SHA256 hash: 777b8de96335f86e1c14f6b27e15f4006674e27198330fa7c33f5b0e9b2e4d2c
                                                         |

Data hex:    ae9c54162150d2ea0afbd0c6236b31a1e97f9d7aa4f6b7fb6f5f29855e0378a76f
SHA256 hash: 68673e06f8ea6385da01a950cf5797c6a54c57f9effe4054fedaa44584da7131
                                                          |

Data hex:    3e203a26c73727ef8a58475b2523ddbad13cef292710a42a0131de3572a5ae56a1
SHA256 hash: 22f6accf03d9373b19ad63db9ecfb4aaae0183cd030b300ca32a3bd86a74e1ab
                                                           |

Data hex:    375cb209213c20b4c7ee6232adf96bff1480603a0722e04cf3ef40f8cf63092172
SHA256 hash: ca052fe1edd9a933f22b1735766c05756ea0b8a8a00077100a05fb911a7088dc
                                                            |

Data hex:    1cbbcd32708ab97a680799a657bcfc377feb107e6678dfe5ea4de84dc8f78c3705
SHA256 hash: 73fca2abae31654e98594e962edd07686d517dca2ed327130b92ae5d76c59b70
                                                             |

Data hex:    794775135c1289d0a0dbc77ead15a6f7042805d5d7ac98d07770f5703b518d2017
SHA256 hash: fb404fc609acba869ba6f65707ee1568c82f3cddb4609be3a0da5ab19eb0996c
                                                              |

Data hex:    1459865eefbb905bb5355f7a91e4b0ad1ffba5e1a49cc3ab012a5344115a1827a0
SHA256 hash: 9d478a9d167f4057dff14fc7137400f50983bb2a944cb375e003b54aa5d98691
                                                               |

Data hex:    a30bb5a0f41cfef09f46d5562487ddcaf1a25168c3807f598bc55efb7bbe8eb9e3
SHA256 hash: ba3b3e85ce6c5b100aed14d93a060fbc65104f7c52dc509eb3809aace2c14859
                                                                |

Data hex:    9eec999bdc5c9901361cd11ac2fb7803269d2300c3eca24ab6e2a9c791c39af43e
SHA256 hash: d4288bf557655dd353ade86dacc4fd0e84dc4c80cb11a0d4ba0d04cf26bf4552
                                                                 |

Data hex:    a46d47c64d3431624e2c734e0ed8872e3a2c850dad00b6c32a881125638ec76c72
SHA256 hash: 599e9e64f05ebc00184314efae1e86035698ba1da2c03fe463fbc046c36a555d
                                                                  |

Data hex:    d88b6b84c7320f0057e9470510ff133fdb23c7ce2caccccef77e318a211496cd52
SHA256 hash: 1275909827b9a52f3b846a9515520275dfac558057cd4a4f4228330802b2cfe5
                                                                   |

Data hex:    ae9d22dd4d24d84ef2e7e98c7000e4ee90bdb65a2b8b6a5daf7d1a93a6de9f8e3c
SHA256 hash: bfd1c71d5eaa75030b0b94d70827d5f7cddccd313135718cd0806ba0de0cf7fb
                                                                    |

Data hex:    ccff1df4aab96606b59f59702bcae75cf1e0c434f8371e6063bfac7c69c5b789e8
SHA256 hash: 09f12261b32b90f126104635089ea388c7062c2491f3e825752bb69308c37564
                                                                     |

Data hex:    b040049cdf67a1f3e6e09fd2fc87fee1e18b170007dd0d7f8640655b4035c5570e
SHA256 hash: 128a8f157dc7e51bf818a4bbf90dd93491e16a73cc404c79c833b60be0143a40
                                                                      |

Data hex:    b4a75ab116086aeb4b3eb540067331da193593adf3ca33841e8920bec17164c5d0
SHA256 hash: 7c75ed9f38e327fccceac12edbec8a679f7afa15841fa1b49a10d428d90412a7
                                                                       |

Data hex:    208175c68eef53ddfeff37f787fac3bff09bf7e79e51d4a70bb7a1781724587660
SHA256 hash: 7ab96a345ab0c07b379cacaa7a280447e397171906452784eb3ecc6a89800dc3
                                                                        |

Data hex:    5dac13cb5455f77e68410dc85fcb1fedeb7c076abf605f0191087611960b78a51f
SHA256 hash: 6640ed93815559e748cc44ba19bb44f4a174f4eff8e1de5b7d233e1e430102fa
                                                                         |

Data hex:    cc8c87a17a8c353dd9f89000b12ae6837da349d7139874fcfccc5d21fd1ab37da4
SHA256 hash: dd9081a433d1cf0c94cb1de7f07d190b0daaa31ab8064d0a79417481b64c6008
                                                                          |

Data hex:    cc8c87a17a8c353dd9f89000b12ae6837da349d7139874fcfccc5d21fd1ab37da4
SHA256 hash: dd9081a433d1cf0c94cb1de7f07d190b0daaa31ab8064d0a79417481b64c6008
                                                                           |

Data hex:    b040049cdf67a1f3e6e09fd2fc87fee1e18b170007dd0d7f8640655b4035c5570e
SHA256 hash: 128a8f157dc7e51bf818a4bbf90dd93491e16a73cc404c79c833b60be0143a40
                                                                            |
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
