```
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
``

back to default
```
echo 2 | sudo tee /proc/sys/kernel/randomize_va_space
``

```
$checksec --output=json --file=./jumpout | jq .
```
```
$ ldd -v jumpout
```