import path
from datasources import DataSource
from particledatatools import ParticleDataToolFetcher
from scikithep import SciKitHEPFetcher
from extra_info import ExtraInfoFetcher

#available sources
particledatatool = DataSource(ParticleDataToolFetcher())
scikitHEP = DataSource(SciKitHEPFetcher())
extrainfo = DataSource(ExtraInfoFetcher())

#sources assigned
sources = {
    'getMass':particledatatool, #scikitHEP
    'getCharge':particledatatool, #scikitHEP
    'getTau':particledatatool, #scikitHEP
    'getPDGId':particledatatool,#scikitHEP
    'getComposition':extrainfo,
    'getType':extrainfo #scikitHEP
}

class ParticleDataSource(object):
    @staticmethod
    def getPDGId(name):
        return sources['getPDGId'].getPDGId(name)

    @staticmethod
    def getMass(name):
        return sources['getMass'].getMass(name)

    @staticmethod
    def getCharge(name):
        return sources['getCharge'].getCharge(name)

    @staticmethod
    def getTau(name):
        return sources['getTau'].getTau(name)

    @staticmethod
    def getComposition(name):
        pdgid = str(ParticleDataSource.getPDGId(name))
        return sources['getComposition'].getComposition(pdgid) #extrainfo only accessed by pdgid

    @staticmethod
    def getType(name):
        pdgid = ParticleDataSource.getPDGId(name)
        return sources['getType'].getType(pdgid)
