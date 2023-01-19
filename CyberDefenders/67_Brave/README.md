# Writeups
## lesson
- The way to dump is changed from volatility3 ver.1 to its ver.2.
  
## question
- What is a difference netween "netscan" and "netstat" at volatility 3?
  
## #1
```
$ vol3 -f 20210430-Win10Home-20H2-64bit-memdump.mem windows.info.Info
```
  
## #2
```
$ sha256sum 20210430-Win10Home-20H2-64bit-memdump.mem
```
  
## #3
```
$ vol3 -f 20210430-Win10Home-20H2-64bit-memdump.mem windows.pslist.PsList > windows_pslist_PsList.txt
$ cat windows_pslist_PsList.txt | grep -i brave
```
  
## #4
windows.netscan.NetScan ... 10 (answer)  
windows.netstat.NetStat ... 9  
What is a difference netween "netscan" and "netstat"?
```
$ vol3 -f 20210430-Win10Home-20H2-64bit-memdump.mem windows.netscan.NetScan > windows_netscan_NetScan.txt
$ cat windows_netscan_NetScan.txt | grep -i establish | wc -l
```
  
## #5
OSINT, whois  
  
## #6
```
$ mkdir output
$ vol3 -f 20210430-Win10Home-20H2-64bit-memdump.mem -o ./output windows.pslist.PsList --pid 6988 --dump
```
  
## #7
binary editor  
  
## #8
```
$ cat windows_pstree_PsTree.txt | grep -i powershell -B 15
```
  
## #9
```
$ vol3 -f 20210430-Win10Home-20H2-64bit-memdump.mem windows.cmdline.CmdLine --pid 2520 > windows_cmdline_CmdLine_2520.txt
```
  
## #10
```
$ vol3 -f 20210430-Win10Home-20H2-64bit-memdump.mem windows.registry.userassist > windows_registry_userassist.txt
```
 

 
