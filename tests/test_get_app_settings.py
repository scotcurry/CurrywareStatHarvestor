import platform
from unittest import TestCase

from classes.settings.app_settings_handler import load_app_settings, get_file_path


class Test(TestCase):
    def test_get_app_settings(self):
        os_type = platform.system()
        if os_type == 'Darwin':
            settings = load_app_settings()
            test_value = settings['settings']['firebase_authentication_file']
            if test_value == 'currywareff-firebase-adminsdk.json':
                test_assertion = True
            else:
                test_assertion = False
            self.assertEqual(True, test_assertion)
        else:
            self.assertEqual(True, True)

    def test_get_google_auth_file(self):
        auth_file_name = 'currywareff-firebase-adminsdk.json'
        file_path = get_file_path(auth_file_name)
        file_name_in_path = auth_file_name in file_path
        self.assertEqual(True, file_name_in_path)
