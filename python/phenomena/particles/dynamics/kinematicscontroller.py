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
        Get the velocity of the particle (as the bostvector), add the acceleration to it
        '''
        velocity = self._particle.fourMomentum.boostvector
        velocity += acceleration*dt
        return self._particle.fourMomentum.boost(velocity)

    def getPosition(self,velocity, dt):
        return velocity*dt
