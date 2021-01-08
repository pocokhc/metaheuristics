import unittest
import random
import time

import numpy as np

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from codes.problems.LifeGame import LifeGame


class Test(unittest.TestCase):

    def test_1(self):
        p = LifeGame(5, 49)
        p.init()

        # ブリンカー
        arr = np.asarray([
            0, 0, 0, 0, 0, 
            0, 0, 1, 0, 0, 
            0, 0, 1, 0, 0, 
            0, 0, 1, 0, 0, 
            0, 0, 0, 0, 0, 
        ])

        score = p.eval(arr)
        self.assertEqual(score, 3)

        #p.view(arr)


if __name__ == "__main__":
    unittest.main()
