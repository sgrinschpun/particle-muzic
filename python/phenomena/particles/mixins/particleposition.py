#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from skhep.math import Vector3D, LorentzVector, Point3D
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
        next_position_vector = self._nextPosition(dt)
        deltaincrement =  LorentzVector.from3vector(next_position_vector,dt)
        self._position += deltaincrement
        return self._position

    def _nextPosition(self,dt):
        self._acceleration = self._dynamics.updateAcceleration(dt)
        self.fourMomentum = self._kinematics.updateFourMomentum(self._acceleration, dt)
        self._velocity =self.fourMomentum.boostvector
        return self._kinematics.getPosition(self._velocity,dt)

    def distanceTravelled(self):
        originalpoint = Point3D(self._initialposition.x,self._initialposition.y,self._initialposition.z)
        thispoint = Point3D(self._position.x,self._position.y,self._position.z)
        return thispoint.distance(originalpoint)

    def timeTravelled(self):
        return self.fourMomentum.t
