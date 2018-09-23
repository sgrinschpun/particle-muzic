from __future__ import print_function
import path
import math

from phenomena.particles.sources import ParticleDataSource
from phenomena.particles.sources import ParticleDataToolFetcher, SciKitHEPFetcher, ExtraInfoFetcher, DecayLanguageFetcher

from decaylanguage.particle import Particle

if __name__ == '__main__':
    print (ParticleDataSource.getName(-223))

    #print (ParticleDataSource.getMass('p-'))
    #print (ParticleDataSource.getPDGId('p-'))

    #print (ExtraInfoFetcher.getType(83))


    #print (ParticleDataSource.getMass('e+'))
    #print (ParticleDataSource.getPDGId('e+'))
    #print (ParticleDataSource.getCharge('e+'))
    #print (ParticleDataSource.getTau('mu+'))
    #print (ParticleDataSource.getComposition('pi0'))
    #print (ParticleDataSource.getCharge('mu+'))
    #print (ParticleDataSource.getAnti('K+'))



    #pi = Particle.from_pdgid(ParticleDataSource.getPDGId('pi+'))
    #print (pi.quarks)
    #print (list(Particle.from_pdgid(211).quarks))
    #print (pi.spin_type.name)
    #print (pi.status.name)
