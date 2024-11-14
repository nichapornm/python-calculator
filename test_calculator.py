import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(3, 5), 8)
    # Add the following test methods to the TestCalcul

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 4), -1)
        self.assertEqual(self.calc.subtract(7, 5), 2)

    # Add the following test methods to the TestCalculator class:
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)   
        self.assertEqual(self.calc.multiply(5, 3), 15)   

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)     
        self.assertEqual(self.calc.divide(14, 7), 2)  

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(14, 4), 2)     
        self.assertEqual(self.calc.modulo(13, 3), 1)

if __name__ == '__main__':
    unittest.main()