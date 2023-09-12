import string

# 16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }
encryptedFlag_a = ["16", "9", "3", "15", "3", "20", "6"]
encryptedFlag_b = ["20", "8", "5", "14", "21", "13", "2", "5", "18", "19", "13", "1", "19", "15", "14"]

# c = string.ascii_letters + string.digits + string.punctuation
c = string.ascii_letters + string.digits

flagA = ""
flagB = ""
rotNumberForFlag = 0

for rotNumber in range(len(c)):
    tmp = ""
    for e in encryptedFlag_a:
        tmp += c[(int(e)+rotNumber) % len(c)]

    if tmp[0] == "p" :
        print(tmp)
        flagA = tmp
        rotNumberForFlag = rotNumber

for e in encryptedFlag_b:
    flagB += c[(int(e)+rotNumberForFlag) % len(c)]


flag = flagA + "{" + flagB + "}"

print(flag)