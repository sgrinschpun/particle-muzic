from __future__ import print_function
import path

from phenomena.particles.particletest import ParticleTest

if __name__ == '__main__':
    pi = ParticleTest('pi0')
    print (pi.mass)
    print (pi.decay)
    print (pi.decay_time)
    print (pi.decayvalues)
