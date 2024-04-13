happiness_input = input()
happiness_factors_input = input()

happiness = [int(x) for x in happiness_input.split()]
happiness_factor = int(happiness_factors_input)

adjusted_happiness = [h * happiness_factor for h in happiness]

average_happiness = sum(adjusted_happiness) / len(adjusted_happiness)

happy_count = sum(1 for h in adjusted_happiness if h >= average_happiness)

total_count = len(adjusted_happiness)
if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
