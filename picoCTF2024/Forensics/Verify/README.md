# Lessons
- training for statement on shell

# Memo
1. modify "decrypt.sh" for debug  
changed a path in "decrypt.sh" and created "decrypt_debug.sh".
2. search
    ```zsh
    $ for f in `ls ./challenge/home/ctf-player/drop-in/files`; do ./decrypt_debug.sh files/$f; done
    bad magic number
    Error: Failed to decrypt 'files/0QFPjDGl'. This flag is fake! Keep looking!
    bad magic number
    Error: Failed to decrypt 'files/0wKPM7Vk'. This flag is fake! Keep looking!
    bad magic number
    ...
    ...
    $
    $ for f in `ls ./challenge/home/ctf-player/drop-in/files`; do ./decrypt_debug.sh files/$f; done | grep -v "This flag is fake! Keep looking"
    bad magic number
    bad magic number
    ...
    ...
    bad magic number
    picoCTF{trust_but_verify_451fd69b}
    bad magic number
    bad magic number
    ...
    ```