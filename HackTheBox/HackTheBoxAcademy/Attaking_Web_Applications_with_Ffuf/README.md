# Lesson
- the way to use `ffuf`

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
```

## this is shit  
Sub-domain Fuzzing.  
I could not access the web site.   
I guessed the answer.