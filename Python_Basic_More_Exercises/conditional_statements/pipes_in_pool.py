pool_volume_in_liters_v = int(input())
first_pipe_debit_per_hour_p1 = int(input())
second_pipe_debit_per_hour_p2 = int(input())
hours_of_absence_of_the_worker = float(input())

liters_of_first_pipe = first_pipe_debit_per_hour_p1 * hours_of_absence_of_the_worker
liters_of_second_pipe = second_pipe_debit_per_hour_p2 * hours_of_absence_of_the_worker
total_liters = liters_of_first_pipe + liters_of_second_pipe
pool_occupancy_percentage = (total_liters / pool_volume_in_liters_v) * 100
percentage_of_the_first_pipe = (liters_of_first_pipe / total_liters) * 100
percentage_of_the_second_pipe = (liters_of_second_pipe / total_liters) * 100
difference = abs(pool_volume_in_liters_v - total_liters)

if pool_occupancy_percentage <= pool_volume_in_liters_v:
    print(f'The pool occupancy is {pool_occupancy_percentage:.2f} full.'
          f'Pipe 1: {percentage_of_the_first_pipe:.2f}%.'
          f'Pipe 2: {percentage_of_the_second_pipe:.2f}%.')
else:
    print(f'For {hours_of_absence_of_the_worker:.2f} hours the pool overflows with {difference:.2f} liters.')





