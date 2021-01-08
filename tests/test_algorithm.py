import unittest
import random
import time

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from codes.algorithm_common import AlgorithmCommon as AC


class Test(unittest.TestCase):

    def test_randomFromRanking(self):
        for weight_len in range(2, 100):
            weights = [ 1 + i for i in range(weight_len)]
            self._testSub(weights, lambda weights: AC.randomFromRanking(len(weights)))


    def test_randomFromPriority(self):
        for weight_len in range(2, 100):
            weights = [random.random()*20-10 for _ in range(weight_len)]
            for is_reverse in [False, True]:
                if is_reverse:
                    weights = list(reversed(weights))
                self._testSub(weights, lambda weights: AC.randomFromPriority(weights))
        

    def _testSub(self, weights, method):
                
        counter = [0 for _ in range(len(weights))]
        N = 10000
        for _ in range(N):
            n = method(weights)
            counter[n] += 1
        counter = [x/N for x in counter]
        w_min = min(weights)
        if w_min < 0:
            weights = [ w + (-w_min*2) for w in weights]
        weights = [w/sum(weights) for w in weights]

        for k in range(len(weights)):
            r2 = abs(weights[k] - counter[k])
            assert r2 < 0.05, "{} weight:{} counter:{}".format(k, weights, counter)


if __name__ == "__main__":
    unittest.main()
