from Intelligence import create_bot
from Intelligence import bot_play_easy
from Intelligence import bot_play_medium
from Intelligence import bot_play_hard
from Intelligence import calculate_score


def test_create_bot_default():
    assert create_bot() != "Computer"
    assert create_bot() != 0


def test_bot_play_easy():
    assert bot_play_easy != 7
    assert bot_play_easy != 0


def test_bot_play_medium():
    assert bot_play_medium != 7
    assert bot_play_medium != 0


def test_bot_play_hard():
    assert bot_play_hard != 7
    assert bot_play_hard != 0


def test_calculate_score_default():
    assert calculate_score(bot_play_easy(create_bot())) != str
    assert calculate_score(bot_play_medium(create_bot())) != str
    assert calculate_score(bot_play_hard(create_bot())) != str
