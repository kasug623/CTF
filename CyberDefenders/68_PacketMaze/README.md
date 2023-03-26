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

## #7
```
$ tshark -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'tls.handshake.session_id' -T fields -e frame.number
$ tshark -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'tls.handshake.session_id' -T fields -e frame.number -e tls.handshake.session_id
$ tshark -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'tls.handshake.session_id' -T fields -e frame.number -e tls.handshake.session_id | grep da4a0000342e4b73459d7360b4bea971cc303ac18d29b99067e46d16cc07f4ff
$ tshark -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'frame.number == 26913' -T fields -e tls.handshake.server_point
```
this comman dons not work. why?
```
$ tshark -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'tls.handshake.session_id == da4a0000342e4b73459d7360b4bea971cc303ac18d29b99067e46d16cc07f4ff' -T fields -e frame.number
tshark: "da4a0000342e4b73459d7360b4bea971cc303ac18d29b99067e46d16cc07f4ff" is not a valid byte string.
```

## #8
```
$ tshark -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -V | grep -A 5 -B 5 --color 'protonmail.com'
$ tshark -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'ip.addr == 185.70.41.35 and tls.handshake.random' -T fields -e frame.number
$ tshark -r UNODC-GPC-001-003-JohnDoe-NetworkCapture-2021-04-29.pcapng -Y 'ip.addr == 185.70.41.35 and tls.handshake.random' -T fields -e frame.number -e tls.handshake.random
```