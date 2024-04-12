budget = float(input())
type_of_season = input()
class_type = ""
car_type = ""
price = 0

if budget <= 100:
    class_type = "Economy class"
    if type_of_season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.35
    elif type_of_season == "Winter":
        car_type = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    class_type = "Compact class"
    if type_of_season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.45
    elif type_of_season == "Winter":
        car_type = "Jeep"
        price = budget * 0.80
elif budget > 500:
    class_type = "Luxury class"
    car_type = "Jeep"
    price = budget * 0.90

print(class_type)
print(f'{car_type} - {price:.2f}')

