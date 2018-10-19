from phenomena.particles.transformations import Transformation
from inelasticdata import InelasticData

class InelasticCollision(Transformation):

    def __init__(self, particle, target = 'p+'):
        self._particle = particle
        self._target = target
        self._values = {}
        if  self._particle.name in InelasticData.listOriginParticles(target):
            self._buildTransfValues()

    def _outputParticles(self):
        return InelasticData.energyCutParticles(self._particle.name, self._target, self._particle.E)

    def _transfTime(self):
        return 1
