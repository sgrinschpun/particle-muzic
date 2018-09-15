from __future__ import division
import math

from datasources import DataSourceFetcher

#http://scikit-hep.org/
from skhep.pdg import ParticleDataTable
from skhep.simulation import pdgid as PDGID
from phenomena.particles.particle import ParticleDT

#tbl = ParticleDataTable('data/mass_width_2017.mcd')
tbl = ParticleDataTable()

class SciKitHEPFetcher(DataSourceFetcher):

    def getPDGId(self, name):
        return tbl(name).id

    def getMass(self, name):
        return tbl(name).mass  #GeV

    def getCharge(self, name):
        return tbl(name).charge

    def getTau(self, name):
        tau = tbl(name).lifetime #ps
        if tau is None:
            tau = ParticleDT.STABLE
        return tau

    def getType(self, pdgid):
        type = ''
        if PDGID.isLepton(pdgid):
            type = 'lepton'
        elif PDGID.isBaryon(pdgid):
            type = 'baryon'
        elif PDGID.isMeson(pdgid):
            type = 'meson'
        elif pdgid in [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]:
            type = 'quark'
        else:
            type = 'boson'

        return type
