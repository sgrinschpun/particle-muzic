import pytest
from phenomena.particles.models import UndercoverParticle
from phenomena.particles.transformations import KinematicsController
from phenomena.particles.transformations.types import PairProductionKinematics

from testparticles import PairProductionParticle

test_particles = [(PairProductionParticle("gamma", p=2.0))]

@pytest.mark.parametrize("particle",test_particles)
def test_PairProduction_Calculations(particle):
    target = None
    finallist = []
    for part in particle.transformation.selectedChannel:
        finallist.append(UndercoverParticle(part))
    calculations = PairProductionKinematics(particle,target,finallist)._calculations

    assert calculations._initialparticleCM.p == 0
    vector0 = calculations._finalparticlesCM[0].fourMomentum.vector
    vector1 = calculations._finalparticlesCM[1].fourMomentum.vector
    assert vector0.isantiparallel(vector1) # final particles in CM are antiparallel
    eLAB_init = particle.E
    eCM_init = calculations._initialparticleCM.e
    eCM_final = calculations._finalparticlesCM[0].fourMomentum.e + calculations._finalparticlesCM[1].fourMomentum.e
    eLAB_final = calculations._finalparticlesLAB[0].fourMomentum.e + calculations._finalparticlesLAB[1].fourMomentum.e
    assert round(eCM_init,4) == round(eCM_final,4) #energy is conserved in the CM
    assert round(eLAB_init,4) == round(eLAB_final,4) #energy is conserved in the LAB

@pytest.mark.parametrize("particle",test_particles)
def test_pairproduction_basics(particle):
    assert particle.name == 'gamma'
    alltypes = particle.transformation.allTypes
    thisType = [transf for transf in alltypes if transf['type']=='PairProduction']
    assert set(thisType[0]['list'][0][1]) == set(['e-', 'e+'])

    output = particle.transformation.output
    assert len(output) == 2

    for outputpart in output:
        assert isinstance(outputpart,UndercoverParticle)
        #assert outputpart.E < particle.E

@pytest.mark.parametrize("particle",test_particles)
def test_pairproduction_conservation(particle, conservation, resolution, print_particle):
    print_particle

    for attr in ['E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)

    for attr in ['P']:
        assert getattr(conservation.In,attr) == getattr(conservation.Out,attr)
