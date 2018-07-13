from __future__ import division
import math, random

from particle import Particle, ParticleDT, toDictionary

from phenomena.particles.kinematics.decay.calculations import DecayCalc
from phenomena.particles.kinematics.parameters import boostParams
from phenomena.particles.kinematics.virtual_particle import VirtualChannel

#Santi was here

NO_PARENT = -1
class ParticleBoosted(ParticleDT):
    c= 299792458 #m/s

    def __init__(self, name, parent = NO_PARENT, **kwargs): #initialize either with momentum (p) or energy (E)
        super(ParticleBoosted, self).__init__(name,parent)#inherit properties from ParticleDT
        self._theta = kwargs.get('theta',0) #the angle of this instance

        #decide if we want the decay to happen through a virtual channel
        VirtualChannel(self.decay,self._masses)
        #the decay particles and masses have been reset inside ParticleVirtual if necessary

        #calculate and assign boosted parameters
        self._setBoostedParameters(kwargs)

        # increase lifetime by gamma factor
        self._lifetime *= self._gamma


    def _setBoostedParameters(self,kwargs):
        self._params = boostParams(self._name,p=kwargs.get('p',None),E=kwargs.get('E',None)) # sets boosted parameters for this instance
        self._p = self._params.p
        self._E = self._params.E
        self._gamma = self._params.gamma
        self._beta = self._params.beta
        self._T = self._params.T

        self.decayvalues = DecayCalc(self._mass,self._gamma,self._theta,self.decay).values # sets values for decay particles



    @property
    def p(self):
        return self._p

    @property
    def E(self):
        return self._E

    @property
    def gamma(self):
        return self._gamma

    @property
    def beta(self):
        return self._beta

    @property
    def theta(self):
        return self._theta

    @property
    def T(self):
        return self._T

    def toDictionary(self):
        return toDictionary(self)
