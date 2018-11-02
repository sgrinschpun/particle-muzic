#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from phenomena.particles.sources import ParticleDataSource

class ParticleData(object):
    '''
    This is a mixin class for the Particle class
    It adds the attributes and methods related to particle data
    Particle data is managed by the ParticleDataSource class
    '''
    @property
    def name(self):
        return self._name

    def _set_name(self, name):
        self._name = name

    @property
    def pdgid(self):
        return self._pdgid

    def _set_pdgid(self, name):
        self._pdgid = ParticleDataSource.getPDGId(name)

    @property
    def mass(self):
        return self._mass

    def _set_mass(self):
        self._mass = ParticleDataSource.getMass(self._name)

    @staticmethod
    def getmass(name):
        return ParticleDataSource.getMass(name)

    @property
    def charge(self):
        return self._charge

    def _set_charge(self):
        self._charge = ParticleDataSource.getCharge(self._name)

    @staticmethod
    def getcharge(name):
        return ParticleDataSource.getCharge(name)

    @property
    def lifetime(self):
        return self._lifetime

    def _set_lifetime(self):
        self._lifetime = ParticleDataSource.getTau(self._name)

    @property
    def type(self):
        return self._type

    def _set_type(self):
        self._type= ParticleDataSource.getType(self._name)

    @property
    def composition(self):
        return self._composition

    def _set_composition(self):
        self._composition = ParticleDataSource.getComposition(self._name)

    @property
    def decay_channels(self):
        return self._decay_channels

    def _set_decayChannels(self):
        self._decay_channels = ParticleDataSource.getDecayChannels(self._name)

    @property
    def baryonnumber(self):
        nq = 0.
        nqbar = 0.
        for q in self._composition:
            if 'bar' in q:
                nqbar += 1
            elif 'bar' not in q:
                nq += 1
        return (nq-nqbar)/3

    @property
    def leptonnumber(self):
        dict = {
        'e-':1,'nu_e':1,
        'e+':-1,'nu_ebar':-1,
        'mu-':1,'nu_mu':1,
        'mu+':-1,'nu_mubar':-1,
        'tau-': 1,'nu_tau':1,
        'tau+':-1,'nu_taubar':-1
        }
        if self.type == 'lepton':
            leptonnumber = dict[self.name]
        else:
            leptonnumber = 0

        return leptonnumber
