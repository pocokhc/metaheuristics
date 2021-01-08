
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

    max_score = a.getMaxScore()
    for i in range(1000):
        a.step()
        if max_score < a.getMaxScore():
            max_score = a.getMaxScore()
            print("{} {}".format(i, max_score))
    
    a.getMaxElement().view()

if __name__ == "__main__":
    main()
