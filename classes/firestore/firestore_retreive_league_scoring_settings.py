from classes.authentication.firebase_authentication_handler import get_firebase_base_database

from classes.settings.app_settings_handler import load_app_settings


def get_league_settings(team_name):

    app_settings = load_app_settings()
    yahoo_path = app_settings['settings']['yahoo_info_path']
    path_to_league_settings = yahoo_path + '/' + team_name
    db = get_firebase_base_database()
    reference = db.child(path_to_league_settings)
    score_settings_child = reference.child('score_settings')
    league_stats = score_settings_child.get()
    return league_stats
