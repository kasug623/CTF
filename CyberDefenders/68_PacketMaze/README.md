
## #1
```
$ tshark -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'ftp or tcp.port == 21 or tcp.port == 20' -V | grep pass -i -A 15 -B 15 --color
```

## #2
```
$ tshark -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'dns and udp.dstport == 53' -T fields -e 'ipv6.addr' | sort | uniq -c | sort -nr
```