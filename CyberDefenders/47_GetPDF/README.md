# Writeup
## #1
```
$ capinfos lala.pcap
$ tshark -r lala.pcap -Y http -T fields -e http.request.full_uri | sort | uniq -c | sort -nr
```

## #2
Wireshark. pick up suspicious "http" found in #1 and follow http stream.
```
http
```