import pickle


class player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def set_player_name(self, name):
        self.name = name
        return self

    def save_player(self, player, filename):
        try:
            with open(filename, 'rb') as file:
                players = pickle.load(file)
        except (OSError, IOError):
            players = []

        players.append(player)

        with open(filename, 'wb') as file:
            pickle.dump(players, file)

    def clear_file(self, filename):
        with open(filename, 'wb') as f:
            pass

    def update_player_score(self, player_name, new_score, filename):
        with open(filename, 'rb') as f:
            players = pickle.load(f)
        for player in players:
            if player.name == player_name:
                player.score = new_score
        with open(filename, 'wb') as f:
            pickle.dump(players, f)

    def get_player_by_name(self, player_name, filename):
        with open(filename, 'rb') as f:
            players = pickle.load(f)
        for player in players:
            if player.name == player_name:
                return player
        return None

    def get_player_score(self, name, filename):
        with open(filename, 'rb') as file:
            players = pickle.load(file)
        for player in players:
            if player.name == name:
                return player.score

        return None

    def print_all_players(filename):
        with open(filename, "rb") as file:
            players = pickle.load(file)

            for player in players:
                print(f"{player.name} : {player.score}")
        return players


# Hur man kan använda den
# janne = get_player_by_name('Alice', filename)
# if alice:
    # print(f"Found player {alice.name} with score {alice.score}")
# else:
    # print("Player not found")