def find_substrings(input1, input2):

    sequence1 = input1.split(", ")
    sequence2 = input2.split(", ")

    result = [substring for substring in sequence1 if any(substring in s for s in sequence2)]

    return result

# Example usage:
input1 = input()
input2 = input()
output = find_substrings(input1, input2)

print(output)

