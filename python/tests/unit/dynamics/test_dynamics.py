import copy
import pytest
from testparticles import MagneticParticle, ElectricParticle, IonizationParticle
from phenomena.particles.models import UndercoverParticle
from phenomena.particles.dynamics import DynamicsController, KinematicsController
from phenomena.particles.dynamics.dynamicscontroller import DynamicType, MagneticField, ElectricField, Ionization
from skhep.math  import Vector3D, LorentzVector

dt = 1

undercover_particles = [(UndercoverParticle("pi-", p=1.0))]
magnetic_particles = [(MagneticParticle("pi-", p=1.0))]

@pytest.mark.parametrize("particle",undercover_particles)
def test_MagneticField_DynamicType(particle):
    Field = MagneticField(particle)
    assert isinstance(Field, DynamicType)
    acceleration = Field.getAcceleration(dt)
    velocity = particle.fourMomentum.vector
    assert isinstance(acceleration, Vector3D)
    assert acceleration.isperpendicular(velocity)
    #test of the direction depending on the charge

@pytest.mark.parametrize("particle",undercover_particles)
def test_MagneticField_Controllers(particle):
    DC = DynamicsController(particle,[MagneticField])
    assert isinstance(DC, object)
    acceleration = DC.updateAcceleration(dt)
    velocity0 = copy.deepcopy(particle.fourMomentum.vector)
    assert isinstance(acceleration, Vector3D)
    assert acceleration.isperpendicular(velocity0)

    KC = KinematicsController(particle)
    assert isinstance(KC, object)
    KC.updateFourMomentum(acceleration, dt)
    velocity1 = particle.fourMomentum.vector
    assert velocity1 != velocity0
    position = KC.getPosition(velocity1)
    assert isinstance(position, Vector3D)

@pytest.mark.parametrize("particle",undercover_particles)
def test_Ionization(particle):
    IonizationObject = Ionization(particle)
    assert isinstance(IonizationObject, DynamicType)
    acceleration = IonizationObject.getAcceleration(dt)
    velocity0 = copy.deepcopy(particle.fourMomentum.vector)
    assert isinstance(acceleration, Vector3D)
    assert acceleration.isantiparallel(velocity)


@pytest.mark.parametrize("particle",undercover_particles)
def test_Ionization_Controllers(particle):
    DC = DynamicsController(particle,[Ionization])
    assert isinstance(DC, object)
    acceleration = DC.updateAcceleration(dt)
    velocity = particle.fourMomentum.vector
    assert isinstance(acceleration, Vector3D)
    assert acceleration.isantiparallel(velocity0)
