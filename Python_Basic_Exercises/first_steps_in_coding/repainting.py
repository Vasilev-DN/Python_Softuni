needed_amount_of_nylon_in_square_meters = int(input())
needed_amount_of_paint_in_liters = int(input())
needed_amount_of_thinner = int(input())
needed_hours_per_work = int(input())
price_of_nylon_per_square_meter = 1.50
price_of_paint_per_liter = 14.50
price_of_thinner_per_liter = 5.00
sum_for_nylon = float((needed_amount_of_nylon_in_square_meters + 2) * price_of_nylon_per_square_meter)
sum_for_paint = float((needed_amount_of_paint_in_liters + needed_amount_of_paint_in_liters * 0.1) * price_of_paint_per_liter)
sum_for_thinner = float(needed_amount_of_thinner * price_of_thinner_per_liter)
sum_for_bags = 0.40
total_sum_for_materials = float(sum_for_nylon + sum_for_paint + sum_for_thinner + sum_for_bags)
sum_for_masters = float((total_sum_for_materials * 0.3) * needed_hours_per_work)
total = float(total_sum_for_materials + sum_for_masters)

print(total)