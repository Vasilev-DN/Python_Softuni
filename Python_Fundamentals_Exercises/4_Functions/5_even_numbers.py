def get_even_numbers(sequence):

    numbers = list(map(int, sequence.split()))

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    return even_numbers

# Example usage:
input_sequence = input()
result = get_even_numbers(input_sequence)
print(result)
