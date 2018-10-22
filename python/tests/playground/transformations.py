from __future__ import print_function, division
import sys
sys.path.append('../')
from context import phenomena

from phenomena.particles.transformations import TransformManager, ComptonEffect, PairProduction, Annihilation, InelasticCollision, Decay2, ElasticCollision
from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseParticle

if __name__ == '__main__':

    part4 = BubbleChamberParticle('K-', p=3)
    print (part4.transformation.allTypes)
