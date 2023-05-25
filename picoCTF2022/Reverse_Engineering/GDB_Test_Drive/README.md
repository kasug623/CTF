# Learned
- the way to use gdb like `"break *(main+99)"` and `"jump *(main+104)"`  
  
# Procedure
just follow instructions written in the question  
``` bash
$ chmod +x gdbme
$ gdb gdbme
(gdb-peda) break *(main+99)
(gdb-peda) run
(gdb-peda) jump *(main+104)
```