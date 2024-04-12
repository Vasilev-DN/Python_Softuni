number_of_chrysanthemums = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
type_of_season = input()
holiday = input()
chrysanthemum_price = 0
rose_price = 0
tulip_price = 0
price_to_arrange = 2

if type_of_season == "Spring" or type_of_season =="Summer":
    chrysanthemum_price = 2
    rose_price = 4.10
    tulip_price = 2.50
elif type_of_season == "Autumn" or type_of_season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15

sum_for_flowers = (chrysanthemum_price * number_of_chrysanthemums) + (rose_price * number_of_roses)\
                  + (tulip_price * number_of_tulips)
if holiday == "Y":
    sum_for_flowers *= 1.15

number_of_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips

if number_of_roses > 7 and type_of_season == "Spring":
    sum_for_flowers *= 0.95

if number_of_roses >= 10 and type_of_season == "Winter":
    sum_for_flowers *= 0.90

if number_of_flowers > 20:
    sum_for_flowers *= 0.80

total_sum = sum_for_flowers + price_to_arrange
print(f"{total_sum:.2f}")
