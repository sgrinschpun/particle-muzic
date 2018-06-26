from __future__ import division
import math, random

from particle import Particle, ParticleDT

from kinematics.decay import LABcalc

class ParticleBoosted(ParticleDT):
    c= 299792458 #m/s

    def __init__(self, name, p=0, E=0, theta=0): #initialize either with momentum (p) or energy (e)
        super(ParticleBoosted, self).__init__(name) #inherit properties from ParticleDT
        self._theta = theta
        self._set_boostvalues(p,E)

        self._set_decayBoostedvalues()

    @staticmethod
    def beta_from_gamma(gamma):
        return math.sqrt(1-1/math.pow(gamma,2))

    def _set_gamma_from_E(self):
        return self._E/self.mass

    def _set_gamma_from_p(self):
        return math.sqrt(1+math.pow(self._p/self.mass,2))

    def _set_p_from_E(self):
        return self._beta*self._E

    def _set_E_from_p(self):
        return self._p/self._beta

    def _set_T(self):
        return (self._gamma-1)*self.mass

    def _set_boostvalues(self,p,E):
        if p and E:
            print ("You can't define both E & p")
        elif p and not E:
            self._p = p   # Momentum of the particle, GeV/c, because mass comes in GeV/c^2
            if self.mass != 0:
               self._gamma= self._set_gamma_from_p()
            else:
                self._gamma = float("inf")
            self._beta = ParticleBoosted.beta_from_gamma(self._gamma)
            self._E = self._set_E_from_p()
            self._T = self._set_T()
        elif E and not p:
            self._E = E   # Energy of the particle, GeV, because mass comes in GeV/c^2
            if self.mass != 0:
                self._gamma= self._set_gamma_from_E()
            else:
                self._gamma = float("inf")
            self._beta = ParticleBoosted.beta_from_gamma(self._gamma)
            self._p = self._set_p_from_E()
            self._T = self._set_T()
        elif E==0 and p==0:
            self._E = 0
            self._p = 0
            self._gamma=1
            self._beta=0
            self._T = 0


    def _set_decayAnglesCM(self):
        angle = 2*math.pi * random.random()
        self._decayAnglesCM = [angle,angle+math.pi]

    def _set_decayBoostedvalues(self):
        self._set_decayAnglesCM()
        self._decayvalues = LABcalc(self._mass,self._gamma,self.decay,self._decayAnglesCM,self._theta).values

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, value):
        self._set_boostvalues(p=value, E=0)

    @property
    def E(self):
        return self._E

    @E.setter
    def E(self, value):
        self._set_boostvalues(P=0,E=value)

    @property
    def gamma(self):
        return self._gamma

    @property
    def beta(self):
        return self._beta

    @property
    def T(self):
        return self._T

    @ParticleDT.lifetime.getter
    def lifetime(self):
        return self._gamma*self._lifetime
