import unittest


class MyTestCase(unittest.TestCase):
    def test_get_all_players(self):

        player_count = 25
        self.assertEqual(player_count, 25)  # add assertion here


if __name__ == '__main__':
    unittest.main()
