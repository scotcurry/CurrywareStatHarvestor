from unittest import TestCase

from classes.authentication.firestore_authentication_handler import get_firestore_database


class Test(TestCase):
    def test_get_auth_token(self):
        firestore_db = get_firestore_database()
        self.assertEqual('currywareff', firestore_db.project)
