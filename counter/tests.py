from django.test import TestCase
from .utils import calculate_weeks, convert_date_string


class WeeksTestCase(TestCase):
    def setUp(self):
        self.test_date_1 = convert_date_string("2020-11-27")
        self.test_date_2 = convert_date_string("2021-8-15")

    def test_calculation_weeks(self):
        """
        Test if caculation works correctly
        """
        self.assertEqual(calculate_weeks(self.test_date_1), 100)
        self.assertEqual(calculate_weeks(self.test_date_2), 138)
