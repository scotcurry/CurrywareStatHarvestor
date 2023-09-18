import unittest

from classes.firebase.firebase_league_names import get_league_name_info


class GetLeagueNames(unittest.TestCase):

    def test_get_league_names(self):
        league_names = get_league_name_info()
        self.assertEqual(league_names['olcc_2021']['league_id'],
                         967657)
