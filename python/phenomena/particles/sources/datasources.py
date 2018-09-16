class DataSource(object):
    """
    Define the abstraction's interface.
    Maintain a reference to an object which represents the Implementor.
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
