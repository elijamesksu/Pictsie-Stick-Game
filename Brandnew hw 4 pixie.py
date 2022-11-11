import random

'''Display board for the pictsie stick game'''


def display_board(num_sticks):
    count = 0
    for row in range(5):
        for column in range(num_sticks):
            count += 1
            if count < 10:
                print("|", end = ' ')
            else:
                print("|", end = '  ')
        count = 0
        print()

    for i in range(num_sticks):
        print(i + 1, end = ' ')


'''% chance of sticks being added back to game after user input'''


def not_quite_right(num_sticks):
    if num_sticks < 20:
        if random.randint(1, 10) <= 3:
            return random.randint(1, 4)
        else:
            return 0


'''current player turn and number of sticks on the display board along with wrong input code'''


def get_sticks_to_take(player, num_sticks):
    display_board(num_sticks)
    sticks_taken = int(input())
    if sticks_taken > 3:
        print("Come on! Dont break the rules! You can only take 1,2 or 3 sticks!")
        print("Player", player, "how many sticks would you like to take? Select: (1,2 or 3)")
        sticks_taken = int(input())
        return sticks_taken
    elif sticks_taken < 1:
        print("Come on! Dont break the rules! You must take at least 1 stick!")
        print("Player", player, "how many sticks would you like to take? Select: (1,2 or 3)")
        int(input())
        get_sticks_to_take(player, num_sticks)
        return sticks_taken
    else:
        return sticks_taken


''' parameters listing the current player with the sticks taken, added, and remaining '''


def display_summary(player, sticks_taken, sticks_added, sticks_remaining):
    print("Player", player, "took", sticks_taken, "pictsie sticks and added", sticks_added, "back, leaving",
          sticks_remaining, "sticks left")


'''main source code'''


def main():
    num_sticks = 20
    player = 1
    while num_sticks > 0:
        player = 1
        if num_sticks > 20:
            num_sticks = 20
        print("There are currently", num_sticks, "sticks left on the board")
        print("Player 1, how many sticks would you like to take? Select: (1,2 or 3)")
        sticks_taken = get_sticks_to_take(player, num_sticks)
        num_sticks -= sticks_taken
        sticks_added = not_quite_right(num_sticks)
        num_sticks += sticks_added
        display_summary(player, sticks_taken, sticks_added, num_sticks)
        sticks_taken -= num_sticks
        if num_sticks == 0:
            print("Player", player, "you lost!! Better luck next time!!")
            break
        player = 2
        if num_sticks > 20:
            num_sticks = 20
        print("There are now currently", num_sticks, "sticks left on the board")
        print("Player 2, how many sticks would you like to take? Select: (1,2 or 3)")
        sticks_taken = get_sticks_to_take(player, num_sticks)
        num_sticks -= sticks_taken
        sticks_added = not_quite_right(num_sticks)
        num_sticks += sticks_added
        display_summary(player, sticks_taken, sticks_added, num_sticks)
        sticks_taken -= num_sticks
        continue
    else:
        print("Player", player, "you lost!! Better luck next time!!")


main()


