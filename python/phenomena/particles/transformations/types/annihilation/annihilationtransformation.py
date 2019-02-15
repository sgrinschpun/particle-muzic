from phenomena.particles.transformations.transformationchannel import TransformationChannels
from phenomena.particles.transformations.types import Transformation
from phenomena.particles.sources import ParticleDataSource

class Annihilation(Transformation):

    INPUT = ['e+']
    OUTPUT = map(ParticleDataSource.getPDGId, ['gamma'])
    TARGET = 'e-'

    def __init__(self, particle):
        self._particle = particle
        self._values = {}
        if  self._particle.name in Annihilation.INPUT:
            self._buildTransfValues()

    def _transformationChannels(self):
        return TransformationChannels.from_decaylist([(1.0,Annihilation.OUTPUT)])

    def getProbability(self, dt=1./60.):
        gamma = self._particle.fourMomentum.gamma
        FACTOR = 0.1
        probability = 1- math.exp(-0.3*dt*gamma)
        return FACTOR*probability
