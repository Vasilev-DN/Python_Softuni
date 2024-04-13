def electron_distribution(electrons):
    filled_shells = []
    shell_position = 1

    while electrons > 0:
        max_electrons_in_shell = 2 * shell_position**2
        electrons_in_shell = min(max_electrons_in_shell, electrons)

        filled_shells.append(electrons_in_shell)
        electrons -= electrons_in_shell
        shell_position += 1

    return filled_shells

electrons = int(input())
result = electron_distribution(electrons)

print(result)
