
# study after ctf
- #9, how to detect dns query. about DNS frame structure around flag
- #11, DNS frame structure around query and response

# #1
```
$ capinfos ./stealer.pcap
```

# #2
```
$ capinfos ./stealer.pcap
$ date --date '2019-04-11 05:37:07 JST' --utc '+%Y-%m-%d %H:%M:%S %Z'
```

# #3
```
$ capinfos stealer.pcap -u
$ i=3821 && sec=$((i%60)) && min=$((i%3600/60)) && hrs=$((i/3600)) && echo $(printf "%02d:%02d:%02d" $hrs $min $sec)
```

# #4
NetworkMiner

# #5
NetworkMiner

# #6
Google

# #6
NetworkMiner
The answer includes IP which looks like a network device.

# #7
NetworkMiner

# #8
NetworkMiner

# #9
NetworkMiner

# #10
Wireshark
```
frame.number == 204
```

# #11
Wireshark
```
frame.number gt 203 && dns
```