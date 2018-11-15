from phenomena.particles.transformations.types import Transformation
from phenomena.particles.sources import ParticleDataSource

class ComptonEffect(Transformation):

    INPUT = ['gamma']
    OUTPUT = ['gamma', 'e-']
    TARGET = 'e-'

    def __init__(self, particle):
        self._particle = particle
        self._values = {}
        if  self._particle.name in ComptonEffect.INPUT:
            self._buildTransfValues()

    def _outputParticles(self):
        return [(1.0,ComptonEffect.OUTPUT)]

    def getProbability(self, dt=1./60.):
        gamma = self._particle.fourMomentum.gamma
        FACTOR = 0.05
        probability = math.exp(-30*dt*gamma)
        return FACTOR*probability
