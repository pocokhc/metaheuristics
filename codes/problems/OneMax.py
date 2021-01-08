import numpy as np

from ..problem import Problem


class OneMax(Problem):
    def __init__(self, size):
        super().__init__(self, size)
        self.MIN_VAL = 0
        self.MAX_VAL = 1
        self.SCORE_MIN = 0
        self.SCORE_MAX = size

    def init(self):
        pass

    def eval(self, np_arr):
        np_arr = np.round(np_arr)  # 2値化
        return np_arr.sum()

    def view(self, np_arr):
        print("score: {}".format(self.eval(np_arr)))
        np_arr = np.round(np_arr)  # 2値化
        tmp = ["{:.2f}".format(x) for x in np_arr]
        print(" ".join(tmp))


