import datetime
from google.cloud.firestore_v1 import FieldFilter

from classes.authentication.firestore_authentication_handler import get_firestore_database


def get_statistics_week(date_to_check):

    db = get_firestore_database()
    all_weeks = (
        db.collection('2023_weeks').where(filter=FieldFilter('week_start',
                                                             '>=',
                                                             date_to_check)).stream())

    counter = 0
    required_week = None
    for current_week in all_weeks:
        if counter == 0:
            required_week = current_week.id
            counter = counter + 1

    return required_week


def add_weeks(start_week, start_datetime):

    db = get_firestore_database()
    for counter in range(start_week, 18, 1):

        time_delta = datetime.timedelta(6, 59, 0, 0, 59, 23, 0)
        end_week_datetime = start_datetime + time_delta
        week_data = {'week_start': start_datetime, 'week_end': end_week_datetime}
        week_document = 'week_' + str(start_week)
        db.collection('2022_weeks').document(week_document).set(week_data)
        time_delta = datetime.timedelta(0, 1, 0, 0, 0, 0, 0)
        start_datetime = end_week_datetime + time_delta
        start_week = start_week + 1
