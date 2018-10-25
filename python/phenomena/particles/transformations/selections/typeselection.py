import random

class TransTypeSelect(object):

    def __init__(self, allvalues):
        self._allValues = allvalues
        self._selectType()

    @property
    def value(self):
        return self._selectedType

    #for improvement
    def _selectType(self):
        self._selectedType = random.choice(self._allValues)
