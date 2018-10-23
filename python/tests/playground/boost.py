from __future__ import print_function, division
import sys
sys.path.append('../')
from context import phenomena

from math import sqrt

from phenomena.particles.models import BubbleChamberParticle, UndercoverParticle
from phenomena.particles.sources import ParticleDataSource, ParticleDataToolFetcher
from skhep.math import Vector3D, LorentzVector
from skhep.math  import Kallen_function
from skhep.units import MeV, GeV





if __name__ == '__main__':
    pi = BubbleChamberParticle('pi-', p=1)
    p =  UndercoverParticle('p+')
    theboost = pi.fourMomentum.boostvector
    # print (pi.fourMomentum)
    # print (p.fourMomentum)
    # print (theboost)
    # print (theboost/2)
    # piCM = pi.fourMomentum.boost(theboost/2)
    # pCM = p.fourMomentum.boost(theboost/2)
    # print (piCM)
    # print (pCM)
    # print (piCM.vector.isantiparallel(pCM.vector))

    piCM = pi.fourMomentum.boost(theboost)
    decaylist= ParticleDataToolFetcher.getDecayParticles('pi-')[0]

    M = pi.mass
    m1 = ParticleDataSource.getMass(decaylist[0])
    m2 = ParticleDataSource.getMass(decaylist[1])

    p = sqrt( Kallen_function( M**2, m1**2, m2**2 ) ) / (2*M)

    print (p / GeV)

    for decay:
    method (particle: 4momentum + decay) -> [undercover1, undercover2,...]

    for collision:
    method (particle: 4momentum + target + trasnformation) -> [undercover1, undercover2,...]
