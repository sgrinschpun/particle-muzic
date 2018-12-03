from __future__ import division
import math
from skhep import units as u
from phenomena.particles.transformations.transformationchannel import TransformationChannels
from phenomena.particles.transformations.types import Transformation

class Decay(Transformation):

    TARGET = None

    def __init__(self, particle):
        self._particle = particle
        self._values = {}
        self._buildTransfValues()

    def _transformationChannels(self):
        return TransformationChannels.from_decaylist(self._particle.decay_channels)

    def getProbability(self, dt=1./60.):
        dt = dt *u.s
        FACTOR = 1e8
        probability = 1- math.exp(-1*dt/self._particle.lifetime * u.picosecond / u.s)
        return probability * FACTOR
