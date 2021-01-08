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

            # 2個体をランダムに選択
            pos1 = self.agents[random.randint(0, len(self.agents)-1)].getArray()
            pos2 = self.agents[random.randint(0, len(self.agents)-1)].getArray()

            # 2個体の差分から新個体をだす
            pos = agent.getArray()
            for j in range(len(pos)):
                if random.random() < self.crossover_rate:
                    pos[j] = pos[j] + self.scaling * (pos2[j] - pos1[j])
                else:
                    pass  # 更新しない

            # 優れている個体なら置き換える
            new_agent = self.problem.create(pos)
            self.count += 1
            if agent.getScore() < new_agent.getScore():
                self.agents[i] = new_agent

