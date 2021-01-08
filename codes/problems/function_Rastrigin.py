import math

from ..problem import Problem
from ..algorithm_common import AlgorithmCommon as AC


class function_Rastrigin(Problem):
    def __init__(self, size):
        super().__init__(self, size)
        self.MIN_VAL = -5.12
        self.MAX_VAL = 5.12
        self.SCORE_MIN = -float('inf')
        self.SCORE_MAX = 0


    def init(self):
        pass

    def eval(self, np_arr):
        n = sum([x**2 - 10 * math.cos(2*math.pi*x) for x in np_arr])
        return -( 10*self.size + n)

    def view(self, np_arr):
        print("score: {}".format(self.eval(np_arr)))



