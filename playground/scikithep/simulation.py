from __future__ import print_function
import path
import math

from skhep.simulation import pdgid
from phenomena.particles.particle import ParticleDT

if __name__ == '__main__':

    p = ParticleDT('p+')
    print(pdgid.hasFundamentalAnti(p.pdgid))
    #print(pdgid.hasUp(p.pdgid))
    #print(pdgid.hasDown(p.pdgid))
    #print(pdgid.isHadron(p.pdgid))
    #print(pdgid.isBaryon(p.pdgid))

    #print(pdgid.hasUp(-100213))


    # pdgid.isValid
    # print (pdgid.charge(-4444))
    # pdgid.threeCharge
    # pdgid.jSpin
    # pdgid.lSpin
    # pdgid.sSpin
    # pdgid.hasFundamentalAnti
    # pdgid.hasDown
    # pdgid.hasUp
    # pdgid.hasStrange
    # pdgid.hasCharm
    # pdgid.hasBottom
    # pdgid.hasTop
    # pdgid.isHadron
    # pdgid.isBaryon
    # pdgid.isMeson
    # pdgid.isLepton
