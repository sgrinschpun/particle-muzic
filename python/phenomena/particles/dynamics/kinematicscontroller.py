#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from skhep.math import Vector3D, LorentzVector

class KinematicsController(object):

    def __init__(self, particle):
        self._particle = particle

    def updateFourMomentum(self,acceleration,dt):
        '''
        Get the velocity of the particle (as the bostvector), add the acceleration to itself. Change the fourmomentum by using the boost method. We go to (0,0,0) before boosting to new velocity.
        Would boosting to acceleration*dt have the same effect?
        '''
        velocity = self._particle.fourMomentum.boostvector
        fourMomentumCM = self._particle.fourMomentum.boost(velocity)
        velocity += acceleration*dt
        return fourMomentumCM.boost(-1*velocity)

    def getPosition(self,velocity, dt):
        return velocity*dt
