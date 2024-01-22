# Lesson
- Shell Parameter Expansion
    - https://www.gnu.org/software/bash/manual/bash.html#Shell-Parameter-Expansion-1  
    - https://qiita.com/a_yasui/items/ec4f75b300410af8958d  

# Memo
```zsh
Special$ ${parameter:=ls}
${parameter:=ls}
blargh
Special$ ${parameter:=ls} ./blargh
${parameter:=ls} ./blargh
flag.txt
Special$ ${parameter:=cat} ./blargh/flag.txt
${parameter:=cat} ./blargh/flag.txt
picoCTF{5p311ch3ck_15_7h3_w0r57_f906e25a}
```
This also works well
```zsh
Special$ ${parameter:=cat ./blargh/flag.txt}
${parameter:=cat ./blargh/flag.txt}
picoCTF{5p311ch3ck_15_7h3_w0r57_f906e25a}
```