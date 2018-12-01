import unittest
from beerproject2 import brew_home

class MyUnitTest(unittest.TestCase):

    def test_multiply_by_two(self):
        result = brew_home.multiply_by_two(4)

        self.assertEqual(result, 8)