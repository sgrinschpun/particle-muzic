from __future__ import division
import math, random

from skhep.constants import half_pi, two_pi

import nbody

class LAB4BodyCalc(nbody.LabCalc):

    def __init__(self, decay, masses,angles,gamma):
        self._values = []
        for part in decay:
            self._values.append({
            'name': part,
            'p': 5*random.random(),
            'phi': 2*math.pi*random.random(),
            'theta':half_pi,
            })

    @property
    def values(self):
        return self._values
