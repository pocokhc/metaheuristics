import math

from ..problem import Problem
from ..algorithm_common import AlgorithmCommon as AC


class function_StyblinskiTang(Problem):
    def __init__(self, size):
        super().__init__(self, size)
        self.MIN_VAL = -5
        self.MAX_VAL = 4
        self.SCORE_MIN = -float('inf')
        self.SCORE_MAX = 0


    def init(self):
        pass

    def eval(self, np_arr):
        n = sum([x ** 4 - 16*(x**2) + 5*x for x in np_arr])
        return -n/2

    def view(self, np_arr):
        print("score: {}".format(self.eval(np_arr)))


