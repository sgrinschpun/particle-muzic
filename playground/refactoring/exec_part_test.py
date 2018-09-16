from __future__ import print_function
import path

from phenomena.particles.particletest import ParticleTest

if __name__ == '__main__':
    pi = ParticleTest('W+')
    print (pi.mass)
    print (pi.decay)
