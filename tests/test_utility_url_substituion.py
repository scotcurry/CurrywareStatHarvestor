import unittest

from classes.utilities.url_substitution_utility import build_url


class UrlSubstitution(unittest.TestCase):

    def test_url_substitution(self):
        url_to_modify = '/league/{game_id}.l.{league_id}/settings'
        league_id = 321592
        game_id = 423
        modified_url = build_url(url_to_modify, str(game_id), str(league_id))

        self.assertEqual(modified_url, '/league/423.l.321592/settings')
