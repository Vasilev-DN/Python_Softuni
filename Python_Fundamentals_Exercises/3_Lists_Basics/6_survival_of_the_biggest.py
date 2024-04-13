def remove_smallest_numbers(numbers, n):
    numbers = list(map(int, numbers.split()))

    if n >= len(numbers):
        print()
        return

    for _ in range(n):
        numbers.remove(min(numbers))

    result = ", ".join(map(str, numbers))
    print(result)

numbers_input = input()
n = int(input())

remove_smallest_numbers(numbers_input, n)
