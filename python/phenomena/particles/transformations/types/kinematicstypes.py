from __future__ import division
import math, random, copy
import abc
from skhep.math  import Kallen_function, Vector3D, LorentzVector
from skhep.units import MeV, GeV

class KinematicsCalculations(object):
    '''
    We expect initialparticle and target to be a class particle and outputparticles a list of particles
    '''
    def __init__(self, initialparticle, target, finalparticles):
        self._initial= initialparticle
        self._target = target
        self._final = finalparticles
        self._set_calculations()

    def getFinalState(self):
        return self._calculations.finalState

    @abc.abstractmethod
    def _set_calculations(self):
        pass

class LABNBody(object):
    '''
    Steps for the calculation:
    - Solve output in CM frame of reference
        - Get the BoostVector
        - Transform initial + target to CM
        - Get S, P, vectors of 2 bodies. Use dalitz if 3 bodies.
    - Boost to LAB frame of reference
    '''
    def __init__(self,initialparticle, target, finalparticles):
        self._setInitialParticleLAB(initialparticle)
        self._setTargetLab(target)
        self._setFinalparticlesCM(finalparticles)
        self._setBoost()
        self._setCM()
        self._setLAB()

    @property
    def finalState(self):
        return self._finalparticlesLAB

    @abc.abstractmethod
    def _setInitialParticleLAB(self, initialparticle):
        pass

    def _setTargetLab(self, target):
        if target !=None:
            self._targetLAB = target

    def _setFinalparticlesCM(self, finalparticles):
        self._finalparticlesCM = finalparticles

    def _setBoost(self):
        self._setBoostVector()
        self._initialparticleCM  = self._initialparticleLAB.fourMomentum.boost(self._boostVector)
        self._targetCM = self._targetLAB.fourMomentum.boost(self._boostVector)

    def _setBoostVector(self):
        A = self._targetLAB.mass/(self._initialparticleLAB.mass*self._initialparticleLAB.fourMomentum.gamma)
        factor = 1/(A+1)
        self._boostVector = self._initialparticleLAB.fourMomentum.boostvector*factor

    def _setCM(self):
        self._setS()
        self._setP(self._s,self._initialparticleLAB.mass,self._targetLAB.mass)
        self._setFourMomenta()

    def _setS(self):
        self._s = (self._initialparticleCM.e + self._targetCM.e)**2

    def _setP(self, s, m1, m2):
        self._p = math.sqrt( Kallen_function(s, m1**2, m2**2)/(4*s))

    def _setFourMomenta(self):
        vector3Dlist = self._setVector3D(self._p)
        for id, particle in enumerate(self._finalparticlesCM):
            particle.fourMomentum.setpxpypzm(vector3Dlist[id].x,vector3Dlist[id].y,vector3Dlist[id].z,particle.mass)

    def _setVector3D(self,p):
        theta = math.pi * random.random() # [0, math.pi]
        phi = 2*math.pi * random.random()#random.choice([-math.pi/2, math.pi/2])
        vector1 = Vector3D.fromsphericalcoords(p,theta,phi)
        vector2 = -1*vector1
        return [vector1, vector2]

    def _setLAB(self):
        self._finalparticlesLAB = copy.deepcopy(self._finalparticlesCM)
        for particle in self._finalparticlesLAB:
            newfourMomentum = particle.fourMomentum.boost(-1*self._boostVector)
            particle.fourMomentum = newfourMomentum
