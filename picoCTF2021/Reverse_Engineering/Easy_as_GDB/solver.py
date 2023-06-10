import string
from pwn import *

#correctPointAddress=0x56555000 - 0x10000 + 0x10a6b
#incorrectPointAddress=0x56555000 - 0x10000 + 0x10a7f
nextLoopJugdePointAdress=0x56555000 - 0x10000 + 0x109a7

d = process(['gdb','./brute'])
d.recvuntil(b'gdb-peda$ ') #print("1 ", d.recvuntil(b'gdb-peda$ '))
d.sendline(b'start')
d.recvuntil(b'gdb-peda$ ') #print("2 ", d.recvuntil(b'gdb-peda$ '))
#d.sendline(('b *(' + hex(correctPointAddress) + ')').encode('utf8'))
#d.recvuntil(b'gdb-peda$ ') #print("3 ",d.recvuntil(b'gdb-peda$ '))
#d.sendline(('b *(' + hex(incorrectPointAddress) + ')').encode('utf8'))
#d.recvuntil(b'gdb-peda$ ') #print("4 ",d.recvuntil(b'gdb-peda$ '))
d.sendline(('b *(' + hex(nextLoopJugdePointAdress) + ')').encode('utf8'))
d.recvuntil(b'gdb-peda$ ') #print("5 ",d.recvuntil(b'gdb-peda$ '))

alphabet=string.ascii_uppercase+string.ascii_lowercase+string.digits+'{_}'
flag='picoCTF{'
safeStopper=30
numLetters=len(flag)

while numLetters < safeStopper:
    numLetters+=1
    for c in alphabet:
        d.sendline(b'run')
        d.recvline() #print("6", d.recvline())
        d.recvline() #print("7", d.recvline())
        d.recvline() #print("8", d.recvline())

        print('trying ... ' + flag + c)

        d.sendline((flag+c).encode('utf8'))
        d.recvuntil(b'gdb-peda$ ') #print("9 ",d.recvuntil(b'gdb-peda$ '))

        d.sendline(b'x/x $ebp-0x14')
        a = d.recvline()

        #log.info(a)
        #print(type(a.decode()))
        
        count = int(a.decode().split(':')[1], 16)
        if len(flag+c) == count :
            flag+=c
            print("current : " + flag)
            break