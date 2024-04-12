month = input()
number_of_nights = int(input())
apartment_price_per_night = 0
studio_price_per_night = 0

if month == 'May' or month == 'October':
    studio_price_per_night = 50
    apartment_price_per_night = 65
    if 7 < number_of_nights <= 14:
        studio_price_per_night *= 0.95
    elif number_of_nights > 14:
        studio_price_per_night *= 0.7
        apartment_price_per_night *= 0.9
elif month == 'June' or month == 'September':
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70
    if number_of_nights > 14:
        studio_price_per_night *= 0.8
        apartment_price_per_night *= 0.9
elif month == 'July' or month == 'August':
    studio_price_per_night = 76
    apartment_price_per_night = 77
    if number_of_nights > 14:
        apartment_price_per_night *= 0.9

sum_for_apartment = apartment_price_per_night * number_of_nights
sum_for_studio = studio_price_per_night * number_of_nights

print(f'Apartment: {sum_for_apartment:.2f} lv.')
print(f'Studio: {sum_for_studio:.2f} lv.')







