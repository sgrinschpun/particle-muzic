#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from datasources import DataSource
from particledatatools import ParticleDataToolFetcher
from scikithepsource import SciKitHEPFetcher
from extra_info import ExtraInfoFetcher
from decaylanguagesource import DecayLanguageFetcher

from skhep import units as u

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
    'getWidth':particledatatool, #particledatatool,scikitHEP, decaylanguage  skhep.math.kinematics.width_to_lifetime
    'getCTau':scikitHEP, #particledatatool, scikitHEP
    'getRadius':decaylanguage,
    'getAnti':decaylanguage,
    'isNewPhysics':scikitHEP,
    'getParticleList':particledatatool,
    'getParticleByComposition':extrainfo
}

class ParticleDataSource(object):
    '''
    This class manages the sources of information of each parameter, according to the sources dict.
    All information is accessed by pdgid but the mixin uses name, that's why the getPDGId method is used throughout. The 'getPDGId' element of the sources dict determines the list of particles available.
    Units are managed by the class

    usage example in mixin: self._mass = ParticleDataSource.getMass(self._name)
    '''

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
        return sources['getMass'].getMass(pdgid) / u.GeV

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
        pdgid = ParticleDataSource.getPDGId(name)
        return sources['getWidth'].getWidth(pdgid) * u.GeV / u.GeV

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

    @staticmethod
    def isNewPhysics(name):
        pdgid = ParticleDataSource.getPDGId(name)
        return sources['isNewPhysics'].isNewPhysics(pdgid)

    @staticmethod
    def getParticleList():
        return sources['getParticleList'].getParticleList()

    @staticmethod
    def getParticleByComposition():
        return ParticleDataSource.getName(sources['getParticleByComposition'].getParticleByComposition())
