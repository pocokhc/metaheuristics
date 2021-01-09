import math
import random

import numpy as np

from ..algorithm_common import AlgorithmCommon as AC
from ..algorithm_common import IAlgorithm


class PSO(IAlgorithm):
    def __init__(self,
        particle_max,
        inertia=0.9,
        global_acceleration=0.9,
        personal_acceleration=0.9,
    ):
        self.particle_max = particle_max
        self.inertia = inertia
        self.global_acceleration = global_acceleration
        self.personal_acceleration = personal_acceleration


    def init(self, problem):
        self.problem = problem
        self.count = 0

        self.global_best = None
        self.particles = []
        for _ in range(self.particle_max):
            o = problem.create()

            # 初期加速度
            v = [(problem.MAX_VAL - problem.MIN_VAL) * random.uniform(-1, 1) for _ in range(problem.size)]

            d = {
                "particle": o,
                "personal": None,
                "v": np.asarray(v),
            }
            self.particles.append(d)
            self._updateBest(d)
    
    def getMaxElement(self):
        return self.global_best

    def getElements(self):
        return [x["particle"] for x in self.particles]

    def step(self):

        for particle in self.particles:
            pos = particle["particle"].getArray()
            g_pos = self.global_best.getArray()
            p_pos = particle["personal"].getArray()

            # 加速度を計算
            v = particle["v"]
            v = self.inertia * v
            v += self.global_acceleration * (g_pos-pos) * random.random()
            v += self.personal_acceleration * (p_pos-pos) * random.random()
            particle["v"] = v

            # 座標を更新
            particle["particle"].setArray(pos + v)
            self.count += 1

            self._updateBest(particle)


    def _updateBest(self, particle):

        # パーソナルベストの更新
        if particle["personal"] is None or particle["personal"].getScore() < particle["particle"].getScore():
            particle["personal"] = particle["particle"].copy()

        # グローバルベストの更新
        if self.global_best is None or self.global_best.getScore() < particle["particle"].getScore():
            self.global_best = particle["particle"].copy()


