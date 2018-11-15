import abc
from phenomena.particles.sources import ParticleDataSource

class Transformation(object):
    '''
    Abstract Transformation class
    '''
    @abc.abstractproperty
    def values(self):
        return self._values

    @property
    def name(self):
        return self.__class__.__name__

    @abc.abstractmethod
    def _buildTransfValues(self):
        '''
        Creates the dict with the values
        Empty dict if not happening
        '''
        dict_values = {}
        list = self._outputParticles()
        if self.__class__.__name__ == 'NoTransformation':
            if self._particle.lifetime == -1:
                dict_values['type']=self.__class__.__name__
                dict_values['target'] = self.__class__.TARGET
                dict_values['list']=list
        elif list != []:
            dict_values['type']=self.__class__.__name__
            dict_values['target'] = self.__class__.TARGET
            dict_values['list']=list
        self._values = dict_values

    @abc.abstractmethod
    def _outputParticles(self):
        pass

    def getProbability(self,t):
        return 0.05

    @staticmethod
    def channelListToNames(channels):
        newchannels =[]
        for item in channels:
            newchannels.append( (item[0],Transformation.ParticleListToNames(item[1])) )
        return newchannels

    @staticmethod
    def ParticleListToNames(particlelist):
        return map(ParticleDataSource.getName, particlelist)

    # @staticmethod
    # def ParticleListToIds(particlelist):
    #     return map(ParticleDataSource.getPDGId, particlelist)
