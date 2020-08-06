from django.test import TestCase
from myapi.functions import get_fuel_tank
from myapi.functions import get_fuel_consumption
from myapi.functions import get_maximum_mins


class BasicTest(TestCase):
    def test_functions(self):
        self.assertEqual(200, get_fuel_tank(1))
        self.assertEqual(0.004, get_fuel_consumption(1, 2))
        self.assertEqual(500, get_maximum_mins(2, 0.004))
