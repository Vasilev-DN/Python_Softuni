def analyze_numbers(sequence):

    numbers = list(map(int, sequence.split()))

    min_number = min(numbers)
    max_number = max(numbers)
    sum_numbers = sum(numbers)

    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {sum_numbers}")

input_sequence = input()
analyze_numbers(input_sequence)
