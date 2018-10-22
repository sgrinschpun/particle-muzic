from phenomena.particles.transformations.types import Transformation
from phenomena.particles.sources import ParticleDataSource

class ElasticCollision(Transformation):

    def __init__(self, particle, target):
        self._particle = particle
        self._target = target
        self._values = {}
        self._buildTransfValues()

    def _outputParticles(self):
        #return [(1.0,map(ParticleDataSource.getPDGId, [self._particle.name, self._target]))]
        return [(1.0,[self._particle.name, self._target])]

    def _transfTime(self):
        return 1

class ElasticCollisionWithProton(ElasticCollision):
    def __init__(self, particle, target = 'p+'):
        super(ElasticCollisionWithProton, self).__init__(particle, target)

class ElasticCollisionWithElectron(ElasticCollision):
    def __init__(self, particle, target = 'e-'):
        super(ElasticCollisionWithElectron, self).__init__(particle, target)

class ElasticCollisionWithNeutron(ElasticCollision):
    def __init__(self, particle, target = 'n0'):
        super(ElasticCollisionWithNeutron, self).__init__(particle, target)
