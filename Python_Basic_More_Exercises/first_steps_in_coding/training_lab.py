import math
length_of_the_hall_in_m = float(input())
width_of_the_hall_in_m = float(input())
workplaces_loss_because_of_the_door = 1
workplaces_loss_because_of_the_chair = 2
total_workplaces_lost = workplaces_loss_because_of_the_door + workplaces_loss_because_of_the_chair
width_of_the_hall_without_corridor_in_m = float(width_of_the_hall_in_m - 1)
width_of_one_workplace_in_m = 0.7
number_of_desks_per_row = (math.floor(width_of_the_hall_without_corridor_in_m / width_of_one_workplace_in_m))
lenght_of_one_workplace_in_m = 1.2
number_of_rows_in_hall = (math.floor(length_of_the_hall_in_m / lenght_of_one_workplace_in_m))
total_desks_in_the_hall = number_of_desks_per_row * number_of_rows_in_hall - total_workplaces_lost

print(total_desks_in_the_hall)