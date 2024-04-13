def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    result = ''.join([char for char in text if char not in vowels])
    return result

user_input = input()

result_text = remove_vowels(user_input)
print(result_text)

