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

#### WSL
```
$ sudo apt install zsh
$ chsh -s $(which zsh)
$ sudo apt install john
$ sudo apt install binwalk
$ sudo apt install foremost
$ sudo apt install exiftool
$ sudo apt install qpdf
$ cd ~/
$ git clone https://github.com/jesparza/peepdf.git
$ git clone https://github.com/keydet89/RegRipper3.0.git
$ git clone https://github.com/volatilityfoundation/volatility.git
$ git clone https://github.com/volatilityfoundation/volatility3.git
$ mkdir -p /home/user/DidierStevensTool/oledump
$ mkdir -p /home/user/DidierStevensTool/pdf-parser
$ mkdir -p /home/user/DidierStevensTool/pdfid
$ pip install virtualenv
$ mkdir /home/user/virtual_py2
$ mkdir /home/user/virtual_py3
```

##### when you fail "apt update"
- Becasuse of a time difference between host and guset machine on WSL.  
So, 'WSL restart' will be needed.  
But sometimes, a time of host machine VM will be off.  
Then you must update host machine's one.
```
// At Host Machine
$ wsl --shutdown
$ wsl
```

##### .zshrc
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
alias vol3='sudo ~/virtual_py3/bin/python3 ~/volatility3/vol.py'
alias volshell3='sudo ~/virtual_py3/bin/python3 ~/volatility3/volshell.py'
alias a='uname -a'
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

##### vim color
```
~/.vim/colors
(put here iceberg.vim which is downloaded by Internet)
```

##### .vimrc
```
cd ~/
vim .vimrc
```
```
inoremap <silent> jj <ESC>
syntax on
colorscheme iceberg
```

##### .dircolors
Default powershell terminal at Windows are not good for bash "ls" looks.
```
$ cp (.dircolors) ~/
```

##### python
For use Python2 and Python3, virtualenv is installed.
```
$ sudo apt install python3
$ sudo apt install python2
$ sudo apt install python3-virtualenv
$ cd ~/
$ virtualenv virtual_py3
$ virtualenv -p python2.7 virtual_py2
```

##### volatility3
```
$ cd ~/
$ git clone https://github.com/volatilityfoundation/volatility3.git
```
test
```
$ pa3
$ vol3 -h
```

##### volatility2
```
cd ~/
git clone https://github.com/volatilityfoundation/volatility.git
sudo apt-get install python2.7-dev
pa2
// load necessary modules with pip
pip install pycryptodome
// manually load necessary modules.
// distorm3 is deleted pip repo so need to install manually. Then high version of distrom3 does not suit to volatility2. 
cd ~/virtual_py2/lib/python2.7/site-packages/
wget https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/distorm3/3.4.1-5/distorm3_3.4.1.orig.tar.gz
tar -zxvf distorm3_3.4.1.orig.tar.gz
rm distorm3_3.4.1.orig.tar.gz
```
test
```
// already alias is created
pa2
vol2 -h
```

##### oledump
```
cd ~/
mkdir oledump
cd oledump
wget https://didierstevens.com/files/software/oledump_V0_0_71.zip
unzip oledump_V0_0_71.zip
pa3
pip install olefile
chmod +x oledump.py
```
test
```
oleduump.py -h
```

##### RegRipper
```
https://github.com/keydet89/RegRipper3.0.git
sudo apt install cpanminus
chmod +x rip.pl
```
test
```
perl rip.pl
```
