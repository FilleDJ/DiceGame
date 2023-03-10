from Player import player
from Dice import dice_hand
import random


def create_bot():
    bot = player("Computer", 0)
    return bot


def bot_play_easy(bot):
    score = dice_hand(bot.name)
    final_score = 0
    final_score = final_score + score
    chance = random.randint(1, 5)
    if chance < score:
        add = bot_play_easy(bot)
        final_score = final_score + add
    return final_score


def bot_play_medium(bot):
    score = dice_hand(bot.name)
    final_score = 0
    final_score = final_score + score
    chance = random.randint(1, 4)
    if chance < score:
        add = bot_play_medium(bot)
        final_score = final_score + add
    return final_score


def bot_play_hard(bot):
    score = dice_hand(bot.name)
    final_score = 0
    final_score = final_score + score
    chance = random.randint(1, 2)
    if chance < score:
        add = bot_play_hard(bot)
        final_score = final_score + add
    return final_score


def calculate_score(final_score):
    return final_score


bot = create_bot()
calculate_score(bot_play_medium(bot))
