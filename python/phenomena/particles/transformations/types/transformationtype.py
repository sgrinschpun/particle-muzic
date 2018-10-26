import abc
from phenomena.particles.sources import ParticleDataSource

class Transformation(object):
    '''
    Abstract Transformation class
    '''
    @abc.abstractproperty
    def values(self):
        return self._values

    @abc.abstractmethod
    def _buildTransfValues(self):
        '''
        Creates the dict with the values
        Empty dict if not happening
        '''
        dict_values = {}
        list = self._outputParticles()
        if list != []:
            dict_values['type']=self.__class__.__name__
            dict_values['target'] = self.__class__.TARGET
            dict_values['list']=list
        self._values = dict_values

    @abc.abstractmethod
    def _outputParticles(self):
        pass

    @staticmethod
    def channelListToNames(channels):
        newchannels =[]
        for item in channels:
            newchannels.append( (item[0],Transformation.ParticleListToNames(item[1])) )
        return newchannels

    @staticmethod
    def ParticleListToNames(particlelist):
        return map(ParticleDataSource.getName, particlelist)

    @staticmethod
    def ParticleListToIds(particlelist):
        return map(ParticleDataSource.getPDGId, particlelist)
