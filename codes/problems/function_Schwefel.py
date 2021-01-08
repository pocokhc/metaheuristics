import math

from ..problem import Problem
from ..algorithm_common import AlgorithmCommon as AC


class function_Schwefel(Problem):
    def __init__(self, size):
        super().__init__(self, size)
        self.MIN_VAL = -500
        self.MAX_VAL = 500
        self.SCORE_MIN = -float('inf')
        self.SCORE_MAX = 0


    def init(self):
        pass

    def eval(self, np_arr):
        n = sum([x * math.sin(math.sqrt(abs(x))) for x in np_arr])
        return n

    def view(self, np_arr):
        print("score: {}".format(self.eval(np_arr)))

