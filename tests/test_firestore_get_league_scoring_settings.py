import unittest

from classes.firestore.firestore_retreive_league_scoring_settings import \
    get_league_settings


class RetrieveLeagueSettingsTestCase(unittest.TestCase):
    def test_something(self):
        team_name = 'olcc_2023'
        league_settings = get_league_settings(team_name)
        first_stat = league_settings[0]['stat_id_4']
        stat_name = first_stat['display_name']
        self.assertEqual('Pass Yds', stat_name)  # add assertion here


if __name__ == '__main__':
    unittest.main()
