import os
import sys
import logging

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from classes.settings.app_settings_handler import load_app_settings, get_file_path

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
logger.addHandler(stream_handler)
logger.setLevel(level=LOGLEVEL)


def get_firestore_database():

    app_settings = load_app_settings()
    authentication_file = app_settings['settings']['firebase_authentication_file']
    authentication_file_path = get_file_path(authentication_file)

    creds = credentials.Certificate(authentication_file_path)
    try:
        firebase_admin.get_app('currywareff')
    except ValueError:
        app = firebase_admin.initialize_app(creds, None, 'currywareff')
        logger.info('Project ID: ' + app.project_id)

    db = firestore.client()

    return db
