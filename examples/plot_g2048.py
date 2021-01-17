
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from codes.problems.g2048 import g2048
from codes.algorithms.DE import DE


def main():
    p = g2048(200)
    a = DE(11, 0.98, 1.85)

    p.init()
    a.init(p)

    for i in range(1000):
        if i%100 == 0:
            print(i)
        a.step()
    
    a.getMaxElement().view()

if __name__ == "__main__":
    main()
