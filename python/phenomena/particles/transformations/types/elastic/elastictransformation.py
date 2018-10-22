from phenomena.particles.transformations.types import Transformation
from phenomena.particles.sources import ParticleDataSource

class ElasticCollision(Transformation):

    def __init__(self, particle, target = 'p+'):
        self._particle = particle
        self._target = target
        self._values = {}
        self._buildTransfValues()

    def _outputParticles(self):
        return [(1.0,map(ParticleDataSource.getPDGId, [self._particle.name, self._target]))]

    def _transfTime(self):
        return 1
