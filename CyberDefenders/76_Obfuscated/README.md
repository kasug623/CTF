# Lesson
- another solution of #3 with cmdwatche

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
olevba

# #5
jscript???

# #6    

#　いらないかも
vipermonkey用の環境用意してもいいかも、regexの古いバージョンに依存するため  
pa2  
vipermoneky is installed on python2 env.
# pip install --upgrade pip wheel setuptools requests
sudo apt install python2-dev
pip install "regex<2022.1.18"
pip install -U https://github.com/decalage2/ViperMonkey/archive/master.zip
vmonkey -h