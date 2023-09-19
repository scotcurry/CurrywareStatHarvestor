import json
import os
import platform
import unittest

from classes.authentication.google_build_authentication import \
    build_json_from_environment_variables


class BuildAuthenticationTestCase(unittest.TestCase):
    def test_something(self):

        os_type = platform.system()
        build_json_from_environment_variables()
        if os_type == 'Darwin':
            temp_path = os.environ['TMPDIR']
        else:
            temp_path = os.environ['RUNNER_TEMP']
            if not temp_path.endswith('/'):
                temp_path = temp_path + '/'

        cred_file_path = temp_path + 'credentials.json'
        file_to_read = open(cred_file_path, 'r')
        auth_json = file_to_read.read()
        file_to_read.close()
        auth_content = json.loads(auth_json)
        auth_uri = auth_content['auth_uri']
        self.assertEqual('https://accounts.google.com/o/oauth2/auth', auth_uri)


if __name__ == '__main__':
    unittest.main()
