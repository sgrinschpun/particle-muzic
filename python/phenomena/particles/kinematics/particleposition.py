from skhep.math import Vector3D, LorentzVector

PARTICLE_INIT_POSITION = Vector3D(x=0.0, y=0.0, z=0.0)

class ParticlePosition(object):
    '''
    This is a mixin class for the Particle class
    It adds the attributes and methods related to the 4-dimensional Minkowski space-time vector of the particle as defined in the LorentzVector class of SciKitHEP
    '''

    @property
    def position(self):
        return self._position

    def _set_initPosition(self):
        self._position = LorentzVector.from3vector(PARTICLE_INIT_POSITION,0.)
