import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from classes.settings.app_settings_handler import load_app_settings, get_file_path

app_settings = load_app_settings()
authentication_file = app_settings['settings']['firebase_authentication_file']
database_url = app_settings['settings']['firebase_database_name']
database_url_json = {'databaseURL': database_url}


def get_firebase_base_database():

    path_to_authorization_file = get_file_path(authentication_file)
    creds = credentials.Certificate(path_to_authorization_file)
    try:
        firebase_admin.get_app()
    except ValueError:
        firebase_admin.initialize_app(creds, database_url_json)

    return db.reference('/')
