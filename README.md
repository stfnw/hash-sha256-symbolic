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

Some data where the i-th hash-nibble and its mirror are zero:

```
Data hex:    ce32b1e7a40aecace24caae907cd29e86039575d023c063976cef2dee8e02cd3a9
SHA256 hash: 2008d7280be9309c6926da8dc483c9cdf38913e9de6966453ed891f4ded9ae0c
              |                                                            |

Data hex:    045e9421d719c9f1bd3f0c4018078aecb8f2813a2b2328cf6126a7bdaeb29fe48c
SHA256 hash: 530084c80a854e65a06daead59c5c727aaf911023ae473c8d6d7e30215cc03a8
                |                                                        |

Data hex:    fe4123202a4a063969a9bf6fc423dbea7e8d5d6725bfd776ffd277023daa6589b3
SHA256 hash: 64d8b0ef40d83e9184ed9e11fbe1805dde0ae74a42b55fef7e5ad9eabb0c9fde
                  |                                                    |

Data hex:    d9f81bef80628498472e5cd5043eab000b1781cd312037240cb1bd9e0b16b7be1f
SHA256 hash: 43a4f5c015269c07faf757ce2357a88eedd1bb358341db21d096be370630b5f4
                    |                                                |

Data hex:    cec8d31ddddfe3f24d0ccd0690c9705f1b87e968f02d0b2a7cd60fdd95b6353195
SHA256 hash: 979a0bd9c0e0f3a33512ddd01947b4cca9ade323776e5a1cbaca3c033dba50f7
                      |                                            |

Data hex:    52398a4de8e6613796175c88c21e8758e67274a02f8bfeca4871e5a3d72a436669
SHA256 hash: 5b4c7eb7281015cab6ec3fbf7c70b8973fce073947840080b65607ac06ec7e85
                        |                                        |

Data hex:    25eb24f14758008448d260c7ea5a43b3f8ea3d8679df3b056d4f7cec4b0334f60a
SHA256 hash: 36d12ca4a57f80c0aa92666f5213dd1771d019311189ce55780000ace27d3f11
                          |                                    |

Data hex:    be64f3d4358d9e77ed00fd866e8f352368aefa4b0247e57530bebe72372fc77717
SHA256 hash: 09058cd72562b680a8890a9f8fb56bf835283d756e68fefc05fdab5382999c69
                            |                                |

Data hex:    de630e346dd23716b8118ca6897bbfc125930b23b8c3459b4d447e8f01b6460ce6
SHA256 hash: 45247c3067d163369088ef1291eb7b8f7fdd3ebefdaf8101d3a8b6222a6149c3
                              |                            |

Data hex:    cbeec1d0365db7ac975e31f041fd48ede062a6a1cc0106396c2005d655bd0bc49c
SHA256 hash: 7968120cf0a1c6bd56100c59c367dec8514a823af12c012cf27710707572afaf
                                |                        |

Data hex:    d874c7e0f15aee5084cd36cfb9dc0a4e3797041a9c7d33d97449deab829d09afbd
SHA256 hash: d560f3186b17ff553ec85088c2e1b96e70060a12340ab85e69f30e230bca84a9
                                  |                    |

Data hex:    a264783885fce367cd79d9b947dd21314b8f28570a59fbfcba270a8d0d5110616f
SHA256 hash: c255fbbee55aed078ddd4e7020725a6d5d44e0d80900d8966ec1a63c9d3a75f8
                                    |                |

Data hex:    3d06c7ea4741a6786ef49ef37c09bf6dbb37e2ff2188469c879a832b020b80ead0
SHA256 hash: efee062e75670ceaa94178c69048083c5754530c6751949ca793a8662d1410ba
                                      |            |

Data hex:    8b812ab0053085ff303e94b7e4bb0a7d9d890beb9bd645418b8c080b3399fe0ee2
SHA256 hash: 66e766d995ac62ccdb709cd17350d1b8bf9308242266b48ea555287747139ed8
                                        |        |

Data hex:    3807827ff25a5ce4cdaf157f7fbfe443609b7acb11682c78b3e2a1656a0d65407a
SHA256 hash: a6a856f2e59c4017c4c19a8b385cf024ff0cf1855af52fa3f153f5761a452af5
                                          |    |

Data hex:    882064c97fff9fc0b47c9ee4289997a7ae15ff3a01ea25f5a1e1eeb05554df1ec8
SHA256 hash: fadfac9c89650e37df8175b6a357702003756254febadf2e72c3e0cd19fe82ba
                                            ||

Data hex:    d4b65970cbf7e0196707166796ea0a9f9f0a787e311be4f12cea8a836ac8b9ca96
SHA256 hash: 041ad4776b0e1a7b57fe91ed3e6f3c097043a32847e500c0eb9b064413228a7c
                                           |  |

Data hex:    0f6c0a74e2b01886229936cafbf05dd7cfc0fd08ea6b940908ba1211b6b06896c9
SHA256 hash: e546f3216d38344adf4185383be106485e60200f016806fbc49c62ffdaef96df
                                         |      |

Data hex:    8eee99117948e020269cbae82c7a9604ea24f15a7429588b894050f5c2f4b18efd
SHA256 hash: ae164d0577557f81ae426534c402700e7b21a045e054c2b580d5852fea41000a
                                       |          |

Data hex:    e99db092e792c47da02bf7f5d367d26d9b7ed4e2326ab630cdcf80b7fc8eba7fd1
SHA256 hash: a15d74513ab2973adf7a6a9e08bf5f1425b0f310a81635f4e3bcb15d374ec5c4
                                     |              |

Data hex:    297e28befc3d9d62f562f5079cc554604a7b5e3b70d0011b62904ab852b7aa2128
SHA256 hash: 16dfae75c676a0bd2768600da25f64eb37b005d93090caecbe91b628b9320b5e
                                   |                  |

Data hex:    6b0155404c4a5742135d03e53f6eb025cbbcf90559ed5fb5086ab46ab0d90ad193
SHA256 hash: 7ef52d8e8828be2f94e70741a1ef0be64bface403a003a71dbfd08499007eeb6
                                 |                      |

Data hex:    fbf75221dff40e4e621ad031f3667c7b8d4c81625f1a8d3d6ddc313069a06bb23c
SHA256 hash: 0956647697d2e401f8001fb41ca1c3505248e686b09a304a0629c07a32f4b4b9
                               |                          |

Data hex:    48e3c30011195b5a304e9dad87fc7e77cf231c4f6d0365fdf227b48649cf82b82b
SHA256 hash: 8a339cd443c661ca01c222a684b6c0582c14c7f60ec810309396eb43a84a4578
                             |                              |

Data hex:    f5739461f88ad197603139482e02b43a2f61f7c35c8b798d9dbec0ada7e87f7316
SHA256 hash: bac06fc8ebbef502fb5e8e93bcf41276859e8531fb60ec0ae05fc06f26b13927
                           |                                  |
```

Some data where the i-th hash-byte and its mirror have the same value:

```
TODO
```

Some data where i-th input and hash nibble have the same value:

```
Data hex:    293fdfff11f148c4f53f45e0b3c507874d3c429f61375bb895896b23cf1705ba73
SHA256 hash: 2a073196215f8ad24ef5e911d84526dd36e2a01b62f959e660d19445b358d4f1
             |

Data hex:    04e87febcf2123df484d1a33a3e7569482ae03c607c565fd698dff1334681b3013
SHA256 hash: 04e53053affd92d1563999bf41b06427952cc34e86a6d9534b39127e77744a12
              |

Data hex:    44fe7487d27c8769aa6fad38f399371909dfaeba1d3170cc99502f036c6855cf0b
SHA256 hash: 3ff37013887d37621f2fa1b714356aa0c9f8ab2148d8f736b53bc41a0ca0aed7
               |

Data hex:    a22c63ad5bb45fbd7ebd37f779fa2bf788f382bb16d2a7e8a59e158b7d246bcc9a
SHA256 hash: 63dcd0591b2d2f6f34ed245dec7eff01cac9ddf272714c612da40b8969452607
                |

Data hex:    924fb9aa4c7b8783ff3bfe8a4f54fc0ef16bc6140c8f219faa33c04a169ec6fbd9
SHA256 hash: 2b15b2bd749287607d0c5ad8e0d41d7e98e73c28ceb52f9d80d4792c17698ef0
                 |

Data hex:    30091f2a2d7e34dbeb296e9d82cde072be752a3a5d66fc88df6b680748ec258c0a
SHA256 hash: 045b7f32fa16c7a0b294c38211b8bdbad0a0a920fc40e4391d1229e1d0e9dccd
                  |

Data hex:    ebc8edea8a8b3c9a65a545a48530116bcf86ff0bf143445aa43d0713c7ee5f654f
SHA256 hash: 8286beed3d632e3c9f4cd8a4d0047b811b64a5542793cb6517558fc0ce3b6059
                   |

Data hex:    a56db9bf616dc9e028defe5b8e43fc2db704ff1fcf0148e19a7647a5b2c5e0b17d
SHA256 hash: d5a23b9fadd9fdb9ce843caba0acd41efe6a312327386fe7bcb86f99d0d94761
                    |

Data hex:    ce77ecfebc73d7da59ee48c4a031fdb2f5f76343264a531a30a8de534f6e3d1114
SHA256 hash: 974d5b9bb869b05f2c8ddcf08467d372ebcbe05a312132e22cc342c483e1faa0
                     |

Data hex:    81a3e9dd29f9c6c3f340160175e92f121b58cfa2df9cdd5de8da07d64b8577d5e0
SHA256 hash: f6dd5adb59ef7050518c0a087115b562af9503f216915f914678386c3e75f103
                      |

Data hex:    12f1258d5bdf260f080e5ff809daf2ea92ed387dbeab1106d1f398b43328257764
SHA256 hash: 6b572d035adaaa665671a7928ff5d4ed7e94f41e549e5244bee9022c0a72d284
                       |

Data hex:    20c03bf2548e571ec96607622bfba73bb619878b3de5a3a0ffe21a64f179d96358
SHA256 hash: 6ab42f67dfae0bd0bab8de89a27f4a9ff44ff4af6b746ae5e584c29e8094be83
                        |

Data hex:    3f1e61c989043dee74f7e624f1daffd67c2472619dabcd7c42ba82bfc795a93567
SHA256 hash: 504bdacda8633ce12f66f0a8387b0c53ac91c331700878709645bc6921a1f636
                         |

Data hex:    acc7f79900bac3fd6b9fefdd25f6afffa6af6e09d70534ef2184bfc94b8ce1b5ca
SHA256 hash: 9fc34dae8e97c329f06a4aef02a3c93de045d64f2bfdb7a561a754aaa31444bf
                          |

Data hex:    47e79b1a1c54b6ab93d8d9cc4f57fd1e1d75b476b6e7317f11beaf37fa2016bdde
SHA256 hash: a07b4fafa17048ae438b8bf1097940c248cfaaa3421e3aa20c44842c8cef1a82
                           |

Data hex:    0cdafdebb0afc891d680cf4c2df7cf2544b8d6ec61e61403394c1767046b9886b3
SHA256 hash: 60c361e42f431d91910a0cb7007c30d7df056b60a742a6b207bb9fba23430f78
                            |

Data hex:    5dd3bcdfd15efae22ff930fee0276ecf6708ba6e62a170fcd0e6783e8954843b4f
SHA256 hash: 8e52eefd65b5e0f52c2ed4b8889854cf2c6a350d71ae8c63e598c9cdf0f2bb7f
                             |

Data hex:    39db71d3fa3ed45e2d4fb272551bc24488a007b004ff5f0803838e525c5363b217
SHA256 hash: 82c90501bcdf1f59ed2bbbe89f01d37a25dba2e53758a97a9d7e6bc1e9ddeae3
                              |

Data hex:    40ccce6719ac75fde33a38efe8f656f6e18148429c73d31ab421ca89157007b6d8
SHA256 hash: d68699b88ba19254873f4c98509018be811ddce2a4cdbc17f730be21202c29a9
                               |

Data hex:    e59428633814418b480af49ee12ebea8f869bb1180d2d5bbee3f725a12f0210c52
SHA256 hash: 03444529e87d4ae838da9d51ea3fac54fcde47a4d35395f9fb75ac3b62987230
                                |

Data hex:    831cfaab20b643b1be985ce715658e3ad86336cbafd6a0d5da5c5e3421dd4ffcd1
SHA256 hash: 91eb608d714ab98c379658a45657e57468489e022971b932cbf1a092d6b78978
                                 |

Data hex:    139d88d11372bab380e67652c04b280b70120d320bb98e45fe03913a31414e61be
SHA256 hash: 038e277638feb433a1fe968366ea9eea4e8d330ffb666291f5247031318b529f
                                  |

Data hex:    b96a876c4644cdf6a3df6ed08c2ca25e29960c98b71a004e77cc8772343004d515
SHA256 hash: 98594a32722118b6f193b3d9080e9f854952c5c269c9efb024f4542413684ae6
                                   |

Data hex:    ca583444d1b62b313f49892a477e1bfb2e580f5cde3d8620918ddcd6a9cb10f42b
SHA256 hash: 81cad2f1420fd655b253d6ca91118e7bc22573b64d944133eb01a42803f2a756
                                    |

Data hex:    cf61bd5b70d506b59e7e50f4d21583c83cc2c5dc2d07cd9b46636f0deb9d75aba6
SHA256 hash: c3cf6e31d7e02254e569ceadde176e17b76fbf6ec0fe8ea90afb91c943b7ca58
                                     |

Data hex:    66b965302e6feacd95fd4a7e07b0a3bcb84b142fe41a922b9f4dd9bde321599dc9
SHA256 hash: 35692720ff7d2d52be9924ad27d7308642d44b85d46f6ba8814c1fb445643fd5
                                      |

Data hex:    02f1da4dbe1a4d89284d5c90cd38f690e80161aac992c0b179792911eb0041e869
SHA256 hash: 9147a5d2c2874ca2e24879f00f3ad42c584e460c96cf279c0638e100f0170d87
                                       |

Data hex:    20fe94bfbcf3071231c64e8dd21a0d567ee24840f97519560f9e70a351d0263507
SHA256 hash: 2961e3d237178a57ff4fd32d828a34c659393fd872697bf160c57f42d8a54903
                                        |

Data hex:    8f1c364c262a38b13c1c97b5ddbf9a981d46dce00f53e34779910d1b51d657366f
SHA256 hash: fee16c2275dffe946967e11636c29fd1a21fc76cf41138092fac05cf43370281
                                         |

Data hex:    c2ce5ec639bbb46a76a0ae179f579291e2ae0b1b46abce9f41ef1370785837b1bc
SHA256 hash: 23cfc12cad57b6e8d0b67aba35e1f245161ef4ab5a808c1e20179f23ad6de22d
                                          |

Data hex:    aa9652158ef8a7bfa6c0b9a50b72299e13e5aae99f90b9af6a28dff64fc34dc9d8
SHA256 hash: fc5f127227425df48faa8eaf53bcd6945bd97aa6d7f9092a49b6f5bd010efc9d
                                           |

Data hex:    0c5680d70c2ff75bbf901ec039079f5bb098f4c9aaf2b6bf479cb1df34d565a752
SHA256 hash: 72226122ad80a8f12fa8c4df9fb794fbd0d0bd89b826c5ad7c72961cf0ce8f0e
                                            |

Data hex:    d5681c6d96b5167726f63ea2f3c46f9dd39ac95f25ec7b5af055fc2ded72211ca4
SHA256 hash: 9e127d1f4efa571eaccb9ef503e902bedd57715b639a805e374d2b01c9520b4e
                                             |

Data hex:    9ae21f61150e04bb9eaea69a15ac08108b978b3d27de1d4bd1c4842d84ccfa2a32
SHA256 hash: f9da342a7be514c1d2236bd7856016833b88308fde331fa097575fba687bf1cd
                                              |

Data hex:    dfcc08a43cd006b45bbc9e88a3dbde230caabaa73761f67e97f8454e6335091c2d
SHA256 hash: e37616f0a9e71d1f4b8f1be8b892a822c7a5d00ea0389e18561de077dfbfcedd
                                               |

Data hex:    49ccad6196913202c84f124ef04f0caa64e06da8f190a25428508554c37c14d2ac
SHA256 hash: 40c0ac2c59d979ec8219d5f1b2381e92bd00be9bbeefd912efbf2e2d39249ab9
                                                |

Data hex:    8d406f9b01b031f0c69f2b49065e5af725452564825e7709f788a2c0f681aa8c03
SHA256 hash: 54d28179c76047be1c1c3a788992da97a8cc25fb5e0e2d48c487471140f68167
                                                 |

Data hex:    cdff47f1733da140c0ef4acd5e8010386840308aa67e44e4a55f00584c6d388e30
SHA256 hash: a6d48ecd195037fd340243ef06cf4144647690fc4746772b8ef9ccafaafa5d80
                                                  |

Data hex:    614c1dc59343e2d9cc0353c289f89da0ebae1ff2fa807639c9385e0a69b9b2a3bc
SHA256 hash: 362a0ea926dc304a0b83b3b8a308d8dacc8b7ffd6a4239c41a9a54c2c4d09244
                                                   |

Data hex:    d8dfac81911e02e2ab251e81f550f7dbdaedccaa2f75230182c2f3608221d75ee7
SHA256 hash: 15df783c5f964c85c0bc56e098a3a48e6e58bf0aa403aa7bac5c8472191ade05
                                                    |

Data hex:    d85b375470a7589eb858f1a0ec9d28b85b87f88e8cf08d2e6dc3c98357121645d2
SHA256 hash: 0cbc26a7750ba096dff3886d5fa6f4284193ce79800793e92f85930f82ad9de9
                                                     |

Data hex:    659370d651b4ca9a99c358676d063af4e386663743e96770b0877d8fc2f4d43db7
SHA256 hash: 1f978413fbaeeca0dd9417dedd2904bd2812853fa35533071d9e51ec7f331233
                                                      |

Data hex:    a5cb4713b5231773398bd7deaad2f8819fc713fe55543db8f22a3067c7a1b27f8c
SHA256 hash: 488e4d758e8e2096f87f5e751d61cd1e848decba48527dad70253a852f5583d2
                                                       |

Data hex:    7ab2af5484c17c1e10825bbe16f840e59786ccbe67117fe7427ffb5eda3ab084b9
SHA256 hash: c46ebe502693aa01bd28740cbbf3efc3e1d5a24332415f3cc0a86927339b54c1
                                                        |

Data hex:    d55b790010ef67a6a938787104a9a205da523d9c243ec4eab783300076dc6a8370
SHA256 hash: 7c884012de10c88a169a4cd9a5732f9145b7a6c53aeec5b189e9c93a6dc403fd
                                                         |

Data hex:    481d42d3ec8e187fea0aca34d025ff4854823a10c388b696ac076d16cc4a0e6fae
SHA256 hash: 9624b1e8a782555c7bdd4358f3201aefd3cb21088ae7b6003df5851a4d388544
                                                          |

Data hex:    5379821939910b1f3c9ae7669505c27dc324e2bcbdf96d6733fd2b18d5ec40241d
SHA256 hash: 72142b1affa73a35b6d7970bd6486c21746a30bad627fa69f4ebf14a6e636162
                                                           |

Data hex:    43cbc6bef23c602eb6dca5efca36ebbe0f7b0635dd2fabf0892ceddfc31ae1816c
SHA256 hash: 200b7b2cb4140cbeb6a4dbce6d99f9e4cf531f73edcc47c01e57c0470e2e26db
                                                            |

Data hex:    ee3e7244f31b9095059f639fa0e0912ca19be69aae9957b5306d65a976c07ea729
SHA256 hash: 9c6edf5f6c283d5dc703a11b58f900a796c61ef805c82d7535bfc5c66cc158ba
                                                             |

Data hex:    ece71935841fe8212eb5d3e3c034ebf482dd155c1e7a08e36c3d0e4f528bccd5b6
SHA256 hash: 8ef0000cc1dc05eae4081dadbd9606f3d086f5514881ac213c3e5e551e8f15bd
                                                              |

Data hex:    a687d35bab65db4f205aadfdf5daf32e2028a3c3d0b8f773c5b8c6f9a04b87f70a
SHA256 hash: 2a49865d379bc8fa43b0be22db33b26cf1fdc9db1a6fd66cf2be9790e2133317
                                                               |

Data hex:    a0ba55f3907c1706d746ce1bdcfd9fe1810135beee6d33fc395bff9bf623af9fb6
SHA256 hash: 809310118e7660df59879dd4f28be624c0a905393917c1fd67fba9e50e0c6c79
                                                                |

Data hex:    bc3e38855126c2610de97ad5516d86530adcc561f00bbd85ea32a0c53b1fd28fb3
SHA256 hash: ae3344ad4648998dbe19ba8b14fefcf59b6fa21156c3d51fc3eda345e776ac4d
                                                                 |

Data hex:    b9e54b7dd07b6f55ca208001260c72b12460a6a4d6cd3c2d0f045b392b1b5ff805
SHA256 hash: 06cd3b37034fc13d9f506958b063e7561cbc502be2417a8fb3a9cb01f70c652e
                                                                  |

Data hex:    ca01d56534239670c80f919c1b4e24b990df5c2a9b84b23ba560dc8564c52d06aa
SHA256 hash: 9352440c9a479e735df495a0feaa85623898dad434a8e59b5366808fbbeffc4c
                                                                   |

Data hex:    a6dfa3fc109cef98dba516a7d0fe0c8e70efc2cde6daae32a11f9e2cd6243ab268
SHA256 hash: e6386b064966202f08b45e76fc7127501f78ff687ccbd78a484dcf0c08fa0cc9
                                                                    |

Data hex:    eb1402551bdfd910327c3bfb650b3ae8f2e5c7194493fd767dd34718c6fb72b701
SHA256 hash: 781a7bb21e6dbe1b521f64c9f47d2c17dad1c125ec17c549a6236547c531cc05
                                                                     |

Data hex:    010ef77064b7a5e70286dbd201302516f644fc532126c5f8dc3c5655c3e19145c3
SHA256 hash: e0f3e697d0cceeeb1dbc6ed86a49f357ac099e333fa9434385c6cbdba3028c36
                                                                      |

Data hex:    e3d5d57b413116842551727b072950db76fcfe4f90bd8107a0d0f6bc2e6f9c8cc4
SHA256 hash: 4235feffd6931d5842803a06444d0107d9aaf04be0f220d6f20753f11e699e8f
                                                                       |

Data hex:    af1d6427315179bd6ea736efd764116f468656e07e7f201f0c5129b078537455a1
SHA256 hash: 07624d78c4293fbe5d25fa2d6d7b6a02fe689a441a46c30087e5cc3cfae34654
                                                                        |

Data hex:    6166c8102b4f3bf50d10c7567081405cfd9cebb3d0e8b9d2a380b305e59fbd103a
SHA256 hash: 531022940fc6a3468d6237d149639b545412c42153abefe856b4151e9340b0d6
                                                                         |

Data hex:    57e039973c9889c684a22f6ceba06c6715c47c043b41b7c767ae7d44277c963569
SHA256 hash: dcd1d384b793e4d731ffa0cb2ba5c825f2ca7b1deb3dce6dc173a24d9267a6d6
                                                                          |

Data hex:    575f23c20089da66130fd8f6d4a075932ab0964ecf483567b806800210f859c0a2
SHA256 hash: afc11e8a7583663300f66fe63b51648330c252147ba095969a6c7a23f77078c9
                                                                           |

Data hex:    058662b74269ce8e287cae2923ef0c37f34beb3bd8036fbce07f1c1d240f2710f8
SHA256 hash: 1c0b6a8a85cba42f8e9f7da0a2918b1eacce42eaeae0252026bf47bb1a6aec70
                                                                            |
```

Some data where i-th input and hash byte have the same value:

```
Data hex:    df004f3668a85190c1cf4817a7db89a1cc645bdeccb1e4dfe0c8b4628fe7e05d03
SHA256 hash: dfb8fc900a70e7a309e80f082b38b6010fa58cae74c4c41b4b69e825ed4655ae
             ||

Data hex:    d4446537f8442a6290a314a53648f9b017db81ac30ab95ad4a434fb491d2a820a5
SHA256 hash: 2b44180a8009da7c963aa1b550c00500d2a875ab200ee35f4ca80a6b95666383
               ||

Data hex:    8e1561fa4bc38438d9d74c81d880cbb415508ab0abf3dd42893dbdb45a35418996
SHA256 hash: b9316191cea4cc5c31756dfed9a24866fb919164f36fe4c9637f68654d5252b0
                 ||

Data hex:    46286aec3e8e2ce57451c6c78850b0ef1fa44029f85ad78f47571b1c9e401e1c6a
SHA256 hash: 1a16d3ec98cc04f79d8e370f49cf08d86238059992fbfccadadcc5e71b40c4c4
                   ||

Data hex:    60723f7e49dee2fedbfb958b3eb571efc64740d9511af50a39beb048f1228c53b1
SHA256 hash: 9b12511e498a697a5ca59189ba9f4deb63a3ffdfcb85064ff04bddeb9b640f09
                     ||

Data hex:    721f2281cfdb27ad0c3bba80f58661e345ce4ba4515250f160b80d4aa10ad07f05
SHA256 hash: 993f32930ddb7e1728839648e5a1dd95d68c3d0aeb62ab664d69591f234c5bd1
                       ||

Data hex:    97701f31d1b4d1f90c40bc0af7860d055e7b3ca6684cbc370cd22284e86f6b538b
SHA256 hash: 7d4deba21bf3d103d16df21be5bbc2969595fdd5347db9cf36a13f2c9d271bb9
                         ||

Data hex:    f9cbc9fe9829b087eab5e0bf95f84c2a2c642e7e05e9089a9144d85c4cb06aee16
SHA256 hash: dd6e1af2f441a78729808cbff4443f9aa477d4dfd6aba8ab5418c9fa58aaca7b
                           ||

Data hex:    a87d0f5b6f5e091c1bf009c476fe5f13367b80eb72245474f000aba8e8f25d73a7
SHA256 hash: 2fdca8a56346a8351bcd41c64de5e18ad8d180a7c32a19f06e1dad0cc796bdbd
                             ||

Data hex:    82d8db5356aba178654eb1e2505e6356aaee82c4aa0173e9b6925909c96feda1bb
SHA256 hash: 4c877ba06ae353fe7f4eaedb14be8a0de2e5fbe8c29ae79151f07a1b8b9d2504
                               ||

Data hex:    bd36d89ec38126c80d0d8dfe95f28e03968b63208bcd5958c502b16341f4aaf831
SHA256 hash: db9fd5694ddf6631739a8d60020578dec96cbf7c085c3ed962da2f57de82290f
                                 ||

Data hex:    facf1c519dfb43db1aef3b49ca0bf7cf9bb4795326f044ae3ddbe14bbbcdcae179
SHA256 hash: f684635b3cbcd995575ebe499b1f9aec5adb6c3fb63b2ff119412e77796ba82e
                                   ||

Data hex:    7ddf4bd0276b92adf20bd03afad2c6282187ebf58787cebdec1ab7e1ada75e3156
SHA256 hash: 4e97965f13b5954270e32be9faca20924e23f24b73f34d9a3843ad57ecd5616f
                                     ||

Data hex:    fabd03bd729d499319d5d0dcad1493ee27501861af5a27ff9f210f67ffbfeb5bc2
SHA256 hash: daed2f69572a987108f9ba96621418b6627d228e26966705714e211108d883e9
                                       ||

Data hex:    65b762a4ab838f297f894e767f8ffa063db4a30798beaa79ee293ff5acccab03a4
SHA256 hash: e20d474491990bcc623f8ad60eb5fa684729f42d4bf2924e12cb94287a2cd80a
                                         ||

Data hex:    1f1e50e24e71c5b5d4983bd1063c47c69bfe2fb70b6e77ec3ebfd43c94d76934aa
SHA256 hash: 9b78f0b9fa49873f11b6029c957523c6572223088f4f40b3a35a160ad15a7a3e
                                           ||

Data hex:    f1e423e34daf7e6157ff13e43f6ae3d817aec28079b82d2ae2b5ee30b97707fcf1
SHA256 hash: 2ca94a72c2c398d47df358f44a470acb17385c8ee446672bf2dda6e33d9ac4e0
                                             ||

Data hex:    72c727ff28314a29f211cffa7f021e2fb6c9daf9741157690300f00cea895d5660
SHA256 hash: f4fbdfc302801724bc31bcee609d7da6e7c9e3b6bd606f07d6f2cd43a8fc629c
                                               ||

Data hex:    2e432a72dbcfeab27fbfd5122a9926e74f29c8e23f70427cb41007942a402d344d
SHA256 hash: 59715be2f12395882035704d43de2a132316c869d017bd7cc9492ac32cb9a3a2
                                                 ||

Data hex:    6b2254839058410d23bd8bba83d3f6bb70163738c8051a90f1a53c900152f4856f
SHA256 hash: 7f82cbcb5a13e3495da079b9e3c748dce19ab138d68f74d5144c56bad144097d
                                                   ||

Data hex:    bfbc1f10797ff302ba88fb7fd7eb06ec8c4182e2e4cf67d48847f5d3bf1fc00857
SHA256 hash: 9209a3555d282f7b1558faa1a1047c25581f91cce4cbc58096f0882550d60418
                                                     ||

Data hex:    27e6a3ed3cbc4fc158cd6e946a0c7e7d343547e47a33df8a3a5c9f197c456a180c
SHA256 hash: 9987f71c36a6ce79238df433a2f605b5000611214b33a0fae3aa5383c8d93bc3
                                                       ||

Data hex:    0c3f8f338565b0898243f86c82a2a9aff41d93895ffb43298d8abb5b78c5d44c1d
SHA256 hash: d6226889d399598ec3b04d23a98b372892fe908f54064335dac33eaa42192cf9
                                                         ||

Data hex:    1ddf91b9a16a8a60ed2cc2eaf62f78c5e2c8ba25c63507a9a1ba14e1d004d2204a
SHA256 hash: dc01dc3d5d904f44e1317cb6b7a1ed96c27c6f916bd6eba9d050e519814cb099
                                                           ||

Data hex:    fe70a788afb13fe5d8e3f5bb43f518b1f098fb3fcc548fa994d8758bbdf88be952
SHA256 hash: 3e1bfba24d0fc3b1d361ccc4ae5a58a7da2508a4375dc951941144999d221eb3
                                                             ||

Data hex:    d6c3cd57b4065b820fc1e42aa0db46576ea4c43597d0152010bb73802498e81a37
SHA256 hash: 89e07e4d3ce18da84c520b1ba0b00f389b6176916aadf0a372bb4ee43dcc8c9d
                                                               ||

Data hex:    9fca80acba59f85b109b93d30d0780583d6104d17b27866cf9ad4cc635d3267c9a
SHA256 hash: b7cce8a96f57dc978b4f57d48351fed4e12859c045f8521728594c7b3cfeabcf
                                                                 ||

Data hex:    973e6af49f74eb28598bc950e5302aefde6bf2d9700a4d007fe91c8b77a3bd7434
SHA256 hash: 11de5af20767a4f2a16469a195559f7392de531ecb0c8e0c4b3a058b85b76499
                                                                   ||

Data hex:    dd3304a5e6fb326f9c3b4f45dbcd2c2145bf7f3f17a0500263248b5f000f01770f
SHA256 hash: 6df22d2dd1b50286076a3fd25527de6334efb1cc20312de8b9805a5e00c0145a
                                                                     ||

Data hex:    591ccffb90f2e52577cf7983bee2549dcf643b309e7004018b927a97bf6c208fc4
SHA256 hash: 6e731c3be2081f35064fb7bac2df4170db89f6e026ef8b50c06e907f9b6cd1f2
                                                                       ||

Data hex:    42efa51d22df01a2d3a72e4fcfa5cf35a74db2175bc671e70a688bce2d229cab77
SHA256 hash: b2062cb7046ea800b250d291ad5b93bfdaaa9926f10e51b5afeaff25601d9cdc
                                                                         ||

Data hex:    6e9425f6b10368c23e3442912ba1f0e83b7e40c304005eb82681a09de5de15f338
SHA256 hash: 0f955ecdb3ef0b99367c50829eeafffce1dfcd248df1a7769d43fcdf2c3dfef3
                                                                           ||
```

Some data were the i-th and (i+1)-th hash-byte have the same value:

```
Data hex:    4d631d13974bb0272fa8f76277973894fb06a9ed9a47a51ace97aef5c7871bd446
SHA256 hash: c0c00f853e8f4a66b865093474bba183bc700aeeec5f787cf38c743192a3ed59
             ||||

Data hex:    e0709d1e999a54cae87cf19c861544354cde6f940b504904e136b9e224fe193b53
SHA256 hash: 86a0a01213f850a324f1f1a4f7c10d3222d6725e1718a80c1f60600b215570c5
               ||||

Data hex:    f21bb9c5c072ce626212b580b6c9df8c99878e161cf4f9320c20e76cf3e73ba79e
SHA256 hash: f4161414a266203093b157a10977c5ad713e3ad97125fe84fb5900050d79f9f3
                 ||||

Data hex:    b7e83d319660af170c68da894ecd2a0d8f68e72a9cc890f8d14bd4c46f17eec019
SHA256 hash: 677106ebeb6bc0ecd9305b204022b4fdca78cc480d5063133bf021286fbba472
                   ||||

Data hex:    99b03a77168d20cf23719725940d84f2c53a8eed07fa51fc145b7122c8e718ff66
SHA256 hash: 9dc420bdcacab8350a842a908ce367e040aeec4e71249164e28606c6425146bb
                     ||||

Data hex:    6fafd8e03c1846736bcc7e278a8dc696b1d8ff345c0f0c56ded8aacd677668f4f2
SHA256 hash: 0beb993386b4b4b9de1c7b96f85fba4b88a6f68c4769f15268c0d31e47350f5d
                       ||||

Data hex:    324ec4e899d88059a6df2f66f183c0b697d2ffe34adc34f9d1f03df55ee3ceec02
SHA256 hash: 399701d2242295953a79ac0aa554284e64a16010a4f64eac5090b263154c12e3
                         ||||

Data hex:    295480d542c0d916c4934db024e0735b58a15fc42e65205139b1d09bd34ae742a2
SHA256 hash: d86d791ec751d4fefe9a87e736b09272519206e4bfbafa571b7267611f0f6672
                           ||||

Data hex:    f894845fd5ff380c38cc8b5cf200bf84489c01755188d677aa026ae44f8e308828
SHA256 hash: 523dee9c23c22eebf7f77ef3c542e74f1f5273f79d78f45b22fec126fee6e4de
                             ||||

Data hex:    bcfc6ed347ebf3a55a4f5cd49d0e530da78d760fafddeb4dacc6b2a849055a45fe
SHA256 hash: a14bbdaab7e5ef13c6a5a5e71386a9b6a34843707654b147cebb83f3eabdb1f7
                               ||||

Data hex:    4efe7dbd300505d6d40a8b7fa6c6ccbcd93e189a658c81a783ba763603d527b7fc
SHA256 hash: cc5879eede108037657dcdcde0a172ed70551ae101ce07eff4185e888a964af7
                                 ||||

Data hex:    1d4aa957a7d961b844d8ffcbf1ce838a5a8491d97da59b56afd7f2bfa2fc7a2fbf
SHA256 hash: 308dde78ada99fc6bb22067070a71b50549428bfd0296693a24eedd75e203ee7
                                   ||||

Data hex:    cdf1341e3d7b7cd3cbc76e36549269457d6bda9dd7c07a88e5659d98848fe5d3bc
SHA256 hash: b87da02e359408ecc868a2616a6a193293cadfe44fd4909e6ca311b61f8c5be0
                                     ||||

Data hex:    c2679c87538a3928c55c7f9ca98a5be20b218483a1d213d3f8d8dad6461561cd55
SHA256 hash: 024e23550db40d125c876f048ecdcd20520be3dfb20ad8eff543ba6deffb3c9f
                                       ||||

Data hex:    111901c55c4f10510c26fd3b576b2d02fc86c9e6db8ed8e35444ea043470531d5a
SHA256 hash: f8309104f6a646b89bc320b85c7b3f3f3737f0c8d1a32e1714bbf03a398f3be1
                                         ||||

Data hex:    9e432992702dbf7a5c09d7ecaa60c3a687cb747bd8d5ddd112395ad920b2566e73
SHA256 hash: 3923150f1e18b98733a7515c43b2278888a725a3deba62cea8747bc49bb88c2e
                                           ||||

Data hex:    775c51b515ae4dfc438e27ad21262afc478a7c70c51bbe4faf33c3fc01bfe96079
SHA256 hash: 321e1a47006a578a2e254fd7a4fdbde48c8c10cc8169f141ac6990dbd30532b5
                                             ||||

Data hex:    309cb7b1fc6e31d3ad49e60e97e2839948788fed4212e3b173ae07d74a76f00406
SHA256 hash: 69105d12ad9527c74db5b059d16e66abb626267f33c2e8fc5acd74b2ef3e498b
                                               ||||

Data hex:    2f237d7b715aa44cdc01ec04cacb63284b68a0c7e855fedc21f69d3e31df68b99c
SHA256 hash: 3f2a26b22e0c65f2fe071ee1fc33d959f38c0707531bd896404caee6c4d4ce53
                                                 ||||

Data hex:    b4dff0ed553775f7596b41ff5371e689881d1177ee44f2811fc7deba1d6f991621
SHA256 hash: 5f9a1fda447323a3a25799b2bfc565271fb23ccccc05ada3e5d6bf1ffb178f61
                                                   ||||

Data hex:    63f1d01074ee36b4360bcaba0d7d2ce9d8b5755c6d3d7a92ba13ab3645cd3e3020
SHA256 hash: 420beae261ca58bb84aa8d359878fb1e35a74cd72626018d7641af662a47c24c
                                                     ||||

Data hex:    f918ef13f4105cc1893ce3951492fb26dfc3fc17cc1044701d1ea2e4b3792db40d
SHA256 hash: f65b824d4f4db142c6d41186c13e9efe35ebeec53d8484566c4e38d7c0f5bd6a
                                                       ||||

Data hex:    950e49b215b8ea8e553393f8cb7f258566ab919a9433a44ea7e886b50a59249d5e
SHA256 hash: 674ed73b71ff49e733102b6515796bb747489419f9fb0a0ad8b82603ee57174a
                                                         ||||

Data hex:    682223e142499fa3b3a0553c39c5f6017f116c7bbc384ab2b8afb9ecdace848c17
SHA256 hash: 16fbff1cdd3189d1257d9b00100a6231d17a1361a785ab3e3e86f4025192bba4
                                                           ||||

Data hex:    e6def8f0e2645e28fdd371b28e8fda9c15e0a61e17de72096de65ee774495c7bd8
SHA256 hash: 6e663a70d121f656b00a9a3e5b070c1758b53c5e9dc370750101fe3d8c9048df
                                                             ||||

Data hex:    57f4cfd87a2f029a6c5649de70d5bdd593c432d2acbd125f17e15b68791d9e56dc
SHA256 hash: 51d2c0eb3c0d13193ba0bf1acf03721b259ecf7d8d23114adcbdbd9a6667c912
                                                               ||||

Data hex:    0d208959bfbe650486f83f6c82fb98089bbd9c1de4992501768aa3519166efc016
SHA256 hash: 308cbdd19682ca3cb63479704381ebe8e6386e4c1bd1685c576c6464718f9397
                                                                 ||||

Data hex:    3850231c9f057296b4e349e1e1f63bb90fc599e6a44cfd10ef6d71cfab8a0e4a03
SHA256 hash: 3992bb669fcf4e03d3dd133943cfc205a5a24027d3b85c9b50e460bfbf8fc748
                                                                   ||||

Data hex:    73e87f527517f4f33145a49ce91f6682c14b895aa0abecbbda37daf93f576c4cb3
SHA256 hash: 80484e47d6d2fad44e22d18ca62a0c54da0a83049ded4f867ebc9a4b9f9f92c3
                                                                     ||||

Data hex:    6e155b8a6533e375b997e0a7c5efd7430b5f9c9f1fb4270eebe3e37e110bbb6e16
SHA256 hash: 9c562c0868259b7a921c7bf0552922dfa9d099ece73b06d0c5b5f3bc14c0c035
                                                                       ||||

Data hex:    e1c82a6c260f28996f35401c20829b03c982caddf970b346a872cd75d7df09f7de
SHA256 hash: 83c6f5a8c9ab72c3207d45fd6e1baf4c03399b3c92a2e6d3d153f11dfe51b7b7
                                                                         ||||
```

Some hashes where the i-th, (i+1)-th, (i+2)-th, and (i+3)-th hash-nibble have the same value: 

```
TODO
```

TODO longest subsequence of same bit value
