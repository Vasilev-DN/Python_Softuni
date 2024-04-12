number_of_juniors_bikers = int(input())
number_of_seniors_bikers = int(input())
track_type = input()
juniors_fee = 0
seniors_fee = 0

if track_type == "trail":
    juniors_fee = number_of_juniors_bikers * 5.50
    seniors_fee = number_of_seniors_bikers * 7
elif track_type == "cross-country":
    juniors_fee = number_of_juniors_bikers * 8
    seniors_fee = number_of_seniors_bikers * 9.50
elif track_type == "downhill":
    juniors_fee = number_of_juniors_bikers * 12.25
    seniors_fee = number_of_seniors_bikers * 13.75
elif track_type == "road":
    juniors_fee = number_of_juniors_bikers * 20
    seniors_fee = number_of_seniors_bikers * 21.50

total_fees = juniors_fee + seniors_fee

if number_of_juniors_bikers + number_of_seniors_bikers >= 50 and track_type == 'cross-country':
    total_fees *= 0.75

collected_sum = total_fees * 0.95

print(f'{collected_sum:.2f}')