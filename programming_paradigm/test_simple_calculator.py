import unittest
# from simple_calculator import SimpleCalculator


class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b


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
