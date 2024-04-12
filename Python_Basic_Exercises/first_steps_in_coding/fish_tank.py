lenght = int(input())
width = int(input())
height = int(input())
percent_non_free_volume = float(input())
volume_of_the_aquarium_in_centimeters = lenght * width * height
volume_of_the_aquarium_in_liters = volume_of_the_aquarium_in_centimeters * 0.001
percent_occupied_volume = percent_non_free_volume * 0.01
needed_liters = volume_of_the_aquarium_in_liters * (1-percent_occupied_volume)

print(needed_liters)



