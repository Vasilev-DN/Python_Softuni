number_break_days = int(input())
number_work_days = 365 - int(number_break_days)
total_play_time = number_work_days*63 + number_break_days*127
difference = abs(30000 - int(total_play_time))
difference_hours = abs(difference // 60)
difference_minutes = abs(difference % 60)
if total_play_time > 30000:
    print(f'Tom will run away')
    print(f'{difference_hours} hours and {difference_minutes:02d} minutes more for play')
else:
    print(f'Tom sleeps well')
    print(f'{difference_hours} hours and {difference_minutes} minutes less for play')







