from collections import namedtuple

from phenomena.particles.sources import ParticleDataSource

Channel = namedtuple('Channel', 'BR particles')

class TransformationChannel(object):
    def __init__(self, BR, particles):
        self._item = Channel(BR,particles)

    @property
    def BR(self):
        return self._item.BR

    @property
    def ids(self):
        return self._item.particles

    @property
    def names(self):
        return map(ParticleDataSource.getName,self.ids )

    def len(self):
        return len(self.ids)

    def nameSet(self):
        return set(self.names)

    def idSet(self):
        return set(self.ids)

    def totalCharge(self):
        charge = 0.
        for name in self.names:
            charge += ParticleDataSource.getCharge(name)

    leptonDict= [{
    'e-':1,'nu_e':1,
    'e+':-1,'nu_ebar':-1},{
    'mu-':1,'nu_mu':1,
    'mu+':-1,'nu_mubar':-1},{
    'tau-': 1,'nu_tau':1,
    'tau+':-1,'nu_taubar':-1
    }]

    LeptonNumber = namedtuple('LeptonNumber', 'total, list')

    def leptonNumber(self):
        leptonnumber = [0,0,0]
        for index, family in enumerate(TransformationChannel.leptonDict):
            for name in self.names:
                try:
                    leptonnumber[index] += leptonDict[name]
                except:
                    leptonnumber[index] += 0

        return LeptonNumber(sum(leptonnumber),leptonnumber)

    def isLeptonNeutrino(self):
        


class TransformationChannels(object):
    pass
