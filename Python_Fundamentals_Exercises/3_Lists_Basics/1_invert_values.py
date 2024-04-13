list_with_numbers = input().split()

opposite_list = []

for number in list_with_numbers:
    opposite_number = -int(number)
    opposite_list.append(opposite_number)

print(opposite_list)

