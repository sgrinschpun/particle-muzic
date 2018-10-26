from __future__ import print_function
import sys
sys.path.append('../')
from context import phenomena

from phenomena.particles.models import BubbleChamberParticle
from phenomena.particles.transformations.kinematics import ElasticKinematics, InelasticKinematics, DecayKinematics
from phenomena.particles.transformations.kinematics import KinematicsController

if __name__ == '__main__':

    pi = BubbleChamberParticle('pi-')

    print (pi.transformation.selectedType)
    print (pi.transformation.time)
    for particle in pi.transformation.output:
        print (particle.name, particle.fourMomentum)
