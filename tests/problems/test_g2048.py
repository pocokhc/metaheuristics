import unittest
import random
import time

import numpy as np

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from codes.problems.g2048 import g2048


class Test(unittest.TestCase):

    def test_1(self):
        p = g2048(10)

        random.seed(1)
        p.init()
        random.seed()

        arr = np.asarray([0, 1, 2, 3, 0, 1, 2, 3, 0, 1])
        score = p.eval(arr)
        self.assertEqual(score, 8)

        p.view(arr)
        

if __name__ == "__main__":
    unittest.main()
