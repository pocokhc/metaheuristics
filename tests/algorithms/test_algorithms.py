import unittest
import random
import time

import numpy as np

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from codes.problem import Problem

class MockProblem(Problem):
    def __init__(self):
        super().__init__(self, 4)
        self.MIN_VAL = 0
        self.MAX_VAL = 1

    def init(self):
        pass
    
    def eval(self, np_arr):
        np_arr = np.round(np_arr)  # 2値化
        return np_arr.sum()

    def view(self, np_arr):
        pass


from codes.algorithms.ABC import ABC
from codes.algorithms.Bat import Bat
from codes.algorithms.Cuckoo import Cuckoo
from codes.algorithms.Cuckoo_greedy import Cuckoo_greedy
from codes.algorithms.DE import DE
from codes.algorithms.Firefly import Firefly
from codes.algorithms.GA import GA
from codes.algorithms.PfGA import PfGA
from codes.algorithms.Harmony import Harmony
from codes.algorithms.PSO import PSO
from codes.algorithms.WOA import WOA


class Test(unittest.TestCase):

    def test_1(self):

        test_patterns =[
            ABC(10),
            Bat(10),
            Cuckoo(10),
            Cuckoo_greedy(10),
            DE(10),
            Firefly(10),
            GA(10),
            PfGA(),
            Harmony(10),
            PSO(10),
            WOA(10),
        ]

        for o in test_patterns:
            with self.subTest(alg=o):
                o.init(MockProblem())
                for _ in range(100):
                    o.step()
                self.assertTrue(o.count >= 100)
                self.assertEqual(o.getMaxScore(), 4)


if __name__ == "__main__":
    unittest.main()
