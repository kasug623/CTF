numbers = [66, 79, 78, 74, 79, 86, 73]

result = ''.join(chr(num) for num in numbers)
flag = "picoCTF{" + result + "}"
print(flag)
