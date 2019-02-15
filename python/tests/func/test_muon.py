import pytest
from phenomena.particles.models import QuantumUniverseVirtualParticle
from phenomena.particles.transformations.types.decaysviavirtual.virtualparticlechannel import VirtualParticleChannel, RealInfo, VirtualInfo, VirtualChannel

from phenomena.particles.server_particle import ServerParticle


testparticle = [(QuantumUniverseVirtualParticle("mu-")),]

@pytest.mark.parametrize("particle",testparticle)
def test_muon(particle):
    assert isinstance(particle, QuantumUniverseVirtualParticle)
    assert particle._virtuality == 0
    assert isinstance(particle.transformation._selectedChannel,VirtualChannel)
    for item in particle.transformation.output:
        #print item.name, item.__class__
        newpart = ServerParticle.fromparticle(item)
        print newpart.name, newpart.transformation._selectedChannel, newpart.transformation._virtual, newpart.transformation.output

    #for item in  particle.transformation.output:
    #    print ServerParticle.fromparticle(item)
