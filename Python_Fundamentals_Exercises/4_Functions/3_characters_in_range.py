def char_range(first_char, second_char):
    result = ''

    for i in range(ord(first_char) + 1, ord(second_char)):
        result += chr(i) + ' '

    return result

first_char = input()
second_char = input()

print(char_range(first_char, second_char))