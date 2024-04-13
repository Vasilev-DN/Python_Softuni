def decipher_secret_message(secret_message):
    words = secret_message.split()

    deciphered_words = []
    for word in words:

        code, rest = "", ""
        for char in word:
            if char.isdigit():
                code += char
            else:
                rest += char


        deciphered_word = chr(int(code)) + rest[-1] + rest[1:-1] + rest[0] if len(rest) >= 2 else chr(int(code)) + rest

        deciphered_words.append(deciphered_word)


    deciphered_message = ' '.join(deciphered_words)
    return deciphered_message


secret_message = input()
result = decipher_secret_message(secret_message)
print(result)



