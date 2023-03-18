# TOC


# CTF environment
## HOST
### VMWare Workstation
put on Intel VT-x/EPT Virtualization  
![ScreenShot_VMWareWorkstation Image](doc/image/ScreenShot_VMWareWorkstation.png) 

### cmd
hyper-v off is needed to use WSL on VM.  
```
bcdedit /set hypervisorlaunchtype off
```

## Setup VM
### Windows OS
system sound off due to noisy at click tab many times.

#### GUI app
- Process Hacker
- Wireshark
- Geo IP Database for Wireshark
https://wiki.wireshark.org/HowToUseGeoIP#:~:text=MaxMind%20produces%20databases%20and%20software,information%20for%20an%20IP%20address.

#### WSL
##### when you fail `apt update`
- Becasuse of a time difference between host and guset machine on WSL.  
So, 'WSL restart' will be needed.  
But sometimes, a time of host machine VM will be off.  
Then you must update host machine's one.
```
// At Host Machine
$ wsl --shutdown
$ wsl
```

##### ~/.zshrc
```
# my setting
# setxkbmap -layout jp
eval $(dircolors -b ~/.dircolors)
alias ll='ls -l'
alias la='ls -la'
alias win='cd /mnt/c/Users/user'
alias lin='cd ~/'
alias ..='cd ..'
alias clip='/mnt/c/WINDOWS/system32/clip.exe'
alias pa2='source /home/user/virtual_py2/bin/activate'
alias pa3='source /home/user/virtual_py3/bin/activate'
alias pa3j='source /home/user/virtual_py3.10_jupyterlab/bin/activate'
alias pd='deactivate'
alias vol2='sudo ~/virtual_py2/bin/python2.7 ~/volatility/vol.py'
alias vol3='sudo ~/virtual_py3/bin/python3.10 ~/volatility3/vol.py'
alias volshell3='sudo ~/virtual_py3/bin/python3 ~/volatility3/volshell.py'
alias a='uname -a'
alias elasticsearch='/home/user/arkime/elasticsearch-8.6.2/bin/elasticsearch'
alias arkimeviewer='cd /opt/arkime/viewer && /opt/arkime/bin/node /opt/arkime/viewer/viewer.js'
alias gb='git branch'
alias gs='git switch'
alias ctf='cd /mnt/c/Users/user/CTF/CyberDefenders/43_BankingTroubles/c27-banking-troubles'
export PATH=$PATH:/home/user/DidierStevensTool/oledump
export PATH=$PATH:/home/user/DidierStevensTool/pdf-parser
export PATH=$PATH:/home/user/DidierStevensTool/pdfid
export PATH=$PATH:/home/user/DidierStevensTool/js-1.7.0-mod-c/Windows
export PATH=$PATH:/home/user/RegRipper3.0
export PATH=$PATH:/home/user/anaconda3/bin
export PATH=$PATH:/home/user/peepdf
precmd_functions=""
export PS1='%F{042}┌  ─  ─  (%f%F{014}%n@%M%f%F{042})─  [%f%F{222}%d%f%F{042}]%f
%F{042}└  ─ %f %F{014}$%f '

# for show others
# export PS1=' %F{014}$%f '
```

##### vim
###### put a custom color sheme
the way to put depends on the color sheme.
```
~/.vim/colors
(put here iceberg.vim which is downloaded by Internet)
```

###### ~/.vimrc
```
inoremap <silent> jj <ESC>
set relativenumber

# depends on a installed color scheme
syntax on
set background=dark
colorscheme everforest
```

##### /etc/wsl.conf
caution: systemd=tru conflicts with code(VSCode) on WSL
```
[boot]
systemd=true
```

##### setup
```
$ sudo apt install zsh
$ chsh -s $(which zsh)
$ sudo apt install john
$ sudo apt install binwalk
$ sudo apt install foremost
$ sudo apt install exiftool
$ sudo apt install qpdf
$ sudo apt install cpanminus # for RegRipper
$ sudo apt install tshark
$ sudo apt install whois
$ cd ~/
$ git clone https://github.com/jesparza/peepdf.git
$ git clone https://github.com/keydet89/RegRipper3.0.git
$ git clone https://github.com/volatilityfoundation/volatility.git
$ git clone https://github.com/volatilityfoundation/volatility3.git
$ mkdir -p /home/user/DidierStevensTool/oledump
$ mkdir -p /home/user/DidierStevensTool/pdf-parser
$ mkdir -p /home/user/DidierStevensTool/pdfid
#
#
# ----- python ------
# - For use Python2 and Python3, virtualenv is installed.
#
$ sudo apt install python3.10
$ sudo apt install python2.7
$ sudo apt install python3-virtualenv
$ sudo apt install python2-pip-whl
$ sudo apt install python2-setuptools-whl
$ cd ~/
$ mkdir /home/user/virtual_py3.10
$ mkdir /home/user/virtual_py2.7
$ virtualenv -p python3.10 virtual_py3.10
$ virtualenv -p python2.7 virtual_py2.7
# -------------------
#
#
# --- volatility3 ---
$ cd ~/
$ git clone https://github.com/volatilityfoundation/volatility3.git
#
# - test
#
$ pa3
$ vol3 -h
$
$ pip install pycrypto
$ pip install pefile
$ pip install yara-python
# -------------------
#
#
# --- volatility2 ---
$ cd ~/
$ git clone https://github.com/volatilityfoundation/volatility.git
#
# - test
#
$ pa2
$ vol2 -h
#
# - load necessary modules with pip
#
$ pip install pycryptodome
$ pip2 install distorm3==3.3.4
#
# - If you failed to install distorm with pip, you have to manually load necessary modules.
# -- distorm3 is deleted pip repo so need to install manually. Then high version of distrom3 does not suit to volatility2. 
# --- $ cd ~/virtual_py2.7/lib/python2.7/site-packages/
# --- $ wget https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/distorm3/3.4.1-5/distorm3_3.4.1.orig.tar.gz
# --- $ tar -zxvf distorm3_3.4.1.orig.tar.gz
# --- $ rm distorm3_3.4.1.orig.tar.gz
# -------------------
#
#
# ---- oledump ----
$ cd /home/user/DidierStevensTool/oledump
$ wget https://didierstevens.com/files/software/oledump_V0_0_71.zip
$ unzip oledump_V0_0_71.zip
$ chmod +x oledump.py
$ pa3
#
# - test
#
$ oledump.py -h
$
$ pip install olefile
$
$ oledump.py -h
# ------------------
#
#
# ---- RegRipper ----
$ cd /home/user/RegRipper3.0
& chmod +x rip.pl
#
# - test
#
$ perl rip.pl
# -------------------
#
# ----- Arkime ------
$ mkdir ~/arkime
$ cd ~/arkime
$
# just follow official instructions at arkime HP
## download arikime .deb
$ wget (URL written in Arkime HP)
$ dpkg -i XXX.deb
#
## install elasticsearch (https://raw.githubusercontent.com/arkime/arkime/main/release/README.txt)
### follow oficial manual
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.6.2-linux-x86_64.tar.gz
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.6.2-linux-x86_64.tar.gz.sha512
$ shasum -a 512 -c elasticsearch-8.6.2-linux-x86_64.tar.gz.sha512 
$ tar -xzf elasticsearch-8.6.2-linux-x86_64.tar.gz
$ cd ~/arkimeelasticsearch-8.6.2/
#
### disable TLS on elasticsearch.yml
$ vim ~/arkimeelasticsearch-8.6.2/elasticsearch.yml
# 
#
$ /opt/arkime/bin/Configure
$ /opt/arkime/db/db.pl http://localhost:9200 init
#
# set ID/PW
##  user: foo_user
##  password: foo_password
$ /opt/arkime/bin/arkime_add_user.sh foo_user "Admin User" foo_password --admin 
#
# -------------------
#
#
```

##### elasticsearch for arkime
###### elasticsearch.yml
```
xpack.security.autoconfiguration.enabled: false

xpack.security.enabled: false

xpack.security.http.ssl:
  enabled: false

xpack.security.transport.ssl:
  enabled: false

cluster.initial_master_nodes: ["DESKTOP-LM712CE"]

http.host: 0.0.0.0
```
