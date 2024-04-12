price_of_vegetables_per_kg = float(input())
price_of_fruit_per_kg = float(input())
total_kg_of_vegetables = int(input())
total_kg_of_fruit = int(input())
sum_for_vegetables = price_of_vegetables_per_kg * total_kg_of_vegetables
sum_for_fruit = price_of_fruit_per_kg * total_kg_of_fruit
total_sum_in_bgn = sum_for_vegetables + sum_for_fruit
total_sum_in_eur = total_sum_in_bgn / 1.94

print("{:.2f}".format(total_sum_in_eur))
