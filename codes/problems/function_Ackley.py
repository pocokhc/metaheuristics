import math

from ..problem import Problem
from ..algorithm_common import AlgorithmCommon as AC


class function_Ackley(Problem):
    def __init__(self, size):
        super().__init__(self, size)
        self.MIN_VAL = -32.768
        self.MAX_VAL = 32.768
        self.SCORE_MIN = -float('inf')
        self.SCORE_MAX = 0

    def init(self):
        pass

    def eval(self, np_arr):

        sum1 = sum([x**2 for x in np_arr])
        sum2 = sum([math.cos(2*math.pi*x) for x in np_arr])
        n = len(np_arr)

        score = 20 - 20 * math.exp(-0.2 * math.sqrt(sum1/n)) + math.e - math.exp(sum2/n)
        return -score

    def view(self, np_arr):
        print("score: {}".format(self.eval(np_arr)))



