from __future__ import print_function, division
import math
import path

from phenomena.particles.particletest import ParticleTest

if __name__ == '__main__':
    pi = ParticleTest('pi+', p=1)
    print (pi.fourMomentum)
    print (pi.position)
    print (pi.decayvalues)
    mu = ParticleTest('mu+', p=1)
    print (mu.decayvalues)
