"""
Sample tests
"""

from django.test import SimpleTestCase

from app import cal

class CalcTests(SimpleTestCase):
    """ test the calc module """
    def test_add_numbers(self):
        """ test adding numbers together """
        res = cal.add(3, 4)

        self.assertEqual(res,7)

    def test_substract_number(self):
        """ test substracting numbers """
        res = cal.substract(10, 15)

        self.assertEqual(res,5)

