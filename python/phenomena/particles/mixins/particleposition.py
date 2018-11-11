#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from skhep.math import Vector3D, LorentzVector
from phenomena.particles.dynamics import DynamicsController, KinematicsController

PARTICLE_INIT_POSITION = Vector3D(x=0.0, y=0.0, z=0.0)

class ParticlePosition(object):
    '''
    This is a mixin class for the Particle class
    It adds the attributes and methods related to the 4-dimensional Minkowski space-time vector of the particle as defined in the LorentzVector class of SciKitHEP
    '''

    @property
    def position(self):
        return self._position

    def _set_initPosition(self):
        self._position = LorentzVector.from3vector(PARTICLE_INIT_POSITION,0.)
        self._initialposition = self._position.copy()

    def _set_dynamics(self, dynamicsclasslist):
        self._dynamics = DynamicsController(self, dynamicsclasslist)

    def _set_kinematics(self) :
        self._kinematics = KinematicsController(self)

    def updatePosition(self,dt):
        deltaincrement = self._nextPosition(dt)
        self._position += deltaincrement
        return self._position

    def _nextPosition(self,dt):
        self._acceleration = self._dynamics.updateAcceleration(dt)
        self._kinematics.updateFourMomentum(self._acceleration, dt)
        return self._kinematics.getPosition(self.fourMomentum.boostvector,dt)

    def distanceTravelled():
        return self._position.distance(self._initialposition)

    def timeTravelled():
        pass
