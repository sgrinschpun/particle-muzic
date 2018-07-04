from __future__ import division
import math

from phenomena.particles.kinematics.parameters import boostParams

import nbody

class CM2BodyCalc(nbody.CMCalc):
    @staticmethod
    def E(masses):
        E1 = (math.pow(masses[0],2)+math.pow(masses[1],2)-math.pow(masses[2],2))/(2*masses[0])
        E2 = (math.pow(masses[0],2)-math.pow(masses[1],2)+math.pow(masses[2],2))/(2*masses[0])
        return [E1,E2]

    @staticmethod
    def p(masses):
        num1 = math.pow(masses[0],2)-math.pow(masses[1]-masses[2],2)
        num2 = math.pow(masses[0],2)-math.pow(masses[1]+masses[2],2)
        p = math.sqrt(num1*num2)/(2*masses[0])
        return [p,p]

    @staticmethod
    def pxy(masses,angles):
        p = CM2BodyCalc.p(masses)
        return [{   'x':p[0]*math.cos(angles[1]),
                    'y':p[0]*math.sin(angles[1])
                },{
                    'x':p[1]*math.cos(angles[2]),
                    'y':p[1]*math.sin(angles[2])
                }]

class LAB2BodyCalc(nbody.LabCalc):

    def __init__(self,decay,masses,angles,gamma):
        self._decay = decay
        self._gamma = gamma
        self._masses = masses
        self._anglesCM = angles

        self._pxy = self._set_pxy(self._masses,self._anglesCM, self._gamma)
        self._p = self._set_p()
        self._theta = self._set_boostedAngles()

        self._values = self._set_values()


    def _set_pxy(self,masses,angles,gamma):
        beta = boostParams.beta_from_gamma(gamma)
        CMpxy = CM2BodyCalc.pxy(masses,angles)
        CME = CM2BodyCalc.E(masses)
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

    def _set_p(self):
        return [math.sqrt(self._pxy[0]['x']**2+self._pxy[0]['y']**2),math.sqrt(self._pxy[1]['x']**2+self._pxy[1]['y']**2)]

    def _set_boostedAngles(self):
        if self._gamma != 1:
            theta0 = self._pxy[0]['y']/self._pxy[0]['x']
            theta1 = self._pxy[1]['y']/self._pxy[1]['x']
            theta = [math.atan(theta0),math.atan(theta1)]
        else:
            theta = self._anglesCM[1:]

        return [theta[0]+self._anglesCM[0],theta[1]+self._anglesCM[0]]


    def _set_values(self):
        return  [{
                    'name': self._decay[0],
                    'p': self._p[0],
                    'theta':self._theta[0]},{
                    'name': self._decay[1],
                    'p': self._p[1],
                    'theta':self._theta[1]
                }]

    @property
    def values(self):
        return self._values
