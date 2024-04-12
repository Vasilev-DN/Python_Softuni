number_of_packs_of_pens = int(input())
number_of_packs_of_markers = int(input())
liters_of_detergent = int(input())
percent_discount = int(input())
price_per_pack_of_pens = 5.80
price_per_pack_of_markers = 7.20
price_per_liter_of_detergent = 1.20
total_sum_without_discount = price_per_pack_of_pens * number_of_packs_of_pens \
                             + price_per_pack_of_markers * number_of_packs_of_markers \
                             + price_per_liter_of_detergent * liters_of_detergent
total_sum_with_discount = total_sum_without_discount - total_sum_without_discount * percent_discount / 100

print(float(total_sum_with_discount))
