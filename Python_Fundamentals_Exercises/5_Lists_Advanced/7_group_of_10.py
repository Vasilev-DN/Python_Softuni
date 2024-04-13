def group_numbers(input_sequence):
    numbers = [int(num) for num in input_sequence.split(", ")]

    groups = {}

    for num in numbers:
        group_key = ((num -1) // 10 + 1) * 10
        if group_key not in groups:
            groups[group_key] = []
        groups[group_key].append(num)

    for i in range(10, max(numbers) + 10, 10):
        if i not in groups:
            groups[i] = []

    for group, numbers_in_group in sorted(groups.items()):
        print(f"Group of {group}'s: {numbers_in_group}")

input_sequence = input()
group_numbers(input_sequence)






