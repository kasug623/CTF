# $ echo "0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x35 0x63 0x31 0x31 0x5f 0x6e 0x30 0x5f 0x71 0x75 0x33 0x35 0x37 0x31 0x30 0x6e 0x35 0x5f 0x31 0x6c 0x6c 0x5f 0x74 0x33 0x31 0x31 0x5f 0x79 0x33 0x5f 0x6e 0x30 0x5f 0x6c 0x31 0x33 0x35 0x5f 0x34 0x34 0x35 0x64 0x34 0x31 0x38 0x30 0x7d" | sed 's/0x/"/g' | sed 's/ /", /g'

input = ["70", "69", "63", "6f", "43", "54", "46", "7b", "34", "35", "63", "31", "31", "5f", "6e", "30", "5f", "71", "75", "33", "35", "37", "31", "30", "6e", "35", "5f", "31", "6c", "6c", "5f", "74", "33", "31", "31", "5f", "79", "33", "5f", "6e", "30", "5f", "6c", "31", "33", "35", "5f", "34", "34", "35", "64", "34", "31", "38", "30", "7d"]

flag =""
for i in input:
    flag += chr(int(i,16))

print(flag)


