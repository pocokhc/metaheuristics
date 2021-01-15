import math
import random

from ..algorithm_common import AlgorithmCommon as AC
from ..algorithm_common import IAlgorithm

class Harmony(IAlgorithm):
    def __init__(self,
        harmony_max,
        bandwidth=0.1,
        enable_bandwidth_rate=False,
        select_rate=0.8,
        change_rate=0.3,
    ):
        self.harmony_max = harmony_max
        self.bandwidth = bandwidth
        self.enable_bandwidth_rate = enable_bandwidth_rate
        self.select_rate = select_rate
        self.change_rate = change_rate

    def init(self, problem):
        self.problem = problem
        self.count = 0

        self.harmonys = []
        for _ in range(self.harmony_max):
            self.harmonys.append(problem.create())
    
    def getMaxElement(self):
        self.harmonys.sort(key=lambda x: x.getScore())
        return self.harmonys[-1]

    def getElements(self):
        return self.harmonys

    def step(self):

        # 新しいharmonyを作成
        arr = []
        for i in range(self.problem.size):
            
            if random.random() < self.select_rate:
                # 新しく和音を生成
                arr.append(self.problem.randomVal())
                continue

            # harmonyを1つ選択
            h_arr = self.harmonys[random.randint(0, self.harmony_max-1)].getArray()

            if random.random() < self.change_rate:
                # 和音を変更
                if self.enable_bandwidth_rate:
                    # 割合で bandwidth を指定
                    bandwidth = self.bandwidth * (self.problem.MAX_VAL - self.problem.MIN_VAL)
                else:
                    bandwidth = self.bandwidth
                n = h_arr[i] + bandwidth * (random.random()*2-1)
                arr.append(n)
            else:
                # 和音を複製
                arr.append(h_arr[i])

        harmony = self.problem.create(arr)
        self.count += 1

        # 新しいharmonyが最悪harmonyより評価が高ければ置き換え
        self.harmonys.sort(key=lambda x: x.getScore())
        if self.harmonys[0].getScore() < harmony.getScore():
            self.harmonys[0] = harmony


