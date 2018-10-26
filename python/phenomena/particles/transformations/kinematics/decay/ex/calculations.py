from __future__ import division
import math

from phenomena.particles.sources import ParticleDataSource
from _2body import LAB2BodyCalc
from _3body import LAB3BodyCalc
from _4body import LAB4BodyCalc

class DecayCalc(object):
    """ Checks number of decay particles and assigns appropriate calculation.
        Creates aray of values:
            - masses = [m0, m1, m2,....mn]
            - values = [{'name':, 'p':, 'phi':, 'theta':},]
    """
    @staticmethod
    def _setMassArray(mass, decay):
        masses = [mass]  # array of masses 0: parent particle, 1: first decay particle, ...
        for particle in decay:
            masses.append(ParticleDataSource.getMass(particle))
        return masses

    @staticmethod
    def getValues(mass,gamma,phi,decay):
        masses = DecayCalc._setMassArray(mass, decay)
        values = []
        if len(decay) == 2:
            values = LAB2BodyCalc(decay,masses,phi,gamma).values
        elif len(decay) == 3:
            values = LAB3BodyCalc(decay,masses,phi,gamma).values
        else:
            values = LAB4BodyCalc(decay,masses,phi,gamma).values
        return values
