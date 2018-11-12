#!/usr/bin/env python

__author__ = "Sergi Masot"
__license__ = "--"
__version__ = "0.1"
__email__ = "sergimasot13@gmail.com"
__status__ = "development"

from phenomena.particles.sources import ParticleDataSource

class ParticleVirtual(object):
    '''
    This is a mixin class for the Virtual Particle class
    It adds the attributes and methods related exclusively to virtual particle data.
    This is only complementary to ParticleData. Virtual Particles need the particleData mixin too.
    Particle data is managed by the ParticleDataSource class
    '''

    def _set_virtual_mass(self,name,mass):
        try:
            self._mass = mass
        except:
            self._mass = ParticleDataSource.getMass(name)

    def _set_virtual_lifetime(self):
        self._lifetime = ParticleDataSource.getTau(self._name) # The prefactor is a TEMPORAL solution for the brevity of lifetime in virtual particles
        if self._lifetime != -1 : # We stablish -1 for stable particles. Changing this number is a mess for other checks!
            self._lifetime *= 2e9

    # We have to decide if virtuality of a particle is an extra attribute or if it's a different type
    # This is what we can use for adding an extra attribute:

    @property
    def virtuality(self):
        return self._virtuality

    def _set_virtuality(self):
        if self._mass == ParticleDataSource.getMass(self._name):
            self._virtuality = 0
        else:
            self._virtuality = 1

    # Otherwise, we can change the method from particledata to set up the particle type for this other method

    # def _set_virtual_type(self):
    #     if self._mass == ParticleDataSource.getMass(name):
    #         self._type = ParticleDataSource.getType(self._name)
    #     else:
    #         self._type = ParticleDataSource.getType((self._name+'_virtual'))

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
