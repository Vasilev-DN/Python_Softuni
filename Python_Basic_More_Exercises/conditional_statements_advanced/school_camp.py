season = input()
type_of_group = input()
number_of_students = int(input())
number_of_nights = int(input())
price_per_night = 0
type_of_sport = ''

if season == 'Winter':
    if type_of_group == 'boys':
        price_per_night = 9.60
        type_of_sport = 'Judo'
    elif type_of_group == 'girls':
        price_per_night = 9.60
        type_of_sport = 'Gymnastics'
    elif type_of_group == 'mixed':
        price_per_night = 10
        type_of_sport = 'Ski'
elif season == 'Spring':
    if type_of_group == 'boys':
        price_per_night = 7.20
        type_of_sport = 'Tennis'
    elif type_of_group == 'girls':
        price_per_night = 7.20
        type_of_sport = 'Athletics'
    elif type_of_group == 'mixed':
        price_per_night = 9.50
        type_of_sport = 'Cycling'
elif season == 'Summer':
    if type_of_group == 'boys':
        price_per_night = 15
        type_of_sport = 'Football'
    elif type_of_group == 'girls':
        price_per_night = 15
        type_of_sport = 'Volleyball'
    elif type_of_group == 'mixed':
        price_per_night = 20
        type_of_sport = 'Swimming'

total_sum = number_of_nights * number_of_students * price_per_night

if number_of_students >= 50:
    total_sum *= 0.5
elif 20 <= number_of_students < 50:
    total_sum *= 0.85
elif 10 <= number_of_students < 20:
    total_sum *= 0.95

print(f'{type_of_sport} {total_sum:.2f} lv.')
