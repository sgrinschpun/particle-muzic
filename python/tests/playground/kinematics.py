from __future__ import print_function, division
import sys
sys.path.append('../')
from context import phenomena

from phenomena.particles.models import BubbleChamberParticle
from phenomena.particles.transformations.kinematics import ElasticKinematics, InelasticKinematics, DecayKinematics
from phenomena.particles.transformations.kinematics import KinematicsController

from skhep import units as u

import math
import random



if __name__ == '__main__':

    pi = BubbleChamberParticle('pi-', p=0.5)

    for i in range(100):
        print (pi.transformation.query(1./60.))
    #print (random.shuffle(pi.transformation._transformationlist))
    #print (pi.transformation.allTypes)
    #print (pi.transformation.selectedChannel)

    #print(pi.transformation.query())

    #print (pi.transformation.selectedType)
    #print (pi.transformation.time)
    #for particle in pi.transformation.output:
    #    print (particle.name, particle.fourMomentum)
