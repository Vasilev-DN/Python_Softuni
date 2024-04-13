def solve(first_num, second_num, input_operator):
    result = 0

    if input_operator == "multiply":
        result = first_num * second_num
    elif input_operator == "divide":
        result = int(first_num / second_num)
    elif input_operator == "add":
        result = first_num + second_num
    elif input_operator == "subtract":
        result = first_num - second_num
    return result

input_operator = input()
first_num = int(input())
second_num = int(input())

result = solve(first_num, second_num, input_operator)

print(result)





