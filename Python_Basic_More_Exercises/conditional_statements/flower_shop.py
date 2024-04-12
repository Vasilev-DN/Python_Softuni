from math import ceil, floor
number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cactus = int(input())
gift_price = float(input())

magnolia_price = 3.25
hyacinth_price = 4
rose_price = 3.50
cactus_price = 8

sum_of_magnolias = number_of_magnolias * magnolia_price
sum_of_hyacinths = number_of_hyacinths * hyacinth_price
sum_of_roses = number_of_roses * rose_price
sum_of_cactus = number_of_cactus * cactus_price
total_sum = sum_of_magnolias + sum_of_hyacinths + sum_of_roses + sum_of_cactus
total_sum_after_tax = total_sum * 0.95
difference = abs(total_sum_after_tax - gift_price)

if total_sum_after_tax >= gift_price:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")

