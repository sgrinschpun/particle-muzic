#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from phenomena.particles.particle import Particle
from phenomena.particles.transformations import TransformController

class ParticleTransformation(object):
    '''
    This is a mixin class for the Particle class
    It adds the attributes and methods required for particle transformtions
     - sets all particle transformations types for the particle: particle list and probability
     - selects the particle transformation types and channel
     - incudes implementaton of continuos probability and also setting on instantiations
    The ParticleTransformation requires the ParticleData mixin.
    '''

    def _setTransformationManager(self, particle, transformationslist):
        self._transformation = TransformController(particle, transformationslist)

    def start(self, callback):
        pass

    @property
    def transformation(self):
        return self._transformation

    @property
    def allTransformations(self):
        return self._transformation.allTransformations

    @property
    def selTransformation(self):
        return self._transformation.selectedType

    @property
    def transformationoutput(self):
        return self._transformation.output
