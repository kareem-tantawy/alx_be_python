import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(self, 1, 2), 3)
        self.assertEqual(self.calc.add(self, -2, -4), -6)
        self.assertEqual(self.calc.add(self, -2, 2), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(self, -5, 4), -9)
        self.assertEqual(self.calc.subtract(self, 12, 2), 10)
        self.assertEqual(self.calc.subtract(self, -12, -5), -7)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(self, 5, 5), 25)
        self.assertEqual(self.calc.multiply(self, 5, 0), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(self, 10, 2), 5)
        self.assertEqual(self.calc.divide(self, 2, 10), 0.2)
        self.assertEqual(self.calc.divide(self, 10, 0), None)
