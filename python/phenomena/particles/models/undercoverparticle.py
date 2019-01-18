#!/usr/bin/env python
__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from phenomena.particles.mixins import ParticleData, ParticleBoost, ParticlePosition
from phenomena.particles.transformations.types.decaysviavirtual.virtualparticlechannel import VirtualInfo
from phenomena.particles.sources import ParticleDataSource

class UndercoverParticle(ParticleBoost, ParticleData):
    '''
    This particle class is used when we need to consider interaction with particles that are not logged in the server. Also when doing kinematic calculations.
        To construct existing  particles (and take the mass from ParticleDataSource): argv[0] -> name (string)
        To construct non-exiting particles (with invented mass): argv[0] -> name (string) argv[1] -> mass (float):
        For both: kwargs -> p, theta, phi
    '''

    def __init__(self, *argv, **kwargs):
        #### You can create an undercoverparticle with the mass you choose
        try:
            self._name = argv[0]
            self._mass = argv[1]
        except:
            self._set_name(argv)  # Name of the particle
            self._set_pdgid() # Id from PDG
            self._set_mass() # Mass of the particle in GeV
            self._set_charge() # Charge of the particle
            self._set_type() # Particle Type (quark, lepton, boson, meson, baryon)
            self._set_composition()

        #### ParticleBoost
        self._set_fourMomentum(kwargs)#assign 4momentum vector and  boosted parameters

class VirtualUndercoverParticle(ParticleBoost,ParticleData):

    def __init__(self, *argv, **kwargs):
        self._virtuality =1
        self._name = argv[0].name
        self._mass = argv[0].mass
        self._decay_channels = [(1.0, map(ParticleDataSource.getPDGId, argv[0].decay))]
        self._set_pdgid() # Id from PDG
        self._set_charge() # Charge of the particle
        self._set_type() # Particle Type (quark, lepton, boson, meson, baryon)
        self._set_composition()

        #### ParticleBoost
        self._set_fourMomentum(kwargs)#assign 4momentum vector and  boosted parameters
