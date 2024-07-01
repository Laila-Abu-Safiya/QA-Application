import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        
    def test_add(self):
        self.assertEqual(self.calculator.add(4,3),7)
        self.assertEqual(self.calculator.add(5,-3),2)
        self.assertEqual(self.calculator.add(-5,3),-2)
        self.assertEqual(self.calculator.add(-7,-5),-12)
        
    def test_sub(self):
        self.assertEqual(self.calculator.sub(12, 8), 4)
        self.assertEqual(self.calculator.sub(9, -3), 12)
        self.assertEqual(self.calculator.sub(-8, 6), -14)
        self.assertEqual(self.calculator.sub(-6, -3), -3)

    def test_multy(self):
        self.assertEqual(self.calculator.multy(4, 3), 12)
        self.assertEqual(self.calculator.multy(3, -3), -9)
        self.assertEqual(self.calculator.multy(-6, -2), 12)
        self.assertEqual(self.calculator.multy(0, 333), 0)

    def test_div(self):
        self.assertEqual(self.calculator.div(16, 4), 4)
        self.assertEqual(self.calculator.div(30, -5), -6)
        self.assertEqual(self.calculator.div(-27, -3), 9)
        self.assertEqual(self.calculator.div(0, 10), 0)
        
        with self.assertRaises(ValueError):
            self.calculator.div(10, 0)

    def test_decimal(self):
        self.assertAlmostEqual(self.calculator.add(3.1, 2.8), 5.9)
        self.assertAlmostEqual(self.calculator.sub(7.6, 5.3), 2.3)
        self.assertAlmostEqual(self.calculator.multy(11.6, 4), 46.4)
        self.assertAlmostEqual(self.calculator.div(3.6, 7.2), 0.5)
    
    def test_exploratory(self):
        self.assertAlmostEqual(self.calculator.add(self.calculator.multy(3,2), 7), 13)
        self.assertAlmostEqual(self.calculator.sub(self.calculator.multy(5,2), self.calculator.div(7,-2)), 13.5)
        self.assertEqual(self.calculator.add(999999991,9),1000000000)


if __name__ == '__main__':
    unittest.main()