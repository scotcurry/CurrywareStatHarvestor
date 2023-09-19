import os
import platform
import sys
import logging

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from classes.settings.app_settings_handler import load_app_settings, get_file_path
from classes.authentication.google_build_authentication import \
    build_json_from_environment_variables

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
logger.addHandler(stream_handler)
logger.setLevel(level=LOGLEVEL)


def get_firestore_database():

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

    creds = credentials.Certificate(authentication_file_path)
    os.remove(authentication_file_path)
    try:
        firebase_admin.get_app('currywareff')
    except ValueError:
        app = firebase_admin.initialize_app(creds, None, 'currywareff')
        logger.info('Project ID: ' + app.project_id)

    db = firestore.client()

    return db
