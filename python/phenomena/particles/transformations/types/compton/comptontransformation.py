from phenomena.particles.transformations.transformationchannel import TransformationChannels
from phenomena.particles.transformations.types import Transformation
from phenomena.particles.sources import ParticleDataSource

class ComptonEffect(Transformation):

    INPUT = ['gamma']
    OUTPUT = map(ParticleDataSource.getPDGId, ['gamma', 'e-'])
    TARGET = 'e-'

    def __init__(self, particle):
        self._particle = particle
        self._values = {}
        if  self._particle.name in ComptonEffect.INPUT:
            self._buildTransfValues()

    def _transformationChannels(self):
        return TransformationChannels.from_decaylist([(1.0,ComptonEffect.OUTPUT)])

    def getProbability(self, dt=1./60.):
        gamma = self._particle.fourMomentum.gamma
        FACTOR = 0.05
        probability = math.exp(-30*dt*gamma)
        return FACTOR*probability
