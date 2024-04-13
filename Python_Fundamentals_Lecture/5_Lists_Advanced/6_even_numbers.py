numbers_input = input()
numbers = [int(num) for num in numbers_input.split(', ')]

even_indices = [index for index, num in enumerate(numbers) if num % 2 == 0]

print(even_indices)
