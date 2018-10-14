from setdecay import Decay
from timeremap import TimeRemap
from phenomena.particles.particle import Particle

class ParticleDecay(object):
    '''
    This is a mixin class for the ParticleBoosted class
    It adds the attributes and methods related to particle decays
     - selects and sets particle decay channel
     - sets the time of next decay
     - includes de start method that is used by the particle server
    The ParticleDecay requires the ParticleData mixin.
    '''

    @property
    def decay(self):
        return self._decay

    def _set_decay(self):
        self._decay = Decay.set(self._decay_channels)

    @property
    def decay_time(self):
        return self._decay_time

    def _set_decay_time(self):
        if self._lifetime != Particle.STABLE :
            self._decay_time = TimeRemap.getNextDecayTime(self._lifetime)
        else:
            self._decay_time = Particle.STABLE

    def start(self, callback):
        if self._decay_time != Particle.STABLE:
            wait_time = TimeRemap.renormalize(self._decay_time)
            print "Wait for: ", wait_time
            threading.Timer(wait_time, callback).start()
        else:
            print "Wait for: ", 10
            threading.Timer(10, callback).start()
