# Writeup
## point
- For searching js data in pcap, fully relying on `content-type` is not good.

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

## #3
extract javascript from HTTP stream and use Spidermonkey
```
$ code ./script.js
$ js-beautify -f ./script.js > ./script-b.js
$ js -f ./my-objects.js -f ./script.js > ./out.js
$ js-beautify -f ./out.js > ./out-b.js
```