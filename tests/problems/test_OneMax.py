import unittest
import random
import time

import numpy as np

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from codes.problems.OneMax import OneMax


class Test(unittest.TestCase):

    def test_1(self):
        p = OneMax(10)
        p.init()

        arr = np.asarray([0, 0.6, 0, 0.4, 0, 0, 0, 1, 0, 0])
        score = p.eval(arr)
        self.assertEqual(score, 2.0)

        #p.view(arr)
        

if __name__ == "__main__":
    unittest.main()
