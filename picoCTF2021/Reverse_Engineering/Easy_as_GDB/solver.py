import string
from pwn import *

a = 0
print("aaaa")
print(a)
a+=1


d = process('gdb')
d.sendline