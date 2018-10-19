#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

import time, threading
from phenomena.particles.particle import Particle
from phenomena.particles.transformations.types.decays import Decay, TimeRemap

from phenomena.particles.transformations.kinematics import DecayCalc

class ParticleDecay(object):
    '''
    This is a mixin class for the Particle class
    It adds the attributes and methods related to particle decays
     - selects and sets particle decay channel
     - sets the time of next decay
     - includes de start method that is used by the particle server
    The ParticleDecay requires the ParticleData mixin.
    '''

    @property
    def decay(self):
        return self._decay

    def _set_decay(self):
        self._decay = Decay.set(self._decay_channels)

    @property
    def decay_time(self):
        return self._decay_time

    def _set_decayTime(self):
        if self._lifetime != Particle.STABLE :
            self._decay_time = TimeRemap.getNextDecayTime(self._lifetime)
        else:
            self._decay_time = Particle.STABLE

    def start(self, callback):
        if self._decay_time != Particle.STABLE:
            wait_time = TimeRemap.renormalize(self._decay_time)
            print "Wait for: ", wait_time
            threading.Timer(wait_time, callback).start()
        else:
            print "Wait for: ", 10
            threading.Timer(10, callback).start()

    @property
    def decayvalues(self):
        return self._decayvalues

    def _set_decayBoostedParameters(self):
        self._decayvalues = DecayCalc.getValues(self._mass,self._fourMomentum.gamma,self._fourMomentum.phi(),self._decay) # sets values for decay particles
