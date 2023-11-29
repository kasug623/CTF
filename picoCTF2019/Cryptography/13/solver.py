encrypted_text = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

flag = ""

for s in encrypted_text:
    if s == "_" or s =="{" or s =="}":
        flag += s
        continue
    
    new_codepoint = ""

    if s.isupper():
        new_codepoint = ord("A") + (ord(s) - ord("A") + 13) % 26

    if s.islower():
        new_codepoint = ord("a") + (ord(s) - ord("a") + 13) % 26

    flag += chr(new_codepoint)
    
print(flag)