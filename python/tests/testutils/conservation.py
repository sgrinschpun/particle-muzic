import math
import operator
from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseParticle, UndercoverParticle

PARTICLE = BubbleChamberParticle


class InOut(object):
    def __init__(self):
        pass

    @property
    def E(self):
        return self._E

    @E.setter
    def E(self, E):
        self._E = E

    @property
    def Pt(self):
        return self._Pt

    @Pt.setter
    def Pt(self, Pt):
        self._Pt = Pt

    @property
    def baryonnumber(self):
        return self._baryonnumber

    @baryonnumber.setter
    def baryonnumber(self, baryonnumber):
        self._baryonnumber = baryonnumber

    @property
    def leptonnumber(self):
        return self._leptonnumber

    @leptonnumber.setter
    def leptonnumber(self, leptonnumber):
        self._leptonnumber = leptonnumber

class Conservation(object):
    def __init__(self, particle, momentum):
        self._particle = PARTICLE(particle,p=momentum)
        print '1', self._particle.name
        print self._particle.transformation.selectedType
        print '2',self._particle.transformation.target
        print '3',self._particle.transformation.selectedChannel
        self._in()
        self._out()

    @property
    def In(self):
        return self._in

    def _in(self):
        self._in = InOut()
        self._in.E = self._sumIn('E')
        self._in.Pt = self._sumIn('Pt')
        self._in.charge = self._sumIn('charge')
        self._in.baryonnumber = self._sumIn('baryonnumber')
        self._in.leptonnumber = self._sumIn('leptonnumber')

    def _sumIn(self, attribute):
        value = getattr(self._particle, attribute)
        if self._particle.transformation.target:
            target = UndercoverParticle(self._particle.transformation.target)
            value += getattr(target, attribute)
        return value

    @property
    def Out(self):
        return self._out

    def _out(self):
        self._out = InOut()
        self._out.E = self._sumOut('E')
        self._out.Pt = self._SumPt()
        self._out.charge = self._sumOut('charge')
        self._out.baryonnumber = self._sumOut('baryonnumber')
        self._out.leptonnumber = self._sumOut('leptonnumber')

    def _SumPt(self):
        if self._particle.transformation.selectedType != 'NoTransformation':
            thislist = self._particle.transformation.output
            value = thislist[0].Pt - thislist[1].Pt
        else:
            thislist = [self._particle]
            value = thislist[0].Pt
        return value


    def _sumOut(self, attribute):
        value = 0.
        if self._particle.transformation.selectedType != 'NoTransformation':
            thislist = self._particle.transformation.output
        else:
            thislist = [self._particle]

        for id, item in enumerate(thislist):
                value += getattr(item, attribute)
        return value
