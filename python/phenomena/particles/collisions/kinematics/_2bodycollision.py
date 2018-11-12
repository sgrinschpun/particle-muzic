from __future__ import division
import math, random

# In the original we import BoostParams, which is missing in this version. If an error raises it could be This
# Currently, BoostParams's methods are in particleboost ( I think )

import nbodycollision

# This class gets the parameters of the outgoing particle in a CM scenario when given the energy of the system plus the energy
# of the incoming particles
class CM2ColCalc(nbodycollision.CMCalc):

    def __init__(self,particles,energy,masses):
        en1 = (energy**2+masses[0]**2-masses[1]**2)/(2*energy)
        en2 = (energy**2-masses[0]**2+masses[1]**2)/(2*energy)
        self._values = self._set_values(en1,en2,energy)

    def _set_values(self,en1,en2,energy):
        return  {
                    'p': 0,
                    'theta': 0,
                    'E': energy,
                    'mass': energy,
                    'E1': en1,
                    'E2': en2
                }

    @property
    def values(self):
        return self._values

# This class gets the parameters for the outgoing particle given the momenta and angles of incoming particles
class Lab2ColCalc(nbodycollision.LabCalc):

    def __init__(self,particles,momenta,angles,masses):
        self._inc_particles = particles
        inc_energies = self._set_energies(momenta,masses)
        # From here on, all calculations are for outgoing particle ('virtual')
        self._pExyz = self._set_pExyz(momenta,angles,inc_energies)
        self._p = self._set_p()
        self._mass = self._set_mass(self._p,self._pExyz['E'])
        self._theta = self._set_angle(self._pExyz['x'],self._pExyz['y'])

        self._values = self._set_values()

    def _set_energies(self,momenta,masses):
        E1 = (masses[0]**2+momenta[0]**2)**(1/2) # For 2D
        E2 = (masses[1]**2+momenta[1]**2)**(1/2) # For 2D
        return [E1,E2]

    def _set_pExyz(self,momenta,angles,energies):
        return {
            'x':momenta[0]*math.cos(angles[0])+momenta[1]*math.cos(angles[1]),
            'y':momenta[0]*math.sin(angles[0])+momenta[1]*math.sin(angles[1]),
            'z':0,
            'E':energies[0]+energies[1]
        }

    def _set_p(self):
        return math.sqrt(self._pExyz['x']**2+self._pExyz['y']**2)

    def _set_mass(self,p,E):
        return (E**2-p**2)**(1/2)

    def _set_angle(self,px,py):
        if px != 0:
            angle=math.atan(py/px)
        elif py != 0:
            sign = py/(py**2)**(1/2)
            angle=sign*math.pi/2
        else:
            angle=0
        return angle

    def _set_values(self):
        return  {
                    'p': self._p,
                    'theta': self._theta,
                    'E': self._pExyz['E'],
                    'mass': self._mass
                }

    @property
    def values(self):
        return self._values
