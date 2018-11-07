# Author: Cristobal Pio
# Company: IFAE
# Date: 4 November 2018
# Mail: cgarcia@ifae.es
# Information: 
from threading import Lock

from phenomena.particles.particle import Particle
from phenomena.particles import ServerParticle

class ParticleDecayTimer:
    def __init__(self, particle, decay_callback):
        self._decayCallback = decay_callback
        self._particle = particle
        self._particle.start(self._particleDecay)

    def _particleDecay(self):
        new_particles = self._particle.decayvalues   #changed
        self._decayCallback(self._particle, new_particles)

    def getParticle(self):
        return self._particle
    
class ParticleAccumulator:
    
    def __init__(self):
        self._particle_accumulator = []
        self._timers_available = []
        self._transform_lock = Lock()
    
    def addParticle(self, particle):
        assert issubclass(type(particle), Particle)
        print "Accumulating particle: {0}".format(particle.name)
        self._timers_available.append(ParticleDecayTimer(particle, self._decayedParticle))
        self._particle_accumulator.append(particle)

    def removeParticle(self, particle):
        assert issubclass(type(particle), Particle)
        rm_particles_timer = [particle_timer for particle_timer in self._timers_available if particle_timer.getParticle() == particle]
        for rm_particle_timer in rm_particles_timer:
            print "removing: ", rm_particle_timer.getParticle().name
            self._timers_available.remove(rm_particle_timer)
        print "Values inside: ", len(self._timers_available)

    def transformParticle(self, particle, new_particles):
        assert issubclass(type(particle), Particle)
        assert isinstance(new_particles, list)
        for new_particle in new_particles:
            self.addParticle(new_particle)
        self.removeParticle(particle)

    def _decayedParticle(self, particle, new_particles):
        self._transform_lock.acquire()
        tr_new_particles = []
        try:
            for new_particle in new_particles:
                name = new_particle['name']
                kwargs = {'phi': new_particle['phi'], 'theta': new_particle['theta'], 'p': new_particle['p']}
                print "Particle causes error:  " + name
                tr_new_particles.append(ServerParticle.init(name, parent = particle.id, **kwargs))
            print " New particles: "
            for new_particle in new_particles: print new_particle['name'], new_particle['p'], new_particle['phi']
            self.transformParticle(particle, tr_new_particles)
        finally:
            self._transform_lock.release()

    def getActualFrame(self):
        self._transform_lock.acquire()
        actual_particles_list = []
        for particle in self._particle_accumulator:
            actual_particles_list.append(particle.toDictionary())
        self._transform_lock.release()
