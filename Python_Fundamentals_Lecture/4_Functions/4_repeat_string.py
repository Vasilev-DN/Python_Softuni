repeat_string = lambda s, n: s * n

def main():
    input_string = input()
    repeat_count = int(input())

    result = repeat_string(input_string, repeat_count)
    print(result)

if __name__ == "__main__":
    main()
