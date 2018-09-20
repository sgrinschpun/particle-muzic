import pytest
import math

#rest particles: parameters, boosted values,
@pytest.mark.parametrize("particle, mass, charge",[
("pi+", 0.13957018, 1.0),
("mu-", 0.1056583745, -1.0)])
def test_particle_at_rest(particle_rest, particle, mass, charge,resolution):
    #parameters
    assert particle_rest.name == particle
    assert round(particle_rest.mass,resolution) == round(mass,resolution)
    assert particle_rest.charge == charge
    #boosted parameters
    assert particle_rest.p == 0
    assert particle_rest.E == particle_rest.mass
    assert particle_rest.gamma == 1
    assert particle_rest.beta == 0
    assert particle_rest.T == 0

#boosted particle: boosted parameters
@pytest.mark.parametrize("particle, momentum",[
("pi+", 1),
("mu-", 0.5)])
def test_particle_boosted(particle_boosted,particle,momentum):
    assert particle_boosted.p == momentum
    assert particle_boosted.E > particle_boosted.mass
    assert particle_boosted.gamma > 1
    assert particle_boosted.beta > 0
    assert particle_boosted.beta < 1
    assert particle_boosted.T > 0

#decay results conservations
@pytest.mark.parametrize("particle, momentum, number",[
("pi+", 1, 2)])
def test_particle_conservations(particle_boosted, particle_decay_values, particle_conservation_energy, particle_conservation_momentum, particle_conservation_charge, particle, momentum,number,resolution):
    #number of expected particles
    assert len(particle_boosted.decayvalues) == number
    #energy conservation
    energy_in =  round(particle_conservation_energy["energy_in"],resolution)
    energy_out =  round(particle_conservation_energy["energy_out"],resolution)
    assert energy_in == energy_out
    #momentum conservation
    #transverse
    pt_in =  round(particle_conservation_momentum["pt_in"],resolution)
    pt_out =  round(particle_conservation_momentum["pt_out"],resolution)
    assert pt_in == pt_out
    #longitudinal
    pl_in =  round(particle_conservation_momentum["pl_in"],resolution)
    pl_out =  round(particle_conservation_momentum["pl_out"],resolution)
    assert pl_in == pl_out
    #charge conservation
    charge_in = round(particle_conservation_charge["charge_in"],resolution)
    charge_out = round(particle_conservation_charge["charge_out"],resolution)
    assert charge_in == charge_out
