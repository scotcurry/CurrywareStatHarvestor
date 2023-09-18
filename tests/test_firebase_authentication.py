from unittest import TestCase

from classes.authentication.firebase_authentication_handler import \
    get_firebase_base_database


class Test(TestCase):
    def test_get_firestore_client(self):
        firebase_database_reference = get_firebase_base_database()
        self.assertEqual('/', firebase_database_reference.path)
