#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from phenomena.particles.particle import Particle

class ParticleTransformation(object):
    '''
    This is a mixin class for the Particle class
    It adds the attributes and methods required for particle transformtions
     - sets all particle transformations types: particle list and probability
     - selects the particle transformation types and channel
     - incudes implementaton of continuos probability and also setting on instatiations
    The ParticleTransformation requires the ParticleData mixin.
    '''
