numbers = [114, 114, 114, 111, 99, 107, 110, 114, 110, 48, 49, 49, 51, 114]

result = ''.join(chr(num) for num in numbers)
flag = "picoCTF{" + result + "}"
print(flag)
