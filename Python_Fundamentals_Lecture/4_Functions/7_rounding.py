def round_numbers_to_int(numbers):

    num_list = numbers.split()

    rounded_numbers = [int(round(float(num))) for num in num_list]

    return rounded_numbers

def main():
    input_numbers = input()
    rounded_list = round_numbers_to_int(input_numbers)

    print(rounded_list)

if __name__ == "__main__":
    main()
