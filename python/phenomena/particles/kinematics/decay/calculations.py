from __future__ import division
import math
import abc
import collections
import six

from phenomena.particles.particle import ParticleDT
from phenomena.particles.kinematics.decay._2body import LAB2BodyCalc
from phenomena.particles.kinematics.decay._3body import LAB3BodyCalc
from phenomena.particles.kinematics.decay._4body import LAB4BodyCalc

class DecayCalc(object):
    """ Checks number of decay particles and assigns appropriate calculation.
        Creates aray of values:
            - masses = [m0, m1, m2,....mn]
            - values = [{'name':, 'p':, 'theta':},]
    """

    def __init__(self, mass, gamma, theta, decay):
        self._gamma = gamma
        self._decay = decay
        self._setMassArray(mass,decay)
        self._theta = theta

        self._setCalculation(self._decay, self._masses, self._theta, self._gamma)

    def _setMassArray(self, mass, decay):
        masses = [mass]  # array of masses 0: parent particle, 1: first decay particle, ...
        for particle in decay:
            if isinstance(particle, collections.Mapping):
                masses.append(particle['mass'])
            elif isinstance(particle, six.string_types):
                masses.append(ParticleDT.getmass(particle))

        self._masses = masses

    def _setCalculation(self, decay, masses, theta, gamma):
        if len(decay) == 2:
            self._values = LAB2BodyCalc(decay,masses,theta,gamma).values
        elif len(decay) == 3:
            self._values = LAB3BodyCalc(decay,masses,theta,gamma).values
        else:
            self._values = LAB4BodyCalc(decay,masses,theta,gamma).values


    @property
    def values(self):
        return self._values
