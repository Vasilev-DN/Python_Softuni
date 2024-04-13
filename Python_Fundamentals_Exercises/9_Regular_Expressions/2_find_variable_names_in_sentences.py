import re

main_string = input()

patterns = re.compile(r"\b_(?P<word>[A-Za-z0-9]+\b)")
result = re.finditer(patterns, main_string)
result_show = []
for show in result:
    result_show.append(show["word"])

print(','.join(result_show))