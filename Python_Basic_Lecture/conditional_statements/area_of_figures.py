from math import pi
figure = input()

if figure == "square":
    a = float(input())
    area = a * a
    print(f"{area:.3f}")

if figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")

if figure == "circle":
    r = float(input())
    area = r * r * pi
    print(f"{area:.3f}")

if figure == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2
    print(f"{area:.3f}")

