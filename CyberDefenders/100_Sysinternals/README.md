# Lesson
- `AppCompatCache`  
- `Amcache`  
- `UsnJrnl`  
    During forensic analysis, sometimes you may not be able to open `UsnJrnl`.  
    Then, `UsnJrnl` might be corrupted and you should try other artifacts.
- "Public" folder on Windows  
    "Public" folder is a special directory designed for sharing files and documents with other users on the same computer or on a network. This folder is typically located in the C:\Users directory and is accessible to all user accounts on the computer.
- FTK Imager  
- Malware Family  
    A malware family refers to a group of malicious software programs (malware) that share common characteristics, code, and behaviors. Malware families are classified based on similarities in their codebase, functionality, and the techniques they use to compromise and exploit systems. Security researchers and antivirus vendors use the concept of malware families to categorize and analyze different types of malicious software efficiently.  

    The naming of malware families is typically done by the cybersecurity community, including security researchers, antivirus vendors, and organizations specializing in threat intelligence. There isn't a centralized authority that officially assigns names to malware; instead, the process involves collaboration and communication within the cybersecurity industry.  

# Writeup  
## #1  
check "Download" folder  

## #2  
AppCompatCache  
```cmd
$ AppCompatCacheParser.exe -f ./SYSTEM --csv . --csvf AppCompatCache.csv
```

## #3  
Amcache  
- Amcache Location
```
Windows/appcompat/Programs/Amcache.hve
```
- Zimmerman
```
$ AmcacheParser.exe -i -f Amcache.hve --csv . --csvf amcache.csv
```

## #4  
VT

## #5, #6
check powershell history  
```
Users\*\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

## #7
check `AppCompatCache` around a suspicious file - "SysInternals.exe".  
guess with timestamp and a suspicious path.

## #8
Event Log

## #9
UsnJrnl might be corrupted.  
Then I took another approach like malware analysis.  
pestdio