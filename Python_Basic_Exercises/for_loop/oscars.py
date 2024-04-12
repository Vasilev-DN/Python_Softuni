name_of_actor = input()
academy_points = float(input())
number_of_evaluative = int(input())
total_points = academy_points

for current_grade in range(number_of_evaluative):
    name_of_evaluative = input()
    points_from_the_evaluator = float(input())
    current_points = (len(name_of_evaluative) * points_from_the_evaluator) / 2
    total_points += current_points
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f'Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!')
else:
    difference = abs(1250.5 - total_points)
    print(f'Sorry, {name_of_actor} you need {difference:.1f} more!')