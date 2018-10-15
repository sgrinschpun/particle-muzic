from __future__ import print_function, division
import math
import path

from phenomena.particles.particletest import ParticleTest
from phenomena.particles.particle_boosted import ParticleBoosted

if __name__ == '__main__':
    pi = ParticleBoosted('pi+', p=1, phi=1.)
    print (pi.fourMomentum)
    print (pi.decayvalues)
    mu = ParticleBoosted('mu+', p=1)
    print (mu.decayvalues)
    gamma = ParticleBoosted('gamma', p=1)
