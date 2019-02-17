#!/usr/bin/env python

from __future__ import print_function

__author__ = "Cristobal Pio"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "cgarcia@ifae.es"
__status__ = "Development"

import abc
from threading import Timer, Lock

from particle import Particle
from server_particle import ServerParticle
from phenomena.nodes import get_save_node, ConfigurableNode


class ParticleDecayTimer:
    def __init__(self, particle, transform_callback):
        self._transformCallback = transform_callback
        self._particle = particle
        self._particle.start(self._particleTransform)

    def _particleTransform(self):
        new_particles = self._particle.transformation.output   #changed
        self._transformCallback(self._particle, new_particles)

    def getParticle(self):
        return self._particle

class ParticleAction(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def addParticle(self, particle):
        pass

    @abc.abstractmethod
    def removeParticle(self, particle):
        pass

    @abc.abstractmethod
    def transformParticle(self, particle, new_particles):
        pass

class ParticleActionNodeEnd(ParticleAction, ConfigurableNode):


    def __init__(self):
        self._node = get_save_node()

    def findModule(self, module_path):
        if (module_path == self.getIdentifier()):
            return self
        raise Exception("Module Not found!")

    def setNextNode(self, n_node):
        self._node.setNextNode(n_node)


    def setPastNode(self, p_node):
        self._node.setPastNode(p_node)


class ParticleActionNodeChain(ParticleAction, ConfigurableNode):


    def __init__(self):
        self._node = get_save_node()

    def findModule(self, module_path):
        if(module_path == self.getIdentifier()): return self
        else: self._node.findModule(module_path)


    def setNextNode(self, n_node):
        self._node.setNextNode(n_node)


    def setPastNode(self, p_node):
        self._node.setPastNode(p_node)


# Fixed Particles Nodes

class ParticleAccumulatorNode(ParticleActionNodeChain):

    def __init__(self):
        ParticleActionNodeChain.__init__(self)
        self._particles_available = []
        self._transform_lock = Lock()

    # Here Particles are accumulated and waiting to decay
    def addParticle(self, particle):
        assert issubclass(type(particle), Particle)
        print ("Accumulating particle: {0}".format(particle.name))
        self._particles_available.append(ParticleDecayTimer(particle, self._transformedParticle))

    def removeParticle(self, particle):
        assert issubclass(type(particle), Particle)
        rm_particles_timer = [particle_timer for particle_timer in self._particles_available if particle_timer.getParticle() == particle]
        for rm_particle_timer in rm_particles_timer:
            print ("removing: ", rm_particle_timer.getParticle().name)
            self._particles_available.remove(rm_particle_timer)
        print ("Values inside: ", len(self._particles_available))

    def transformParticle(self, particle, new_particles):
        assert issubclass(type(particle), Particle)
        assert isinstance(new_particles, list)
        for new_particle in new_particles:
            self.addParticle(new_particle)
        self.removeParticle(particle)

    def _transformedParticle(self, particle, new_particles):
        self._transform_lock.acquire()
        tr_new_particles = []
        try:
            print ("particle: {0}".format(particle.name)),
            print ("Will transform in: "),
            for new_particle in new_particles:
                print ("Particle causes error:  " + new_particle.name)
                tr_new_particles.append(ServerParticle.fromparticle(new_particle, parent = particle.id))
            print (" New particles: ")
            for new_particle in new_particles: print (new_particle.name, new_particle.p, new_particle.phi, new_particle.theta)
            self._node.getNextNode(self).transformParticle(particle, tr_new_particles)
        finally:
            self._transform_lock.release()

    #def findModule(self, module_path):
    #    if (module_path == self._identifier):
    #        return self
    #    else:
    #        next_module_path = module_path.split(' ', 1)
    #        if (len(next_module_path) == 1): raise Exception("Module Not found!")
    #        self._root_node.findModule(next_module_path[1])

    def getIdentifier(self):
        return "accumulator"

    def execute(self, incoming_message):
        pass

class ParticleEntryNode(ParticleActionNodeEnd):

    def __init__(self):
        super(ParticleActionNodeEnd, self).__init__()
        self._node = get_save_node()

    def addParticle(self, particle):
        assert issubclass(type(particle), Particle)
        self._node.getNextNode(self).addParticle(particle)

    def removeParticle(self, particle):
        assert issubclass(type(particle), Particle)

    def transformParticle(self, particle, new_particles):
        assert issubclass(type(particle), Particle)
        assert isinstance(new_particles, list)
        self._node.getNextNode(self).transformParticle(particle, new_particles)

    def getIdentifier(self):
        return "entry"

    def setNextNode(self, n_node):
        self._node.setNextNode(self, n_node)

    def setPastNode(self, p_node):
        self._node.setPastNode(self, p_node)

    def execute(self, incoming_message):
        pass

if __name__ == '__main__':
    pass
