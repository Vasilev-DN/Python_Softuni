one_puzzle_price = 2.60
one_speaking_doll_price = 3
one_teddy_bear_price = 4.10
one_minion_price = 8.20
one_truck_price = 2
excursion_price = float(input())
puzzles_amount = int(input())
speaking_dolls_amount = int(input())
teddy_bears_amount = int(input())
minions_amount = int(input())
trucks_amount = int(input())

total_amount_toys = puzzles_amount + speaking_dolls_amount + teddy_bears_amount + minions_amount + trucks_amount
total_price_of_toys = puzzles_amount * 2.60 + speaking_dolls_amount * 3 + teddy_bears_amount *4.10\
                      + minions_amount * 8.20 + trucks_amount * 2

if total_amount_toys >= 50:
    total_price_of_toys *= 0.75
store_rent = total_price_of_toys * 0.1
order_profit = total_price_of_toys - store_rent
difference = abs(order_profit - excursion_price)

if order_profit >= excursion_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")


