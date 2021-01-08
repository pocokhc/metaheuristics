
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from codes.problems.OneMax import OneMax
from codes.problems.function_Ackley import function_Ackley
from codes.problems.function_Griewank import function_Griewank
from codes.problems.function_Michalewicz import function_Michalewicz
from codes.problems.function_Rastrigin import function_Rastrigin
from codes.problems.function_Schwefel import function_Schwefel
from codes.problems.function_StyblinskiTang import function_StyblinskiTang
from codes.problems.function_XinSheYang import function_XinSheYang



def draw2d(func_cls):
    fig = plt.figure()

    o = func_cls(1)
    dx = []
    dy = []
    for i in range(100000):
        diff = (o.MAX_VAL-o.MIN_VAL)
        x = o.MIN_VAL + (i/100000)*diff
        y = o.eval(np.asarray([x]))
        dx.append(x)
        dy.append(y)
    plt.plot(dx, dy)

    tmp_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')
    path = os.path.join(tmp_dir, "{}_2.png".format(func_cls.__name__))
    print(path)
    plt.savefig(path)
    #plt.show()



def draw3d(func_cls):
    fig = plt.figure()

    o = func_cls(2)

    dx1 = []
    dx2 = []
    dy = []
    diff = (o.MAX_VAL-o.MIN_VAL)
    for x1 in range(100):
        x1 = o.MIN_VAL + (x1/100)*diff

        _dx1 = []
        _dx2 = []
        _dy = []
        for x2 in range(100):
            x2 = o.MIN_VAL + (x2/100)*diff
            y = o.eval(np.asarray([x1, x2]))
            _dx1.append(x1)
            _dx2.append(x2)
            _dy.append(y)
        dx1.append(_dx1)
        dx2.append(_dx2)
        dy.append(_dy)

    dx1 = np.asarray(dx1)
    dx2 = np.asarray(dx2)
    dy = np.asarray(dy)

    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("y")
    ax.plot_wireframe(dx1, dx2, dy)

    tmp_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')
    path = os.path.join(tmp_dir, "{}_3.png".format(func_cls.__name__))
    print(path)
    plt.savefig(path)
    #plt.show()


def main():
    
    funcs = [
        OneMax,
        function_Ackley,
        function_Griewank,
        function_Michalewicz,
        function_Rastrigin,
        function_Schwefel,
        function_StyblinskiTang,
        function_XinSheYang,
    ]
    for func in funcs:
        draw2d(func)
        draw3d(func)



if __name__ == "__main__":
    main()


