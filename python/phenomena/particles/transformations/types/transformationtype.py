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
        if self.__class__.__name__ == 'NoTransformation' and self._particle.lifetime == -1:
            self._values = TransformationValues(type,target,channels)
        elif channels.all != []:
            self._values = TransformationValues(type,target,channels)


    @abc.abstractmethod
    def _transformationChannels(self):
        pass

    @abc.abstractmethod
    def getProbability(self,t):
        pass

    # @staticmethod
    # def channelListToNames(channels):
    #     newchannels =[]
    #     for item in channels:
    #         newchannels.append( (item[0],Transformation.ParticleListToNames(item[1])) )
    #     return newchannels
    #
    # @staticmethod
    # def ParticleListToNames(particlelist):
    #     return map(ParticleDataSource.getName, particlelist)
