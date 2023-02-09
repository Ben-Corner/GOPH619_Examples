###Test_exp

import unittest

import numpy as np

from goph619_examples.function import exp

class TestExpValues(unittest.TestCase):
    
    def setUp(self):    #Will always be run first, it is optional to do. This is where initial code is set up
        self.e = 2.7182818284590452353602874713526624977572470936999
        self.x_vals = np.linspace(-10.,10.,100)

    def test_exp_0(self): #One test, One check
        self.assertEqual(exp(0), 1.)

    def test_exp_1(self):  #Equality of floating point numbers
        expected = self.e
        self.assertAlmostEqual(exp(1),expected,delta = 1e-15)

    def test_exp_2(self):
        expected = self.e ** 2
        self.assertAlmostEqual(exp(2), expected, delta = 1e-15)

    def test_exp_array(self):
        expected = np.exp(self.x_vals)
        actual = exp(self.x_vals)
        self.assertTrue(np.allclose(actual, expected))
    
class TestExpString(unittest.TestCase):

    def setUp(self):    #Will always be run first, it is optional to do. This is where initial code is set up
        self.e = 2.7182818284590452353602874713526624977572470936999

    def test_exp_valid_string(self):
        self.assertAlmostEqual(exp('1.0'),self.e)

    def test_exp_invalid_str(self):
        with self.assertRaises(ValueError):    #This passes only if it raises this expected type of error
            exp('zero')

if __name__ == '__main__':
    unittest.main()



