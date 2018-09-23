from __future__ import print_function
import path

from phenomena.particles.particle_boosted import ParticleBoosted

if __name__ == '__main__':
    pi = ParticleTest('pi0')
    print (pi.mass)
    print (pi.decay)
    print (pi.decay_time)
    print (pi.decayvalues)
