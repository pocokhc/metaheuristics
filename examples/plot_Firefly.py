
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from codes.algorithms.Firefly import Firefly


def main():

    MIN = 0
    MAX = 1
    N = 10000

    plt.figure()

    for j in range(10):
        absorb = 1 + (j/10)*20
        ff = Firefly(10, attract=1, absorb=absorb, alpha=0)

        dx = []
        dy = []
        for i in range(N):
            x = MIN + (i/N) * (MAX-MIN)
            y = ff.light_intensity(x)
            dx.append(x)
            dy.append(y)
        plt.plot(dx, dy, label="absorb={:.0f}".format(absorb))
    
    plt.legend()
    #tmp_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')
    #path = os.path.join(tmp_dir, "{}_2.png".format(func_cls.__name__))
    #print(path)
    #plt.savefig(path)
    plt.show()


if __name__ == "__main__":
    main()


