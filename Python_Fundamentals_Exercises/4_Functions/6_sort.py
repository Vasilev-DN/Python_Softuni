def sort_numbers(sequence):

    numbers = list(map(int, sequence.split()))

    sorted_numbers = sorted(numbers)

    return sorted_numbers

# Example usage:
input_sequence = input()
result = sort_numbers(input_sequence)
print(result)
