import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        self.assertAlmostEqual(SimpleCalculator.add(self, 1, 2), 3)
        self.assertAlmostEqual(SimpleCalculator.add(self, -2, -4), -6)

    def test_subtract(self):
        self.assertAlmostEqual(SimpleCalculator.subtract(self, -5, 4), -9)
        self.assertAlmostEqual(SimpleCalculator.subtract(self, 12, 2), 10)

    def test_multiply(self):
        self.assertAlmostEqual(SimpleCalculator.multiply(self, 5, 5), 25)
        self.assertAlmostEqual(SimpleCalculator.multiply(self, 5, 0), 0)

    def test_divide(self):
        self.assertAlmostEqual(SimpleCalculator.divide(self, 10, 2), 5)
        self.assertAlmostEqual(SimpleCalculator.divide(self, 10, 0), None)
