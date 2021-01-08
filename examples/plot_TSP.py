
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from codes.problems.TSP import TSP
from codes.algorithms.PfGA import PfGA


def main():
    p = TSP(10)
    a = PfGA()

    p.init()
    a.init(p)

    for _ in range(1000):
        a.step()
    
    a.getMaxElement().view()

if __name__ == "__main__":
    main()
