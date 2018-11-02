#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division
import sys
sys.path.append('../')
from context import phenomena

from phenomena.particles.models import BubbleChamberParticle
from phenomena.particles.transformations.types import InelasticData


if __name__ == '__main__':

    pi = BubbleChamberParticle('pi-',p=10)

    #print (pi.transformation.allTypes)
    #print (pi.transformation.selectedType)
    print (pi.transformation.selectedType)
    #print (pi.transformation.selectedChannel)
    print (pi.transformation.output)






    #print(InelasticData.energyCutParticles('pi-', 'p+', 0.7))
