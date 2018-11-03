#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division
import sys
sys.path.append('../')
from context import phenomena

from phenomena.particles.models import BubbleChamberParticle
from phenomena.particles.transformations.types import InelasticData
from phenomena.particles.transformations.kinematics import LAB2BodyInelastic
from skhep.math  import Kallen_function, Vector3D, LorentzVector
from skhep.units import MeV, GeV


if __name__ == '__main__':

    pi = BubbleChamberParticle('pi-',p=2)

    print (pi.transformation.allTypes)
    # p = BubbleChamberParticle('p+')
    #
    # pi0 = BubbleChamberParticle('pi0')
    # n0 = BubbleChamberParticle('Sigma_c++')
    #
    # twobody = LAB2BodyInelastic(pi, p, [pi0,n0])
    # new1 = twobody._finalparticlesLAB[0].fourMomentum
    # new2 = twobody._finalparticlesLAB[1].fourMomentum
    #
    # print (new1.e+new2.e)
    #
    # print (pi.fourMomentum.e + p.fourMomentum.e)
    #
    # print (twobody._finalparticlesLAB[0].E+twobody._finalparticlesLAB[1].E)
