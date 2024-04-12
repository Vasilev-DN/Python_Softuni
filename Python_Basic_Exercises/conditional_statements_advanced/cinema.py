screening_time = input()
rows = int(input())
columns = int(input())
total_seats = rows * columns
ticket_price = 0

if screening_time == 'Premiere':
    ticket_price = 12.00
elif screening_time == 'Normal':
    ticket_price = 7.50
elif screening_time == 'Discount':
    ticket_price = 5
total_income = ticket_price * total_seats

print(f'{total_income:.2f} leva')