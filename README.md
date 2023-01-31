# CTF

```
$ sudo apt isntall john
$ sudo apt install binwalk
$ sudo apt install foremost
```

## when you fail "apt update"
- Becasuse of a time difference between host and guset machine on WSL.  
So, 'WSL restart' will be needed.  
But sometimes, a time of host machine VM will be off.  
Then you must update host machine's one.
```
// At Host Machine
$ wsl --shutdown
$ wsl
```

