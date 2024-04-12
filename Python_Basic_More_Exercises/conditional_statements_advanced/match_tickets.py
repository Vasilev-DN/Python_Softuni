budget = float(input())
ticket_category = input()
people_in_group = int(input())
ticket_price = 0

if 1 <= people_in_group <= 4:
    budget *= 0.25
elif 5 <= people_in_group <= 9:
    budget *= 0.40
elif 10 <= people_in_group <= 24:
    budget *= 0.50
elif 25 <= people_in_group <= 49:
    budget *= 0.60
elif people_in_group >= 50:
    budget *= 0.75

if ticket_category == 'VIP':
    ticket_price = 499.99
elif ticket_category == 'Normal':
    ticket_price = 249.99

sum_for_tickets = ticket_price * people_in_group
difference = abs(sum_for_tickets - budget)

if budget >= sum_for_tickets:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')



