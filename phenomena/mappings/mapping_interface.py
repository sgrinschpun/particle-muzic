import abc

class Mapping:

    class Particle(object):
        __metaclass__ = abc.ABCMeta

    def translateValue(self, value):
        pass