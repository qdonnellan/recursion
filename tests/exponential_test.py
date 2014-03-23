from exponential import exponential
import unittest

class TestExponentialFunctionImplementation(unittest.TestCase):
    """
    test my implementation of the exponential function
    """

    def test_case_of_3_to_the_0(self):
        """
        3**0 should be 1
        """
        self.assertEqual(exponential(3,0), 1)

    def test_case_of_2_to_the_3(self):
        """
        2**3 should be 8
        """
        self.assertEqual(exponential(2,3), 8)

    def test_case_if_negative_exponent(self):
        """
        2^(-9) should raise a value error
        """
        self.assertRaises(ValueError, exponential, 2,-9)
