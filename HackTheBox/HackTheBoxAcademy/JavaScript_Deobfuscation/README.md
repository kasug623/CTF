# Lesson
- bash for `ASCII code point conversion` with `xxd` command
- bash for `Caesar cipher` with `tr` command
- `xxd`
  - `-x` option:  
    The -x option stands for "hexdump."  
    It displays the hex dump of the file in a more verbose format, including the hexadecimal offset, the hexadecimal values of each byte, and the ASCII representation of the data.
  - `-p` option:  
    The -p option stands for "plain."  
    It displays a plain hex dump without the offset and ASCII representation, just the hexadecimal values of the bytes.

# Memo
```console
$ echo https://example.com/ | xxd -p
68747470733a2f2f6578616d706c652e636f6d2f0a
$
$ echo 68747470733a2f2f6578616d706c652e636f6d2f0a | xxd -p -r
https://example.com/
$ echo 68 | xxd -p -r
h                                                                                                                  $
$ echo 6874 | xxd -p -r
ht
```
```console
$ echo https://example.com | tr 'A-Za-z' 'N-ZA-Mn-za-m'
uggcf://rknzcyr.pbz
$
$ echo uggcf://rknzcyr.pbz | tr 'A-Za-z' 'N-ZA-Mn-za-m'
https://example.com
```
