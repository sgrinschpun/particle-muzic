import pytest

from phenomena.particles import ServerParticle
from phenomena.particles.models import BubbleChamberParticle,QuantumUniverseParticle, QuantumUniverseVirtualParticle
from phenomena.particles.models.undercoverparticle import UndercoverParticle, VirtualUndercoverParticle
from phenomena.particles.transformations.types.decaysviavirtual.virtualparticlechannel import VirtualInfo
from phenomena.particles.sources import ParticleDataSource

testparticle = [("B+"),("B-"),("B0"),("D+"),("D-"),("D0"),("J/psi"),("K*-"),("K*+"),("K*0"),("K+"),("K-"),("K0"),("Lambda0"),("Sigma+"),("Sigma-"),("Sigma0"),("Upsilon"),("W+"),("W-"),("Xi-"),("Xi0"),("Z0"),("u"),("ubar"),("s"),("sbar"),("t"),("tbar"),("b"),("bbar"),("c"),("cbar"),("d"),("dbar"),("e+"),("e-"),("eta\'"),("eta"),("g"),("gamma"),("h0(H_1)"),("mu+"),("mu-"),("n0"),("nu_e"),("nu_ebar"),("nu_mu"),("nu_mubar"),("nu_tau"),("nu_taubar"),("omega"),("p+"),("phi"),("pi+"),("pi-"),("pi0"),("rho+"),("rho-"),("rho0"),("tau+"),("tau-")]

attribs = ['name', 'mass', 'p', 'theta', 'phi','fourMomentum']

@pytest.mark.parametrize("particle",testparticle)
def test_fromparticle(particle):
    UP = UndercoverParticle(particle, p=1, theta=0.1, phi= 0.2)
    SP1 = ServerParticle.fromparticle(UP)
    assert isinstance(SP1, ServerParticle.PARTICLE)
    for attrib in attribs:
        assert getattr(UP, attrib) == getattr(SP1, attrib)

    name = particle
    decay = ['e-','nu_ebar']  #this is just for testing
    mass= ParticleDataSource.getMass(particle)
    VI = VirtualInfo(name,mass, decay)
    VUP = VirtualUndercoverParticle(VI, p=1, theta=0.1, phi= 0.2)
    SP2 = ServerParticle.fromparticle(VUP)
    assert isinstance(SP2, ServerParticle.PARTICLE)
    for attrib in attribs:
        assert getattr(VUP, attrib) == getattr(SP2, attrib)
