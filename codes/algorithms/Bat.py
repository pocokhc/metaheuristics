import math
import random
import sys

import numpy as np

from ..algorithm_common import AlgorithmCommon as AC
from ..algorithm_common import IAlgorithm


class Bat(IAlgorithm):
    def __init__(self,
        bat_max,
        frequency_min=0,
        frequency_max=1,
        good_bat_rate=0.2,
        volume_init=1.0,
        volume_update_rate=0.9,
        pulse_convergence_value=0.5,
        pulse_convergence_speed=0.9,
    ):
        self.bat_max = bat_max
        self.frequency_min = frequency_min
        self.frequency_max = frequency_max

        self.good_bat_num = int(bat_max * good_bat_rate + 0.5)
        if self.good_bat_num > bat_max:
            self.good_bat_num = bat_max
        if self.good_bat_num < 1:
            self.good_bat_num = 1
        self.volume_init = volume_init
        self.volume_update_rate = volume_update_rate
        self.pulse_convergence_value = pulse_convergence_value
        self.pulse_convergence_speed = pulse_convergence_speed


    def init(self, problem):
        self.problem = problem
        self.count = 0

        self.step_count = 0
        self.best_bat = None
        self.bats = []
        for _ in range(self.bat_max):
            o = problem.create()

            d = {
                "bat": o,
                "pulse": self._calcPulse(0),
                "volume": self.volume_init,
                "v": np.zeros(problem.size)
            }
            self.bats.append(d)

            if self.best_bat is None or self.best_bat.getScore() < o.getScore():
                self.best_bat = o


    def getMaxElement(self):
        return self.best_bat

    def getElements(self):
        return [x["bat"] for x in self.bats]
        
    def _calcPulse(self, count):
        return self.pulse_convergence_value * (1-math.exp(-self.pulse_convergence_speed*count))
        
    def step(self):
        self.bats.sort(key=lambda x: x["bat"].getScore())

        for bat in self.bats:

            # 周波数
            frequency = self.frequency_min + (self.frequency_max - self.frequency_min) * random.random()
            
            # 最良のコウモリに近づく
            pos_best = self.best_bat.getArray()
            pos = bat["bat"].getArray()
            bat["v"] = bat["v"] + frequency * (pos_best - pos)
            new_bat1 = self.problem.create(pos + bat["v"])
            self.count += 1

            # 音量判定
            if random.random() >= bat["volume"]:
                # 新しい位置で更新
                bat["bat"] = new_bat1
            
                # 最良コウモリチェック
                if self.best_bat.getScore() < bat["bat"].getScore():
                    self.best_bat = bat["bat"]
                continue


            # 乱数で良いコウモリの近くに移動
            new_bat2 = None
            if bat["pulse"] < random.random():
            
                # 全コウモリの平均音量
                volume = np.average([x["volume"] for x in self.bats])
                
                # いいコウモリを選ぶ
                r = random.randint(1, self.good_bat_num)
                pos_good = self.bats[-r]["bat"].getArray()
                
                rn = np.random.uniform(-1, 1, len(pos_good))  # -1,1の乱数
                new_bat2 = self.problem.create(pos_good + volume * rn)
                self.count += 1
            
            # ランダムに生成
            new_bat3 = self.problem.create()
            self.count += 1
                
            # 新しい位置の比較
            score1 = new_bat1.getScore()
            score2 = None if new_bat2 is None else new_bat2.getScore()
            score3 = new_bat3.getScore()
            if (score2 is None or score1 > score2) and score1 > score3 :
                if score2 is None or score2 <= score3:
                    bat["bat"] = new_bat3
                else:
                    bat["bat"] = new_bat2
                
                # パルス率の更新
                bat["pulse"] = self._calcPulse(self.step_count)

                # 音量の更新
                bat["volume"] = self.volume_update_rate * bat["volume"]
            else:
                bat["bat"] = new_bat1

            # 最良コウモリチェック
            if self.best_bat.getScore() < bat["bat"].getScore():
                self.best_bat = bat["bat"]

        self.step_count += 1
