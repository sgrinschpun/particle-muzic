from __future__ import division
import math, random

from skhep.constants import half_pi, two_pi
import nbody

def beta_from_gamma(gamma):
    return math.sqrt(1-1/math.pow(gamma,2))

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

    def __init__(self,decay,masses,phi,gamma):
        self._decay = decay
        self._gamma = gamma
        self._masses = masses
        self._anglesCM = self._set_AnglesCM(phi)
        self._pExyz = self._set_pExyz(self._masses,self._anglesCM, self._gamma)
        self._p = self._set_p()
        self._phi = self._set_boostedAngles()

        self._values = self._set_values()

    def _set_AnglesCM(self, phi):
        anglesCM = []  # list 0:parent particle angle, 1:first decay particle angle in CM, etc
        anglesCM.append(phi)
        angle = 2*math.pi * random.random()
        angles = [angle,angle+math.pi]
        for angle in angles:
            anglesCM.append(angle)
        return anglesCM

    def _set_pExyz(self,masses,angles,gamma):
        beta = beta_from_gamma(gamma)
        CMpxy = CM2BodyCalc.pxy(masses,angles)
        CME = CM2BodyCalc.E(masses)
        return [
            {
            'x':gamma*(CMpxy[0]['x']+ beta*CME[0]),
            'y':CMpxy[0]['y'],
            'z':0,
            'E':gamma*(beta*CMpxy[0]['x']+ CME[0])
            },
            {
            'x':gamma*(CMpxy[1]['x']+ beta*CME[1]),
            'y':CMpxy[1]['y'],
            'z':0,
            'E':gamma*(beta*CMpxy[1]['x']+ CME[1])
            }
        ]

    def _set_p(self):
        return [math.sqrt(self._pExyz[0]['x']**2+self._pExyz[0]['y']**2),math.sqrt(self._pExyz[1]['x']**2+self._pExyz[1]['y']**2)]

    def _set_boostedAngles(self):
        if self._gamma != 1:
            phi0 = self._pExyz[0]['y']/self._pExyz[0]['x']
            phi1 = self._pExyz[1]['y']/self._pExyz[1]['x']
            phi = [math.atan(phi0),math.atan(phi1)]
        else:
            phi = self._anglesCM[1:]

        return [phi[0]+self._anglesCM[0],phi[1]+self._anglesCM[0]]


    def _set_values(self):
        return  [{
                    'name': self._decay[0],
                    'p': self._p[0],
                    'phi':self._phi[0],
                    'theta':half_pi,
                    'E':self._pExyz[0]['E']      },{
                    'name': self._decay[1],
                    'p': self._p[1],
                    'phi':self._phi[1],
                    'theta':half_pi,
                    'E':self._pExyz[1]['E']
                }]

    @property
    def values(self):
        return self._values
