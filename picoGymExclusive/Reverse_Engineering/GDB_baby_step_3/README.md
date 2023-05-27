# Learned 
- the way to use `gdb` for checking memory on specific address
```
(gdb-peda)$ x 0x7fffffffdfa0-0x4
(gdb-peda)$ x $rbp-0x4
(gdb-peda)$ x/4xb 0x7fffffffdfa0-0x4
(gdb-peda)$ x/4xb $rbp-0x4
```
https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_55.html
- practice of thinking about endianess

# Procedures
Dollowing the question, 
1. using ghidra  
2. using gdb and find this  
```
mov    DWORD PTR [rbp-0x4],0x2262c96b
```
3. check [rbp-0x4] using gdb
a value of rbp is easily obtained by gdb.  
```
(gdb-peda)$ x/4xb 0x7fffffffdfa0-0x4
(gdb-peda)$ x/4xb $rbp-0x4
// 0x6b    0xc9    0x62    0x22
```  
Following flag format written in the question, the falg is here.  
picoCTF{0x6bc9222}