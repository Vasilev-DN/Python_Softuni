mackerel_price_per_kg = float(input())
sprats_price_per_kg = float(input())
bonito_kg = float(input())
scad_kg = float(input())
seashell_kg = int(input())
seashell_price = 7.50
bonito_price = mackerel_price_per_kg * 1.6
scad_price = sprats_price_per_kg * 1.8
sum_of_bonito = bonito_price * bonito_kg
sum_of_scad = scad_price * scad_kg
sum_of_seashell = seashell_kg * seashell_price
total_sum = sum_of_bonito + sum_of_scad + sum_of_seashell

print("{:.2f}".format(total_sum))


