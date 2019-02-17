#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

import time, threading
from phenomena.particles.transformations import TransformController

class ParticleTransformation(object):
    '''
    This is a mixin class for the Particle class
    It adds the attributes and methods required for particle transformations
     - sets all particle transformations types for the particle: particle list and probability
     - selects the particle transformation types and channel
     - incudes implementaton of continuos probability and also setting on instantiations
    The ParticleTransformation requires the ParticleData mixin.
    '''

    def _setTransformationManager(self, particle, transformationslist):
        self._transformation = TransformController(particle, transformationslist)

    def start(self, callback):
        if self.transformation.selectedType.type != 'NoTransformation':
            wait_time = self.transformation.transformtime
            print ("Wait for: ", wait_time)
            threading.Timer(wait_time, callback).start()
        else:
            print ("Wait for: ", 15)
            threading.Timer(15, callback).start()

    @property
    def transformation(self):
        return self._transformation

    @property
    def transformtime(self):
        return self._transformation.transformtime
