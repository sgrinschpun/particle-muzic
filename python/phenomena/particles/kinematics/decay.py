from __future__ import division
import math, random

from phenomena.particles.particle import ParticleDT
from phenomena.particles.kinematics.parameters import boostParams

class CMcalc(object):
    @staticmethod
    def E(m0, m1, m2):
        E1 = (math.pow(m0,2)+math.pow(m1,2)-math.pow(m2,2))/(2*m0)
        E2 = (math.pow(m0,2)-math.pow(m1,2)+math.pow(m2,2))/(2*m0)
        return [E1,E2]

    @staticmethod
    def p(m0, m1, m2):
        num1 = math.pow(m0,2)-math.pow(m1-m2,2)
        num2 = math.pow(m0,2)-math.pow(m1+m2,2)
        p = math.sqrt(num1*num2)/(2*m0)
        return [p,p]

    @staticmethod
    def pxy(m0,m1,m2,angleCM):
        return [{   'x':CMcalc.p(m0,m1,m2)[0]*math.cos(angleCM[0]),
                    'y':CMcalc.p(m0,m1,m2)[0]*math.sin(angleCM[0])
                },{
                    'x':CMcalc.p(m0,m1,m2)[1]*math.cos(angleCM[1]),
                    'y':CMcalc.p(m0,m1,m2)[1]*math.sin(angleCM[1])
                }]

class LABcalc(object):

    def __init__(self,m0,gamma,decay,angleCM,parentTheta):
        self._decay = decay
        if len(self._decay) == 2:   # for 2-body decay
            self._gamma = gamma
            self._angleCM = angleCM
            self._parentTheta = [parentTheta, parentTheta]
            self._m0 = m0
            self._m1= ParticleDT.getmass(self._decay[0])
            self._m2= ParticleDT.getmass(self._decay[1])
            self._pxy2 = self._set_pxy2(self._m0,self._m1,self._m2,self._gamma,self._angleCM)
            self._p = self._set_p2()
            self._theta = self._set_boostedAngle2()
            self._values = [{
                'name': self._decay[0],
                'p': self._p[0],
                'theta':self._theta[0]},{
                'name': self._decay[1],
                'p': self._p[1],
                'theta':self._theta[1]}]
        else:  # here comes the calculations of 3body decay (4body,5body,...). at the moment random
            self._values = []
            for part in self._decay:
                self._values.append({
                'name': part,
                'p': 5*random.random(),
                'theta': 2*math.pi*random.random()
                })

    @property
    def values(self):
        return self._values

    def _set_pxy2(self,m0,m1,m2,gamma,angleCM):
        beta = boostParams.beta_from_gamma(gamma)
        CMpxy = CMcalc.pxy(m0,m1,m2,angleCM)
        CME = CMcalc.E(m0,m1,m2)
        return [
            {
            'x':gamma*(CMpxy[0]['x']+ beta*CME[0]),
            'y':CMpxy[0]['y']
            },
            {
            'x':gamma*(CMpxy[1]['x']+ beta*CME[1]),
            'y':CMpxy[1]['y']
            }
        ]

    def _set_p2(self):
        return [math.sqrt(self._pxy2[0]['x']**2+self._pxy2[0]['y']**2),math.sqrt(self._pxy2[1]['x']**2+self._pxy2[1]['y']**2)]

    def _set_boostedAngle2(self):
        if self._gamma != 1:
            ttheta0 = self._pxy2[0]['y']/self._pxy2[0]['x']
            ttheta1 = self._pxy2[1]['y']/self._pxy2[1]['x']
            theta = [math.atan(ttheta0),math.atan(ttheta1)]
        else:
            theta = self._angleCM

        return [theta[i]+self._parentTheta[i] for i in range(len(theta))]
