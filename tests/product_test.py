from product import product
import unittest

class TestRecursiveProductImplementation(unittest.TestCase):
    """
    test my implementation of a recursive product function
    """

    def test_two_positive_integers(self):
        """
        product(2,3) should return 6
        """
        self.assertEqual(product(2,3), 6)

    def test_one_postive_and_one_negative_integer(self):
        """
        product(2, -3) should return -6
        """
        self.assertEqual(product(2,-3), -6)

    def test_two_negative_integers(self):
        """
        product(-2, -3) should return 6
        """
        self.assertEqual(product(-2,-3), 6)

    def test_one_float_and_one_int(self):
        """
        product(1.3, 10) should return 13

        need to use AlmostEqual because of floating point precision
        after several decimal places!!!
        """
        self.assertAlmostEqual(product(1.3, 10), 13)

    def test_two_floats(self):
        """
        product(2, 1.3) should raise an error
        """
        self.assertRaises(TypeError, product, 2, 1.3)
