day_counter = int(input())
number_of_patients = int(input())
number_of_doctors = 7
examined_patients = 0
unexamined_patients = 0
total_examined_patients = 0
total_unexamined_patients = 0

for day_counter in range(day_counter):
    if day_counter < 3:
        examined_patients = number_of_doctors * 1
        if number_of_patients < number_of_doctors:
            examined_patients = number_of_patients
        unexamined_patients = number_of_patients - examined_patients
        total_examined_patients += examined_patients
        total_unexamined_patients += unexamined_patients
        number_of_patients = int(input())
    elif day_counter == 3 and total_unexamined_patients > total_examined_patients:
        number_of_doctors += 1
        examined_patients = number_of_doctors * 1
        if number_of_patients < number_of_doctors:
            examined_patients = number_of_patients
        unexamined_patients = number_of_patients - examined_patients
        total_examined_patients += examined_patients
        total_unexamined_patients += unexamined_patients
        number_of_patients = int(input())
    elif day_counter > 3:
        examined_patients = number_of_doctors * 1
        if number_of_patients < number_of_doctors:
            examined_patients = number_of_patients
        unexamined_patients = number_of_patients - examined_patients
        total_examined_patients += examined_patients
        total_unexamined_patients += unexamined_patients
        number_of_patients = int(input())

print(f'Treated patients: {total_examined_patients}.')
print(f'Untreated patients: {total_unexamined_patients}.')
