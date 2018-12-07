#!/usr/bin/env python

__author__ = "Sergi Masot"
__license__ = "--"
__version__ = "0.1"
__email__ = "sergimasot13@gmail.com"
__status__ = "Development"

from phenomena.particles.particle import Particle
from phenomena.particles.mixins import ParticleId, ParticleVirtual, ParticleData, ParticleBoost, ParticleTransformation
from phenomena.particles.transformations.types import Decay, NoTransformation #VirtualDecay

class QuantumUniverseVirtualParticle(ParticleTransformation, ParticleBoost, ParticleVirtual, ParticleData, ParticleId, Particle):
    '''
    This class is intended for the QuantumUniverse simulation allowing virtual particles.
    argv[0] -> Name  |  {'Name':Name(str), 'Mass':Mass(float), 'Decay':Decay(list of tuples)}
    argv[1] -> Parent
    kwargs -> p, theta, phi
    '''
    TRANSFORMATIONS = [Decay, NoTransformation]

    DECAYTHROUGHVIRTUAL = True

    def __init__(self, *argv, **kwargs):

        #### ParticleId
        self._set_id() # Class Counter
        self._set_parent(argv) # The parent id of particle

        #### ParticleVirtual
        self._set_virtuality(argv)
        if self._virtuality == 0: #NonVirtual Init
            self._set_name(argv)  # Name of the particle
            self._set_pdgid() # Id from PDG
            self._set_mass() # Mass of the particle in GeV
            self._set_charge() # Charge of the particle
            self._set_lifetime() # Lifetime of the particle in ****units****
            self._set_type() # Particle Type (quark, lepton, boson, meson, baryon)
            self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...]
            self._set_decayChannels() #All the decay channels and BRs of the particle in format [(BR,[part1,..,partn]),...]
        elif self._virtuality == 1: #Virtual Init
            self._set_name(argv)
            self._set_pdgid()
            self._set_virtual_mass(argv)
            self._set_charge()
            self._set_type()
            self._set_composition()
            self._set_lifetime()  # Should it be special for virtual particles?
            self._set_decayChannels()
            self._set_virtualChannels(argv)
        else:
            return None

        #### ParticleBoost
        self._set_fourMomentum(kwargs)#assign 4momentum vector and  boosted parameters
        self._set_boostedLifetime()# lifetime is recalculated

        ### ParticleTransformation
        self._setTransformationManager(self, QuantumUniverseVirtualParticle.TRANSFORMATIONS)
