from phenomena.particles.transformations.types import Transformation

class NoTransformation(Transformation):

    TARGET = None

    def __init__(self, particle):
        self._particle = particle
        self._buildTransfValues()

    def _outputParticles(self):
        return []
