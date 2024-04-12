loads_number = int(input())
cargo_tonnage = int(input())
price_per_ton = 0
vehicle_type = ''
cargo_tonnage_van = 0
cargo_tonnage_truck = 0
cargo_tonnage_train = 0

for current_tonnage in range(loads_number):
    if cargo_tonnage <= 3:
        cargo_tonnage = cargo_tonnage_van
        vehicle_type = 'Van'
        price_per_ton = 200
        cost_of_cargo_by_van = cargo_tonnage_van * price_per_ton
        current_tonnage = int(cargo_tonnage)
    elif cargo_tonnage <= 11:
        cargo_tonnage = cargo_tonnage_truck
        vehicle_type = 'Truck'
        price_per_ton = 175
        cost_of_cargo_by_truck = cargo_tonnage_truck * price_per_ton
        current_tonnage = int(cargo_tonnage)
    elif cargo_tonnage >= 12:
        cargo_tonnage = cargo_tonnage_train
        vehicle_type = 'Train'
        price_per_ton = 120
        cost_of_cargo_by_train = cargo_tonnage_train * price_per_ton
        current_tonnage = int(cargo_tonnage)
total_cargo_tonnage = cargo_tonnage_van + cargo_tonnage_truck + cargo_tonnage_train


