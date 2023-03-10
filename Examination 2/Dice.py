import random


class dice:
    def __init__(self, score):
        self.score = score

    def roll_dice(self):
        self.score = random.randint(1, 6)
        print(f'Dice rolls a {self.score}')
        return self.score

    def roll_dice_cheat(self):
        self.score = random.randint(50, 55)
        print(f'Dice rolls a {self.score}')
        return self.score


def dice_hand(player):
    print(f'{player} rolls the dice')
    Dice = dice(1)
    player = Dice.roll_dice()
    return player


def dice_hand_cheat(player):
    print(f'{player} rolls the dice')
    Dice = dice(1)
    player = Dice.roll_dice_cheat()
    return player
