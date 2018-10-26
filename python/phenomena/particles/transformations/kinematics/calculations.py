import abc

class KinematicsCalculations(object):
    '''
    We expect initialparticle and target to be a LorentzVector and outputparticles a list of LorentzVectors
    '''
    def __init__(self, initialparticle, finalparticles):
        self._initial= initialparticle
        self._final = finalparticles
        self._set_finalState()

    @abc.abstractmethod
    def getFinalState(self):
        return self._final

    @abc.abstractmethod
    def _set_finalState(self):
        pass
