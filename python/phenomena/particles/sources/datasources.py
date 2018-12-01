#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

class DataSource(object):
    """
    Defines the abstraction's interface for data sources.
    Maintain a reference to an object which represents the Implementor.

    Use example: particledatatool = DataSource(ParticleDataToolFetcher)
    """
    def __init__(self, imp):
       self._imp = imp

    def getName(self, pdgid):
         return self._imp.getName(pdgid)

    def getMass(self, pdgid):  #GeV
       return self._imp.getMass(pdgid)

    def getCharge(self, pdgid):
       return self._imp.getCharge(pdgid)

    def getPDGId(self, name):
       return self._imp.getPDGId(name)

    def getTau(self, pdgid):
       return self._imp.getTau(pdgid)

    def getCTau(self, name):
       return self._imp.getCTau(name)

    def getWidth(self, name):
         return self._imp.getWidth(name)

    def getComposition(self, pdgid):
         return self._imp.getComposition(pdgid)

    def getType(self, pdgid):
         return self._imp.getType(pdgid)

    def getSpin(self, pdgid):
         return self._imp.getSpin(pdgid)

    def getDecayChannels(self, name):
        return self._imp.getDecayChannels(name)

    def getRadius(self, pdgid):
         return self._imp.getRadius(pdgid)

    def getAnti(self, pdgid):
         return self._imp.getAnti(pdgid)

    def getParticleList(self):
         return self._imp.getParticleList()
