def menu():
    print("1. New game\n 2. Check game history\n 3. Check Scoreboard\
        \n 4. Game rules\n 5. Quit")
    choice = input("Enter your choice!")
    return choice


def game_mode_menu():
    print("Select gamemode!\n1. Singleplayer\n2. Multiplayer")
    choice = input("Enter your choice!")
    return choice


def current_round():
    print("1. Roll again!\n2. Hold!")
    choice = input("Enter your choice!")
    return choice


def current_game_menu():
    print("1. Continue vs opponent\n2. Exit game!")
    choice = input("Enter your choice!")
    return choice


def game_rules():
    print("The game rules is as follows!\n* Take turns rolling the dice\
        between 1 and 6.\n* if u roll 1 then it is opponents turn\
        otherwise you collect the points you roll untill you decide to\
        hold. But if you dont hold and on ex. your 3rd roll you hit 1 you\
        get 0 points!\n The player with the highest score wins the game and\
        gets 1 point")
