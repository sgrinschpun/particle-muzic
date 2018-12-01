import math
from phenomena.particles.transformations.types import Transformation
from phenomena.particles.sources import ParticleDataSource

class ElasticCollision(Transformation):
    excluded_part = ['gamma','e-','e+','nu_e','nu_mu','nu_tau','nu_ebar','nu_mubar','nu_taubar']

    def __init__(self, particle, target):
        self._particle = particle
        self._target = target
        self._values = {}
        if self._particle.name not in ElasticCollision.excluded_part:
            self._buildTransfValues()

    def _outputParticles(self):
        #return [(1.0,map(ParticleDataSource.getPDGId, [self._particle.name, self._target]))]
        return [(1.0,[self._particle.name, self._target])]

    def getProbability(self, dt=1./60.):
        gamma = self._particle.fourMomentum.gamma
        FACTOR = 0.05
        probability = math.exp(-30*dt*gamma)
        return FACTOR*probability

class ElasticCollisionWithProton(ElasticCollision):

    TARGET = 'p+'

    def __init__(self, particle, target = 'p+'):
        super(ElasticCollisionWithProton, self).__init__(particle, target)

class ElasticCollisionWithElectron(ElasticCollision):

    TARGET = 'e-'

    def __init__(self, particle, target = 'e-'):
        super(ElasticCollisionWithElectron, self).__init__(particle, target)

class ElasticCollisionWithNeutron(ElasticCollision):

    TARGET = 'n0'

    def __init__(self, particle, target = 'n0'):
        super(ElasticCollisionWithNeutron, self).__init__(particle, target)
