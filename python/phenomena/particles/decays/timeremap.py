import math
import random

class TimeRemap(object):

    @staticmethod
    def getNextDecayTime(lifetime):
        magnitude = TimeRemap.magnitude(float(lifetime))
        lifetime_renormalized = TimeRemap.renormalize(magnitude)
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
        return (math.log(x,10))

if __name__ == '__main__':
    lifetime = 1e-12
    print TimeRemap.getNextDecayTime(lifetime)
