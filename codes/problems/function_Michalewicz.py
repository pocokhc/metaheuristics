import math

from ..problem import Problem
from ..algorithm_common import AlgorithmCommon as AC


class function_Michalewicz(Problem):
    def __init__(self, size):
        super().__init__(self, size)
        self.MIN_VAL = 0
        self.MAX_VAL = math.pi
        self.SCORE_MIN = -float('inf')
        self.SCORE_MAX = 0


    def init(self):
        pass

    def eval(self, np_arr):
        n = -sum([math.sin(x) * math.sin((i+1)*(x**2)/math.pi)**(2*10) for i,x in enumerate(np_arr)])
        return -n

    def view(self, np_arr):
        print("score: {}".format(self.eval(np_arr)))


