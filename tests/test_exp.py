###Test_exp

import unittest

import numpy as np

from goph619_examples.function import exp

class TestExpValues(unittest.TestCase):
    
    def setUp(self):    #Will always be run first, it is optional to do. This is where initial code is set up
        pass

    def test_exp_0(self): #One test, One check
        self.assertEqual(exp(0), 1.)

if __name__ == '__main__':
    unittest.main()



