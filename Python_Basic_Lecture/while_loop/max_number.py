max_number = int(input())
while True:
    number = input()
    if number == 'Stop':
        break
    number = int(number)
    if number > max_number:
        max_number = number

print(max_number)








