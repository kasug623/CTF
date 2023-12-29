# Lesson  
- `unzip -p`  
    - extracts the contents of the zip file to standard output without creating any files on the disk. The output is then piped to the next command.

# Memo  
```zsh
$ unzip -p big-zip-files.zip | grep pico
```