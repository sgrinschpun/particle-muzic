import abc
from collections import namedtuple
from phenomena.particles.sources import ParticleDataSource

TransformationValues = namedtuple("TransformationValues", "type, target, channels")

class Transformation(object):
    '''
    Abstract Transformation class
    '''
    @property
    def values(self):
        return self._values

    @property
    def name(self):
        return self.__class__.__name__

    def _buildTransfValues(self):
        channels = self._transformationChannels()
        type = self.__class__.__name__
        target = self.__class__.TARGET
        self._values = TransformationValues(type,target,channels)

    @abc.abstractmethod
    def _transformationChannels(self):
        pass

    @abc.abstractmethod
    def getProbability(self,t):
        pass
