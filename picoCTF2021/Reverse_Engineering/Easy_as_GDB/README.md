# Learning
- how to use pwntools  
https://hiziriai.hatenablog.com/entry/2017/09/18/124628
- how to debug script with pwntool
check code by line comapared to run  
- how to get adress  
match ghidra address to gdb  
- how to use python  
type: bytes  
- how to think about creating brute focrce program  
I'm not used to creating this kind of program.  

# Procedures
1. find logic with ghidra  
    -  locate entrypoint
2. get a image of flow with gdb  
    - compared address of ghidra with one of gdb, get a relation between these addresses  
        - check an address on the top of display at ghidra
        - check an first address on gdb using `start` and `info proc mappings` 
            ```
            (gdb-peda)$ start
            (gdb-peda)$ info proc mappings
            (gdb-peda)$ b *(0x56555000+0xa63)
            ```
            c.f.
            ```
            (gdb-peda)$ set $eax=1
            (gdb-peda)$ info registers
            (gdb-peda)$ x/x $ebp-0x14
            ```
3. think about how to get a information of flag  
    - patterns  
        - information of flag is directory stored in a binary  
        - inforamtion of flag is encrypted or scatterd in a binary  
            - a logic is static  
                - the logic can be used many times (<-**this case**)
                    - write a script with decrypt logic  
                    - write a brute force (<-**this case**)
                - the logic can be used only a few times  
                    - write a script with decrypt logic  
            - a logic is dynamic  
                - the logic can be used many times  
                    - write a script with decrypt logic  
                    - write a brute force  
                - the logic can be used only a few times  
                    - write a script with decrypt logic  

4. write a solver  
    - TIPS: when you write a script with `pwntools`, you should check every statement of "send() and recv()" using gdb or a display of running.     
        it is imorpotant to debug every code step by step


