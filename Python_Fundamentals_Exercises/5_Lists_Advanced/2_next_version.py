def increment_version(version):

    version_parts = version.split(".")

    version_numbers = [int(part) for part in version_parts]

    version_numbers[-1] += 1

    for i in range(len(version_numbers) - 1, 0, -1):
        if version_numbers[i] > 9:
            version_numbers[i] = 0
            version_numbers[i - 1] += 1

    next_version = ".".join(map(str, version_numbers))

    return next_version

current_version = input()
next_version = increment_version(current_version)

print(next_version)
