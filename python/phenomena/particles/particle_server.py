from particle_boosted import ParticleBoosted

NO_PARENT = -1

class ParticleServer(object):
    '''
    Class used in the server to create particle instances
    This class helps changing which class to use
    '''
    PARTICLE = ParticleBoosted

    @staticmethod
    def init (name, parent = NO_PARENT, **kwargs):
        return ParticleServer.PARTICLE(name, parent, **kwargs)
