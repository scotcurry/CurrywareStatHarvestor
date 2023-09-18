import unittest

from classes.utilities.get_game_and_league_from_name import \
    get_league_and_game_id_from_league_name


class GetLeagueIDFromName(unittest.TestCase):
    def test_something(self):
        league_name = 'picard_2023'
        game_id, league_id = get_league_and_game_id_from_league_name(league_name)
        string_to_test = game_id + '|' + league_id
        self.assertEqual('423|670923', string_to_test)  # add assertion here


if __name__ == '__main__':
    unittest.main()
