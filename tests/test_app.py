import unittest
import Calculator

class TestCalculator(unittest.TestCase):
    def testAddition(self):
        a = 5
        b = 4
        expetected_result = 9
        self.assertEqual(Calculator.add(a,b), expected_result)


if __name__ == '__main__':
    unittest.main()

