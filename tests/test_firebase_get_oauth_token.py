import unittest

from classes.firebase.firebase_get_oauth_token import get_oauth_token


class GetFirebaseOAuthTokenCase(unittest.TestCase):

    def test_get_firebase_oauth_token(self):
        oauth_token = get_oauth_token()
        if len(oauth_token) > 800:
            have_auth_token = True
        self.assertEqual(have_auth_token, True)  # add assertion here
