import math

from ..problem import Problem
from ..algorithm_common import AlgorithmCommon as AC

class function_Griewank(Problem):
    def __init__(self, size):
        super().__init__(self, size)
        self.MIN_VAL = -600
        self.MAX_VAL = 600
        self.SCORE_MIN = -float('inf')
        self.SCORE_MAX = 0


    def init(self):
        pass

    def eval(self, np_arr):
        sum1 = sum([x**2 for x in np_arr])
        prod = 1
        for i, x in enumerate(np_arr):
            prod *= math.cos( x / math.sqrt(i+1) )
        n = 1 + (sum1 - prod) / 4000
        return -n

    def view(self, np_arr):
        print("score: {}".format(self.eval(np_arr)))



