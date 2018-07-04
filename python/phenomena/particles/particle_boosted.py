from __future__ import division
import math, random

from particle import Particle, ParticleDT, toDictionary

from phenomena.particles.kinematics.decay.calculations import DecayCalc
from phenomena.particles.kinematics.parameters import boostParams


NO_PARENT = -1
class ParticleBoosted(ParticleDT):
    c= 299792458 #m/s

    def __init__(self, name, parent = NO_PARENT, **kwargs): #initialize either with momentum (p) or energy (E)
        super(ParticleBoosted, self).__init__(name,parent)#inherit properties from ParticleDT
        self._theta = kwargs.get('theta',0) #the angle of this instance
        self._decayAnglesCM = self._set_decayAnglesCM() #the angle of the decay particles

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

        self._set_decayBoostedvalues() # sets values for decay particles

    def _set_decayAnglesCM(self):
        #this should be imporved for nbody decays
        angle = 2*math.pi * random.random()
        #angle = math.radians(55) just to test
        return [angle,angle+math.pi]

    def _set_decayBoostedvalues(self):
        self._set_decayAnglesCM()
        self.decayvalues = DecayCalc(self._mass,self._gamma,self._theta,self.decay,self._decayAnglesCM).values

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
