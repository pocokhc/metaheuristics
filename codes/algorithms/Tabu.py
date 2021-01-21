import math
import random

from ..algorithm_common import AlgorithmCommon as AC
from ..algorithm_common import IAlgorithm


class Tabu(IAlgorithm):
    def __init__(self, 
            individual_max,
            epsilon=0.1,
            tabu_list_size=100,
            tabu_range_rate=0.1,
        ):
        self.individual_max = individual_max

        self.epsilon = epsilon
        self.tabu_list_size = tabu_list_size
        self.tabu_range_rate = tabu_range_rate


    def init(self, problem):
        self.problem = problem
        self.count = 0
        
        self.tabu_range = (problem.MAX_VAL - problem.MIN_VAL) * self.tabu_range_rate
        self.tabu_list = []

        self.best_individual = problem.create()
        self.individuals = [self.best_individual]


    def getMaxElement(self):
        return self.best_individual

    def getElements(self):
        return self.individuals


    def step(self):

        # 基準となる個体(前stepの最良個体)
        individual = self.individuals[-1]

        # 個体数が集まるまで近傍を生成
        next_individuals = []
        for _ in range(self.individual_max*99):  # for safety
            if len(next_individuals) >= self.individual_max:
                break
            
            # 近傍を生成
            pos = individual.getArray()
            ri = random.randint(0, len(pos)-1)  # 1成分は必ず変更
            trans = []  # タブーリスト用
            for i in range(len(pos)):
                if i == ri or random.random() < self.epsilon:
                    # ランダムな値に変更
                    val = self.problem.randomVal()
                    trans.append((i, pos[i]-val))  # 変更内容を保存
                    pos[i] = val
            
            # タブーリストにある遷移は作らない
            if self._isInTabuList(trans):
                continue
            
            self.count += 1
            o = self.problem.create(pos)
            next_individuals.append((o, trans))

        # 近傍が0なら別途新しく生成する
        if len(next_individuals) == 0:
            o = self.problem.create()
            if self.best_individual.getScore() < o.getScore():
                self.best_individual = o
            self.individuals = [o]
            return

        # sort
        next_individuals.sort(key=lambda x: x[0].getScore())

        # 次のstep用に保存
        self.individuals = [x[0] for x in next_individuals]

        # このstepでの最良個体
        step_best = next_individuals[-1][0]
        if self.best_individual.getScore() < step_best.getScore():
            self.best_individual = step_best
        
        # タブーリストに追加
        step_best_trans = next_individuals[-1][1]
        self.tabu_list.append(step_best_trans)
        if len(self.tabu_list) > self.tabu_list_size:
            self.tabu_list.pop(0)


    def _isInTabuList(self, trans):
        for tabu in self.tabu_list:
            # 個数が違えば違う
            if len(tabu) != len(trans):
                continue
            
            f = True
            for i in range(len(trans)):
                # 対象要素が違えば違う
                if tabu[i][0] != trans[i][0]:
                    f = False
                    break
                # 範囲内なら該当
                tabu_val = tabu[i][1]
                val = trans[i][1]
                if not(tabu_val - self.tabu_range < val and val < tabu_val + self.tabu_range):
                    f = False
                    break

            # 該当するものがある
            if f:
                return True

        return False

