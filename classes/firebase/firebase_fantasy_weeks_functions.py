import datetime

from google.cloud.firestore_v1 import FieldFilter


# This function takes in a DB instance and a date.  Based on the date it looks up
# where in the schedule the date is. Will be used to figure out when to get the
# statistics from the prior week.  Console URL
# console.firebase.google.com/project/currywareff/firestore/data/~2F2023_weeks~2Fweek_1
def get_statistics_week(db, date_to_check):

    all_weeks = (
        db.collection('2023_weeks').where(filter=FieldFilter('week_start',
                                                             '>=',
                                                             date_to_check))
        .stream()
    )

    counter = 0
    required_week = None
    for current_week in all_weeks:
        if counter == 0:
            required_week = current_week.id
            counter = counter + 1

    return required_week


# This function is just to automate the adding of the weeks to the firestore database.
# Takes in the database, start_week, and the start datetime.  There is no test for this
# as it is a one and done type function used once a year.
def add_weeks(db, start_week, start_datetime):

    for counter in range(start_week, 18, 1):

        time_delta = datetime.timedelta(6, 59, 0,
                                        0, 59, 23, 0)
        end_week_datetime = start_datetime + time_delta
        week_data = {'week_start': start_datetime, 'week_end': end_week_datetime}
        week_document = 'week_' + str(start_week)
        db.collection('2022_weeks').document(week_document).set(week_data)
        time_delta = datetime.timedelta(0, 1, 0,
                                        0, 0, 0, 0)
        start_datetime = end_week_datetime + time_delta
        start_week = start_week + 1
