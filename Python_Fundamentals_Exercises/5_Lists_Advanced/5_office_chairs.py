def check_chairs(n, rooms):
    needed_chairs_in_rooms = []

    for room_number, room in enumerate(rooms, start=1):
        chairs, visitors = room.split()
        chairs_count = len(chairs)
        visitors_count = int(visitors)

        if chairs_count < visitors_count:
            needed_chairs = visitors_count - chairs_count
            needed_chairs_in_rooms.append((needed_chairs, room_number))

    if needed_chairs_in_rooms:
        for needed_chairs, room_number in needed_chairs_in_rooms:
            print(f"{needed_chairs} more chairs needed in room {room_number}")
    else:
        total_free_chairs = sum(max(0, len(chairs) - int(visitors)) for chairs, visitors in (room.split() for room in rooms))
        print(f"Game On, {total_free_chairs} free chairs left")

n = int(input())
rooms_info = [input() for _ in range(n)]

check_chairs(n, rooms_info)
