# Writeups
## lesson
- The way to dump is changed from volatility3 ver.1 to its ver.2.
    <details>
    <summary>Details</summary>
    The difference in results between using the netscan plugin and the netstat plugin in the Volatility framework can be attributed to the different sources of information they use and the way they process that information.

    The netscan plugin uses memory dumps to scan for and extract information about active network connections. It searches for various data structures in memory, such as TCP and UDP tables, to gather information about open connections and the state of those connections.

    On the other hand, the netstat plugin uses the output of the netstat command, which is a command-line utility that displays active network connections and network statistics. The netstat plugin runs the netstat command within the context of a profile and collects the output of the command, which is then processed and analyzed by the plugin.

    Due to the differences in the sources of information used by the netscan and netstat plugins, it is possible for the results obtained by these plugins to be different. For example, the netscan plugin may reveal network connections that are not shown by the netstat plugin, or vice versa. Additionally, the way that the plugins process the information they gather can also lead to differences in the results.

    In general, the choice of plugin to use in a given scenario depends on the specific requirements of the analysis, the state of the system being analyzed, and the type of information that is required. It is important to understand the strengths and limitations of each plugin and choose the one that is best suited to the task at hand.
    </details> 
[details](#a-difference-between-netscan-and-netstat-at-volatility)


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

## description
### A difference between "netscan" and "netstat" at volatility.
The difference in results between using the netscan plugin and the netstat plugin in the Volatility framework can be attributed to the different sources of information they use and the way they process that information.

The netscan plugin uses memory dumps to scan for and extract information about active network connections. It searches for various data structures in memory, such as TCP and UDP tables, to gather information about open connections and the state of those connections.

On the other hand, the netstat plugin uses the output of the netstat command, which is a command-line utility that displays active network connections and network statistics. The netstat plugin runs the netstat command within the context of a profile and collects the output of the command, which is then processed and analyzed by the plugin.

Due to the differences in the sources of information used by the netscan and netstat plugins, it is possible for the results obtained by these plugins to be different. For example, the netscan plugin may reveal network connections that are not shown by the netstat plugin, or vice versa. Additionally, the way that the plugins process the information they gather can also lead to differences in the results.

In general, the choice of plugin to use in a given scenario depends on the specific requirements of the analysis, the state of the system being analyzed, and the type of information that is required. It is important to understand the strengths and limitations of each plugin and choose the one that is best suited to the task at hand.

 
