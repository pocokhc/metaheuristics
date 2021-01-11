
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from codes.algorithms.Cuckoo import Cuckoo


def main():

    MIN = 0
    MAX = 2
    N = 10000

    plt.figure()

    N2 = 10
    for j in range(N2):
        MIN2 = 0
        MAX2 = 4
        c = MIN2 + (j/N2) * (MAX2-MIN2)
        ff = Cuckoo(10)

        dx = []
        dy = []
        for i in range(N):
            x = MIN + (i/N) * (MAX-MIN)
            y = ff.levy(x, c=c)
            dx.append(x)
            dy.append(y)
        plt.plot(dx, dy, label="c={:.2f}".format(c))
    
    plt.legend()
    #tmp_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')
    #path = os.path.join(tmp_dir, "{}_2.png".format(func_cls.__name__))
    #print(path)
    #plt.savefig(path)
    plt.show()


if __name__ == "__main__":
    main()


