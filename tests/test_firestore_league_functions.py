import pytz
from datetime import datetime
from unittest import TestCase

from classes.firestore.firestore_database_functions import get_statistics_week, add_weeks


class Test(TestCase):
    def test_get_statistics_week(self):
        day_to_check = datetime(2023, 11, 7, 10, 14, 3)
        week_to_check = get_statistics_week(day_to_check)
        self.assertEqual(week_to_check, 'week_11')

    def test_add_weeks(self):
        start_week = 1
        utc_timezone = pytz.timezone('America/New_York')
        start_time = datetime(2022, 9, 6, 7, 0, 0, tzinfo=utc_timezone)
        add_weeks(start_week, start_time)
