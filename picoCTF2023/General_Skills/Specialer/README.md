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
        $ alias cat='while read -r f || [ -n "$f" ]; do echo $f; done <'
        ```
        or
        ```zsh
        $ echo $(<kazam.txt)
        ```
    - reading lines from a file  
        https://genzouw.com/entry/2020/04/15/140408/1972/    
        - `|| [[ -n "$line" ]]` on shell loop  
            `|| [ -n "$line" ]` ensures that the loop continues if the last line of the file doesn't end with a newline character.  
            "while read line; do echo $line; done < hoge.txt" cannot read a content if the file has only one line and no "\n" at the end of the line.  
            "vim" seems to add "\n" automatically at the end of a line.  
        - `IFS=`  
            With `IFS=`, leading and trailing spaces are not removed during the read operation.  
        - `-r`  
            With `-r` option, unusual behavior can be avoided when there is a \ at the end of each line.  
        - test     
            ```zsh
            $ vim test
            $ cat test
            This is 1.\nHoge
            This is 2.
             This is 3 with single space.
                    This is 4 with single tab.
            This is 5.
            $
            $ echo -n "aaaaa" >> test
            $
            $ cat test
            This is 1.\nHoge
            This is 2.
            This is 3 with single space.
                    This is 4 with single tab.
            This is 5.
            aaaaa%
            $
            $ while read f || [[ -n "$f"]]; do echo $f; done < test
            zsh: parse error near ';'
            $
            $ while read f || [[ -n "$f" ]]; do echo $f; done < test
            This is 1.nHoge
            This is 2.
            This is 3 with single space.
            This is 4 with single tab.
            This is 5.
            aaaaa
            $
            $ while read f || [[ -n $f]]; do echo $f; done < test
            zsh: parse error near ';'
            $
            $ while read f || [[ -n $f ]]; do echo $f; done < test
            This is 1.nHoge
            This is 2.
            This is 3 with single space.
            This is 4 with single tab.
            This is 5.
            aaaaa
            $
            $ while IFS= read -r f || [[ -n $f ]]; do echo $f; done < test
            This is 1.
            Hoge
            This is 2.
             This is 3 with single space.
                    This is 4 with single tab.
            This is 5.
            aaaaa
            ```

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
Specialer$ alias cat='while read f || [[ -n "$f" ]]; do echo $f; done <'
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