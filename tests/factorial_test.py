from factorial import factorial
import unittest

class TestFactorialImplementation(unittest.TestCase):
    """
    test my recursive factorial implementation
    """

    def test_zero_case(self):
        """
        factorial(0) should return 1
        """
        self.assertEqual(factorial(0), 1)

    def test_negative_case(self):
        """
        factorial(-3) should raise a ValueError
        """
        self.assertRaises(ValueError, factorial, -3)

    def test_non_int_case(self):
        """
        factorial(1.5) should raise a TypeError
        """
        self.assertRaises(TypeError, factorial, 1.5)

    def test_4_factorial(self):
        """
        factorial(4) should return 24
        """
        self.assertEqual(factorial(4), 24)
