from __future__ import print_function
import path
import math

from phenomena.particles.particle_boosted import ParticleBoosted

if __name__ == '__main__':
    pi = ParticleBoosted('nu_mubar')
    print ("Decay Channels:  ", pi.decay)
    print ("Lifetime:  ", pi.lifetime)
    print ('Decay Time:   ',pi.decay_time)

    mu = ParticleBoosted('mu-')
    print ("Decay Channels:  ", mu.decay)
    print ("Lifetime:  ", mu.lifetime)
    print ('Decay Time:   ', mu.decay_time)

    nu1 = ParticleBoosted('nu_mubar')
    print ("Lifetime:  ", nu1.lifetime)
    print ('Decay Time:   ',nu1.decay_time)

    nu2 = ParticleBoosted('nu_ebar')
    print ("Lifetime:  ", nu2.lifetime)
    print ('Decay Time:   ',nu2.decay_time)

    nu3 = ParticleBoosted('nu_mu')
    print ("Lifetime:  ", nu3.lifetime)
    print ('Decay Time:   ',nu3.decay_time)

    e = ParticleBoosted('e-')
    print ("Lifetime:  ", e.lifetime)
    print ('Decay Time:   ',e.decay_time)
