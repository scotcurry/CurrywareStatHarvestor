from classes.authentication.firebase_authentication_handler import \
    get_firebase_base_database
from classes.settings.app_settings_handler import load_app_settings


def get_league_name_info():

    firebase_db = get_firebase_base_database()
    app_settings = load_app_settings()
    yahoo_info_path = firebase_db.child(app_settings['settings']['yahoo_info_path'])
    yahoo_team_info = yahoo_info_path.get()

    return yahoo_team_info
