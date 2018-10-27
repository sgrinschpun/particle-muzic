from __future__ import print_function, division
import sys
sys.path.append('../')
from context import phenomena

from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseParticle
from phenomena.particles.transformations.kinematics import ElasticKinematics, InelasticKinematics, DecayKinematics
from phenomena.particles.transformations.kinematics import KinematicsController

from skhep import units as u

import math
import random



if __name__ == '__main__':

    pi = QuantumUniverseParticle('pi-', p=1)

    print(pi.transformation.selectedType)
    print(pi.transformation.time)
    print(pi.transformation.output)




    # dt = 1/60
    # time = 2
    # for i in range(int(time/dt)):
    #     print (pi.transformation.query(1./60.))
