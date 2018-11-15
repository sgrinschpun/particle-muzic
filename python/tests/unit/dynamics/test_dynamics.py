import copy
import pytest
from testparticles import MagneticParticle, ElectricParticle, IonizationParticle
from phenomena.particles.models import UndercoverParticle, BubbleChamberParticle
from phenomena.particles.dynamics import DynamicsController, KinematicsController
from phenomena.particles.dynamics.dynamicscontroller import DynamicType, MagneticField, ElectricField, Ionization
from skhep.math  import Vector3D, LorentzVector

dt = 1.

undercover_particles = [(UndercoverParticle("pi-", p=1.0))]
magnetic_particles = [(MagneticParticle("pi-", p=1.0))]
ionization_particles = [(IonizationParticle("pi-", p=1.0))]

bubblechmaber_particles = [ (BubbleChamberParticle("pi-", p=1.0)),
                            (BubbleChamberParticle("pi+", p=2.0)),
                            (BubbleChamberParticle("K+", p=2.0)),
                            (BubbleChamberParticle("K-", p=2.0)),
                            (BubbleChamberParticle("pi0", p=2.0)),
                            (BubbleChamberParticle("K0", p=2.0))
                            ]

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
def test_MagneticField_DynamicType(particle):
    DC = DynamicsController(particle,[MagneticField])
    assert isinstance(DC, object)
    acceleration = DC.updateAcceleration(dt)
    velocity0 = copy.deepcopy(particle.fourMomentum.vector)
    assert isinstance(acceleration, Vector3D)
    assert acceleration.isperpendicular(velocity0)

    KC = KinematicsController(particle)
    assert isinstance(KC, object)
    particle.fourMomentum = KC.updateFourMomentum(acceleration, dt)
    velocity1 = particle.fourMomentum.vector
    assert velocity1 != velocity0
    position = KC.getPosition(velocity1, dt)
    assert isinstance(position, Vector3D)
    assert position != particle._initialposition

@pytest.mark.parametrize("particle",magnetic_particles)
def test_MagneticField_Particle(particle):
    position0 = particle._position.copy()
    assert position0 == particle._initialposition
    velocity0 = particle.fourMomentum.boostvector
    particle.updatePosition(dt)
    position1 = particle._position
    assert isinstance(position1 , LorentzVector)
    assert position1 != position0
    acceleration1 = particle._acceleration
    assert isinstance(acceleration1, Vector3D)
    assert acceleration1.isperpendicular(velocity0)
    velocity1= particle.fourMomentum.boostvector
    assert isinstance(velocity1, Vector3D)
    assert velocity1 != velocity0
    assert not acceleration1.isperpendicular(velocity1)
    assert particle.distanceTravelled() !=0
    assert particle.timeTravelled() !=0

@pytest.mark.parametrize("particle",undercover_particles)
def test_Ionization_Dynamics(particle):
    IonizationObject = Ionization(particle)
    assert isinstance(IonizationObject, DynamicType)
    acceleration = IonizationObject.getAcceleration(dt)
    velocity0 = copy.deepcopy(particle.fourMomentum.vector)
    assert isinstance(acceleration, Vector3D)
    assert acceleration.isantiparallel(velocity0)

@pytest.mark.parametrize("particle",undercover_particles)
def test_Ionization_Controllers(particle):
    DC = DynamicsController(particle,[Ionization])
    assert isinstance(DC, object)
    acceleration = DC.updateAcceleration(dt)
    velocity0 = particle.fourMomentum.vector
    assert isinstance(acceleration, Vector3D)
    assert acceleration.isantiparallel(velocity0)

    KC = KinematicsController(particle)
    assert isinstance(KC, object)
    particle.fourMomentum = KC.updateFourMomentum(acceleration, dt)
    velocity1 = particle.fourMomentum.vector
    assert velocity1 != velocity0
    position = KC.getPosition(velocity1, dt)
    assert isinstance(position, Vector3D)
    assert position != particle._initialposition

@pytest.mark.parametrize("particle",ionization_particles)
def test_Ionization_Particle(particle):
    position0 = particle._position.copy()
    assert position0 == particle._initialposition
    velocity0 = particle.fourMomentum.boostvector
    particle.updatePosition(dt)
    position1 = particle._position
    assert isinstance(position1 , LorentzVector)
    assert position1 != position0
    acceleration1 = particle._acceleration
    assert isinstance(acceleration1, Vector3D)
    velocity1= particle.fourMomentum.boostvector
    assert isinstance(velocity1, Vector3D)
    assert velocity1 != velocity0
    assert not acceleration1.isperpendicular(velocity1)
    assert particle.distanceTravelled() !=0
    assert particle.timeTravelled() !=0

@pytest.mark.parametrize("particle",bubblechmaber_particles)
def test_BubbleChamber_Dynamics(particle):
    position0 = particle._position.copy()
    assert position0 == particle._initialposition
    velocity0 = particle.fourMomentum.boostvector.copy()
    particle.updatePosition(dt)
    position1 = particle._position
    assert isinstance(position1 , LorentzVector)
    assert position1 != position0
    acceleration1 = particle._acceleration
    assert isinstance(acceleration1, Vector3D)
    velocity1= particle.fourMomentum.boostvector.copy()
    assert isinstance(velocity1, Vector3D)
    if particle.charge !=0:
        assert velocity1 != velocity0
        assert not acceleration1.isperpendicular(velocity1)
    assert particle.distanceTravelled() !=0
    assert particle.timeTravelled() !=0
