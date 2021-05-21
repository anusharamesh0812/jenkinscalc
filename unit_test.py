import unittest
from calc import Calculator


# Test cases to test Calulator methods
# You always create  a child class derived from unittest.TestCase
class TestCalculator(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.calculator = Calculator()

    # Each test method starts with the keyword test_
    def test_add(self):
        self.assertEqual(self.calculator.add(4, 4), 8)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, -5), 15)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 7), 21)
        self.assertEqual(self.calculator.multiply(-2, -3), 0)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
