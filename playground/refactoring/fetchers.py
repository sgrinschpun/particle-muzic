from __future__ import print_function
import path
import math

from phenomena.particles.sources import ParticleDataSource

from decaylanguage.particle import Particle

if __name__ == '__main__':

    #print (ParticleDataSource.getMass('e+'))
    #print (ParticleDataSource.getPDGId('e+'))
    #print (ParticleDataSource.getCharge('e+'))
    #print (ParticleDataSource.getTau('mu+'))
    print (ParticleDataSource.getComposition('pi0'))
    #print (ParticleDataSource.getCharge('mu+'))
    #print (ParticleDataSource.getAnti('K+'))



    pi = Particle.from_pdgid(ParticleDataSource.getPDGId('pi+'))
    #print (pi.quarks)
    #print (list(Particle.from_pdgid(211).quarks))
    #print (pi.spin_type.name)
    print (pi.status.name)
