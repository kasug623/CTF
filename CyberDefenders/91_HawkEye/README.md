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