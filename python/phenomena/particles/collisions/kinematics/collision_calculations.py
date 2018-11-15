from __future__ import division, print_function
import math
import abc
import collections
import six

from phenomena.particles.sources import ParticleDataSource
from phenomena.particles.collisions.kinematics._2bodycollision import Lab2ColCalc, CM2ColCalc


# Fetches de masses of incoming particles in PDG data and manages the calculation for a collision. Only 2-body collision is implemented
class CollisionCalc(object):
    """ Checks number of collision particles and assigns appropriate calculation.
        Creates array of values:
            - masses of incoming particles = [m0, m1, m2,....mn]
            - values of outgoing particle = [{'name':, 'p':, 'theta':},]
    """

    def __init__(self, particles, *args):

        self._setMassArray(particles)

        self._setCalculation(particles, self._masses, *args)


    def _setMassArray(self,particles):
        masses = []  # array of masses for incoming particles
        for particle in particles:
            if isinstance(particle, collections.Mapping):
                masses.append(particle['mass'])
            elif isinstance(particle, six.string_types):
                masses.append(ParticleDT.getmass(particle))

        self._masses = masses

    def _setCalculation(self, particles, masses, *args):
        if len(particles) == 2:
            if len(args) == 2:
                self._values = Lab2ColCalc(particles,args[0],args[1],masses).values
            else:
                self._values = CM2ColCalc(particles,args[0],masses).values
        else:
            print('3 body collisions have not been implemented')

    @property
    def values(self):
        return self._values
