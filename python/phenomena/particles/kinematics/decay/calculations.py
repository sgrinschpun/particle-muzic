from __future__ import division
import math
import abc

from phenomena.particles.particle import ParticleDT
from phenomena.particles.kinematics.decay._2body import LAB2BodyCalc
from phenomena.particles.kinematics.decay._3body import LAB3BodyCalc

class DecayCalc(object):
    """ Checks number of decay particles and assigns appropriate calculation.
        Creates aray of values:
            - masses = [m0, m1, m2,....mn]
            - anglesCM = [theta0, theta1, theta2,....thetan]
            - values = [{'name':, 'p':, 'theta':},]
    """

    def __init__(self, mass, gamma, theta, decay, angles):
        self._gamma = gamma
        self._decay = decay
        self._setMassArray(mass,decay)
        self._setAnglesCMArray(theta,angles)

        self._setCalculation(self._decay, self._masses, self._anglesCM, self._gamma)

    def _setMassArray(self, mass, decay):
        masses = [mass]
        for particle in decay:
            masses.append(ParticleDT.getmass(particle))

        self._masses = masses

    def _setAnglesCMArray(self, theta, angles):
        anglesCM = []
        anglesCM.append(theta)
        for angle in angles:
            anglesCM.append(angle)

        self._anglesCM = anglesCM

    def _setCalculation(self, decay, masses, angles, gamma):
        if len(decay) == 2:
            self._values = LAB2BodyCalc(decay,masses,angles,gamma).values
        else:
            self._values = LAB3BodyCalc(decay,masses,angles,gamma).values  #change when 3ody is implemented

    @property
    def values(self):
        return self._values
