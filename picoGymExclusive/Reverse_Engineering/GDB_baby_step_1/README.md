# Learned
- a combination of debugger and disassembler is useful.

# Procedure
According to the question, getting EAX at the end of main function is a goal.   
After that, following the question, converting the value of EAX from base16 to base10 is needed.
1. using ghidra, find a start and end address of main function
2. using gdb-peda, run and check EAX at the end of function
```
$ gdb debugger0_a
(gdb-peda) b main
(gdb-peda) n
(gdb-peda) n
(gdb-peda) n
...
// focus on EIP, finally got the EAX value I want.  
// RAX: 0x86342  
```
3. conveting the value from base16 to base10
