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

## #4
exprt pdf with Wireshark and calc md5
```
$ md5sum fcexploit.pdf
```

## #5
```
$ pdfid.py fcexploit.pdf
```

## #6
```
$ pdf-parser.py fcexploit.pdf | grep -i filter -B 5 -A 5
```

## #7
```
$ pdf-parser.py fcexploit.pdf -s javascript
```

## #8
https://forensicskween.com/ctf/cyberdefenders/getpdf/

- investigate flow  
4 : javascript  
4 -> 5  
code review 5  
then focus 6, 8, 24  
6 -> 7  
8 -> 9  

### Search javascript
```
$ pdf-parser.py fcexploit.pdf -s javascript
## focus on object 5
$ pdf-parser.py fcexploit.pdf -o 5
$ pdf-parser.py --raw -o 5 -f fcexploit.pdf -d obj5
```

### At object 5, read the javascript and focus on "Annot"
```
$ pdf-parser.py fcexploit.pdf -a
## focus on 6, 8, 24
### focus on 6
$ pdf-parser.py fcexploit.pdf -o 6
$ pdf-parser.py fcexploit.pdf -o 7
$ pdf-parser.py --raw -o 7 -f fcexploit.pdf -d obj7
### focus on 8
$ pdf-parser.py fcexploit.pdf -o 8
$ pdf-parser.py fcexploit.pdf -o 9
$ pdf-parser.py --raw -o 9 -f fcexploit.pdf -d obj9
```

### At object 5, read the javascript and focus on "U_155bf62c9aU_7917ab39"
```
$ pdf-parser.py fcexploit.pdf -f | grep U_155bf62c9aU_7917ab39 -A 10 -B 10 --color
## focus on object 10
$ pdf-parser.py fcexploit.pdf -o 10
$ pdf-parser.py --raw -o 10 -f fcexploit.pdf -d obj10
```

### Following javascript on object5, process the raw content in object 10
```
sed 's/U_155bf62c9aU_7917ab39//g' obj10 | xxd -r -p > obj10.out
```

### Following processed javascript on object10, process the raw content in object 7, 9
```
sed  's/X_17844743X_170987743/%/g' obj9 | xxd -r -p > obj9.out
sed 's/89af50d/%/g' obj7 | xxd -r -p > obj7.out
cat obj9.out obj7.out > fullobj.out
```

## #9
```
$ echo -en "\x25\x75\x64\x33\x62\x38....hogehoge" > exploit.bin
$ xxd -gl exploit.bin
$ scdbg -f ./exploit.bin  -s -l
```

## #10
Wireshark

## #11
Google  
Are there any other good solution?