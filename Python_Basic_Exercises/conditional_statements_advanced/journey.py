budget = float(input())
season = input()
price = 0
destination = ""
type_of_holiday = ""


if budget <= 100:
    if season == "summer":
        destination = "Bulgaria"
        type_of_holiday = "Camp"
        price = budget * 0.3
    elif season == "winter":
        destination = "Bulgaria"
        type_of_holiday = "Hotel"
        price = budget * 0.7
elif budget <= 1000:
    if season == "summer":
        destination = "Balkans"
        type_of_holiday = "Camp"
        price = budget * 0.4
    elif season == "winter":
        destination = "Balkans"
        type_of_holiday = "Hotel"
        price = budget * 0.8
elif budget > 1000:
    if season == "summer" or season == "winter":
        destination = "Europe"
        type_of_holiday = "Hotel"
        price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{type_of_holiday} - {price:.2f}")















