type_of_fuel = input()
fuel_in_tank = float(input())

if fuel_in_tank >= 25:
    if type_of_fuel == 'Diesel'or type_of_fuel == 'Gasoline' or type_of_fuel == 'Gas':
        print(f'You have enough {type_of_fuel.lower()}.')
    else:
        print(f'Invalid fuel!')
elif fuel_in_tank < 25:
    if type_of_fuel == 'Diesel' or type_of_fuel == 'Gasoline' or type_of_fuel == 'Gas':
        print(f'Fill your tank with {type_of_fuel.lower()}!')
    else:
        print(f'Invalid fuel!')