from mapping_interface import Mapping

class ListMapping(Mapping):

    def __init__(self):
        self._values = [1, 2, 3, 5]

    def translateValue(self, value):
        pass

    def updateMapping(self, new_values):
        pass

class MirrorMapping(Mapping):

    def __init__(self):
        pass

    def translateValue(self, value):
        return value

    def updateMapping(self, new_values):
        pass

import random
class ConstMapping(Mapping):

    def __init__(self, value = 0):
        self._value = value

    def translateValue(self, value):
        return self._value
        #return random.uniform(0, 1)

    def updateMapping(self, new_values):
        pass

class LinealMapping(Mapping):

    def __init__(self):
        pass

    def translateValue(self, value):
        pass

    def updateMapping(self, new_values):
        pass

class ExponentialMapping(Mapping):

    def __init__(self):
        pass

    def translateValue(self, value):
        pass

    def updateMapping(self, new_values):
        pass
