# Writeup

## after ctf
- how to use `editbox` plugin at volatility2

## #1
```
$ vol3 -f win7ecorpoffice2010-36b02ed3.vmem windows.info.Info > windows_info_Info.txt
$ vol3 -f win7ecorpoffice2010-36b02ed3.vmem windows.pstree.PsTree > windows_pstree_PsTree.txt
$ vol3 -f win7ecorpoffice2010-36b02ed3.vmem windows.psscan.PsScan > windows_psscan_PsScan.txt
$ vol3 -f win7ecorpoffice2010-36b02ed3.vmem windows.pslist.PsList > windows_pslist_PsList.txt
$ cat windows_psscan_PsScan.txt | sed '1,2d' | sed '2d' | tr '\t' ',' > windows_psscan_PsScan.csv
$ cat windows_pslist_PsList.txt | sed '1,2d' | sed '2d' | tr '\t' ',' > windows_pslist_PsList.csv
$ vol3 -f win7ecorpoffice2010-36b02ed3.vmem windows.dlllist.DllList --pid 1364 > windows_dlllist_DllList_1364.txt
$ vol3 -f win7ecorpoffice2010-36b02ed3.vmem windows.dlllist.DllList --pid 2692 > windows_dlllist_DllList_2692.txt
```

## #2
```
$ vol3 -f win7ecorpoffice2010-36b02ed3.vmem windows.netscan.NetScan > windows_netscan_NetScan.txt
$ vol3 -f win7ecorpoffice2010-36b02ed3.vmem windows.netstat.NetStat > windows_netstat_NetStat.txt
$ cat windows_netscan_NetScan.txt | sed '1,2d' | sed '2d' | tr '\t' ',' > windows_netscan_NetScan.csv
```

## #3
could not find the answer

## #4
could not find the answer
I don't know `editbox` well.

## #5
```
$ vol2 -f win7ecorpoffice2010-36b02ed3.vmem --profile=Win7SP1x64 yarascan -p 2692 -Y "From:"
```

## #6
```
$ vol2 -f win7ecorpoffice2010-36b02ed3.vmem --profile=Win7SP1x64 dumpfiles -u --physoffset=0x7d4d9450 --dump-dir=./vol2/dumpfiles
$ vol2 -f win7ecorpoffice2010-36b02ed3.vmem --profile=Win7SP1x64 dumpfiles -u --physoffset=0x7db2b520 --dump-dir=./vol2/dumpfiles
$ vol2 -f win7ecorpoffice2010-36b02ed3.vmem --profile=Win7SP1x64 dumpfiles -u --physoffset=0x7fd38c80 --dump-dir=./vol2/dumpfiles
```
filedumop is not clear.
and I have to build environment ofr opening .pst and .ost
