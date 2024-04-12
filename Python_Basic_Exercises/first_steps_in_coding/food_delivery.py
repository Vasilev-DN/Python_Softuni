number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarians_menus = int(input())
price_for_chicken_menu = 10.35
price_for_fish_menu = 12.40
price_for_vegetarian_menu = 8.15
sum_for_chicken_menus = float(number_of_chicken_menus * price_for_chicken_menu)
sum_for_fish_menus = float(number_of_fish_menus * price_for_fish_menu)
sum_for_vegetarian_menus = float(number_of_vegetarians_menus * price_for_vegetarian_menu)
total_price_for_menus = float(sum_for_chicken_menus + sum_for_fish_menus + sum_for_vegetarian_menus)
price_for_dessert = float(total_price_for_menus * 0.2)
price_for_delivery = 2.50
total_price_for_order = float(total_price_for_menus + price_for_dessert + price_for_delivery)

print(total_price_for_order)
