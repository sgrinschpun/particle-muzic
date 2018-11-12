#!/usr/bin/env python

__author__ = "Sergi Masot"
__license__ = "--"
__version__ = "0.1"
__email__ = "sergimasot13@gmail.com"
__status__ = "development"

from phenomena.particles.sources import ParticleDataSource
from phenomena.particles.decays.setdecay_virtual import VirtualDecay

class ParticleChannel(object):
    '''
    This is a mixin class for the Virtual decay
    The ParticleChannel requires the ParticleData and ParticleDecay mixins
    '''

    def _set_virtual_decay(self):

        self._set_decay_masses()
        self._decay = VirtualDecay.set(self._decay,self._mass,self._decay_masses,self._name)

    @property
    def decay_masses(self):
        return self._decay_masses

    def _set_decay_masses(self):
        decay_masses = []
        for part in self._decay:
            decay_masses.append(ParticleDataSource.getMass(part))

        self._decay_masses = decay_masses
