from __future__ import division
import math, random

from phenomena.particles.kinematics.parameters import boostParams

import nbody

class LAB5BodyCalc(nbody.LabCalc):

    def __init__(self,decay,masses,angles,gamma):
        self._values = []
        for part in decay:
            self._values.append({
            'name': part,
            'p': 5*random.random(),
            'theta': 2*math.pi*random.random()
            })

    @property
    def values(self):
        return self._values
