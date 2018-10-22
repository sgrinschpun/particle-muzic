#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from phenomena.particles.particle import Particle
from phenomena.particles.transformations import TransformManager

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
        self._transformation = TransformManager(particle, transformationslist)

    def _setTransformationBoostedParameters(self, particle):
        #call calculation class send this 2 parameters:
        #particle
        #particle.transformation.selectedValues
        #this could be done at the manager level
        pass

    def start(self, callback):
        pass

    @property
    def allTransformations(self):
        return self._transformation.allTransformations

    @property
    def selTransformation(self):
        return self._transformation.selectedType

    @property
    def transformation(self):
        return self._transformation
