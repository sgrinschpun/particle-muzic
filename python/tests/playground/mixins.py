from __future__ import print_function, division
import sys
sys.path.append('../')
from context import phenomena

from phenomena.particles.models import BubbleChamberParticle
from phenomena.particles.server_particle import ServerParticle

if __name__ == '__main__':
    #pi = ParticleServer.init('pi+', p=1, phi=1.)
    #print (pi.mass)
    pi = BubbleChamberParticle('pi+', p=1, phi=1.)
    print (pi.mass)
    print (pi.pdgid)
    print (pi.composition)
