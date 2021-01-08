import random

import numpy as np

class Problem():
    def __init__(self, domain, size):
        self.domain = domain
        self.size = size

    def create(self, arr=None):
        o = ProblemData(self.domain, self.size)
        if arr is None:
            arr = np.random.uniform(self.domain.MIN_VAL, self.domain.MAX_VAL, self.size)
        else:
            arr = np.asarray(arr)
        o.setArray(arr)
        return o

    def randomVal(self):
        return self.domain.MIN_VAL + random.random() * (self.domain.MAX_VAL - self.domain.MIN_VAL)

    def init(self):
        raise NotImplementedError()

    def eval(self, np_arr):
        raise NotImplementedError()

    def view(self, score, np_arr):
        raise NotImplementedError()
    

class ProblemData():
    def __init__(self, domain, size):
        self.domain = domain
        self.size = size
        self.np_arr = np.zeros(self.size)
        self.score = None

    def copy(self):
        o = ProblemData(self.domain, self.size)
        o.np_arr = self.np_arr.copy()
        o.score = self.score
        return o

    def getArray(self):
        return self.np_arr.copy()
        
    def setArray(self, np_arr):
        # 下限と上限でまるめる
        np_arr = np.where(np_arr < self.domain.MIN_VAL, self.domain.MIN_VAL, np_arr)
        np_arr = np.where(np_arr > self.domain.MAX_VAL, self.domain.MAX_VAL, np_arr)
        self.np_arr = np_arr
        self.score = None

    def getScore(self):
        if self.score is not None:
            return self.score
        self.score = self.domain.eval(self.np_arr)
        return self.score

    def view(self):
        self.domain.view(self.np_arr)



