class DataSource(object):
    """
    Define the abstraction's interface.
    Maintain a reference to an object which represents the Implementor.
    """
    def __init__(self, imp):
       self._imp = imp

    def getMass(self, name):  #GeV
       return self._imp.getMass(name)

    def getCharge(self, name):
       return self._imp.getCharge(name)

    def getPDGId(self, name):
       return self._imp.getPDGId(name)

    def getTau(self, name):
       return self._imp.getTau(name)

    def getCtau(self, name):
       return self._imp.getCtau(name)

    def getWidth(self, name):
         return self._imp.getWidth(name)

    def getComposition(self, name):
         return self._imp.getComposition(name)

    def getType(self, name):
         return self._imp.getType(name)


class DataSourceFetcher(object):
    """
    Define the interface for implementation classes that fetch content.
    """
    def getMass(self, name):
        return None

    def getCharge(self, name):
        return None

    def getPDGId(self, name):
        return None

    def getTau(self, name):
        return None

    def getComposition(self, name):
        return None

    def getType(self, name):
        return None
