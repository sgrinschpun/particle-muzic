#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

import abc
from skhep.math import Vector3D, LorentzVector

class DynamicsController(object):

    def __init__(self, particle, dynamicsclasslist):
        self._particle = particle
        self._setDynamicsList(dynamicsclasslist)

    def _setDynamicsList(self, dynamicsclasslist):
        '''
        Sets list of all dynamics objects
        '''
        objectlist = []
        for transformationclass in dynamicsclasslist:
            objectlist.append(transformationclass(self._particle))
        self._dynamicslist = objectlist

    def updateAcceleration(self,dt):
        '''
        The acceleration is the sum of accelerations of every DynamicType
        '''
        acceleration = Vector3D()
        for dynamic in self._dynamicslist:
            acceleration += dynamic.getAcceleration(dt)
        return acceleration

class DynamicType(object):
    '''
    Abstratc class for itema in the dynamic list
    '''
    def getAcceleration(self,dt):
        return self._acceleration

class MagneticField(DynamicType):

    def __init__(self,particle):
        self._B = Vector3D(0,1,0)*0.01
        self._particle = particle

    def getAcceleration(self,dt):
        self._setForce()
        self._setAcceleration()
        return self._acceleration

    def _setForce(self):
        self._Bforce = self._particle.charge * self._particle.fourMomentum.boostvector.cross(self._B)

    def _setAcceleration(self):
        self._acceleration = self._Bforce/self._particle.mass

class ElectricField(DynamicType):

    def __init__(self,particle):
        self._E = Vector3D(0,0,1)
        self._particle = particle

    def getAcceleration(self,dt):
        self._setForce()
        self._setAcceleration()
        return self._acceleration

    def _setForce(self):
        self._Eforce = self._particle.charge * self._E

    def _setAcceleration(self):
        self._acceleration = self._Eforce/self._particle.mass

class Ionization(DynamicType):

    DENSITY = 0.1 #0.07 #gr/cm3

    def __init__(self, particle):
        self._particle = particle

    def getAcceleration(self,dt):
        if self._particle.charge == 0 or self._particle.fourMomentum.beta == 0:
            self._acceleration = Vector3D(0,0,0)
        else:
            self._setAcceleration()
        return self._acceleration

    def _setEnergyLoss(self):
        return self._BetheBlock(self._particle.fourMomentum.beta)

    def _BetheBlock(self,beta):
        return 2.1*Ionization.DENSITY/beta**2

    def _setAcceleration(self):
        newEnergy = self._particle.fourMomentum.e - self._setEnergyLoss()
        newP = self._particle.fourMomentum.beta*newEnergy
        newpvector = newP*self._particle.fourMomentum.vector.unit()
        oldpvector = self._particle.fourMomentum.vector
        self._acceleration = newpvector - oldpvector
