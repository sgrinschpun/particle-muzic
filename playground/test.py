from __future__ import print_function
import sys
import unittest
import numpy as np

python_path = 'C:\Users\Santi\Documents\GitHub\particle-muzic\python'
sys.path.append(python_path)

from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.particle import ParticleDT



class MyTest(unittest.TestCase):
    def test(self):
        part = ParticleBoosted('mu+', theta=3, p=1)
        p = [part.p]
        for moment in part.decayvalues:
            p.append(moment['p'])

        theta = [part.theta]
        for angle in part.decayvalues:
            theta.append(angle['theta'])

        E = [part.E]
        for energy in part.decayvalues:
            E.append(energy['E'])

        px = p * np.sin(theta)
        py = p * np.cos(theta)

        #self.assertEqual(round(sum(self.px[1:]), 5), round(self.px[0], 5))
        self.assertEqual(round(sum(py[1:]), 5), round(py[0], 5))
        self.assertEqual(round(sum(E[1:]), 5), round(E[0], 5))

unittest.main()
