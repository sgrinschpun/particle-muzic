from __future__ import print_function
import path

from phenomena.particles.transformations import TransformManager, ComptonEffect, PairProduction, Annihilation, InelasticCollision, Decay2, ElasticCollision
from phenomena.particles.models import BubbleChamberParticle

from phenomena.particles.transformations.types.inelastic import InelasticFile, InelasticData

if __name__ == '__main__':
    #list1 = InelasticData.allParticles("pi-",'p+')
    # list2 = InelasticData.energyCutParticles("pi-",'p+', 1)
    # probabilitysum = InelasticData.ProbabilitySum("pi-",'p+', 2)
    #print (list1)
    # print(BubbleChamberParticle('pi+').decay_channels)
    #InelasticFile.save_json()
    # part1 = BubbleChamberParticle('gamma', p=1)
    # print (ComptonEffect(part1).values)
    # print (PairProduction(part1).values)
    #
    # part2 = BubbleChamberParticle('mu-')
    # print (ComptonEffect(part2).values)
    # print (PairProduction(part2).values)
    # print (Annihilation(part2).values)
    #
    # part3 = BubbleChamberParticle('e+')
    # print (Annihilation(part3).values)
    # print (ComptonEffect(part3).values)
    # print (PairProduction(part3).values)

    part4 = BubbleChamberParticle('e+', p=3)
    #print (InelasticCollision(part4).values)
    #print (Decay2(part4).values)
    #print (ElasticCollision(part4).values)
    print (TransformManager(part4).allTransformations)
