import json
import os
import platform

from classes.settings.app_settings_handler import load_app_settings, get_file_path


def build_json_from_environment_variables():

    os_type = platform.system()
    if os_type == 'Darwin':
        app_settings = load_app_settings()
        authentication_file = app_settings['settings']['firebase_authentication_file']
        authentication_file_path = get_file_path(authentication_file)
        creds_file = open(authentication_file_path, 'r')
        creds_string = creds_file.read()
        creds_json = json.loads(creds_string)
        private_key = creds_json['private_key']
        cred_file_path = os.environ['TMPDIR']
    else:
        private_key = os.environ['FIREBASE_PRIVATE_KEY']
        cred_file_path = os.environ['RUNNER_TEMP']

    firebase_project_id = os.environ['FIREBASE_PROJECT_ID']
    private_key_id = os.environ['FIREBASE_PRIVATE_KEY_ID']
    client_email = os.environ['FIREBASE_CLIENT_EMAIL']
    client_id = os.environ['FIREBASE_CLIENT_ID']
    client_cert_url = os.environ['FIREBASE_CLIENT_CERT_URL']

    auth_dict = {'type': 'service_account', 'project_id': firebase_project_id,
                 'private_key_id': private_key_id, 'private_key': private_key,
                 'client_email': client_email, 'client_id': client_id,
                 'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
                 'token_uri': 'https://oauth2.googleapis.com/token',
                 'auth_provider_x509_cert_url':
                     'https://www.googleapis.com/oauth2/v1/certs',
                 'client_x509_cert_url': client_cert_url}

    auth_json_string = json.dumps(auth_dict)
    if not cred_file_path.endswith('/'):
        cred_file_path = cred_file_path + '/'

    cred_file_path = cred_file_path + 'credentials.json'
    output_file = open(cred_file_path, 'w')
    output_file.write(auth_json_string)
    output_file.close()

    return auth_json_string
