import unittest
from app import *

class TestCalculator(unittest.TestCase):
    def testAddition(self):
        a = 5
        b = 4
        expected_result = 9
        self.assertEqual(add(a,b), expected_result)

    def testSubtraction(self):
        a = 5
        b = 4
        expected_result = 1
        self.assertEqual(subtract(a,b), expected_result)

if __name__ == '__main__':
    unittest.main()

