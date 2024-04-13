budget = float(input())
price_flour_per_kg = float(input())

price_eggs_per_pack = 0.75 * price_flour_per_kg
price_milk_per_l = 1.25 * price_flour_per_kg
milk_per_loaf = 0.25  # 250ml milk per loaf

loaves_count = 0
colored_eggs = 0

while budget >= price_flour_per_kg + price_eggs_per_pack + price_milk_per_l * milk_per_loaf:
    loaves_count += 1
    colored_eggs += 3
    budget -= price_flour_per_kg + price_eggs_per_pack + price_milk_per_l * milk_per_loaf

    # Check if it's time to lose some eggs
    if loaves_count % 3 == 0:
        eggs_lost = max(0, loaves_count - 2)
        colored_eggs -= eggs_lost

print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
