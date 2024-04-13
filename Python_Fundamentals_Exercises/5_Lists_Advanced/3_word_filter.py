text = input()

even_length_words = [word for word in text.split() if len(word) % 2 == 0]

for word in even_length_words:
    print(word)
