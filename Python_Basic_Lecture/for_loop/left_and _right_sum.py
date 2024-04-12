number = int(input())

left_sum = 0
for _ in range(1,number + 1):
    left_sum += int(input())

right_sum = 0
for _ in range(1,number + 1):
    right_sum += int(input())

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    difference = abs(left_sum - right_sum)
    print(f'No, diff = {difference}')
