#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from phenomena.particles.particle import Particle
from phenomena.particles.mixins import ParticleId, ParticleData, ParticleDecay, ParticlePosition, ParticleBoost

NO_PARENT = -1

class BubbleChamberParticle(ParticleDecay, ParticlePosition, ParticleBoost, ParticleData, ParticleId, Particle):
    '''
    This class is intended for BubbleChamber simulation. That's why these mixins are chosen.
    '''

    def __init__(self, name, parent = NO_PARENT, **kwargs):

        #### ParticleId
        self._set_id() # Class Counter
        self._set_parent(parent) # The parent id of particle

        #### ParticleData
        self._set_name(name)  # Name of the particle
        self._set_pdgid(name) # Id from PDG
        self._set_mass() # Mass of the particle in GeV
        self._set_charge() # Charge of the particle
        self._set_lifetime() # Lifetime of the particle in ****units****
        self._set_type() # Particle Type (quark, lepton, boson, meson, baryon)
        self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...]
        self._set_decayChannels() #All the decay channels and BRs of the particle in format [(BR,[part1,..,partn]),...]

        #### ParticleBoost
        self._set_fourMomentum(kwargs)#assign 4momentum vector and  boosted parameters
        self._set_boostedLifetime()# lifetime is recalculated

        #### ParticlePosition
        self._set_initPosition()

        ### ParticleDecay
        self._set_decay() # Particle decay channel chosen
        self._set_decayTime() #Time until decay in ****units****
        self._set_decayBoostedParameters() #Calculates the boosted parameters of the decayed particles
