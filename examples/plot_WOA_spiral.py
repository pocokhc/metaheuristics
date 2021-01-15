
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from codes.algorithms.WOA import WOA


def main1():

    MIN = -1
    MAX = 1
    N = 10000

    plt.figure()

    N2 = 5
    for j in range(N2):
        MIN2 = 0
        MAX2 = 2
        d = MIN2 + ((1+j)/N2) * (MAX2-MIN2)
        ff = WOA(1, logarithmic_spiral=1)

        dx = []
        dy = []
        for i in range(N):
            x = MIN + (i/N) * (MAX-MIN)
            y = ff.spiral(d, L=x)
            dx.append(x)
            dy.append(y)
        plt.plot(dx, dy, label="d={:.2f}".format(d))
    
    plt.legend()
    plt.grid()
    plt.xlabel("L")
    plt.ylabel("sprial")
    #tmp_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')
    #path = os.path.join(tmp_dir, "{}_2.png".format(func_cls.__name__))
    #print(path)
    #plt.savefig(path)
    plt.show()



def main2():

    MIN = -1
    MAX = 1
    N = 10000

    plt.figure()

    N2 = 5
    for j in range(N2):
        MIN2 = 0
        MAX2 = 1
        logarithmic_spiral = MIN2 + ((1+j)/N2) * (MAX2-MIN2)
        ff = WOA(1, logarithmic_spiral=logarithmic_spiral)

        dx = []
        dy = []
        for i in range(N):
            x = MIN + (i/N) * (MAX-MIN)
            y = ff.spiral(1, L=x)
            dx.append(x)
            dy.append(y)
        plt.plot(dx, dy, label="logarithmic_spiral={:.2f}".format(logarithmic_spiral))
    
    plt.legend()
    plt.grid()
    plt.xlabel("L")
    plt.ylabel("sprial")
    #tmp_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')
    #path = os.path.join(tmp_dir, "{}_2.png".format(func_cls.__name__))
    #print(path)
    #plt.savefig(path)
    plt.show()


if __name__ == "__main__":
    main1()
    main2()


