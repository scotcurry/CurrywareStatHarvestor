from unittest import TestCase

from classes.fantasy.league_settings_loader import get_league_settings_json


class Test(TestCase):
    def test_get_league_settings(self):
        team_name = 'olcc_2023'
        return_value = get_league_settings_json(team_name)
        score_setting = return_value['score_settings'][0]
        value_to_test = score_setting['stat_value']
        self.assertEqual('0.04', value_to_test)  # add assertion here
