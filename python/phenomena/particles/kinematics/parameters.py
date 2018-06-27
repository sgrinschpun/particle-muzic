from __future__ import division
import math

from phenomena.particles.particle import ParticleDT

class boostParams(object):
    c= 299792458 #m/s

    def __init__(self, name, **kwargs):
        self._m = ParticleDT.getmass(name)

        #assert (len(kwargs)<2), "Do not initialize with both E and p"

        if kwargs.get('p',None) == None and kwargs.get('E',None) == None:
            self._build_static()
        elif kwargs.get('p') != None:
            self._build_from_p(kwargs.get('p'))
        elif kwargs.get('E') != None:
            self._build_from_E(kwargs.get('E'))


    def _build_from_p(self,p):
        self._p = p
        self._gamma = boostParams.gamma_from_p(self._m,self._p)
        self._beta =  boostParams.beta_from_gamma(self._gamma)
        self._E = boostParams.E_from_p(self._beta,self._p)
        self._T = boostParams.T_from_gamma(self._m,self._gamma)

    def _build_from_E(self,E):
        assert (E>self._m), "E needs to be > than mass"
        self._E = E
        self._gamma = boostParams.gamma_from_E(self._m,self._E)
        self._beta =  boostParams.beta_from_gamma(self._gamma)
        self._p = boostParams.p_from_E(self._beta,self._E)
        self._T = boostParams.T_from_gamma(self._m,self._gamma)

    def _build_static(self):
        self._E = self._m
        self._p = 0
        self._gamma = 1
        self._beta = 0
        self._T = 0

    @staticmethod
    def beta_from_gamma(gamma):
        return math.sqrt(1-1/math.pow(gamma,2))

    @staticmethod
    def gamma_from_E(m,E):
        if m != 0:
            gamma = E/m
        else:
            gamma = float("inf")
        return gamma

    @staticmethod
    def gamma_from_p(m,p):
        if m != 0:
            gamma = math.sqrt(1+math.pow(p/m,2))
        else:
            gamma = float("inf")
        return gamma

    @staticmethod
    def T_from_gamma(m,gamma):
        return (gamma-1)*m

    @staticmethod
    def p_from_E(beta, E):
        return beta*E

    @staticmethod
    def E_from_p(beta, p):
        return p/beta

    @property
    def E(self):
        return self._E

    @property
    def p(self):
        return self._p

    @property
    def gamma(self):
        return self._gamma

    @property
    def beta(self):
        return self._beta

    @property
    def T(self):
        return self._T
