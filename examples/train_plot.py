
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

from codes.algorithms.GA import GA
from codes.algorithms.PfGA import PfGA
from codes.algorithms.ABC import ABC
from codes.algorithms.Bat import Bat
from codes.algorithms.Cuckoo import Cuckoo
from codes.algorithms.Cuckoo_greedy import Cuckoo_greedy
from codes.algorithms.DE import DE
from codes.algorithms.Firefly import Firefly
from codes.algorithms.Harmony import Harmony
from codes.algorithms.PSO import PSO
from codes.algorithms.WOA import WOA
from codes.algorithms.GA_BLXa import GA_BLXa
from codes.algorithms.GA_SPX import GA_SPX
from codes.algorithms.Tabu import Tabu

def create(D, N):
    funcs = [
        OneMax(D),
        function_Ackley(D),
        function_Griewank(D),
        function_Michalewicz(D),
        function_Rastrigin(D),
        function_Schwefel(D),
        function_StyblinskiTang(D),
        function_XinSheYang(D),
    ]
    algs= [
        GA(N, save_elite=False, select_method="ranking", mutation=0.05),
        PfGA(mutation=0.5),
        ABC(N, follow_bee=15, visit_max=30),
        Bat(N, frequency_min=0, frequency_max=0.05, good_bat_rate=0.1, volume_init=0.5, pulse_convergence_value=0.9, pulse_convergence_speed=0.1),
        Cuckoo(N, scaling_rate=1.0, levy_rate=1.0, bad_nest_rate=0.1),
        Cuckoo_greedy(N, epsilon=0.5, bad_nest_rate=0.1),
        DE(N, crossover_rate=0, scaling=0.4),
        Firefly(N, attracting_degree=0.08, absorb=50.0, alpha=0.02, is_normalization=True),
        Harmony(N, bandwidth=1.0, enable_bandwidth_rate=True, select_rate=0.4, change_rate=0.9),
        PSO(N, inertia=0.2, global_acceleration=0.2, personal_acceleration=0.2),
        WOA(N, a_decrease=2/50, logarithmic_spiral=1),
        GA_BLXa(N, save_elite=False, select_method="ranking", mutation=0.05, blx_a=0.1),
        GA_SPX(N, save_elite=False, select_method="ranking", mutation=0.05),
        Tabu(N, epsilon=0, tabu_list_size=10, tabu_range_rate=0.1),
    ]
    return funcs, algs

def anime2(func, alg):
    tmp_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')

    alg.init(func)
    N = 100
    
    fig = plt.figure()

    func_x = []
    func_y = []
    diff_num = 1000
    for i in range(diff_num):
        diff = (func.MAX_VAL-func.MIN_VAL)
        x = func.MIN_VAL + (i/diff_num)*diff
        y = func.eval(np.asarray([x]))
        func_x.append(x)
        func_y.append(y)

    x_pos = []
    y_score = []
    max_pos = []
    max_score = []
    for _ in range(N):
        alg.step()

        pos = []
        score = []
        for e in alg.getElements():
            pos.append(e.getArray()[0])
            score.append(e.getScore())
        x_pos.append(pos)
        y_score.append(score)

        max_pos.append(alg.getMaxElement().getArray()[0])
        max_score.append(alg.getMaxElement().getScore())

    
    
    def plot(i):
        plt.cla()

        plt.plot(func_x, func_y, label=func.__class__.__name__, linewidth="0.5")
        plt.plot(x_pos[i], y_score[i], 'o', color="orange", markeredgecolor="black")
        plt.plot(max_pos[i], max_score[i], 'o', color="red", markeredgecolor="black")
        plt.title('step={}'.format(i))

    ani = animation.FuncAnimation(fig, plot, N, interval=200)
    path = os.path.join(tmp_dir, "{}_{}_2.gif".format(func.__class__.__name__, alg.__class__.__name__))
    print(path)
    ani.save(path, writer="imagemagick")
    #plt.show()


def main2():
    funcs, algs = create(1, 6)
    for func in funcs:
        for alg in algs:
            anime2(func, alg)



def anime3(func, alg):
    tmp_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')

    alg.init(func)
    N = 100
    
    fig = plt.figure()

    # function
    func_y = []
    diff_num = 50
    diff = (func.MAX_VAL-func.MIN_VAL)
    for x1 in range(diff_num):
        x1 = func.MIN_VAL + (x1/diff_num)*diff
        d = []
        for x2 in range(diff_num):
            x2 = func.MIN_VAL + (x2/diff_num)*diff
            y = func.eval(np.asarray([x2, x1]))
            d.append(y)
        func_y.insert(0, d)

    # search
    pos1 = []
    pos2 = []
    max_pos1 = []
    max_pos2 = []
    for _ in range(N):
        alg.step()

        pos1_ = []
        pos2_ = []
        for e in alg.getElements():
            pos1_.append(e.getArray()[0])
            pos2_.append(e.getArray()[1])
        pos1.append(pos1_)
        pos2.append(pos2_)

        max_pos1.append(alg.getMaxElement().getArray()[0])
        max_pos2.append(alg.getMaxElement().getArray()[1])

    extent = (func.MIN_VAL, func.MAX_VAL, func.MIN_VAL, func.MAX_VAL)
    plt.imshow(func_y, interpolation="nearest",  cmap="jet", extent=extent)
    plt.colorbar()
    def plot(i):
        plt.cla()

        plt.imshow(func_y, interpolation="nearest",  cmap="jet", extent=extent)
        plt.plot(pos1[i], pos2[i], 'o', color="orange", markeredgecolor="black")
        plt.plot(max_pos1[i], max_pos2[i], 'o', color="red", markeredgecolor="black")
        plt.title('step={}'.format(i))

    ani = animation.FuncAnimation(fig, plot, N, interval=200)
    
    path = os.path.join(tmp_dir, "{}_{}_3.gif".format(func.__class__.__name__, alg.__class__.__name__))
    print(path)
    ani.save(path, writer="imagemagick")
    #plt.show()


def main3():
    funcs, algs = create(2, 20)
    for func in funcs:
        for alg in algs:
            anime3(func, alg)



if __name__ == "__main__":
    main2()
    main3()


