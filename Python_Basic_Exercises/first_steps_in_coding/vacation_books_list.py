number_of_pages_of_the_book = int(input())
pages_per_hour = int(input())
number_of_days_to_read_the_book = int(input())
needed_hours_per_whole_book = number_of_pages_of_the_book / pages_per_hour
needed_hours_per_day = needed_hours_per_whole_book / number_of_days_to_read_the_book

print(int(needed_hours_per_day))