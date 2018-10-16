from __future__ import print_function, division
import math
import path

from phenomena.particles.models import BubbleChamberParticle
from phenomena.particles.particle_server import ParticleServer

if __name__ == '__main__':
    #pi = ParticleServer.init('pi+', p=1, phi=1.)
    #print (pi.mass)
    pi = BubbleChamberParticle('pi+', p=1, phi=1.)
    print (pi.mass)
