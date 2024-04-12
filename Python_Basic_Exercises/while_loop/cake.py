cake_width = int(input())
cake_length = int(input())
total_cake_pieces = cake_width * cake_length
no_more_pieces = False
taking_pieces = input()

while taking_pieces != 'STOP':
    taking_pieces = int(taking_pieces)
    total_cake_pieces -= taking_pieces

    if total_cake_pieces <= 0:
        no_more_pieces = True
        break

    taking_pieces = input()

if no_more_pieces:
    print(f'No more cake left! You need {abs(total_cake_pieces)} pieces more.')
else:
    print(f'{total_cake_pieces} pieces are left.')





