from __future__ import print_function
import path
import math

#from phenomena.particles.sources import ParticleDataSource, DataSource, ParticleDataToolFetcher, SciKitHEPFetcher, ExtraInfoFetcher
from phenomena.particles.sources import ParticleDataSource


if __name__ == '__main__':

    print (ParticleDataSource.getMass('e+'))
    print (ParticleDataSource.getPDGId('e+'))
    print (ParticleDataSource.getCharge('e+'))
    print (ParticleDataSource.getTau('mu+'))
    print (ParticleDataSource.getComposition('p+'))
    print (ParticleDataSource.getType('W+'))
