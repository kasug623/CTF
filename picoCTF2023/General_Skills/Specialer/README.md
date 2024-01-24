# Lesson
- bash  
    - alternative command to `ls`
        ```zsh
        $ alias la='printf "%s\n" *'
        ```
    - alternative command to `ls -a`
        ```zsh
        $ alias la='printf "%s\n" * && printf "%s\n" .*'
        ```
    - alternative command to read a content in a file like `cat`
        ```zsh
        $ alias cat='while read f || [ -n "$f" ]; do echo $f; done <'
        ```
        - `|| [ -n "$line" ]` on shell loop  
            The || [ -n "$line" ] ensures that the loop continues if the last line of the file doesn't end with a newline character.  
            "while read line; do echo $line; done < hoge.txt" cannot read a content if the file has only one line and no "\n" at the end of the line.

# Memo
```zsh
Specialer$ alias la='printf "%s\n" * && printf "%s\n" .*'
Specialer$
Specialer$ la
Specialer$
Specialer$ cd (hoge)
Specialer$
Specialer$ alias cat='while read f; do echo $f; done <'
Specialer$ cat kazam.txt
not worked
Specialer$
Specialer$ alias cat='while read f || [ -n "$f" ]; do echo $f; done <'
Specialer$ cat kazam.txt
return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_838b49d1}
```
This also works.  
```zsh
Specialer$ echo $(<kazam.txt)
return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_838b49d1}
```


# Ref
- https://josephkimiri.github.io/posts/Specialer/  
- https://qiita.com/labpixel/items/b6f035dc9547e470266b  