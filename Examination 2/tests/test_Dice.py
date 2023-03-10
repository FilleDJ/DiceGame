from Dice import dice_hand
from Dice import dice_hand_cheat


def test_dice_hand():
    assert dice_hand("Janne") == 1 or 2 or 3 or 4 or 5 or 6
    assert dice_hand("Janne") != 0
    assert dice_hand("Janne") != 7


def test_dice_hand_cheat():
    assert dice_hand_cheat("Janne") == 50 or 51 or 52 or 53 or 54 or 55
    assert dice_hand_cheat("Janne") != 49
    assert dice_hand_cheat("Janne") != 56
