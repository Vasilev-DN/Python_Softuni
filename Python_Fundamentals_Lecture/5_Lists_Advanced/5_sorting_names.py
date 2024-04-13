names_input = input()
names = [name.strip() for name in names_input.split(', ')]

sorted_names = sorted(names, key=lambda x: (-len(x), x.lower()))

print()
print(sorted_names)


