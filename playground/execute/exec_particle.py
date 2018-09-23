from __future__ import print_function
import path
import math

from phenomena.particles.particle_boosted import ParticleBoosted

if __name__ == '__main__':
    #pi = ParticleBoosted('pi+', theta=3, p=1)
    mu = ParticleBoosted('mu-')
    #print (pi.decay)
    pl_out = 0.
    for part in mu.decayvalues:
        pl_out += part['p']*math.cos(part['theta'])
    print (mu.decayvalues)
    print (round(mu.p*math.cos(mu.theta),6))
    print (round(pl_out,6))
