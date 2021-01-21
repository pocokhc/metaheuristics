import math
import random

from ..algorithm_common import AlgorithmCommon as AC
from ..algorithm_common import IAlgorithm


class GA_SPX(IAlgorithm):
    def __init__(self, 
            individual_max,
            save_elite=True,
            select_method="ranking",
            mutation=0.1,
        ):
        self.individual_max = individual_max

        self.save_elite = save_elite
        self.select_method = select_method
        self.mutation = mutation


    def init(self, problem):
        self.problem = problem
        self.count = 0

        assert problem.size+1 <= self.individual_max
        self.spx_e = math.sqrt(problem.size+2)

        self.best_individual = None
        self.individuals = []
        for _ in range(self.individual_max):
            o = problem.create()
            self.individuals.append(o)

            if self.best_individual is None or self.best_individual.getScore() < o.getScore():
                self.best_individual = o
        self.sort()

    def getMaxElement(self):
        return self.best_individual

    def getElements(self):
        return self.individuals

    def sort(self):
        self.individuals.sort(key=lambda x: x.getScore())

    def step(self):

        # 次世代用
        next_individuals = []

        if self.save_elite:
            # エリートを生存させる
            next_individuals.append(self.individuals[-1].copy())
        
        for _ in range(self.individual_max):
            # 個数が集まるまで繰り返す
            if len(next_individuals) > self.individual_max:
                break

            # 選択する
            v_list = []
            for _ in range(self.problem.size+1):
                v_list.append(self._select().getArray())

            # 交叉する
            children = self._cross(v_list)
            for c in children:
                next_individuals.append(c)
        
        self.individuals = next_individuals

        self.sort()

        # 最高評価を保存
        if self.best_individual.getScore() < self.individuals[-1].getScore():
            self.best_individual = self.individuals[-1]

    def _select(self):
        if self.select_method == "roulette":
            weights = [x.getScore() for x in self.individuals]
            index = AC.randomFromPriority(weights)
            return self.individuals[index]
        elif self.select_method == "ranking":
            index = AC.randomFromRanking(len(self.individuals))
            return self.individuals[index]
        else:
            raise ValueError()

    def _cross(self, v_list):

        # 重心
        g_vec = None
        for v in v_list:
            if g_vec is None:
                g_vec = v
            else:
                g_vec += v
        g_vec /= len(v_list)

        s_vec = []
        for v in v_list:
            sx = g_vec + self.spx_e * (v * g_vec)
            s_vec.append(sx)

        r1 = 0
        children = []
        for i, sx in enumerate(s_vec):
            cx = r1 + sx
            r1 = random.random() * (r1 + (sx - s_vec[i-1]))
            
            children.append(self.problem.create(cx))
            self.count += 1

        return children

