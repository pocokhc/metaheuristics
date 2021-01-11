

import random
import math
import time


class IAlgorithm():
    def init(self, problem):
        raise NotImplementedError()

    def step(self):
        raise NotImplementedError()

    def getMaxElement(self):
        raise NotImplementedError()
    
    def getElements(self):
        raise NotImplementedError()

    def getScores(self):
        return [x.getScore() for x in self.getElements()]

    def getMaxScore(self):
        return self.getMaxElement().getScore()


class AlgorithmCommon():

    @staticmethod
    def arithmetic_sequence_sum(size, start=1, diff=1):
        return size*( 2*start + (size-1)*diff )/2

    @staticmethod
    def arithmetic_sequence_sum_inverse(val, start=1, diff=1):
        if diff == 0:
            return val
        t = diff-2*start + math.sqrt((2*start-diff)**2 + 8*diff*val)
        return t/(2*diff)

    @staticmethod
    def randomFromRanking(size):
        num = AlgorithmCommon.arithmetic_sequence_sum(size)
        r = random.random()*num
        index = int(AlgorithmCommon.arithmetic_sequence_sum_inverse(r))
        return index
    
    @staticmethod
    def randomFromPriority(weights):
        w_min = min(weights)
        if w_min < 0:
            weights = [ w + (-w_min*2) for w in weights]
        r = random.random() * sum(weights)

        num = 0
        for i, weight in enumerate(weights):
            num += weight
            if r <= num:
                return i
        # not comming

    @staticmethod
    def mantegna(beta):
        """
        mantegna アルゴリズム
        """
        #beta:  0.0 - 2.0
        if beta < 0.005:
            # 低すぎると OverflowError: (34, 'Result too large')
            beta = 0.005
        
        # siguma
        t = AlgorithmCommon.gamma(1+beta) * math.sin(math.pi*beta/2)

        t = t/( AlgorithmCommon.gamma((1+beta)/2) * beta * 2**((beta-1)/2) )
        siguma = t**(1/beta)

        u = AlgorithmCommon.random_normal()*siguma  # 平均0 分散siguma^2 の正規分布に従う乱数
        v = AlgorithmCommon.random_normal()  # 標準正規分布に従う乱数

        s = (abs(v)**(1/beta))
        if s < 0.0001:
            # 低すぎると ValueError: supplied range of [-inf, inf] is not finite
            s = 0.0001
        s = u / s
        return s

    @staticmethod
    def random_normal():
        """
        正規分布の乱数
        ボックス＝ミュラー法
        """
        r1 = random.random()
        r2 = random.random()
        return math.sqrt(-2.0 * math.log(r1)) * math.cos(2*math.pi*r2)

    ############################################
    # Γ（ｘ）の計算（ガンマ関数，近似式）
    #      ier : =0 : normal
    #            =-1 : x=-n (n=0,1,2,･･･)
    #      return : 結果
    #      coded by Y.Suganuma
    # https://www.sist.ac.jp/~suganuma/programming/9-sho/prob/gamma/gamma.htm
    ############################################
    @staticmethod
    def gamma(x):
        if x <= 0:
            raise ValueError("math domain error")

        ier = 0

        if x > 5.0 :
            v = 1.0 / x
            s = ((((((-0.000592166437354 * v + 0.0000697281375837) * v + 0.00078403922172) * v - 0.000229472093621) * v - 0.00268132716049) * v + 0.00347222222222) * v + 0.0833333333333) * v + 1.0
            g = 2.506628274631001 * math.exp(-x) * pow(x,x-0.5) * s

        else:

            err = 1.0e-20
            w   = x
            t   = 1.0

            if x < 1.5 :

                if x < err :
                    k = int(x)
                    y = float(k) - x
                    if abs(y) < err or abs(1.0-y) < err :
                        ier = -1

                if ier == 0 :
                    while w < 1.5 :
                        t /= w
                        w += 1.0

            else :
                if w > 2.5 :
                    while w > 2.5 :
                        w -= 1.0
                        t *= w

            w -= 2.0
            g  = (((((((0.0021385778 * w - 0.0034961289) * w + 0.0122995771) * w - 0.00012513767) * w + 0.0740648982) * w + 0.0815652323) * w + 0.411849671) * w + 0.422784604) * w + 0.999999926
            g *= t

        return g
