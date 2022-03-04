import unittest
from game import Game
from gestures import Gestures


class TestRockPaperScissors(unittest.TestCase):
    def test_when_game_starts_then_there_are_two_players(self):
        game = Game()
        self.assertEqual(game.number_of_players, 2)

    def test_when_possible_gestures_are_checked_then_only_rock_paper_and_scissor_values_are_retrieved(self):
        gestures_values_entity = Gestures()
        all_possible_gestures = gestures_values_entity.get_list_of_all_gestures()
        expected_gesture_values = ['paper', 'rock', 'scissors']
        self.assertCountEqual(all_possible_gestures, expected_gesture_values)

    def test_given_a_player_then_player_uses_a_gesture(self):
        sample_player = Player(sample_gesture)
        self.assertIsNotNone(sample_player.get_gesture)

if __name__ == '__main__':
    unittest.main()
