import string

encrypted_text = "ynkooejcpdanqxeykjrbdofgkq"

for i in range(0,27):
    flag_candidate = ""
    for s in encrypted_text:
        new_codepoint =  ord("a") + (ord(s) - ord("a") + i) % 26
        flag_candidate += chr(new_codepoint)
    print(flag_candidate)
    flag_candidate = ""