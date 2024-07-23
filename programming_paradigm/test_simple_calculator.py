import unittest
from simple_calculator import SimpleCalculator

class test_SimpleCalculator(unittest.TestCase ):

    def test_add(self):
        self.add = SimpleCalculator()
        self.assertEqual(self.add .add( 4,7),11)

    def test_substract(self):
        self.substract = SimpleCalculator()
        self.assertEqual(self.substract.subtract(5,9),-4)

    def test_multiply(self):

        self.multiply = SimpleCalculator()
        self.assertEqual(self.multiply.multiply(20,3),60)
    def test_divide(self):
        self.divide =SimpleCalculator()
        self.assertEqual(self.divide.divide(6,3),2)

    def test_Zerodivion(self):
        self.Zerodivion =SimpleCalculator()
        self.assertRaises()