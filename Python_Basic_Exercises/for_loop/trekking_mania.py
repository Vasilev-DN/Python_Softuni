number_of_groups = int(input())
mousala_climbers = 0
monblan_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0

for current_croup in range(number_of_groups):
    current_group_climbers = int(input())
    if current_group_climbers <= 5:
        mousala_climbers += current_group_climbers
    elif current_group_climbers <= 12:
        monblan_climbers += current_group_climbers
    elif current_group_climbers <= 25:
        kilimanjaro_climbers += current_group_climbers
    elif current_group_climbers <= 40:
        k2_climbers += current_group_climbers
    elif current_group_climbers >= 41:
        everest_climbers += current_group_climbers
    total_climbers += current_group_climbers

percentage_mousala_climbers = mousala_climbers / total_climbers * 100
percentage_monblan_climbers = monblan_climbers / total_climbers * 100
percentage_kilimanjaro_climbers = kilimanjaro_climbers / total_climbers * 100
percentage_k2_climbers = k2_climbers / total_climbers * 100
percentage_everest_climbers = everest_climbers / total_climbers * 100

print(f'{percentage_mousala_climbers:.2f}%')
print(f'{percentage_monblan_climbers:.2f}%')
print(f'{percentage_kilimanjaro_climbers:.2f}%')
