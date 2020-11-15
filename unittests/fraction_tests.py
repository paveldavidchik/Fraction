import sys
sys.path += ['../Fraction']
from solution import Fraction
import unittest
from unittest.mock import patch


class Fraction_Tests(unittest.TestCase):
    def test_init_error(self):
        with self.assertRaises(ValueError):
            Fraction(-1, 1)
        with self.assertRaises(ValueError):
            Fraction(1, -1)
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)
    
    def test_numerator(self):
        self.assertEqual(Fraction(1, 1).numerator, 1)
    
    def test_numerator_except_value(self):
        fraction = Fraction(1, 1)
        fraction.numerator = -1
        self.assertEqual(fraction.numerator, 1)
    
    def test_numerator_except_type(self):
        fraction = Fraction(1, 1)
        fraction.numerator = 'one'
        self.assertEqual(fraction.numerator, 1)
    
    def test_denominator(self):
        self.assertEqual(Fraction(1, 1).denominator, 1)
    
    def test_denominator_except_value(self):
        fraction = Fraction(1, 1)
        fraction.denominator = -1
        self.assertEqual(fraction.denominator, 1)
    
    def test_denominator_except_type(self):
        fraction = Fraction(1, 1)
        fraction.denominator = 'one'
        self.assertEqual(fraction.denominator, 1)
    
    def test_denominator_except_zero(self):
        fraction = Fraction(1, 1)
        fraction.denominator = 0
        self.assertEqual(fraction.denominator, 1)
    
    def test_read(self):
        fraction = Fraction(1, 1)
        with patch('builtins.input', side_effect=['2', '3']):
            fraction.read()
        self.assertEqual(fraction.numerator, 2)
        self.assertEqual(fraction.denominator, 3)
    
    def test_read_except_type(self):
        fraction = Fraction(1, 1)
        with patch('builtins.input', side_effect=['one', 'one']):
            fraction.read()
        self.assertEqual(fraction.numerator, 1)
        self.assertEqual(fraction.denominator, 1)
    
    def test_ipart(self):
        self.assertEqual(Fraction(6, 4).ipart(), 1)
    
    def test_str(self):
        self.assertEqual(Fraction(2, 3).__str__(), '2/3')
