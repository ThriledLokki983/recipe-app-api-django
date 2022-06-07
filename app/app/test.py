"""
    Sample test file for the app.
    """
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """
    Args:
        SimpleTestCase (_type_): _description_
    """

    def test_add_numbers(self):
        """
            Adding two numbers
        """
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """
            Subtracting two numbers
        """
        res = calc.subtract(5, 6)

        self.assertEqual(res, -1)
