
import numpy as np

from ..problem import Problem

class EightQueen(Problem):
    def __init__(self, size):
        super().__init__(self, size*2)
        self.field_size = size
        self.MIN_VAL = 0
        self.MAX_VAL = size-1
        self.SCORE_MIN = 0
        self.SCORE_MAX = size
    
    def init(self):
        pass
    
    def eval(self, np_arr):

        # arrを駒の座標に変換
        koma_list = self._createKomaPos(np_arr)

        score = 0
        for i in range(len(koma_list)):
            f = True
            for j in range(len(koma_list)):
                if i==j:
                    continue
                # x
                if koma_list[i][0] == koma_list[j][0]:
                    f = False
                    break
                # y
                if koma_list[i][1] == koma_list[j][1]:
                    f = False
                    break
                # 斜め
                ax = abs(koma_list[i][0] - koma_list[j][0])
                ay = abs(koma_list[i][1] - koma_list[j][1])
                if ax == ay:
                    f = False
                    break
            if f:
                score += 1

        return score

    def _createKomaPos(self, np_arr):
        np_arr = np.round(np_arr)  # 2値

        koma_list = []
        for i in range(0, len(np_arr), 2):
            koma_list.append((np_arr[i], np_arr[i+1]))
        return koma_list

    
    def view(self, np_arr):
        print("score: {}".format(self.eval(np_arr)))

        # arrを駒の座標に変換
        koma_list = self._createKomaPos(np_arr)

        for y in range(self.field_size):
            for x in range(self.field_size):

                f = False
                for k in koma_list:
                    if k[0] == x and k[1] == y:
                        f = True
                        break

                if f:
                    print("1", end="")
                else:
                    print("0", end="")
            print("")


