import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    player1, player2 = 0, 0
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    def check_snake_or_ladder(position):
        if position in snakes:
            return snakes[position]
        elif position in ladders:
            return ladders[position]
        else:
            return position

    while player1 < 100 and player2 < 100:
        input("Player 1: Press Enter to roll the dice")
        dice_value = roll_dice()
        player1 += dice_value
        player1 = check_snake_or_ladder(player1)

        if player1 >= 100:
            print("Player 1 wins!")
            break

        input("Player 2: Press Enter to roll the dice")
        dice_value = roll_dice()
        player2 += dice_value
        player2 = check_snake_or_ladder(player2)

        if player2 >= 100:
            print("Player 2 wins!")
            
            break

        print("Player 1: ", player1)
        print("Player 2: ", player2)

play_game()
