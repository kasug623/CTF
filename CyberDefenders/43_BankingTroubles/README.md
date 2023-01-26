# Writeups
## keyword
- DTB

## lesson
- There is a difference like a bug on valatility.
Sometimes volatility 2 can do what volatility 3 cannot do.  
But sometimes volatility 3 can do what volatility 2 cannot do.  
[https://github.com/volatilityfoundation/volatility3/issues/631](https://github.com/volatilityfoundation/volatility3/issues/631) 
[https://github.com/volatilityfoundation/volatility3/issues/135](https://github.com/volatilityfoundation/volatility3/issues/135) 

## question
- volatility 3 cannot parse the memoty at this time.  
  - I tried this but this didn't solve it. (cf. [https://github.com/volatilityfoundation/volatility3/issues/135](https://github.com/volatilityfoundation/volatility3/issues/135))  
1.DL symbol tables from "https://downloads.volatilityfoundation.org/volatility3/symbols/windows.zip"  
2.replace "windows" folder into volatility3/symbols/  



## #1
```
vol2 -f Bob.vmem kdbgscan > kdbgscan.txt
vol2 -f Bob.vmem imageinfo > imageinfo.txt
vol2 -f Bob.vmem --profile=WinXPSP2x86 sockets > sockets.txt
vol2 -f Bob.vmem --profile=WinXPSP2x86 connections > connections.txt
```

## #2
```
vol2 -f Bob.vmem --profile=WinXPSP2x86 hivelist > hivelist.txt
vol2 -f Bob.vmem --profile=WinXPSP2x86 printkey -o 0xe1035b60
vol2 -f Bob.vmem --profile=WinXPSP2x86 printkey -K "CurrentControlSet"
vol2 -f Bob.vmem --profile=WinXPSP2x86 printkey -K "ControlSet001"
vol2 -f Bob.vmem --profile=WinXPSP2x86 printkey -K "ControlSet001\Control\Session Manager\Environment"
```
[https://stackoverflow.com/questions/573817/where-are-environment-variables-stored-in-the-windows-registry](https://stackoverflow.com/questions/573817/where-are-environment-variables-stored-in-the-windows-registry)

## #3
```
vol2 -f Bob.vmem --profile=WinXPSP2x86 printkey -o 0xe1526748 -K "Policies\Microsoft\Windows"
vol2 -f Bob.vmem --profile=WinXPSP2x86 printkey -o 0xe1526748 -K "Microsoft\Windows NT\CurrentVersion\Winlogon"
vol2 -f Bob.vmem --profile=WinXPSP2x86 hashdump -y 0xe1035b60 -s 0xe151ea08 > hashdump_sam.txt
john hashdump_sam.txt
john hashdump_sam.txt --show
```
### prontkey
-o is quick.

### how to get password from memory 
1. check winlogon.
1. check domain, dump "SAM" and crack it.    


### cf.
- john  
[https://qiita.com/y-araki-qiita/items/cda417e49108eee1fb7b](https://qiita.com/y-araki-qiita/items/cda417e49108eee1fb7b)  
[https://nekotosec.com/try-using-john-the-ripper/](https://nekotosec.com/try-using-john-the-ripper/)

- registry  
[https://www.mbsd.jp/blog/20190514.html](https://www.mbsd.jp/blog/20190514.html)

## #4
```
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 pslist > pslist.txt
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 psscan > psscan.txt
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 pstree > pstree.txt
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 psxview > psxview.txt
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 malfind -p 1752 > malfind_1752.txt
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 connections > connections.txt
```


## #7
```
$ strings Bob.vmem | grep "XXX.XXX.XXX.XXX(suspicious ip)" | grep .php | grep http
```