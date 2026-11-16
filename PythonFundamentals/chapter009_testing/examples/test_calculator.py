import unittest

from utils.calculator import Calculator


class CalculatorTesting(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Calculator.add(10, 5), 15)
        self.assertEqual(Calculator.add(100, -120), -20)

    def test_subtraction(self):
        self.assertEqual(Calculator.sub(10, 2), 8)


if (__name__ == "__main__"):
    unittest.main()
