budget = float(input())
season = input()
location = ''
accommodation_type = ''
price = 0

if budget <= 1000:
    accommodation_type = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45
if 1000 < budget <= 3000:
    accommodation_type = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.60
elif budget > 3000:
    accommodation_type = 'Hotel'
    price = budget * 0.90
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'

print(f'{location} - {accommodation_type} - {price:.2f}')