import random

class TimeController(object):

    @staticmethod
    def getTime(particle):
        if particle.name in ['u', "ubar", "d", "dbar","c","cbar","s","sbar","b","bar"]:
            time = 0.2
        else:
            time = random.uniform(0,5)

        try:
            if particle.virtuality==1:
                time = 0.5
        except:
            pass

        return time
