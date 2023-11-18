# Lesson
- the way to use `ffuf`
- the way to use `SecList`

# Memo
```console
$ apt install ffuf -y
$ 
$ ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://XXX.XXX.XXX.XXX:YYY/FUZZ
$
# The wordlist we chose already contains a dot (.), so we will not have to add the dot after "index" in our fuzzing.
$ ffuf -w /opt/useful/SecLists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://XXX.XXX.XXX.XXX:YYY/blog/indexFUZZ
$
$ ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://XXX.XXX.XXX.XXX:YYY/blog/FUZZ.php
$
# Sub-domain Fuzzing
$ ffuf -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://FUZZ.example.com/
#
# VHost Fuzzing
$ ffuf -w wordlist.txt:FUZZ -u http://example.com:PORT/ -H 'Host: FUZZ.example.com' -fs xxx
#
# Parameter Fuzzing
$ ffuf -w wordlist.txt:FUZZ -u http://example.com:PORT/admin/admin.php?FUZZ=key -fs xxx
#
# Combination
$ ffuf -w ./mySubdomain.txt:SUB -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://example.com:PORT/FUZZ -H 'Host: SUB.example.com' -recursion -recursion-depth 1 -e .php,.php7,.phps
$
$ ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://XXX.example.com:PORT/courses/linux-security.php7 -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs 774,780

```
SecList
```
$ wc -l .../SecLists/Usernames/xato-net-10-million-usernames-dup.txt
$ wc -l .../SecLists/Discovery/Web-Content/web-extensions.txt
$ wc -l .../SecLists/Discovery/Web-Content/burp-parameter-names.txt
$ wc -l .../SecLists/Discovery/DNS/subdomains-top1million-5000.txt
```

## this is shit  
Sub-domain Fuzzing.  
I could not access the web site.   
I guessed the answer.