from __future__ import division
import path
import bisect
import random

from phenomena.particles.sources import ParticleDataSource

class eeOutput(object):

    particlesid =  [443, 100443, 30443, 9000443, 9010443, 9020443]
    particles = ['J/psi', 'psi(2S)', 'psi(3770)']
    particles_mass = map(ParticleDataSource.getMass,particles)

    def __init__(self, energy):
        self._energy = energy
        self._interval = bisect.bisect_left(eeOutput.particles_mass, energy)
        self._prob = 0
        self._choosepart()

    def _choosepart(self):
        if self._interval == 0:
            result = eeOutput.particles[0]
        elif self._interval >= len(eeOutput.particles):
            result = eeOutput.particles[-1]
        else:
            thisrange = eeOutput.particles_mass[self._interval]-eeOutput.particles_mass[self._interval-1]
            thisvalue = self._energy - eeOutput.particles_mass[self._interval-1]
            self._prob = round(thisvalue/thisrange,2)
            x = random.uniform(0, 1)
            if x >= self._prob:
                result = eeOutput.particles[self._interval-1]
            else:
                result = eeOutput.particles[self._interval]
        self._chosenparticle = result

    @property
    def particle(self):
        return self._chosenparticle

if __name__ == '__main__':
    print eeOutput.particles_mass
    energies = [1,3.0,3.09692,3.2,3.6,3.68611,3.7,3.77315,4.0]
    for energy in energies:
        output = eeOutput(energy)
        print output.particle, ' with energy ', output._energy, output._interval, output._prob
