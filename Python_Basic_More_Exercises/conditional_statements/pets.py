from math import ceil, floor
number_of_days = int(input())
food_left_in_kg = int(input())
food_per_day_for_dog_in_kg = float(input())
food_per_day_for_cat_in_kg = float(input())
food_per_day_for_turtle_in_gr = float(input())

needed_food_for_dog = number_of_days * food_per_day_for_dog_in_kg
needed_food_for_cat = number_of_days * food_per_day_for_cat_in_kg
needed_food_for_turtle = (number_of_days * food_per_day_for_turtle_in_gr) * 0.001
total_food_needed = needed_food_for_dog + needed_food_for_cat + needed_food_for_turtle
difference = abs(total_food_needed - food_left_in_kg)

if total_food_needed <= food_left_in_kg:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")




