import unittest
import Player


class TestPlayer(unittest.TestCase):
    
    def test_set_player_name(self, name):
        self.name = name
        assert self


if __name__ == "__main__":
    unittest.main()
