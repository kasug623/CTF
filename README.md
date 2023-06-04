# TOC
- [CTF environment](#ctf-environment)
  - [HOST](#host)
  - [Setup VM](#setup-vm)

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
- うさみみハリケーン
- BurpSuite
- Firefox
set CA and FoxyProxy for BurpSuite
- VSCode

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
alias ctf='cd /mnt/c/Users/user/CTF/picoCTF2021/Binary_Exploitation/Stonks'
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
##
## improve zsh
### load git-prompt
source ~/.zsh/git-prompt.sh
### laod git-completion
fpath=(~/.zsh $fpath)
zstyle ':completion:*:*:git:*' script ~/.zsh/git-completion.bash
autoload -Uz compinit && compinit

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
$ sudo apt install ngrep
$ sudo apt install clamav clamav-daemon
$ sudo freshclam
$ cd ~/
$ git clone https://github.com/jesparza/peepdf.git
$ git clone https://github.com/keydet89/RegRipper3.0.git
$ git clone https://github.com/volatilityfoundation/volatility.git
$ git clone https://github.com/volatilityfoundation/volatility3.git
$ mkdir -p /home/user/DidierStevensTool/oledump
$ mkdir -p /home/user/DidierStevensTool/pdf-parser
$ mkdir -p /home/user/DidierStevensTool/pdfid
##
## ----- completion for git at zsh ------
### https://qiita.com/mikan3rd/items/d41a8ca26523f950ea9d
$ mkdir ~/.zsh
$ cd ~/.zsh
$
$ curl -o git-prompt.sh https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh
$ curl -o git-completion.bash https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash
$ curl -o _git https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.zsh 
##
## --------------------------------------
##
## ----- python ------
## - For use Python2 and Python3, virtualenv is installed.
##
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
## -------------------
##
##
## --- volatility3 ---
$ cd ~/
$ git clone https://github.com/volatilityfoundation/volatility3.git
##
## - test
##
$ pa3
$ vol3 -h
$
$ pip install pycrypto
$ pip install pefile
$ pip install yara-python
## -------------------
##
##
## --- volatility2 ---
$ cd ~/
$ git clone https://github.com/volatilityfoundation/volatility.git
##
## - test
##
$ pa2
$ vol2 -h
##
## - load necessary modules with pip
##
$ pip install pycryptodome
$ pip2 install distorm3==3.3.4
##
## - If you failed to install distorm with pip, you have to manually load necessary modules.
## -- distorm3 is deleted pip repo so need to install manually. Then high version of distrom3 does not suit to volatility2. 
## --- $ cd ~/virtual_py2.7/lib/python2.7/site-packages/
## --- $ wget https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/distorm3/3.4.1-5/distorm3_3.4.1.orig.tar.gz
## --- $ tar -zxvf distorm3_3.4.1.orig.tar.gz
## --- $ rm distorm3_3.4.1.orig.tar.gz
## -------------------
##
##
## ---- oledump ----
$ cd /home/user/DidierStevensTool/oledump
$ wget https://didierstevens.com/files/software/oledump_V0_0_71.zip
$ unzip oledump_V0_0_71.zip
$ chmod +x oledump.py
$ pa3
##
## - test
##
$ oledump.py -h
$
$ pip install olefile
$
$ oledump.py -h
## ------------------
##
##
## ---- RegRipper ----
$ cd /home/user/RegRipper3.0
& chmod +x rip.pl
##
## - test
##
$ perl rip.pl
## -------------------
##
## ----- Arkime ------
$ mkdir ~/arkime
$ cd ~/arkime
$
## just follow official instructions at arkime HP
### download arikime .deb
$ wget (URL written in Arkime HP)
$ dpkg -i XXX.deb
##
### install elasticsearch (https://raw.githubusercontent.com/arkime/arkime/main/release/README.txt)
#### follow oficial manual
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.6.2-linux-x86_64.tar.gz
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.6.2-linux-x86_64.tar.gz.sha512
$ shasum -a 512 -c elasticsearch-8.6.2-linux-x86_64.tar.gz.sha512 
$ tar -xzf elasticsearch-8.6.2-linux-x86_64.tar.gz
$ cd ~/arkimeelasticsearch-8.6.2/
##
#### disable TLS on elasticsearch.yml
$ vim ~/arkimeelasticsearch-8.6.2/elasticsearch.yml
## 
##
$ /opt/arkime/bin/Configure
$ /opt/arkime/db/db.pl http://localhost:9200 init
##
## set ID/PW
###  user: foo_user
###  password: foo_password
$ /opt/arkime/bin/arkime_add_user.sh foo_user "Admin User" foo_password --admin 
##
## -------------------
##
## ----- nfdump ------
### https://github.com/phaag/nfdump
### https://gist.github.com/jjsantanna/f2ee2f1fe23208299f4a2ca392f8b23f?permalink_comment_id=3749338
### https://rc30-popo.hatenablog.com/entry/2019/02/02/000702
$ cd ~/
$ git clone https://github.com/phaag/nfdump.git
$ cd nfdump
$ sudo apt install libtool -y
$ ./autogen.sh
$ sudo apt install flex
$ sudo apt install ibbz2-dev
### for nfpcapd
$ sudo apt install libpcap-dev
$ ./configure --enable-nfpcapd
$ make
$ sudo make install
$ sudo ldconfig
## -------------------
##
## ----- gdbgui ------
$ pa3
$ pip install gdbgui
$ gdbgui
## -------------------
##
## ----- gdb-peda ------
$ git clone https://github.com/longld/peda.git ~/peda
$ echo "source ~/peda/peda.py" >> ~/.gdbinit
## -------------------
##
## ------pwntools--------
### https://docs.pwntools.com/en/stable/install.html
### python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential is needed,
### but only libssl-dev was not installed.
$ apt install libssl-dev
$ pa3
$ pip install pwntools
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
