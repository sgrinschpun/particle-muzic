from __future__ import print_function
import sys
sys.path.append('../')
from context import phenomena

from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseParticle

if __name__ == '__main__':

    part = BubbleChamberParticle('K+', p=1)

    print (part.decay_channels)
    #print (part.transformation.selectedType)
    #print (part.transformation.selectedChannel)
    #print (part.transformation.outputValues)

    #print (part.transformation.selectedChannelValues)
    #print (part.transformation.outputValues)
    #print (part.transformation.selectedType)
