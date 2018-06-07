import abc

class Mapping:

    class Particle(object):
        __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def translateValue(self, value):
        pass

    @abc.abstractmethod
    def updateMapping(self, new_values):
        pass