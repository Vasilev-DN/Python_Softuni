import math

count_of_number = int(input())
sum_of_all_elements = 0
max_number = -math.inf

for number in range(count_of_number):
    current_number = int(input())
    sum_of_all_elements += current_number
    if current_number > max_number:
        max_number = current_number
if max_number == sum_of_all_elements - max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    difference = abs(max_number - (sum_of_all_elements - max_number))
    print('No')
    print(f'Diff = {difference}')