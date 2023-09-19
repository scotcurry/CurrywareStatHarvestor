import os
import platform

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from classes.settings.app_settings_handler import load_app_settings, get_file_path
from classes.authentication.google_build_authentication import \
    build_json_from_environment_variables

app_settings = load_app_settings()
authentication_file = app_settings['settings']['firebase_authentication_file']
database_url = app_settings['settings']['firebase_database_name']
database_url_json = {'databaseURL': database_url}


def get_firebase_base_database():

    build_json_from_environment_variables()
    os_type = platform.system()
    if os_type == 'Darwin':
        authentication_file_path = os.environ['TMPDIR'] + 'credentials.json'
    else:
        temp_folder = os.environ['RUNNER_TEMP']
        if not temp_folder.endswith('/'):
            temp_folder = temp_folder + '/'

        authentication_file_path = temp_folder + 'credentials.json'

    # app_settings = load_app_settings()
    # authentication_file = app_settings['settings']['firebase_authentication_file']
    # authentication_file_path = get_file_path(authentication_file)

    # creds = credentials.Certificate(authentication_file_path)

    path_to_authorization_file = get_file_path(authentication_file_path)
    creds = credentials.Certificate(path_to_authorization_file)
    try:
        firebase_admin.get_app()
    except ValueError:
        firebase_admin.initialize_app(creds, database_url_json)

    os.remove(authentication_file_path)

    return db.reference('/')
