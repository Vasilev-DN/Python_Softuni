def calculate_rectangle_area(width, height):
    area = width * height
    return area

def main():
    width = int(input())
    height = int(input())

    area = calculate_rectangle_area(width, height)

    print(area)

if __name__ == "__main__":
    main()
