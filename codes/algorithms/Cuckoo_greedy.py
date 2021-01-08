import math
import random

import numpy as np

from ..algorithm_common import AlgorithmCommon as AC
from ..algorithm_common import IAlgorithm


class Cuckoo_greedy(IAlgorithm):
    def __init__(self, nest_max, epsilon=0.1, bad_nest_rate=0.1):
        self.nest_max = nest_max
        self.epsilon = epsilon
        self.bad_nest_num = int(nest_max * bad_nest_rate + 0.5)
        if self.bad_nest_num > nest_max-1:
            self.bad_nest_num = nest_max-1
        if self.bad_nest_num < 0:
            self.bad_nest_num = 0

    def init(self, problem):
        self.problem = problem
        self.count = 0

        self.nests = []
        for _ in range(self.nest_max):
            self.nests.append(problem.create())
    
    def getMaxElement(self):
        self.nests.sort(key=lambda x: x.getScore())
        return self.nests[-1]

    def getElements(self):
        return self.nests

    def step(self):
        # ランダムに巣を選択
        r = random.randint(0, self.nest_max-1)  # a<=x<=b

        # 新しい巣を作成
        arr = self.nests[r].getArray()

        for i in range(len(arr)):

            # ε-greedy で卵を作成する
            if random.random() < self.epsilon:
                arr[i] = self.problem.randomVal()

        new_nest = self.problem.create(arr)
        self.count += 1

        # ランダムな巣と比べてよければ変える
        r = random.randint(0, self.nest_max-1)  # a<=x<=b
        if self.nests[r].getScore() < new_nest.getScore():
            self.nests[r] = new_nest

        # 悪い巣を消す
        self.nests.sort(key=lambda x:x.getScore())
        for i in range(self.bad_nest_num):
            self.nests[i] = self.problem.create()
            self.count += 1

