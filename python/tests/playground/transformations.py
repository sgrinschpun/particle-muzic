from __future__ import print_function, division
import sys
sys.path.append('../')
from context import phenomena

from phenomena.particles.transformations import TransformManager, ComptonEffect, PairProduction, Annihilation, InelasticCollision, Decay2, ElasticCollision
from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseParticle

if __name__ == '__main__':

    part4 = BubbleChamberParticle('e-', p=3)
    #part4bis = QuantumUniverseParticle('gamma', p=3)
    #print (InelasticCollision(part4).values)
    #print (Decay2(part4).values)
    #print (ElasticCollision(part4).values)
    #print (part4.transformation.allTypes)
    #print (part4.transformation.selectedType)
    print (part4.transformation.selectedChannel)


    #print (part4bis.transformation.allTypes)
    #print (part4bis.transformation.selectedType)
