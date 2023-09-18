import time
import requests

from classes.authentication.firebase_authentication_handler import \
    get_firebase_base_database
from classes.settings.app_settings_handler import load_app_settings


# This function pulls the latest Yahoo information.  The access token may be good,
# and if not, it gets a refresh token.
def get_oauth_token():

    settings = load_app_settings()
    oauth_settings_path = settings['settings']['oauth_settings_path']
    firebase_db = get_firebase_base_database()
    oauth_path = firebase_db.child(oauth_settings_path)
    oauth_settings = oauth_path.get()
    last_updated = oauth_settings['last_token_update']

    current_time = int(time.time())
    if current_time > (last_updated + 3600):
        access_token = get_token_from_refresh(oauth_settings, oauth_path)
    else:
        access_token = oauth_settings['auth_token']

    return access_token


# If the access token is expired, we use this to get a refresh token.  This will force
# us to update the token information in the update_auth_token section.  oauth_settings
# have the information to post, and oauth_path is the
# firebase db reference
def get_token_from_refresh(oauth_settings, oauth_path):

    request_data = {'client_id': oauth_settings['clientID'],
                    'client_secret': oauth_settings['clientSecret'],
                    'redirect_uri': oauth_settings['redirect_url'],
                    'refresh_token': oauth_settings['refresh_token'],
                    'grant_type': 'refresh_token'}
    refresh_token_endpoint = (oauth_settings['authority'] +
                              oauth_settings['token_endpoint'])
    refresh_auth_token = requests.post(refresh_token_endpoint, data=request_data)
    refresh_token_json = refresh_auth_token.json()
    auth_token = refresh_token_json['access_token']
    refresh_token = refresh_token_json['refresh_token']

    update_oauth_token(auth_token, refresh_token, oauth_path)

    return auth_token


def update_oauth_token(auth_token, refresh_token, oauth_path):

    oauth_node = oauth_path
    current_time = int(time.time())
    set_oauth_value = {'auth_token': auth_token, 'refresh_token': refresh_token,
                       'last_token_update': current_time}
    new_reference = oauth_node.update(set_oauth_value)

    return new_reference
