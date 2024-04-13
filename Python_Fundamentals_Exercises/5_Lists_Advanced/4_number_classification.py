numbers = input()

number_list = [int(num) for num in numbers.split(", ")]

positive_numbers = [num for num in number_list if num >= 0]
negative_numbers = [num for num in number_list if num < 0]
even_numbers = [num for num in number_list if num % 2 == 0]
odd_numbers = [num for num in number_list if num % 2 != 0]

print("Positive:", ", ".join(map(str, positive_numbers)))
print("Negative:", ", ".join(map(str, negative_numbers)))
print("Even:", ", ".join(map(str, even_numbers)))
print("Odd:", ", ".join(map(str, odd_numbers)))
