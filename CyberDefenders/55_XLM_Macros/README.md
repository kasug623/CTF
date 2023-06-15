# Learn
- VelvetSweashop  
- the way to use `oledump/plugin_biff.py`  
- the way to use `xlmdeobfuscator`  
- the way to use `msoffcrypto-tool`  

# #1
```bash
$ xlmdeobfuscator -f ./sample1-fb5ed444ddc37d748639f624397cff2a.bin
$ msoffcrypto-tool --test -v ./sample1-fb5ed444ddc37d748639f624397cff2a.bin
$ xlmdeobfuscator --password VelvetSweatshop -f ./sample1-fb5ed444ddc37d748639f624397cff2a.bin
```

# #2
```bash
$ msoffcrypto-tool sample1-fb5ed444ddc37d748639f624397cff2a.bin sample1-decrypted -p VelvetSweatshop
$ msoffcrypto-tool --test -v ./sample1-decrypted
$ oledump.py sample1-decrypted -p plugin_biff.py --pluginoptions '-x' | more
```