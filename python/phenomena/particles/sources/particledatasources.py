from datasources import DataSource
from particledatatools import ParticleDataToolFetcher
from scikithepsource import SciKitHEPFetcher
from extra_info import ExtraInfoFetcher
from decaylanguagesource import DecayLanguageFetcher

#available sources
particledatatool = DataSource(ParticleDataToolFetcher)
scikitHEP = DataSource(SciKitHEPFetcher)
extrainfo = DataSource(ExtraInfoFetcher)
decaylanguage = DataSource(DecayLanguageFetcher)

#sources assigned
sources = {
    'getMass':particledatatool, #particledatatool, scikitHEP, decaylanguage
    'getCharge':particledatatool,#particledatatool, scikitHEP, decaylanguage
    'getTau':particledatatool, #particledatatool, scikitHEP, decaylanguage??????  skhep.math.kinematics.width_to_lifetime
    'getPDGId':particledatatool,#particledatatool, scikitHEP, decaylanguage
    'getComposition':extrainfo, #decaylanguage, extrainfo
    'getType':extrainfo, #scikitHEP,
    'getSpin':scikitHEP,
    'getName':particledatatool,#particledatatool, scikitHEP, decaylanguage
    'getDecayChannels':particledatatool,
    'getWidth':scikitHEP, #scikitHEP, decaylanguage  skhep.math.kinematics.width_to_lifetime
    'getCTau':scikitHEP, #particledatatool, scikitHEP
    'getRadius':decaylanguage,
    'getAnti':decaylanguage
}

class ParticleDataSource(object):

    @staticmethod
    def getName(pdgid):
        name =''
        try:
            name = sources['getName'].getName(pdgid)
        except KeyError:
            newpdgid = pdgid*(-1)   #should check if this make sense
            name = sources['getName'].getName(newpdgid)
        finally:
            return name

    @staticmethod
    def getPDGId(name):
        return sources['getPDGId'].getPDGId(name)

    @staticmethod
    def getMass(name):
        pdgid = ParticleDataSource.getPDGId(name)
        return sources['getMass'].getMass(pdgid)

    @staticmethod
    def getCharge(name):
        pdgid = ParticleDataSource.getPDGId(name)
        return sources['getCharge'].getCharge(pdgid)

    @staticmethod
    def getTau(name):
        pdgid = ParticleDataSource.getPDGId(name)
        return sources['getTau'].getTau(pdgid)

    @staticmethod #ony extra info
    def getComposition(name):
        pdgid = ParticleDataSource.getPDGId(name)
        return sources['getComposition'].getComposition(pdgid)

    @staticmethod
    def getType(name):
        pdgid = ParticleDataSource.getPDGId(name)
        return sources['getType'].getType(pdgid) #extrainfo & scikithep only accessed by pdgid

    @staticmethod
    def getSpin(name):
        pdgid = ParticleDataSource.getPDGId(name)
        return sources['getSpin'].getSpin(pdgid) #scikithep only accessed by pdgid

    @staticmethod
    def getDecayChannels(name):
        return sources['getDecayChannels'].getDecayChannels(name)

    @staticmethod
    def getWidth(name):
        return sources['getWidth'].getWidth(name)

    @staticmethod
    def getCTau(name):
        pdgid = ParticleDataSource.getPDGId(name)
        return sources['getCTau'].getCTau(pdgid)

    @staticmethod
    def getRadius(name):
        pdgid = ParticleDataSource.getPDGId(name)
        return sources['getRadius'].getRadius(pdgid)

    @staticmethod
    def getAnti(name):
        pdgid = ParticleDataSource.getPDGId(name)
        return ParticleDataSource.getName(sources['getAnti'].getAnti(pdgid))
