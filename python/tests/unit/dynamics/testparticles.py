from phenomena.particles.particle import Particle
from phenomena.particles.mixins import ParticleId, NO_PARENT, ParticleData, ParticlePosition, ParticleBoost, ParticleTransformation
from phenomena.particles.dynamics import DynamicsController, KinematicsController
from phenomena.particles.dynamics.dynamicscontroller import MagneticField, ElectricField, Ionization

class TestParticleDynamics(ParticlePosition, ParticleBoost, ParticleData):

    DynamicsList = [MagneticField]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        #### ParticleData
        self._set_name(name)  # Name of the particle
        self._set_mass() # Mass of the particle in GeV
        self._set_charge() # Charge of the particle
        #### ParticleBoost
        self._set_fourMomentum(kwargs)#assign 4momentum vector and  boosted parameters
        #### ParticlePosition
        self._set_initPosition()
        self._set_kinematics()

class MagneticParticle(TestParticleDynamics):

    DynamicsList = [MagneticField]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(MagneticParticle, self).__init__(name, parent = NO_PARENT, **kwargs)
        self._set_dynamics(MagneticParticle.DynamicsList)

class ElectricParticle(TestParticleDynamics):

    DynamicsList = [ElectricField]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(ElectricParticle, self).__init__(name, parent = NO_PARENT, **kwargs)
        self._set_dynamics(ElectricParticle.DynamicsList)

class IonizationParticle(TestParticleDynamics):

    DynamicsList = [Ionization]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(IonizationParticle, self).__init__(name, parent = NO_PARENT, **kwargs)
        self._set_dynamics(IonizationParticle.DynamicsList)
