from __future__ import print_function
import path

#from phenomena.particles.particle import ParticleDT
from phenomena.particles.particle_boosted import ParticleBoosted

if __name__ == '__main__':
    pi = ParticleBoosted('pi+', theta=3, p=1)
    print (pi.decayvalues)
