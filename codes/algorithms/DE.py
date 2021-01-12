import math
import random

import numpy as np

from ..algorithm_common import AlgorithmCommon as AC
from ..algorithm_common import IAlgorithm


class DE(IAlgorithm):
    def __init__(self,
        agent_max,
        crossover_rate=0.5,
        scaling=0.5,
    ):
        self.agent_max = agent_max
        self.crossover_rate = crossover_rate
        self.scaling = scaling

    def init(self, problem):
        self.problem = problem
        self.count = 0

        self.agents = []
        for _ in range(self.agent_max):
            self.agents.append(problem.create())

    def getMaxElement(self):
        self.agents.sort(key=lambda x: x.getScore())
        return self.agents[-1]

    def getElements(self):
        return self.agents
    
    def step(self):

        for i, agent in enumerate(self.agents):

            # iを含まない3個体をランダムに選択
            r1, r2, r3 = random.sample([ j for j in range(len(self.agents)) if j != i ], 3)
            pos1 = self.agents[r1].getArray()
            pos2 = self.agents[r2].getArray()
            pos3 = self.agents[r3].getArray()

            # 3個体から変異ベクトルをだす
            m_pos = pos1 + self.scaling * (pos2 - pos3)

            # 変異ベクトルで交叉させる(一様交叉)
            pos = agent.getArray()
            ri = random.randint(0, len(pos))  # 1成分は必ず変異ベクトル
            for j in range(len(pos)):
                if  ri == j or random.random() < self.crossover_rate:
                    pos[j] = m_pos[j]
                else:
                    pass  # 更新しない

            # 優れている個体なら置き換える
            new_agent = self.problem.create(pos)
            self.count += 1
            if agent.getScore() < new_agent.getScore():
                self.agents[i] = new_agent

