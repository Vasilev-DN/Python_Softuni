name = input()
grades_counter = 0
years_counter = 0
failed_years_counter = 0

while years_counter < 12:
    annual_year_grade = float(input())
    if annual_year_grade < 4:
        failed_years_counter += 1
        if failed_years_counter > 1:
            excluded_year = years_counter + 1
            print(f'{name} has been excluded at {excluded_year} grade')
            break

        continue
    grades_counter += annual_year_grade
    years_counter += 1
else:
    average_grade = grades_counter / years_counter
    print(f'{name} graduated. Average grade: {average_grade:.2f}')
