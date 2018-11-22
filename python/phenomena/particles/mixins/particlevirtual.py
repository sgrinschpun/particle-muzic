#!/usr/bin/env python

__author__ = "Sergi Masot"
__license__ = "--"
__version__ = "0.1"
__email__ = "sergimasot13@gmail.com"
__status__ = "development"
import collections
import six
from phenomena.particles.sources import ParticleDataSource

class ParticleVirtual(object):
    '''
    This is a mixin class for the Virtual Particle class
    It adds the attributes and methods related exclusively to virtual particle data.
    This is only complementary to ParticleData. Virtual Particles need the particleData mixin too.
    Particle data is managed by the ParticleDataSource class
    '''

    def _set_virtuality(self, argv):
        if isinstance(argv[0], collections.Mapping):
            self._virtuality = 1
        elif isinstance(argv[0], six.string_types):
            self._virtuality = 0

    @property
    def virtuality(self):
        return self._virtuality

    def _set_virtual_mass(self,argv):
        self._mass = argv[0].get('mass')

    @property
    def mass(self):
        return self._mass

    # def _set_virtual_lifetime(self):
    #     self._lifetime = ParticleDataSource.getTau(self._name) # The prefactor is a TEMPORAL solution for the brevity of lifetime in virtual particles
    #     if self._lifetime != -1 : # We stablish -1 for stable particles. Changing this number is a mess for other checks!
    #         self._lifetime *= 2e9


    def _set_virtualChannels(self,argv):
        if argv[0].get('decay') is None:
            self._deactivate_decay_channels() # for virtual particles, not all channels are allowed
            self._renorm_decay_channels() # remaining channels must have the probability renormalized
        else:
            self._decay_channels = argv[0].get('decay')


    def _deactivate_decay_channels(self):
        new_decay_channels = []
        for part in self._decay_channels:
            masses = [ParticleDataSource.getMass(ParticleDataSource.getName(x)) for x in part[1]]
            if sum(masses) <= self._mass:
                new_decay_channels.append(part)

        self._decay_channels = new_decay_channels

    def _renorm_decay_channels(self):
        total = 0
        for particle in self._decay_channels:
            total += particle[0]
        for index in range(len(self._decay_channels)):
            self._decay_channels[index]=(self._decay_channels[index][0]*(1/total),self._decay_channels[index][1])
