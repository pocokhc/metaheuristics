import random
import math

import numpy as np

from ..problem import Problem


class g2048(Problem):
    def __init__(self, max_turn):
        super().__init__(self, max_turn)
        self.MIN_VAL = 0
        self.MAX_VAL = 3
        self.SCORE_MIN = 0
        self.SCORE_MAX = float('inf')

        self.max_turn = max_turn

    def init(self):
        # 初期フィールド
        self.fields = [[0 for _ in range(4)] for _ in range(4)]
        for _ in range(2):
            self.fields[random.randint(0, 3)][random.randint(0, 3)] = 2

        # 生成される乱数は固定する
        self.create_pos = []
        for _ in range(self.max_turn):
            self.create_pos.append((random.randint(0, 3), random.randint(0, 3)))
        

    def eval(self, np_arr, is_view=False):
        np_arr = np.round(np_arr)  # 2値

        # 初期フィールドをコピー
        fields = [ x[:] for x in self.fields]

        if is_view:
            self._viewMap(fields)

        # turn分実行
        for i in range(self.max_turn):

            # 更新
            for y in range(4):
                for x in range(4):
                    self._move(fields, np_arr[i], x, y)
            
            # 新しく設置、すでにあれば次のセルを見る
            pos = self.create_pos[i]
            x = pos[0]
            y = pos[1]
            for _ in range(4*4):
                if fields[y][x] == 0:
                    fields[y][x] = 2
                    break
                x += 1
                if x >= 4:
                    x = 0
                    y += 1
                if y >= 4:
                    y = 0

            if is_view:
                cmd = ["up", "right", "down", "left"]
                print("--- turn: {}, cmd: {}".format(i, cmd[int(np_arr[i])]))
                self._viewMap(fields)

        # 最後の盤面で最大値がスコア
        score = 0
        for y in range(4):
            for x in range(4):
                if score < fields[y][x]:
                    score = fields[y][x]
        
        return score

    def _move(self, fields, cmd, x, y):
        if fields[y][x] == 0:
            return
        
        if cmd == 0:  # up
            if y == 0:
                return
            tx = x
            ty = y-1
        elif cmd == 1:  # right
            if x == 3:
                return
            tx = x+1
            ty = y
        elif cmd == 2:  # down
            if y == 3:
                return
            tx = x
            ty = y+1
        elif cmd == 3:  # left
            if x == 0:
                return
            tx = x-1
            ty = y
        else:
            raise ValueError()

        if fields[ty][tx] == 0:
            # 対象がが開いているので移動
            fields[ty][tx] = fields[y][x]
            fields[y][x] = 0
            self._move(fields, cmd, tx, ty)
        elif fields[ty][tx] == fields[y][x]:
            # 同じ数字なので合成
            fields[ty][tx] += fields[y][x]
            fields[y][x] = 0
        

    def view(self, np_arr):
        print("score: {}".format(self.eval(np_arr, is_view=True)))

    def _viewMap(self, fields):
        for y in range(4):
            s = ""
            for x in range(4):
                s += "{:5} ".format(fields[y][x])
            print(s)


