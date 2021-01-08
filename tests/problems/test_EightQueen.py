import unittest
import random
import time

import numpy as np

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from codes.problems.EightQueen import EightQueen


class Test(unittest.TestCase):

    def test_1(self):
        p = EightQueen(4)
        p.init()

        arr = np.asarray([
            0.6, 0.1,
            3.4, 1,
            0  , 2,
            2  , 3,
        ])

        score = p.eval(arr)
        self.assertEqual(score, 4)

        #p.view(arr)


if __name__ == "__main__":
    unittest.main()
