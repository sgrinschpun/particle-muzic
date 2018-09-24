import pytest

#@pytest.mark.parametrize("particle",[
#("B+"),("B-"),("B0"),("D+"),("D-"),("D0"),("J/psi"),("K*-"),("K*+"),("K*0"),("K+"),("K-"),("K0"),("Lambda0"),("Sigma+"),("Sigma-"),("Sigma0"),("Upsilon"),("W+"),("W-"),("Xi-"),("Xi0"),("Z0"),("u"),("ubar"),("s"),("sbar"),("t"),("tbar"),("b"),("bbar"),("c"),("cbar"),("d"),("dbar"),("e+"),("e-"),("eta'"),("eta"),("g"),("gamma"),("h0(H_1)"),("mu+"),("mu-"),("n0"),("nu_e"),("nu_ebar"),("nu_mu"),("nu_mubar"),("nu_tau"),("nu_taubar"),("omega"),("p+"),("phi"),("pi+"),("pi-"),("pi0"),("rho+"),("rho-"),("rho0"),("tau+"),("tau-")])
@pytest.mark.parametrize("particle",[
("B+"),("B-"),("B0"),("D+"),("D-"),("D0"),("J/psi")
])
def test_sources(particledatasource,particledatatools,scikithep,decaylanguage,extrainfo,particle):
    pdgid = particledatasource.getPDGId(particle)

    assert round(particledatatools.getMass(pdgid),3) == round(scikithep.getMass(pdgid),3)
    assert round(decaylanguage.getMass(pdgid),3) == round(scikithep.getMass(pdgid),3)

    assert particledatatools.getCharge(pdgid) == scikithep.getCharge(pdgid)
    assert decaylanguage.getCharge(pdgid) == scikithep.getCharge(pdgid)

    #assert particledatatools.getTau(pdgid) == scikithep.getTau(pdgid)  ## chek units

    assert extrainfo.getComposition(pdgid) == decaylanguage.getComposition(pdgid)

    assert extrainfo.getType(pdgid) == scikithep.getType(pdgid)

    assert round(scikithep.getWidth(pdgid),6) == round(decaylanguage.getWidth(pdgid),6)

    #assert round(particledatatools.getCTau(pdgid),6) == round(scikithep.getCTau(pdgid),6) ## check units
