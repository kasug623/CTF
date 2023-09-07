filePath = './enc'

with open(filePath, 'r') as file:
    
    flag = ""
    
    for char in file.read():
        #print(char)
        #print(ord(char))
        asciiCode = ord(char)
        #print(format(asciiCode, '016b'))
        myBinary = format(asciiCode, '016b')
        #print(myBinary[:8] + " " + myBinary[8:])
        a = myBinary[:8] 
        b = myBinary[8:]
        flag += chr(int(a, 2))
        flag += chr(int(b, 2))
    
    print(flag)