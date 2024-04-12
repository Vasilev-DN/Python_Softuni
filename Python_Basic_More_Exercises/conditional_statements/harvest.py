from math import ceil, floor
area_of_the_vineyard = int(input())
grapes_of_one_square_meter = float(input())
needed_liters_of_wine = int(input())
number_of_workers = int(input())
total_grapes = area_of_the_vineyard * grapes_of_one_square_meter
wine = 0.4 * total_grapes / 2.5
left = abs(needed_liters_of_wine - wine)
if wine < needed_liters_of_wine:
    print(f"It will be a tough winter! More {floor(left)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(left)} liters left -> {ceil(left / number_of_workers)} liters per person.")
