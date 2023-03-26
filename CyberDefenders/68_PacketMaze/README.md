## #1
```
$ tshark -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'ftp or tcp.port == 21 or tcp.port == 20' -V | grep pass -i -A 15 -B 15 --color
```

## #2
```
$ tshark -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'dns and udp.dstport == 53' -T fields -e 'ipv6.addr' | sort | uniq -c | sort -nr
```

## #3
```
$ tshark -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'frame.number == 15174' -V
```

## #4
```
$ mkdir ./output_nfdump
$ nfpcapd -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -w ./output_nfdump
$ nfdump -R ./output_nfdump/ 'proto udp and src ip 192.168.1.26 and dst ip 24.39.217.246'
```

## #5
```
$ tshark -r ./UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'ip.src == 192.168.1.26' -T fields -e eth.src | sort | uniq -c | sort -nr
```

## #6
export object with Wireshark.
```
$ exiftool 20210429_152157.jpg | grep -i camera
```