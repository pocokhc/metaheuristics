import math

from ..problem import Problem
from ..algorithm_common import AlgorithmCommon as AC


class function_XinSheYang(Problem):
    def __init__(self, size):
        super().__init__(self, size)
        self.MIN_VAL = -2*math.pi
        self.MAX_VAL = math.pi
        self.SCORE_MIN = -float('inf')
        self.SCORE_MAX = 0


    def init(self):
        pass

    def eval(self, np_arr):
        sum1 = sum([abs(x) for x in np_arr])
        sum2 = sum([math.sin(x**2) for x in np_arr])
        n = sum1 * math.exp(-sum2)
        return -n

    def view(self, np_arr):
        print("score: {}".format(self.eval(np_arr)))



