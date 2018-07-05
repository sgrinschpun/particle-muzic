from __future__ import print_function
import sys
import unittest
import numpy as np

python_path = 'C:\Users\Santi\Documents\IFAE\particle-muzic-boosted\python'
sys.path.append(python_path)

from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.particle import ParticleDT



class MyTest(unittest.TestCase):
    def test(self, pi):
        self.pi = ParticleBoosted('pi+', theta=3, p=1)
        self.p = [self.pi.p]
        for moment in self.pi.decayvalues:
            self.p.append(moment['p'])

        self.theta = [self.pi.theta]
        for angle in self.pi.decayvalues:
            self.theta.append(angle['theta'])

        self.E = [self.pi.E]
        for energy in self.pi.decayvalues:
            self.E.append(energy['E'])

        self.px = self.p * np.cos(self.theta)
        self.py = self.p * np.sin(self.theta)

        self.assertEqual(round(sum(self.px[1:]), 5), round(self.px[0], 5))
        self.assertEqual(round(sum(self.py[1:]), 5), round(self.py[0], 5))
        self.assertEqual(round(sum(self.E[1:]), 5), round(self.E[0], 5))

unittest.main(pi1)
