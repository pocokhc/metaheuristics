import math
import random

from ..algorithm_common import AlgorithmCommon as AC
from ..algorithm_common import IAlgorithm


class PfGA(IAlgorithm):
    def __init__(self, mutation=0.1):
        self.mutation = mutation

    def init(self, problem):
        self.problem = problem
        self.count = 0
        self.individuals = []  # 局所集団(local genes)
        for _ in range(2):
            self.individuals.append(problem.create())

    def getMaxElement(self):
        self.sort()
        return self.individuals[-1]

    def getElements(self):
        return self.individuals

    def sort(self):
        self.individuals.sort(key=lambda x: x.getScore())

    def step(self):

        # 2以下なら追加
        if len(self.individuals) < 2:
            self.individuals.append(self.problem.create())

        # ランダムに2個取り出す
        p1 = self.individuals.pop(random.randint(0, len(self.individuals)-1))
        p2 = self.individuals.pop(random.randint(0, len(self.individuals)-1))

        # 子を作成
        c1, c2 = self._cross(p1, p2)

        if p1.getScore() < p2.getScore():
            p_min = p1
            p_max = p2
        else:
            p_min = p2
            p_max = p1
        if c1.getScore() < c2.getScore():
            c_min = c1
            c_max = c2
        else:
            c_min = c2
            c_max = c1

        if c_min.getScore() >= p_max.getScore():
            # 子2個体がともに親の2個体より良かった場合
            # 子2個体及び適応度の良かった方の親個体計3個体が局所集団に戻り、局所集団数は1増加する。
            self.individuals.append(c1)
            self.individuals.append(c2)
            self.individuals.append(p_max)
        elif p_min.getScore() >= c_max.getScore():
            # 子2個体がともに親の2個体より悪かった場合
            # 親2個体のうち良かった方のみが局所集団に戻り、局所集団数は1減少する。
            self.individuals.append(p_max)
        elif p_max.getScore() >= c_max.getScore() and p_min.getScore() <= c_max.getScore():
            # 親2個体のうちどちらか一方のみが子2個体より良かった場合
            # 親2個体のうち良かった方と子2個体のうち良かった方が局所集団に戻り、局所集団数は変化しない。
            self.individuals.append(c_max)
            self.individuals.append(p_max)
        elif c_max.getScore() >= p_max.getScore() and c_min.getScore() <= p_max.getScore():
            # 子2個体のうちどちらか一方のみが親2個体より良かった場合
            # 子2個体のうち良かった方のみが局所集団に戻り、全探索空間からランダムに1個体選んで局所集団に追加する。局所集団数は変化しない。
            self.individuals.append(c_max)
            self.individuals.append(self.problem.create())
        else:
            raise ValueError("not comming")

    def _cross(self, o1, o2):
        arr1 = o1.getArray()
        arr2 = o2.getArray()
        
        # 一様交叉
        new_arr1 = []
        new_arr2 = []
        for i in range(len(arr1)):
            r = random.random()
            if r < 0.5:
                val1 = arr1[i]
                val2 = arr2[i]
            else:
                val1 = arr2[i]
                val2 = arr1[i]

            # 突然変異
            r = random.random()
            if r < self.mutation:
                val1 = self.problem.randomVal()
                val2 = self.problem.randomVal()
                
            new_arr1.append(val1)
            new_arr2.append(val2)

        new_o1 = self.problem.create(new_arr1)
        new_o2 = self.problem.create(new_arr2)
        self.count += 2
        return new_o1, new_o2

