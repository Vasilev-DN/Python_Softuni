budget = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_ram_memories = int(input())
video_cards_price = number_of_video_cards * 250
one_processor_price = video_cards_price * 0.35
processors_price = one_processor_price * number_of_processors
one_ram_memory_price = video_cards_price * 0.1
ram_memories_price = one_ram_memory_price * number_of_ram_memories
needed_money = video_cards_price + processors_price + ram_memories_price
if number_of_video_cards > number_of_processors:
    needed_money *= 0.85
difference = abs(budget - needed_money)

if budget >= needed_money:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")

