import random
import math

from matplotlib import pyplot as plt
import numpy as np

from ..problem import Problem


class TSP(Problem):
    def __init__(self, size):
        super().__init__(self, size)
        self.MIN_VAL = 0
        self.MAX_VAL = 1
        self.SCORE_MIN = -(math.sqrt(1+1) * size)
        self.SCORE_MAX = 0

    def init(self):
        self.towns = [
            {
                "x": random.random(),
                "y": random.random()
            } for _ in range(self.size)
        ]
        

    def eval(self, np_arr):
        score = 0

        # 入力値にソートした入力のindexを取得
        tmp = [(i, x) for i, x in enumerate(np_arr)]
        tmp = sorted(tmp, key=lambda x: x[1])
        for i in range(len(tmp)):
            if i == 0:
                town = {"x":0, "y":0}
            else:
                town = self.towns[tmp[i-1][0]]
            next_town = self.towns[tmp[i][0]]

            d = abs(town["x"] - next_town["x"])
            d += abs(town["y"] - next_town["y"])
            score += d
        return -score


    def view(self, np_arr):
        print("score: {}".format(self.eval(np_arr)))
        tmp = [(i, x) for i, x in enumerate(np_arr)]
        tmp = sorted(tmp, key=lambda x: x[1])

        # 都市を表示
        plt.text(0, 0, "start")
        for i in range(len(tmp)):
            town = self.towns[tmp[i][0]]
            plt.scatter(town["x"], town["y"])
            if i == len(self.towns)-1:
                s = "end"
            else:
                s = str(i)
            plt.text(town["x"], town["y"], s)
        
        # 線を表示
        for i in range(len(tmp)):
            if i == 0:
                town = {"x":0, "y":0}
            else:
                town = self.towns[tmp[i-1][0]]
            next_town = self.towns[tmp[i][0]]
            plt.plot([town["x"], next_town["x"]], [town["y"], next_town["y"]])

        plt.show()
