import pickle


def save_game(player, player2, score):
    try:
        with open("gamehistory.bin", 'rb') as file:
            Games = pickle.load(file)
            Thisgame = []

            Thisgame.append(player)
            Thisgame.append(player2)
            Thisgame.append(score)
            Games.append(Thisgame)
    except (OSError, IOError, EOFError):
        Games = []
        Thisgame = []

        Thisgame.append(player)
        Thisgame.append(player2)
        Thisgame.append(score)
        Games.append(Thisgame)

    with open("gamehistory.bin", 'wb') as file:
        pickle.dump(Games, file)


def open_games():
    try:
        with open("gamehistory.bin", 'rb') as file:
            Games = pickle.load(file)

        for game in Games:
            print(game)
            # for danne in game:
            # print(danne)
        return Games
    except EOFError:
        print("No gamehistory was found")
