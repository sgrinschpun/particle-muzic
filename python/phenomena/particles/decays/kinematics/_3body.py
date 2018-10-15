from __future__ import division
import math, random

from skhep.constants import half_pi, two_pi


import nbody

def beta_from_gamma(gamma):
    return math.sqrt(1-1/math.pow(gamma,2))

class C12M3BodyCalc(nbody.C12MCalc):
    # Calculations for energies and momenta in the CM for particles 1 and 2 only (CM 1-2)
    @staticmethod
    def dalitz(masses):
        m12 = random.uniform(masses[1]+masses[2],masses[0]-masses[3])
        return m12

    @staticmethod
    def E(masses,m12):
        E2 = (m12**2-masses[1]**2+masses[2]**2)/(2*m12)
        E1 = (E2**2+masses[1]**2-masses[2]**2)**(1/2)
        E3 = (masses[0]**2-m12**2-masses[3]**2)/(2*m12)
        return [E1,E2,E3]

#    # We divide the Dalitz calculation so we can calculate and save the energies needed for m23
#    def _dalitz2(self,masses, E):
#        m23 = random.uniform((E[1]+E[2])**2-((E[1]**2-masses[2]**2)**(1/2)+(E[2]**2-masses[3]**2)**(1/2))**2,(E[1]+E[2])**2-((E[1]**2-masses[2]**2)**(1/2)-(E[2]**2-masses[3]**2)**(1/2))**2)
#        return m23
#  It's not needed since we use this degree of freedom to randomize the angle between p1 and p3

    @staticmethod
    def p(masses,m12):
        num1 = m12**2-(masses[1]+masses[2])**2
        num2 = m12**2-(masses[1]-masses[2])**2
        p = (num1*num2)**(1/2)/(2*m12)
        return [p,p]

    @staticmethod
    def pxy(masses,m12,angles):
        p = C12M3BodyCalc.p(masses,m12)
        return [{   'x':p[0]*math.cos(angles[1]),
                    'y':p[0]*math.sin(angles[1])
                },{
                    'x':p[1]*math.cos(angles[2]),
                    'y':p[1]*math.sin(angles[2])
                }]

class CM3BodyCalc(nbody.CMCalc):

    @staticmethod
    def p3(masses,m12):
        num1 = masses[0]**2-(m12+masses[3])**2
        num2 = masses[0]**2-(m12-masses[3])**2
        p3 = (num1*num2)**(1/2)/(2*masses[0])
        return p3

    @staticmethod
    def pExyz(masses,angles):
        m12 = C12M3BodyCalc.dalitz(masses)
        C12ME = C12M3BodyCalc.E(masses,m12)
#        dalitz[1] = C12M3BodyCalc._dalitz2(masses,C12ME)
        p3 = CM3BodyCalc.p3(masses,m12)
        gamma = (1+p3**2/m12**2)**(1/2)
        beta = beta_from_gamma(gamma)
        C12Mpxy = C12M3BodyCalc.pxy(masses,m12,angles)

        return [
            {
            'x':gamma*(C12Mpxy[0]['x'] - beta*C12ME[0]),
            'y':C12Mpxy[0]['y'],
            'z':0,
            'E':gamma*(-beta*C12Mpxy[0]['x'] + C12ME[0])
            },
            {
            'x':gamma*(C12Mpxy[1]['x'] - beta*C12ME[1]),
            'y':C12Mpxy[1]['y'],
            'z':0,
            'E':gamma*( -beta*C12Mpxy[1]['x'] + C12ME[1])
            },
            {
            'x':p3,
            'y':0,
            'z':0,
            'E':(masses[3]**2+p3**2)**(1/2)
            }
        ]

class LAB3BodyCalc(nbody.LabCalc):

    def __init__(self,decay,masses,phi,gamma):
        self._decay = decay
        self._gamma = gamma
        self._masses = masses
        self._anglesCM = self._set_AnglesCM12(phi)
        self._pExyz = self._set_pExyz(self._masses, self._anglesCM, self._gamma)
        self._p = self._set_p()
        self._phi = self._set_boostedAngles(self._anglesCM) # Boost angles from CM RF to LAB RF

        self._values = self._set_values()

    # It's convenient to set the angles in the simplest reference frame (CM 1-2 in this case)
    def _set_AnglesCM12(self, phi):
        anglesCM = []  # list 0:parent particle angle, 1:first decay particle angle in CM, etc
        anglesCM.append(phi)
        angle = 2*math.pi * random.random()
        angles = [angle,angle+math.pi]
        for angle in angles:
            anglesCM.append(angle)
        return anglesCM

    def _set_pExyz(self,masses,angles,gamma):
        beta = beta_from_gamma(gamma)
        CMpExy = CM3BodyCalc.pExyz(masses,angles)

        # Change the angles from the CM 1-2 to the new frame CM
        # Also add a random angle between the plane of the decay in CM and the speed of P
        tanphi0 = math.atan2(CMpExy[0]['y'],CMpExy[0]['x'])
        tanphi1 = math.atan2(CMpExy[1]['y'],CMpExy[1]['x'])
        alpha = 2*math.pi * random.random()
        self._anglesCM[1:4] = [tanphi0+alpha,tanphi1+alpha,alpha]

        # Update the momenta with the new angles
        p = [math.sqrt(CMpExy[0]['x']**2+CMpExy[0]['y']**2),math.sqrt(CMpExy[1]['x']**2+CMpExy[1]['y']**2),math.sqrt(CMpExy[2]['x']**2+CMpExy[2]['y']**2)]
        for i in range(1,4):
            CMpExy[i-1]['x'] = p[i-1]*math.cos(self._anglesCM[i])
            CMpExy[i-1]['y'] = p[i-1]*math.sin(self._anglesCM[i])


        return [
            {
            'x':gamma*(CMpExy[0]['x']+ beta*CMpExy[0]['E']),
            'y':CMpExy[0]['y'],
            'z':0,
            'E':gamma*(beta*CMpExy[0]['x']+ CMpExy[0]['E'])
            },
            {
            'x':gamma*(CMpExy[1]['x']+ beta*CMpExy[1]['E']),
            'y':CMpExy[1]['y'],
            'z':0,
            'E':gamma*(beta*CMpExy[1]['x']+ CMpExy[1]['E'])
            },
            {
            'x':gamma*(CMpExy[2]['x']+ beta*CMpExy[2]['E']),
            'y':CMpExy[2]['y'],
            'z':0,
            'E':gamma*(beta*CMpExy[2]['x']+ CMpExy[2]['E'])
            }
        ]

    def _set_p(self):
        return [math.sqrt(self._pExyz[0]['x']**2+self._pExyz[0]['y']**2),math.sqrt(self._pExyz[1]['x']**2+self._pExyz[1]['y']**2),math.sqrt(self._pExyz[2]['x']**2+self._pExyz[2]['y']**2)]

    def _set_boostedAngles(self, angles):
        if self._gamma != 1:
            phi0 = self._pExyz[0]['y']/self._pExyz[0]['x']
            phi1 = self._pExyz[1]['y']/self._pExyz[1]['x']
            phi2 = self._pExyz[2]['y']/self._pExyz[2]['x']
            phi = [math.atan(phi0),math.atan(phi1),math.atan(phi2)]
        else:
            phi = angles[1:]

        return [phi[0]+self._anglesCM[0],phi[1]+self._anglesCM[0],phi[2]+self._anglesCM[0]]


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
                    'E':self._pExyz[1]['E']      },{
                    'name': self._decay[2],
                    'p': self._p[2],
                    'phi':self._phi[2],
                    'theta':half_pi,
                    'E':self._pExyz[2]['E']
                }]

    @property
    def values(self):
        return self._values
