needed_money_for_excursion = float(input())
available_money = float(input())
days_counter = 0
days_with_money_spent = 0

while available_money < needed_money_for_excursion:
    command = input()
    money = float(input())
    days_counter += 1
    if command == 'save':
        available_money += money
        days_with_money_spent = 0
    elif command == 'spend':
        available_money -= money
        days_with_money_spent += 1
        if days_with_money_spent >= 5:
            break
        if available_money < 0:
            available_money = 0

if days_with_money_spent == 5:
    print(f'You can\'t save the money.')
    print(days_counter)
elif available_money >= needed_money_for_excursion:
    print(f'You saved the money for {days_counter} days.')



