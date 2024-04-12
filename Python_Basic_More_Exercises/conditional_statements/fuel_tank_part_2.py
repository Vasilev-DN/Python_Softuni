type_of_fuel = input()
fuel_quantity = float(input())
club_card = input()
sum_for_fuel = 0

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

if type_of_fuel == 'Gasoline' and club_card == 'Yes':
    gasoline_price = gasoline_price - 0.18
    sum_for_fuel = gasoline_price * fuel_quantity
elif type_of_fuel == 'Diesel' and club_card == 'Yes':
    diesel_price = diesel_price - 0.12
    sum_for_fuel = diesel_price * fuel_quantity
elif type_of_fuel == 'Gas' and club_card == 'Yes':
    gas_price = gas_price - 0.08
    sum_for_fuel = gas_price * fuel_quantity

if 20 <= fuel_quantity <= 25:
    sum_for_fuel *= 0.92
elif fuel_quantity > 25:
    sum_for_fuel *= 0.9

print(f'{sum_for_fuel:.2f} lv.')




