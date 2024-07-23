import unittest
from simple_calculator import SimpleCalculator

class test_SimpleCalculator(unittest.TestCase ):

    def test_addition(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.add( 4,7),11)

    def test_substraction(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.subtract(5,9),-4)

    def test_multiplication(self):

        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.multiply(20,3),60)
    def test_division(self):
        self.calc =SimpleCalculator()
        self.assertEqual(self.calc.divide(6,3),2)

