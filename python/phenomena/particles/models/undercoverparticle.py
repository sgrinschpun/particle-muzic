#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from phenomena.particles.mixins import ParticleData, ParticleBoost, ParticlePosition

class UndercoverParticle(ParticlePosition, ParticleBoost, ParticleData):
    '''
    This particle class is only used when we need to consider interaction with particles that are not logged in the server. for example, interaction with protons in the bubble chamber.
    '''

    def __init__(self, name, mass = 0, **kwargs):
        #### ParticleData
        if mass == 0:
            self._set_name(name)  # Name of the particle
            self._set_pdgid(name) # Id from PDG
            self._set_mass() # Mass of the particle in GeV
            self._set_charge() # Charge of the particle
            self._set_type() # Particle Type (quark, lepton, boson, meson, baryon)
            self._set_composition()
        else:
            self._name = name
            self._mass = mass

        #### ParticleBoost
        self._set_fourMomentum(kwargs)#assign 4momentum vector and  boosted parameters

        #### ParticlePosition
        self._set_initPosition()
