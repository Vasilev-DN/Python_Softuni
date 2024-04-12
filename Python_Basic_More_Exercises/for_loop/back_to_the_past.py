inherited_money = float(input())
year_to_live_up_to = int(input())
age = 18
year_in_row = 1800

for i in range(year_to_live_up_to):
    if year_in_row % 2 == 0:
        age += 1
        sum_spent = 12000
        inherited_money -= sum_spent
        year_in_row += 1
        if year_in_row % 2 == 1:
            sum_spent = 12000 + 50 * age
            inherited_money -= sum_spent
            age += 1
            year_in_row += 1
        if year_in_row == year_to_live_up_to:
            break
if inherited_money <=0:
    difference = abs(inherited_money - sum_spent)
    print(f'He will need {difference:.2f} dollars to survive.')
else:
    rest_sum = inherited_money - sum_spent
    print(f'Yes! He will live a carefree life and will have {rest_sum:.2f} dollars left.')






