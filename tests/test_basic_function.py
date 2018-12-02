import unittest
from beerproject2.basic_function import basic_function


class MyUnitTest(unittest.TestCase):

    def test_multiply_by_two(self):
        result = basic_function(4)

        self.assertEqual(result, 8)

