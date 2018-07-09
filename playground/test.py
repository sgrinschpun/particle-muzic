from __future__ import print_function
import sys
import unittest
import numpy as np

python_path = 'C:\Users\Santi\Documents\GitHub\particle-muzic\python'
sys.path.append(python_path)

from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.particle import ParticleDT

#Santi was here

class MyTest(unittest.TestCase):
    def test(self):
        part = ParticleBoosted('pi+')
        p = [part.p]
        for moment in part.decayvalues:
            p.append(moment['p'])

        theta = [part.theta]
        for angle in part.decayvalues:
            theta.append(angle['theta'])

        E = [part.E]
        for energy in part.decayvalues:
            E.append(energy['E'])

        px = p * np.cos(theta)
        py = p * np.sin(theta)

#        print(p)
#        print(theta)
#        print(px)
#        print(py)
#        print(E)
#        print('\n')
#        print(round(px[0], 5) - round(sum(px[1:]), 5))
#        print(round(py[0], 5) - round(sum(py[1:]), 5))

        self.assertEqual(round(sum(px[1:]), 5), round(px[0], 5))
        self.assertEqual(round(sum(py[1:]), 5), round(py[0], 5))
        self.assertEqual(round(sum(E[1:]), 5), round(E[0], 5))

unittest.main()
