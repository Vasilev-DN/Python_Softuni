min_number = int(input())
while True:
    number = input()
    if number == 'Stop':
        break
    number = int(number)
    if number < min_number:
        min_number = number

print(min_number)
