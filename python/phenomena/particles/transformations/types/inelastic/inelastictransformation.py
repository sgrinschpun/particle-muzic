import math
from phenomena.particles.transformations.transformationchannel import TransformationChannels
from phenomena.particles.transformations.types import Transformation
from phenomena.particles.sources import ParticleDataSource
from inelasticdata import InelasticData


class InelasticCollision(Transformation):

    def __init__(self, particle, target):
        self._particle = particle
        self._target = target
        self._values = {}
        if  self._particle.name in InelasticData.listOriginParticles(target):
            self._buildTransfValues()

    def _transformationChannels(self):
        decaylist = InelasticData.energyCutParticles(self._particle.name, self._target, self._particle.E)
        return TransformationChannels.from_decaylistNames(decaylist)


    def getProbability(self, dt=1./60.):
        gamma = self._particle.fourMomentum.gamma
        FACTOR = 0.1
        probability = 1- math.exp(-0.3*dt*gamma)
        return FACTOR*probability

class InelasticCollisionWithProton(InelasticCollision):

    TARGET = 'p+'

    def __init__(self, particle, target = 'p+'):
        super(InelasticCollisionWithProton, self).__init__(particle, target)

class InelasticCollisionWithNeutron(InelasticCollision):

    TARGET = 'n0'

    def __init__(self, particle, target = 'n0'):
        super(InelasticCollisionWithNeutron, self).__init__(particle, target)
