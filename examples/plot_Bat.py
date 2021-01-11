
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from codes.algorithms.Bat import Bat


def main():

    MIN = 0
    MAX = 100
    N = 10000

    plt.figure()

    N2 = 10
    for j in range(N2):
        MIN2 = 0
        MAX2 = 0.2
        pulse_convergence_speed = MIN2 + (j/N2) * (MAX2-MIN2)
        ff = Bat(10, pulse_convergence_value=1.0, pulse_convergence_speed=pulse_convergence_speed)

        dx = []
        dy = []
        for i in range(N):
            x = MIN + (i/N) * (MAX-MIN)
            y = ff._calcPulse(x)
            dx.append(x)
            dy.append(y)
        plt.plot(dx, dy, label="pulse_convergence_speed={:.2f}".format(pulse_convergence_speed))
    
    plt.legend()
    #tmp_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')
    #path = os.path.join(tmp_dir, "bat_pulse_2.png")
    #print(path)
    #plt.savefig(path)
    plt.show()


if __name__ == "__main__":
    main()


