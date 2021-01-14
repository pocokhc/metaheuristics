import math
import random

import numpy as np

from ..algorithm_common import AlgorithmCommon as AC
from ..algorithm_common import IAlgorithm


class Firefly(IAlgorithm):
    def __init__(self,
        firefly_max,
        attracting_degree=1.0,
        absorb=10.0,
        alpha=1.0,
        is_normalization=True
    ):
        self.firefly_max = firefly_max
        self.attracting_degree = attracting_degree
        self.absorb = absorb
        self.alpha = alpha
        self.is_normalization = is_normalization

    def init(self, problem):
        self.problem = problem
        self.count = 0

        # ユークリッド距離正規化用
        t = [problem.MAX_VAL - problem.MIN_VAL for _ in range(problem.size)]
        self.max_norm = np.linalg.norm(t)

        self.fireflys = []
        for _ in range(self.firefly_max):
            self.fireflys.append(problem.create())

    def getMaxElement(self):
        self.fireflys.sort(key=lambda x: x.getScore())
        return self.fireflys[-1]

    def getElements(self):
        return self.fireflys
        
        
    def step(self):
        for i in range(len(self.fireflys)):
            for j in range(len(self.fireflys)):
                if i == j:
                    continue

                # 光が強かったら移動する
                if self.fireflys[i].getScore() < self.fireflys[j].getScore():
                    pos = self.fireflys[i].getArray()
                    pos2 = self.fireflys[j].getArray()

                    d = np.linalg.norm(pos2 - pos)  # ユークリッド距離
                    if self.is_normalization:
                        # 0～1の範囲で正規化する
                        d /= self.max_norm
                    attract = self.light_intensity(d)

                    r = np.asarray([ self._r() for _ in range(self.problem.size)])
                    pos = pos + attract * (pos2 - pos) + self.alpha * r

                    # 更新
                    self.fireflys[i].setArray(pos)
                    self.count += 1

    # ランベルト・ベールの法則
    def light_intensity(self, d):
        return self.attracting_degree * (math.exp(-self.absorb * (d**2)))

    def _r(self):
        r = random.randint(0, 1)
        if r == 0:
            r = -1
        return self.problem.randomVal() * r

