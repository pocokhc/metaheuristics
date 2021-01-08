import unittest
import random
import time

import numpy as np

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from codes.problems.function_Ackley import function_Ackley


class Test(unittest.TestCase):

    def test_1(self):
        p = function_Ackley(10)
        p.init()

        arr = np.asarray([1, 2, 3, -4, -2, -1, 0, 1, 2, 3])
        score = p.eval(arr)
        self.assertEqual(score, -7.1542450698630855)

        #p.view(arr)
        

if __name__ == "__main__":
    unittest.main()
