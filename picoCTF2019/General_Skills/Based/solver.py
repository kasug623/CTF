from pwn import *

r = remote("jupiter.challenges.picoctf.org", 15130)

def question1():
    print("start question 1 ...")
    r.recvuntil(b'Please give the ')

    question_part = r.recvuntil(b' as a word.')
    question_part_extracted = question_part.replace(b' as a word.', b'')
    print(question_part_extracted)

    delimiter = b' '

    # Split the byte string using the delimiter
    target_value_list = question_part_extracted.split(delimiter)
    print(target_value_list)

    ans =b''
    for b in target_value_list:
        binary_byte_string = b

        # Convert binary byte string to an integer
        integer_value = int(binary_byte_string, 2)
        print(integer_value)

        # Convert integer to ASCII character
        ascii_character = chr(integer_value)
        print(ascii_character)

        ans += bytes([ord(ascii_character)])

    r.sendline(ans)
    print(ans)

def question2():
    print("start question 2 ...")
    r.recvuntil(b'Please give me the  ')

    question_part = r.recvuntil(b' as a word.')
    question_part_extracted = question_part.replace(b' as a word.', b'')
    print(question_part_extracted)

    delimiter = b' '

    # Split the byte string using the delimiter
    target_value_list = question_part_extracted.split(delimiter)
    print(target_value_list)

    ans = b''
    for b in target_value_list:
        binary_byte_string = b

        # Convert binary byte string to an integer
        integer_value = int(binary_byte_string, 8)
        print(integer_value)

        # Convert integer to ASCII character
        ascii_character = chr(integer_value)
        print(ascii_character)

        ans += bytes([ord(ascii_character)])

    r.sendline(ans)
    print(ans)

def question3():
    print("start question 3 ...")
    r.recvuntil(b'Please give me the ')

    question_part = r.recvuntil(b' as a word.')
    single_byte_strings = question_part.replace(b' as a word.', b'')
    print(single_byte_strings)

    chunk_size = 2
    target_value_list = [single_byte_strings[i:i+chunk_size] for i in range(0, len(single_byte_strings), chunk_size)]
    print(target_value_list)

    ans = b''
    for b in target_value_list:
        binary_byte_string = b

        # Convert binary byte string to an integer
        integer_value = int(binary_byte_string, 16)
        print(integer_value)

        # Convert integer to ASCII character
        ascii_character = chr(integer_value)
        print(ascii_character)

        ans += bytes([ord(ascii_character)])

    r.sendline(ans)
    print(ans)

def main():

    print("-------------------------------------")
    question1()

    print("-------------------------------------")
    question2()

    print("-------------------------------------")
    question3()

    print("-------------------------------------")
    r.interactive()


if __name__ == "__main__":
    main()