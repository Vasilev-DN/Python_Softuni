def sum_of_odd_even_digits(number):
    number_str = str(number)

    odd_sum = 0
    even_sum = 0

    for digit_str in number_str:
        digit = int(digit_str)
        # Check if the digit is odd or even
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    result_string = f"Odd sum = {odd_sum}, Even sum = {even_sum}"

    return result_string

input_number = int(input())
result = sum_of_odd_even_digits(input_number)
print(result)
