from __future__ import division
import math, random

from phenomena.particles.kinematics.parameters import boostParams

import nbody

class LAB4BodyCalc(nbody.LabCalc):

    def __init__(self, decay, masses,angles,gamma):
        self._values = []
        for i in range(len(decay)):
            p = 5*random.random()
            E = (masses[i+1] ** 2 + p ** 2) ** (1/2)
            self._values.append({
            'name': decay[i],
            'p': p,
            'theta': 2*math.pi*random.random(),
            'E': E
            })

    @property
    def values(self):
        return self._values
