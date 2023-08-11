# Lesson
- another solution of #3 with `CMDWatcher`  
you should try online-sandbox if you encounter an problem on your envinment
- what is `Key-Scheduling Algorithm`
- understand the algorithm of `RC4`  
https://en.wikipedia.org/wiki/RC4  
https://gist.githubusercontent.com/farhadi/2185197/raw/b290c2dcc0eef9c23015eab0bb335f08bee0e862/rc4.js  
https://www.geeksforgeeks.org/implementation-of-rc4-algorithm/
- find an algorithm in a script

# #1
```bash
$ file 49b367ac261a722a7c2bbbc328c32545
$ trid 49b367ac261a722a7c2bbbc328c32545
$ sha256sum 49b367ac261a722a7c2bbbc328c32545
```

# #2
```bash
$ oledump.py 49b367ac261a722a7c2bbbc328c32545
```

# #3
```bash
$ olevba 49b367ac261a722a7c2bbbc328c32545
$ olevba 49b367ac261a722a7c2bbbc328c32545 --deobf
```

# #4
`olevba`

# #5
jscript    
I don't like this format of answer.

# #6
I tried my environment with `CMDWatcher`, but the macro did not work well.  
Then I give up this and following questions except #16 and #17.
I should have try online-sandbox.  

With `HybridAnalysis`, I can see the commands.

# #7, #8, #9, #10. #11
`HybridAnalysis`  
get javascript code and read it.  

# 12
https://forensicskween.com/ctf/cyberdefenders/obfuscated/  
https://www.geeksforgeeks.org/implementation-of-rc4-algorithm/  
```js
function CpPT(bOe3, F5vZ) {
    // bOe3 : key
    // F5vZ : encrypted data
    var AWy7 = [];
    var V2Vl = 0;
    var qyCq;
    var mjqo = '';
    for (var i = 0; i & lt; 256; i++) {
        AWy7[i] = i;
    }
    for (var i = 0; i & lt; 256; i++) {
        V2Vl = (V2Vl + AWy7[i] + bOe3.charCodeAt(i % bOe3.length)) % 256;
        qyCq = AWy7[i];
        AWy7[i] = AWy7[V2Vl];
        AWy7[V2Vl] = qyCq;
    }
    var i = 0;
    var V2Vl = 0;
    for (var y = 0; y & lt; F5vZ.length; y++) {
        i = (i + 1) % 256;
        V2Vl = (V2Vl + AWy7[i]) % 256;
        qyCq = AWy7[i];
        AWy7[i] = AWy7[V2Vl];
        AWy7[V2Vl] = qyCq;
        mjqo += String.fromCharCode(F5vZ[y] ^ AWy7[(AWy7[i] + AWy7[V2Vl]) % 256]);
    }
    // return mjqo;
}
```
Key-Scheduling Algorithm

# 13
read the extracted js  

# 14
read the extracted js

# 15
read scripts and find the algorithm - RC4

# 16
I could answer this with my knowledge.  
flag: Eval

# 17
I could answer this with my knowledge.  
flag: cscript.exe

# 18
decode the encrypted data with base64 and RC4.  
CyberChef is useful.