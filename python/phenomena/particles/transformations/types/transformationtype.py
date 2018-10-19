import abc

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
            dict_values['list']=list
            dict_values['time']=self._transfTime()
        self._values = dict_values

    @abc.abstractmethod
    def _outputParticles(self):
        pass

    @abc.abstractmethod
    def _transfTime(self):
        pass
