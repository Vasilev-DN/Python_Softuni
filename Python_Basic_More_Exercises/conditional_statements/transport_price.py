kilometers = int(input())
time_of_day = input()
bus_price_per_km = 0.09
train_price_per_km = 0.06

initiation_fee_of_taxi = 0.70
if time_of_day == "day":
    taxi_price_per_kilometer = 0.79
elif time_of_day == "night":
    taxi_price_per_kilometer = 0.90
total_taxi_price = initiation_fee_of_taxi + taxi_price_per_kilometer * kilometers
total_bus_price = kilometers * bus_price_per_km
total_train_price = kilometers * train_price_per_km
if kilometers < 20:
    print(f"{total_taxi_price:.2f}")
elif 20 <= kilometers < 100:
    print(f"{total_bus_price:.2f}")
elif 100 <= kilometers:
    print(f"{total_train_price:.2f}")





