# Writeups
## keyword
- DTB
- john
- qpds, pdf-parser.py, peepdf
- foremost
- SpiderMonkey

## lesson
- There is a difference like a bug on valatility.
Sometimes volatility 2 can do what volatility 3 cannot do.  
But sometimes volatility 3 can do what volatility 2 cannot do.  
[https://github.com/volatilityfoundation/volatility3/issues/631](https://github.com/volatilityfoundation/volatility3/issues/631) 
[https://github.com/volatilityfoundation/volatility3/issues/135](https://github.com/volatilityfoundation/volatility3/issues/135) 
- logic of finding DTB 
  <details>
  <summary>Details</summary> 
  The logic of finding the DTB in a memory dump involves locating the data structures that are used by the operating system to manage the memory of each process. The DTB is usually stored in one of these data structures, which can be found using the following steps:

  Locate the process control blocks (PCBs): The first step in finding the DTB is to locate the process control blocks (PCBs) for each running process in the memory dump. PCBs contain information about the state of a process, including its memory layout and access rights.

  Identify the task_struct or EPROCESS data structure: In Windows, the PCB is known as the EPROCESS data structure. In Linux, it is called the task_struct. Both data structures contain information about the memory layout of the process, including the address of the DTB.

  Locate the DTB in the data structure: Once you have identified the task_struct or EPROCESS data structure, you can use its fields to locate the DTB. In Windows, the DTB is usually stored in the "Pcb.DirectoryTableBase" field of the EPROCESS data structure. In Linux, it is stored in the "mm.pgd" field of the task_struct.

  Verify the DTB: After locating the DTB, you can use other data structures, such as page tables, to verify that the DTB is correct. This may involve checking the validity of the page table entries, and verifying that the memory segments described by the DTB are accessible to the process.

  In summary, the logic of finding the DTB in a memory dump involves locating the process control blocks (PCBs), identifying the task_struct or EPROCESS data structure, and using the fields in this data structure to locate the DTB. The accuracy of the DTB can then be verified by checking other data structures, such as page tables.

  But if you want to know the logic of finding PCB on a memory dump, you should read code of volatility's plugins like imageinfo or kdbgscan.
  </details>
- difference between `ldrmodules` and `dlllist`
  <details>
  <summary>Details</summary> 
  The LdrModules plugin and the DLLList plugin in Volatility are both used for analyzing a Windows system's memory to detect and investigate loaded dynamic-link libraries (DLLs). However, there are some differences between the two plugins in terms of the information they provide and the methods they use to gather that information.

  The LdrModules plugin, as the name suggests, focuses specifically on analyzing the loader data structures for DLLs loaded into a process's memory space. This plugin can provide information such as the base address, size, full path, and load count of each DLL, as well as the process that loaded the DLL and the timestamp of the load. It can also be used to identify code injection and other process manipulation techniques.

  The DLLList plugin, on the other hand, is a more general plugin that provides a list of all the loaded DLLs across all running processes. It can be used to identify potential malicious activity, such as DLL injection or suspicious DLLs that are loaded across multiple processes. The DLLList plugin can also show the size and base address of each DLL, as well as the process ID and full path.

  In summary, the LdrModules plugin is more focused on analyzing the loader data structures for a specific process, while the DLLList plugin provides a broader overview of all loaded DLLs across all processes. Both plugins can be useful in a memory forensic investigation, depending on the specific goals of the analysis.

  It is generally true that the LdrModules plugin can analyze deeper than the DLLList plugin. This is because the LdrModules plugin is specifically designed to analyze the loader data structures for DLLs loaded into a process's memory space, while the DLLList plugin provides a more general overview of all the loaded DLLs across all running processes.

  By focusing on the loader data structures, the LdrModules plugin can provide more detailed information about each DLL, such as the base address, size, full path, and load count. It can also be used to detect code injection and other process manipulation techniques. This level of detail is not available in the DLLList plugin, which only provides basic information such as the size and base address of each DLL, as well as the process ID and full path.

  However, it's worth noting that both plugins have their own strengths and use cases, and the choice of which one to use will depend on the specific goals of the analysis. If the investigator needs a broad overview of all the loaded DLLs across all processes, the DLLList plugin might be more appropriate. On the other hand, if the investigator wants to analyze the loader data structures for a specific process in greater detail, the LdrModules plugin would likely be the better choice.
  </details>
- `binwalk` vs `foremost`
  <details>
  <summary>Details</summary>  
   There is a difference of usage between binwalk command and foremost command.
  
  `binwalk` and `foremost` are both open-source tools used for forensic analysis of digital data. However, they have different purposes and functions.
  `binwalk` is a tool for searching a binary image for embedded files and executable code. It scans the input file for known file signatures and extracts any files that are found. `binwalk` is often used to analyze firmware images, disk images, and other types of binary files.

  `foremost` is a digital forensics tool that is used to recover files from a disk image. Unlike `binwalk`, which focuses on identifying and extracting known file types, `foremost` uses a **rule-based approach** to recover files from a disk image, regardless of file type. This makes it useful for recovering lost or deleted files, or for extracting data from an unknown file format.

  In summary, while `binwalk` is used to identify and extract known file types from a binary image, `foremost` is used to recover files from a disk image, regardless of file type.

  The speed of `foremost` and `binwalk` depends on various factors, such as the size of the data being analyzed, the type of data, and the complexity of the analysis. **In general, `foremost` is faster than `binwalk` in analyzing large data sets because it uses a rule-based approach to recover files, which is less computationally intensive than `binwalk`'s signature-based approach**. However, `binwalk` is **more accurate** in identifying and extracting known file types, which makes it a more suitable tool for analyzing firmware images and other types of binary data that contain a large number of known file types.

  **In some cases, `foremost` may be faster than `binwalk` when analyzing smaller data sets, while `binwalk` may be faster when analyzing larger data sets. The actual speed of each tool will depend on the specific use case and the type of data being analyzed**.

  It's also worth noting that both `foremost` and `binwalk` are designed to be used in conjunction with other digital forensics tools, and that each tool has its own strengths and weaknesses. The choice of which tool to use will depend on the specific needs of the analysis and the type of data being analyzed.
  </details>
- how to use `qpdf`
- how to use `pdf-parser.py`  
how to extract. python2 is better.
- how to use `peepdf.py`  
how to extract. python2 is better.


## question
- volatility 3 cannot parse the memoty at this time.  
  - I tried this but this didn't solve it. (cf. [https://github.com/volatilityfoundation/volatility3/issues/135](https://github.com/volatilityfoundation/volatility3/issues/135))  
1.DL symbol tables from "https://downloads.volatilityfoundation.org/volatility3/symbols/windows.zip"  
2.replace "windows" folder into volatility3/symbols/  

## #1
```
$ vol2 -f Bob.vmem kdbgscan > kdbgscan.txt
$ vol2 -f Bob.vmem imageinfo > imageinfo.txt
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 sockets > sockets.txt
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 connections > connections.txt
```

## #2
```
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 hivelist > hivelist.txt
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 printkey -o 0xe1035b60
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 printkey -K "CurrentControlSet"
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 printkey -K "ControlSet001"
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 printkey -K "ControlSet001\Control\Session Manager\Environment"
```
[https://stackoverflow.com/questions/573817/where-are-environment-variables-stored-in-the-windows-registry](https://stackoverflow.com/questions/573817/where-are-environment-variables-stored-in-the-windows-registry)

## #3
```
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 printkey -o 0xe1526748 -K "Policies\Microsoft\Windows"
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 printkey -o 0xe1526748 -K "Microsoft\Windows NT\CurrentVersion\Winlogon"
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 hashdump -y 0xe1035b60 -s 0xe151ea08 > hashdump_sam.txt
$ john hashdump_sam.txt
$ john hashdump_sam.txt --show
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
## #5
search the suscipious process on google and grapsp the overview of it.

## #6
```
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 connections > connections.txt
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 connscan > connscan.txt
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 sockets > sockets.txt
$ vol2 -f Bob.vmem --profile=WinXPSP2x86  > sockscan.txt
```

## #7
```
$ strings Bob.vmem | grep "XXX.XXX.XXX.XXX(suspicious ip)" | grep .php | grep http
```

## #8
```
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 memdump -p 1752 --dump-dir=./output
$ foremost 1752.dmp
$ cd output/
$ md5sum ./*/* | grep 5cc
```
`foremost` is better. `binwalk` cannot be finished.  

## #9
```
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 handles > handles.txt
$ cat handles.txt | wc -l
6920
$ cat handles.txt | grep PDF
```
`handles` takes minutes.

## #10
```
$ vol2 -f Bob.vmem --profile=WinXPSP2x86 dumpfiles -n -p 1752 -r PDF --dump-dir=./output/output_dumpfiles/
$ pdf-parser.py --stats 00601560.pdf
$ pdf-parser.py --search javascript 00601560.pdf
$ pdf-parser.py --object=1054 00601560.pdf
$ pdf-parser.py --object=1054 --filter 00601560.pdf
$ pdf-parser.py --object=1054 --filter --dump=./00601560.pdf_js_1054 00601560.pdf
$ cat 00601560.pdf_js_1054 | clip
(beautify js at https://lelinhtinh.github.io/de4js/)
$ cat 00601560.pdf_js_1054 | grep --color eval
```

## #11
```
$ js-file.exe 00601560.pdf_js_1054
(be careful to run malicious js)
(then you can get the log)
```