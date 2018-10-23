from __future__ import print_function, division
import sys
sys.path.append('../')
from context import phenomena

from phenomena.particles.transformations import TransformManager, ComptonEffect, PairProduction, Annihilation, InelasticCollision, Decay2, ElasticCollision
from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseParticle

from phenomena.particles.sources import ParticleDataSource, ParticleDataToolFetcher

from phenomena.particles.transformations.types.inelastic import InelasticFile, InelasticData


if __name__ == '__main__':
    part = BubbleChamberParticle('pi+', p=3)

    for id, item in enumerate(ParticleDataToolFetcher.getOriginParticles(['pi-','p+'])):
        print (id, item[1][0])
        print (ParticleDataToolFetcher.getDecayParticles(item[1][0]))


    #ParticleDataToolFetcher.getOriginParticles


    #print(ParticleDataSource.getDecayChannels('pi+'))
    #print(ParticleDataToolFetcher.getDecayChannelsWithNames('pi+'))
    #print(ParticleDataToolFetcher.getDecayParticles('pi+'))
    #print(ParticleDataToolFetcher.getOriginParticles(['pi-','p+']))
    #for id, item in enumerate(ParticleDataToolFetcher.getOriginParticles(['K-','p+'])):
    #    print (id, item[1][0])
    #    print (ParticleDataToolFetcher.getDecayParticles(item[1][0]))
    #print(InelasticData.allParticles('pi-','p+'))
