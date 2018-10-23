import abc

class Calculations(object):

    @abc.abstractmethod
    def getValues(self):
        pass

class DecayCalculations(Calculations):

    def __init__(self, fourmomentum0, outputparticles):
        self._fourmomentum0 = fourmomentum0
        self._outputparticles = outputparticles
        self._set_values()

    def getValues(self):
        return self._values

    def _set_values(self):
        # if len(outputparticles) == 2:
        #     values = LAB2BodyCalc(decay,masses,phi,gamma).values
        # elif len(outputparticles) == 3:
        #     values = LAB3BodyCalc(decay,masses,phi,gamma).values
        # else:
        #     values = LAB4BodyCalc(decay,masses,phi,gamma).values
        self._values = ['decay', self._fourmomentum0 , self._outputparticles]

class InelasticCalculations(Calculations):

    def __init__(self, fourmomentum0, target, outputparticles):
        self._fourmomentum0 = fourmomentum0
        self._target = target
        self._outputparticles = outputparticles
        self._set_values()

    def getValues(self):
        return self._values

    def _set_values(self):
        self._values = ['inelastic', self._fourmomentum0 , self._target, self._outputparticles]


class ElasticCalculations(Calculations):

    def __init__(self, fourmomentum0, target, outputparticles):
        self._fourmomentum0 = fourmomentum0
        self._target = target
        self._outputparticles = outputparticles
        self._set_values()

    def getValues(self):
        return self._values

    def _set_values(self):
        self._values = ['elastic', self._fourmomentum0 , self._target, self._outputparticles]
