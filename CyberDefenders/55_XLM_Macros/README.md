# Learn
- VelvetSweashop  
- the way to use `oledump/plugin_biff.py`  
- the way to use `xlmdeobfuscator`  
how to undersatnd logic and background knowledge.  
- the way to use `msoffcrypto-tool`  
how to undersatnd logic and background knowledge.  
- oraganize of `abuse.ch`
- the way to use func `'GET.WORKSPACE()'` of VBA in Malware Analysis
    - Point
        - GET.WORKSPACE(2): Version of Excel Running
        - GET.WORKSPACE(13): Workspace Width
        - GET.WORKSPACE(14): Workspace Height
        - GET.WORKSPACE(19): If a mouse is present
        - GET.WORKSPACE(42):If Machine can play Sound
    - https://0xevilc0de.com/2020/04/12/excel-4-macros-get-workspace-reference/
- anti0sandobox
https://securitynews.sonicwall.com/xmlpost/improvements-in-malicious-excel-files-distributing-zloader/
 - malware family "Zloader"


# #1
sample1 starts.

```bash
$ file ./sample1-fb5ed444ddc37d748639f624397cff2a.bin
$ trid sample1-fb5ed444ddc37d748639f624397cff2a.bin
$ exiftool ./sample1-fb5ed444ddc37d748639f624397cff2a.bin
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

# #3
```bash
$ oledump.py sample1-decrypted -p plugin_biff.py --pluginoptions '-x' | grep http
```

# #4
URLhaus

# #5
sample2 starts.
olevba, check the result.
```bash
$ file ./sample2-b5d469a07709b5ca6fee934b1e5e8e38.bin
$ trid sample2-b5d469a07709b5ca6fee934b1e5e8e38.bin
$ exiftool ./sample2-b5d469a07709b5ca6fee934b1e5e8e38.bin
$ msoffcrypto-tool --test ./sample2-b5d469a07709b5ca6fee934b1e5e8e38.bin
$ olevba ./sample2-b5d469a07709b5ca6fee934b1e5e8e38.bin
```
```bash
$ oledump.py sample2-b5d469a07709b5ca6fee934b1e5e8e38.bin -p plugin_biff.py --pluginoptions '-x' | more
```

# #6
olevba, check the result.
## other solution
oledump, plugin_biff, check the result

# #7
olevba, check the result.  
*Note: Characterisics of "Sandbox" in register about Office*  
```
HKCU\software\policies\microsoft\office\<Office_Version>\word\security
```
https://securitynews.sonicwall.com/xmlpost/improvements-in-malicious-excel-files-distributing-zloader/
## other solution
xlmdeobfuscator, check the result

# #8
olevba, check the result.  
*Note: the way to use GET.WORKSPACE of VBA in Malware Analysis*
## other solution
xlmdeobfuscator, check the result

# #9
olevba, check the result.  
If you search about infomation around an environment, you should search keywords about an environment like "Windows", "Mac", "linux", "VMware" etc.
## other solution
xlmdeobfuscator, check the result

# #10
olevba, check the result.
## other solution
xlmdeobfuscator, check the result

# #11
olevba, check the result.
## other solution
xlmdeobfuscator, check the result

# #12
olevba, check the result.
## other solution
xlmdeobfuscator, check the result

# #13
olevba, check the result.
## other solution
xlmdeobfuscator, check the result

# #14
Hash->VT->check Trend Micro
```bash
$ md5sum sample2-b5d469a07709b5ca6fee934b1e5e8e38.bin
```

# Ref
- https://forensicskween.com/ctf/cyberdefenders/xlm-macros/
- https://0xevilc0de.com/2020/04/12/excel-4-macros-get-workspace-reference/
- https://malware.news/t/excel-4-macros-get-workspace-reference/38892
- https://www.officelabo.net/sonota/get.workspace.html