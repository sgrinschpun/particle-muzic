from phenomena.particles.transformations.types import Transformation
from phenomena.particles.transformations.transformationchannel import TransformationChannels


class NoTransformation(Transformation):

    TARGET = None

    def __init__(self, particle):
        self._particle = particle
        self._buildTransfValues()

    def _transformationChannels(self):
        return TransformationChannels.from_decaylist([(1.0,[])])
