#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from skhep.math import Vector3D, LorentzVector
from skhep.constants import half_pi, two_pi
from phenomena.particles.particle import Particle

THETA_DEFAULT = 0 #half_pi
PHI_DEFAULT = 0

class ParticleBoost(object):
    '''
    This is a mixin class for the Particle class
    It adds the attributes and methods related to 4momentum as defined in the LorentzVector class of SciKitHEP
    The ParticleBoost requires the ParticleData mixin.
    Construction from spherical coordinates:
        - r, radius > 0
        - theta (inclination in radians (theta in [0, pi] rad)
        THETA_DEFAULT = half_pi
        - phi (azimuthal angle in radians (phi in [0, 2pi) rad)
        PHI_DEFAULT = 0
    '''

    @property
    def fourMomentum(self):
        return self._fourMomentum

    @fourMomentum.setter
    def fourMomentum(self, fourMomentum):
        self._fourMomentum = fourMomentum

    def _set_fourMomentum(self, kwargs):
        '''
        Particles are instantiated with momentum and angles.
        Energy is not implemented as parameter for constructor
        A P 3D vector for the constructor?
        '''
        if kwargs.get('p',None) == None:
            self._fourMomentum = ParticleBoost._build_static(self)
        elif kwargs.get('p') != None:
            self._fourMomentum = ParticleBoost._build_from_p(self, kwargs)

    @staticmethod
    def _build_static(self):
        fourmomenta = LorentzVector()
        fourmomenta.setpxpypzm(0,0,0,self._mass)
        return fourmomenta

    @staticmethod
    def _build_from_p(self, kwargs):
        p=kwargs.get('p',0)
        theta=kwargs.get('theta',THETA_DEFAULT)
        phi=kwargs.get('phi',PHI_DEFAULT)
        vector = Vector3D.fromsphericalcoords(p,theta,phi)
        fourmomenta = LorentzVector()
        fourmomenta.setpxpypzm(vector.x,vector.y,vector.z,self._mass)
        return fourmomenta

    def _set_boostedLifetime(self):# lifetime is recalculated if not stable
        if self._lifetime != Particle.STABLE :
            self._lifetime *= self._fourMomentum.gamma

    @property
    def p(self):
        return self._fourMomentum.p

    @property
    def E(self):
        return self._fourMomentum.e

    @property
    def Pt(self):
        return self._fourMomentum.pt

    @property
    def gamma(self):
        return self._fourMomentum.gamma

    @property
    def beta(self):
        return self._fourMomentum.beta

    @property
    def T(self):
        return self._fourMomentum.e - self._mass

    @property
    def theta(self):
        return self._fourMomentum.theta()

    @property
    def phi(self):
        return self._fourMomentum.phi()

    @property
    def vector(self):
        return self._fourMomentum.vector
