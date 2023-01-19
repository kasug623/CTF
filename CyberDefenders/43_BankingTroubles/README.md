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
```