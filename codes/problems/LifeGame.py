import numpy as np

from ..problem import Problem


class LifeGame(Problem):
    def __init__(self, size, max_turn):
        super().__init__(self, size*size)
        self.field_size = size
        self.MIN_VAL = 0
        self.MAX_VAL = 1
        self.SCORE_MIN = 0
        self.SCORE_MAX = size*size

        self.max_turn = max_turn


    def init(self):
        pass

    def eval(self, np_arr):
        np_arr = np.round(np_arr)  # 2値
        # 1次元→2次元に
        cells = np.reshape(np_arr, (self.field_size, self.field_size))

        for _ in range(self.max_turn):
            cells = self._step(cells)
        return cells.sum()

    def _step(self, cells):

        next_cells = np.zeros((self.field_size, self.field_size))
        for y in range(self.field_size):
            for x in range(self.field_size):
                n = 0
                n += self._get(cells, x-1, y-1)
                n += self._get(cells, x  , y-1)
                n += self._get(cells, x+1, y-1)
                n += self._get(cells, x+1, y)
                n += self._get(cells, x-1, y)
                n += self._get(cells, x-1, y+1)
                n += self._get(cells, x  , y+1)
                n += self._get(cells, x+1, y+1)
                if self._get(cells, x, y) == 0:
                    if n == 3:
                        next_cells[y][x] = 1
                else:
                    if n == 2 or n == 3:
                        next_cells[y][x] = 1
                    else:
                        next_cells[y][x] = 0
        
        return next_cells


    def _get(self, cells, x, y):
        if x < 0:
            return 0
        if y < 0:
            return 0
        if x >= self.field_size:
            return 0
        if y >= self.field_size:
            return 0
        return cells[y][x]


    def view(self, np_arr):
        print("score: {}".format(self.eval(np_arr)))
        np_arr = np.round(np_arr)  # 2値
        # 1次元→2次元に
        cells = np.reshape(np_arr, (self.field_size, self.field_size))

        for y in range(self.field_size):
            s = ""
            for x in range(self.field_size):
                if cells[y][x] == 1:
                    s += "■"
                else:
                    s += "□"
            print(s)

        for _ in range(self.max_turn):
            cells = self._step(cells)
        
        print("")
        for y in range(self.field_size):
            s = ""
            for x in range(self.field_size):
                if cells[y][x] == 1:
                    s += "■"
                else:
                    s += "□"
            print(s)

if __name__ == "__main__":
    o = LifeGame(10, 50)
    o.init()
    o2 = o.create()
    o2.view()

