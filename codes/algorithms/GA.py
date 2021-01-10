import math
import random

from ..algorithm_common import AlgorithmCommon as AC
from ..algorithm_common import IAlgorithm


class GA(IAlgorithm):
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
            o1 = self._select()
            o2 = self._select()

            # 交叉する
            new_o1, new_o2 = self._cross(o1, o2)
            next_individuals.append(new_o1)
            next_individuals.append(new_o2)
        
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

    def _cross(self, parent1, parent2):
        genes1 = parent1.getArray()  # 親1の遺伝子情報
        genes2 = parent2.getArray()  # 親2の遺伝子情報

        # 子の遺伝子情報
        c_genes1 = []
        c_genes2 = []
        for i in range(len(genes1)):  # 各遺伝子を走査

            # 50%の確率で遺伝子を入れ替える
            if random.random() < 0.5:
                c_gene1 = genes1[i]
                c_gene2 = genes2[i]
            else:
                c_gene1 = genes2[i]
                c_gene2 = genes1[i]

            # 突然変異
            if random.random() < self.mutation:
                c_gene1 = self.problem.randomVal()
            if random.random() < self.mutation:
                c_gene2 = self.problem.randomVal()

            c_genes1.append(c_gene1)
            c_genes2.append(c_gene2)

        # 遺伝子をもとに子を生成
        childe1 = self.problem.create(c_genes1)
        childe2 = self.problem.create(c_genes2)
        self.count += 2
        return childe1, childe2


