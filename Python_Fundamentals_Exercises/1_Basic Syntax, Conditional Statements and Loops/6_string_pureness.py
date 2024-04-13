def check_purity(n):
    for _ in range(n):
        string = input()

        if all(char not in string for char in [',', '.', '_']):
            print(f"{string} is pure.")
        else:
            print(f"{string} is not pure!")

n = int(input())

check_purity(n)
