import unittest
from calculator import get_operation, sum_values, subtraction_values, multiply_values, divided_values

class CalculatorTest(unittest.TestCase):

    def testOperation(self):
        result = get_operation("+", 2, 2)
        self.assertEqual(result, 4)

    def testSum(self):
        self.assertEqual(sum_values(2, 2), 4)

    def testSubtraction(self):
        self.assertEqual(subtraction_values(4, 2), 2)

    def testMultiply(self):
        self.assertEqual(multiply_values(2, 2), 4)
    
    def testDivided(self):
        self.assertEqual(divided_values(4, 2), 2)

if __name__ == '__main__':
    unittest.main()