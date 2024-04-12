height_of_the_house_x = float(input())
length_of_the_side_wall_of_the_house_y = float(input())
height_of_the_triangular_roof_wall_h = float(input())
area_of_one_side_wall = height_of_the_house_x * length_of_the_side_wall_of_the_house_y #60
window_side = 1.5
window_area = window_side * window_side #2.25
area_on_both_sides_of_the_house = (area_of_one_side_wall * 2) - (window_area * 2) #115.5
width_of_the_front_door = 1.2
height_of_the_front_door = 2
area_of_front_door = width_of_the_front_door * height_of_the_front_door #2.4
area_of_back_wall_of_the_house = height_of_the_house_x * height_of_the_house_x #36
area_of_front_wall_of_the_house = height_of_the_house_x * height_of_the_house_x - area_of_front_door #33.6
area_of_back_and_front_wall_of_the_house = area_of_front_wall_of_the_house + area_of_back_wall_of_the_house #69.6
total_wall_area =area_on_both_sides_of_the_house + area_of_back_and_front_wall_of_the_house
consumption_of_green_paint = 3.4
green_paint_needed = total_wall_area / consumption_of_green_paint

print("{:.2f}".format(green_paint_needed))

total_area_of_the_two_roof_rectangles = (height_of_the_house_x * length_of_the_side_wall_of_the_house_y) * 2
total_area_of_the_two_roof_triangles = (height_of_the_house_x * height_of_the_triangular_roof_wall_h / 2) * 2
total_area_of_the_roof = total_area_of_the_two_roof_rectangles + total_area_of_the_two_roof_triangles
consumption_of_red_paint = 4.3
red_paint_needed = total_area_of_the_roof / consumption_of_red_paint

print("{:.2f}".format(red_paint_needed))



