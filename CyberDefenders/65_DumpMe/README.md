# #1
```
$ sha1sum ./Triage-Memory.mem
```

# #2
```
$ vol2 -f ./Triage-Memory.mem kdbgscan > kdbgscan.txt
$ vol2 -f ./Triage-Memory.mem imageinfo > imageinfo.txt
$ vol3 -f Triage-Memory.mem windows.info.Info > windows_info_Info.txt
```

# #3
```
$ vol2 -f ./Triage-Memory.mem --profile=Win7SP1x64 pslist > pslist.txt &
$ vol2 -f ./Triage-Memory.mem --profile=Win7SP1x64 pstree > pstree.txt &
$ vol2 -f ./Triage-Memory.mem --profile=Win7SP1x64 psscan > psscan.txt &
$ grep --color -E "|notepad" pslist.txt
```

# #4
```
$ grep --color -E "|wscript" pstree.txt
```

# #5
```
$ vol2 -f ./Triage-Memory.mem --profile=Win7SP1x64 netscan > netscan.txt &
$ cat netscan.txt | sort -k 3
```

# #6
```
$ cat netscan.txt | grep --color -E "|3496"
```

# #7
```
$ vol2 -f ./Triage-Memory.mem --profile=Win7SP1x64 dlllist > dlllist.txt &
$ cat dlllist.txt| grep --color -E "VCRUNTIME140.dll|pid|Command Line"
```

# #8
```
$ vol2 -f ./Triage-Memory.mem --profile=Win7SP1x64 procdump -p 3496 --dump-dir=./output/
$ md5sum ./output/executable.3496.exe 
```

# #9
```
$ vol2 -f ./Triage-Memory.mem --profile=Win7SP1x64 hashdump > hashdump.txt &
```

# #10
vadifo plugin takes time even if a target memory size is around 1GB.
```
$ vol2 -f ./Triage-Memory.mem --profile=Win7SP1x64 vadinfo > vadinfo.txt &
$ grep -A 10 -B 10 --color 0xfffffa800577ba10 vadinfo.txt
```

# #11
```
$ grep -A 10 -B 10 --color 0x00000000033c0000 vadinfo.txt | grep -A 10 -B 10 --color 0x00000000033dffff
```

# #12
```
$ vol2 -f ./Triage-Memory.mem --profile=Win7SP1x64 cmdline > cmdline.txt &
$ grep -A 5 -B 5 --color vbs cmdline.txt
```

# #13
```
$ vol2 -f ./Triage-Memory.mem --profile=Win7SP1x64 shimcache > shimcache.txt
$ grep "2019-03-07 23:06:58 UTC" shimcache.txt
```

# #14
```
$ vol2 -f ./Triage-Memory.mem --profile=Win7SP1x64 memdump -p 3032 --dump-dir=./output
$ strings -e l ./output/3032.dmp | grep --color flag
```

# #15
```
$ vol2 -f ./Triage-Memory.mem --profile=Win7SP1x64 mftparser > mftparser.txt
$ grep -A 50 --color 59045 mftparser.txt
```

# #16
find suspicious process and dump it.
use VT and check whether it is created by meterpreter.