#!/usr/bin/env python

__author__ = "Cristobal Pio"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "cgarcia@ifae.es"
__status__ = "Development"

import abc
from threading import Timer, Lock

from particle import Particle, ParticleDT
from nodes import get_save_node, Node


class ParticleDecayTimer:
    def __init__(self, particle, decay_callback):
        self._decayCallback = decay_callback
        self._particle = particle
        t = Timer(2, self._particleDecay)
        t.start()

    def _particleDecay(self):
        new_particles = self._particle.decay()
        self._decayCallback(self._particle, new_particles)

    def getParticle(self):
        return self._particle

class ParticleAction(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getIdentifier(self):
        pass

    @abc.abstractmethod
    def addParticle(self, particle):
        pass

    @abc.abstractmethod
    def removeParticle(self, particle):
        pass

    @abc.abstractmethod
    def transformParticle(self, particle, new_particles):
        pass

class ParticleActionNode(ParticleAction, Node):
    pass

# Fixed Particles Nodes

class ParticleAccumulatorNode(ParticleActionNode):

    def __init__(self):
        self._node = get_save_node()
        self._particles_available = []
        self._transform_lock = Lock()

    # Here Particles are accumulated and waiting to decay
    def addParticle(self, particle):
        assert issubclass(type(particle), Particle)
        print "Accumulating particle: {0}".format(particle.getName())
        self._particles_available.append(ParticleDecayTimer(particle, self._decayedParticle))

    def removeParticle(self, particle):
        assert issubclass(type(particle), Particle)
        rm_particles_timer = [particle_timer for particle_timer in self._particles_available if particle_timer.getParticle() == particle]
        for rm_particle_timer in rm_particles_timer:
            print "removing: ", rm_particle_timer.getParticle().getName()
            self._particles_available.remove(rm_particle_timer)
        print "Values inside: ", len(self._particles_available)

    def transformParticle(self, particle, new_particles):
        assert issubclass(type(particle), Particle)
        assert isinstance(new_particles, list)
        for new_particle in new_particles:
            self.addParticle(new_particle)
        self.removeParticle(particle)

    def _decayedParticle(self, particle, new_particles):
        self._transform_lock.acquire()
        try:
            print "particle: {0}".format(particle.getName()),
            print "Will transform in: ",
            for new_particle in new_particles:
                print "{0} ".format(new_particle.getName()),
            print ""
            self._node.getNextNode(self).transformParticle(particle, new_particles)
        finally:
            self._transform_lock.release()

    def getIdentifier(self):
        return "ParticleAccumulatorNode"

    def setNextNode(self, n_node):
        self._node.setNextNode(n_node)

    def setPastNode(self, p_node):
        self._node.setPastNode(p_node)

class ParticleEntryNode(ParticleActionNode):

    def __init__(self):
        self._node = get_save_node()

    def addParticle(self, particle):
        assert issubclass(type(particle), Particle)
        print "Entrying particle: {0}".format(particle.getName())
        self._node.getNextNode(self).addParticle(particle)

    def removeParticle(self, particle):
        assert issubclass(type(particle), Particle)

    def transformParticle(self, particle, new_particles):
        assert issubclass(type(particle), Particle)
        assert isinstance(new_particles, list)
        self._node.getNextNode(self).transformParticle(particle, new_particles)

    def getIdentifier(self):
        return "ParticleEntryNode"

    def setNextNode(self, n_node):
        self._node.setNextNode(self, n_node)

    def setPastNode(self, p_node):
        self._node.setPastNode(self, p_node)

if __name__ == '__main__':
    a = ParticleAccumulatorNode()
    a.transformParticle(ParticleDT("e+"), [])
