from __future__ import print_function
import path
import math

from phenomena.particles.particle_boosted import ParticleBoosted

if __name__ == '__main__':
    #pi = ParticleBoosted('pi+', theta=3, p=1)
    K = ParticleBoosted('K+', p=0.05)
    print ("Lifetime:  ", K.lifetime)
    print ('Decay Time:   ',K.decay_time)
