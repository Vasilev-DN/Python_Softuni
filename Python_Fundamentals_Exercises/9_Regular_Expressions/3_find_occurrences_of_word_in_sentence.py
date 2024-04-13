import re

main_string = input().lower()
word_to_look_for = input().lower()

patterns = re.compile(r"\b" + word_to_look_for + r"\b")
print(len(list(re.finditer(patterns, main_string))))