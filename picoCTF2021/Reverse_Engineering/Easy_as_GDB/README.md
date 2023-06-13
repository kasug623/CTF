# Learning
- How to use `pwntools`  
https://hiziriai.hatenablog.com/entry/2017/09/18/124628  
- How to debug a script with `pwntool`  
check code by lines, compared with a debug result  
- How to get an address  
match a address of `ghidra` to one of `gdb`  
- How to use python  around `pwntools`  
type: bytes  
- How to think about creating a brute force program  
I'm still not used to creating this kind of program.  

# Procedures
1. Find logic with `ghidra`  
    -  locate entrypoint  
    keyword: main
2. Get a image of flow with `gdb`  
    - Compared an address of `ghidra` with one of `gdb`, get a relation between these addresses  
        - Check an address on the top of display at `ghidra`
        - Check an first address on gdb using `start` and `info proc mappings` 
            ```
            (gdb-peda)$ start
            (gdb-peda)$ info proc mappings
            (gdb-peda)$ b *(0x56555000+0xa63)
            ```
            c.f. other usuful commands of `gdb`  
            ```
            (gdb-peda)$ set $eax=1
            (gdb-peda)$ info registers
            (gdb-peda)$ x/x $ebp-0x14
            ```
3. Think about how to get a information of "flag"  
    - Patterns  
        - Information of "flag" is directory stored in a binary  
            - Just look into with some tools   
        - Inforamtion of "flag" is encrypted or scatterd in a binary  
            - A logic is static  
                - The logic can be used many times (<-**this case**)
                    - write a script with decrypt logic  
                    - write a brute force (<-**this case**)
                - The logic can be used only a few times  
                    - write a script with decrypt logic  
            - A logic is dynamic  
                - The logic can be used many times  
                    - write a script with decrypt logic  
                    - write a brute force  
                - The logic can be used only a few times  
                    - write a script with decrypt logic  

4. Write a solver  
    - When you write a script with `pwntools`, you should check every statement of "send() and recv()" using `gdb` or a display of running.     
        It is imorpotant to debug every code step by step.  