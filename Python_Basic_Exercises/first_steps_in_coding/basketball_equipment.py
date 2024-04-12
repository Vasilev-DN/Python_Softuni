annual_training_fee = int(input())
basketball_sneakers = annual_training_fee * 0.6
basketball_equipment = basketball_sneakers * 0.8
basketball_ball = basketball_equipment / 4
basketball_accessories = basketball_ball / 5
total_price = float(annual_training_fee + basketball_sneakers + basketball_equipment + basketball_ball + basketball_accessories)

print(total_price)