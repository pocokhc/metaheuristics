import math
import random

from ..algorithm_common import AlgorithmCommon as AC
from ..algorithm_common import IAlgorithm


class ABC(IAlgorithm):
    def __init__(self, 
        harvest_bee,
        follow_bee=10,
        visit_max=10
    ):
        self.harvest_bee = harvest_bee
        self.follow_bee = follow_bee
        self.visit_max = visit_max


    def init(self, problem):
        self.problem = problem
        self.count = 0

        self.max_flower = None
        self.flowers = []
        for _ in range(self.harvest_bee):
            o = problem.create()
            self.flowers.append({
                "flower": o,
                "count": 0
            })

            if self.max_flower is None or self.max_flower.getScore() < o.getScore():
                self.max_flower = o

    def getMaxElement(self):
        return self.max_flower

    def getElements(self):
        return [x["flower"] for x in self.flowers]

    def step(self):

        # 収穫バチフェーズ
        for i in range(self.harvest_bee):
            flower = self.flowers[i]["flower"]

            # 食糧源の近くを探索
            pos = flower.getArray()
            k = random.randint(0, len(pos)-1)  # 1つの成分をランダムに決める
            flower2 = self.flowers[random.randint(0, len(self.flowers)-1)]["flower"]
            pos2 = flower2.getArray()  # 別食糧源
            pos[k] += (random.random()*2-1) * (pos[k] - pos2[k])

            # 新しい座標の食糧源を作成
            new_flower = self.problem.create(pos)
            self.count += 1

            # 新しい食糧源がよければ更新する
            if new_flower.getScore() > flower.getScore():
                self.flowers[i]["flower"] = new_flower

                # 最大の食糧源なら保存
                if self.max_flower.getScore() < new_flower.getScore():
                    self.max_flower = new_flower

            # 食糧源の取得回数+1
            self.flowers[i]["count"] += 1

        # 追従バチフェーズ
        for i in range(self.follow_bee):
            weights = [x["flower"].getScore() for x in self.flowers]
            index = AC.randomFromPriority(weights)
            self.flowers[index]["count"] += 1

        # 偵察バチフェーズ
        for i in range(len(self.flowers)):
            # 一定回数以上の食糧源を置き換える
            if self.visit_max < self.flowers[i]["count"]:
                o = self.problem.create()
                self.flowers[i]["count"] = 0
                self.flowers[i]["flower"] = o
                self.count += 1

                # 最大の食糧源なら保存
                if self.max_flower.getScore() < o.getScore():
                    self.max_flower = o
                
