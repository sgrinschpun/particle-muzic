import random
import math

class TimeRemap(object):

    @staticmethod
    def getNextDecayTime(lifetime):
        lifetime_renormalized = TimeRemap.renormalize(TimeRemap.magnitude(lifetime))
        return random.expovariate(1/lifetime_renormalized)

    @staticmethod
    def renormalize(n):
        range1 = [-13., 14.]
        range2 = [1.e-3, 5.]
        delta1 = range1[1] - range1[0]
        delta2 = range2[1] - range2[0]
        return (delta2 * (n - range1[0]) / delta1) + range2[0]

    @staticmethod
    def magnitude(x):
        return int(math.log(x,10))
