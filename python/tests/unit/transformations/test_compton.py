import pytest
from phenomena.particles.models import UndercoverParticle
from phenomena.particles.transformations.types import Transformation, ComptonEffect, ComptonKinematics
from testparticles import ComptonParticle

from skhep.math  import LorentzVector


test_particles = [(ComptonParticle("gamma", p=2.0))]


@pytest.mark.parametrize("particle",test_particles)
def test_comptoneffect_calculations(particle):
    target = UndercoverParticle(particle.transformation.target)
    finallist = []
    for part in particle.transformation.selectedChannel:
        finallist.append(UndercoverParticle(part))
    calculations = ComptonKinematics(particle,target,finallist)._calculations

    assert calculations._targetLAB.p == 0
    assert calculations._initialparticleCM.vector == -1*calculations._targetCM.vector
    assert calculations._p < particle.p

@pytest.mark.parametrize("particle",test_particles)
def test_comptoneffect_basics(particle):
    assert particle.name == "gamma"
    alltypes = particle.transformation.allTypes
    thisType = [transf for transf in alltypes if transf['type']=='ComptonEffect']
    assert thisType[0]['target'] == 'e-'
    assert set(thisType[0]['list'][0][1]) == set(['gamma', 'e-'])

    output = particle.transformation.output
    assert len(output) == 2

    for outputpart in output:
        assert isinstance(outputpart,UndercoverParticle)
        assert outputpart.E <= particle.E

@pytest.mark.parametrize("particle",test_particles)
def test_comptoneffect_conservation(particle, conservation, resolution, print_particle):
    print_particle

    for attr in ['Pt','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
