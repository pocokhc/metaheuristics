import unittest
import random
import time

import numpy as np

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from codes.problems.TSP import TSP


class Test(unittest.TestCase):

    def test_1(self):
        p = TSP(10)

        random.seed(1)
        p.init()
        random.seed()

        arr = np.asarray([0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
        score = p.eval(arr)
        self.assertEqual(score, -10.341323980245443)

        #p.view(arr)
        

if __name__ == "__main__":
    unittest.main()
