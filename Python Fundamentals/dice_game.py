import random

def roll_dice():
    dict_total = random.randint(1,6) + random.randint(1,6)
    return dict_total

def main():
    player1 = input("Enter players 1's name: ")
    player2 = input("Enter players 2's name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    if roll1 > roll2:
        print(player1 + ' wins!')
    elif roll2 > roll1:
        print(player2 + ' wins!')
    else:
        print('You tie!')

main()