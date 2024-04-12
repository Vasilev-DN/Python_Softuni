deposit = float(input())
term_of_the_deposit = int(input())
annual_interest_percent = float(input())
annual_interest = deposit * annual_interest_percent / 100
montly_interest = annual_interest / 12
total_sum = deposit + (term_of_the_deposit * montly_interest)

print(total_sum)