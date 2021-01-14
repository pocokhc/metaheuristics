
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from codes.problems.g2048 import g2048
from codes.algorithms.PfGA import PfGA


def main():
    p = g2048(200)
    a = PfGA()

    p.init()
    a.init(p)

    for i in range(1000):
        a.step()
    
    a.getMaxElement().view()

if __name__ == "__main__":
    main()
