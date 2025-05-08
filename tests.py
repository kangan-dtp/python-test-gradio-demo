# project/test.py

import unittest
from lib.my_calculations import Calculations


class TestCalculations(unittest.TestCase):
    def test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, "The sum is wrong.")
        calculation.a = 0
        self.assertEqual(calculation.get_sum(), 2, "The sum is wrong")
        calculation.a = -2
        self.assertEqual(calculation.get_sum(), 0, "The sum is wrong")

        calculation = Calculations(8.1, 2.2)
        self.assertEqual(calculation.get_sum(), 10.3, "The sum is wrong")

    def test_factorial(self):
        calculation = Calculations(4, 0)
        self.assertEqual(calculation.get_factorial(), 24, "The factorial is wrong.")
        calculation.a = 6
        self.assertEqual(calculation.get_factorial(), 720, "The factorial is wrong.")
        calculation.a = 3
        self.assertEqual(calculation.get_factorial(), 6, "The factorial is wrong.")
        calculation.a = 0
        self.assertEqual(
            calculation.get_factorial(),
            1,
            "The factorial is wrong.  Factorial of 0 is 1",
        )
        calculation.a = -2
        self.assertEqual(
            calculation.get_factorial(),
            None,
            "The factorial is wrong.  Factorial of negative number is not defined",
        )
        calculation = Calculations(8.2, 0)
        self.assertEqual(
            calculation.get_factorial(),
            None,
            "The factorial is wrong.  Factorial of decimal number is not defined",
        )


if __name__ == "__main__":
    unittest.main()
