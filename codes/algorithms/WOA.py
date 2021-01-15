import math
import random

import numpy as np

from ..algorithm_common import AlgorithmCommon as AC
from ..algorithm_common import IAlgorithm

# https://github.com/docwza/woa/blob/master/src/whale_optimization.py

class WOA(IAlgorithm):
    def __init__(self,
        whale_max,
        a_decrease=0.001,
        logarithmic_spiral=1,
    ):
        self.whale_max = whale_max
        self.a_decrease = a_decrease
        self.logarithmic_spiral = logarithmic_spiral

    def init(self, problem):
        self.problem = problem
        self.count = 0

        self.best_whale = None
        self.whales = []
        for _ in range(self.whale_max):
            o = problem.create()
            self.whales.append(o)

            if self.best_whale is None or self.best_whale.getScore() < o.getScore():
                self.best_whale = o.copy()
        self._a = 2


    def getMaxElement(self):
        return self.best_whale

    def getElements(self):
        return self.whales
    
    def step(self):
        for whale in self.whales:
            pos = whale.getArray()
            if random.random() < 0.5:
                r1 = np.random.rand(self.problem.size)  # 0-1の乱数
                r2 = np.random.rand(self.problem.size)  # 0-1の乱数

                A = (2.0 * np.multiply(self._a, r1)) - self._a
                C = 2.0 * r2

                if np.linalg.norm(A) < 1:
                    # 獲物に近づく
                    new_pos = self.best_whale.getArray()
                else:
                    # 獲物を探す
                    new_pos = self.whales[random.randint(0, len(self.whales)-1)].getArray()

                D = np.linalg.norm(np.multiply(C, new_pos) - pos)
                pos = new_pos - np.multiply(A, D)

            else:
                # 回る
                best_pos = self.best_whale.getArray()
                D = np.linalg.norm(best_pos - pos)
                L = np.random.uniform(-1, 1, self.problem.size)  # [-1,1]の乱数
                _b = self.logarithmic_spiral
                pos = np.multiply(np.multiply(D, np.exp(_b*L)), np.cos(2.0*np.pi*L)) + best_pos

            whale.setArray(pos)
            self.count += 1
            if self.best_whale.getScore() < whale.getScore():
                self.best_whale = whale.copy()

        self._a -= self.a_decrease
        if self._a < 0:
            self._a = 0

    def spiral(self, x, L):
        return x * np.exp(self.logarithmic_spiral * L) * np.cos(2.0 * np.pi * L)

