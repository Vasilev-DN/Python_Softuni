def find_smallest(num1, num2, num3):
    return min(num1, num2, num3)

num1_input = int(input())
num2_input = int(input())
num3_input = int(input())

smallest = find_smallest(num1_input, num2_input, num3_input)

print(smallest)
