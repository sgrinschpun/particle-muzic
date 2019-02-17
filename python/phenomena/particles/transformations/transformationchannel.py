from collections import namedtuple
from phenomena.particles.sources import ParticleDataSource, ParticleDataToolFetcher, SciKitHEPFetcher

Channel = namedtuple('Channel', 'BR particles')
#_make, _replace, _asdict() jsdon.dumps,  _fields

class TransformationChannel(Channel):
    '''
    TC class includes ONE channels of a particular transformation
    Subclass of NamedTuple: 1 channel with a BR(float ) and particles (list of ids)
    TC = TransformationChannel(1.0,[11,22])
    TC.ids = [11,22]
    TC.BR = 1.0
    TC.names = ['e-','nu_ebar']
    TC.length =2
    TC.nameSet = set(['e-','nu_ebar'])
    TC.idSet = set([11,22])
    TC.totalCharge = -1
    TC.leptonNumber = 0
    TC.isLeptonNeutrino = 1
    '''
    @property
    def ids(self):
        return self.particles

    @property
    def names(self):
        return map(ParticleDataSource.getName,self.ids )

    @property
    def length(self):
        return len(self.ids)

    @property
    def nameSet(self):
        return set(self.names)

    @property
    def idSet(self):
        return set(self.ids)

    @property
    def totalCharge(self):
        charge = 0.
        for name in self.names:
            charge += ParticleDataSource.getCharge(name)
        return charge

    leptonDict= [{
    'e-':1,'nu_e':1,
    'e+':-1,'nu_ebar':-1},{
    'mu-':1,'nu_mu':1,
    'mu+':-1,'nu_mubar':-1},{
    'tau-': 1,'nu_tau':1,
    'tau+':-1,'nu_taubar':-1
    }]
    leptonList =['e-','e+','mu-','mu+','tau-','tau+']
    neutrinoList = ['nu_e','nu_ebar','nu_mu','nu_mubar','nu_tau','nu_taubar']
    LeptonNumber = namedtuple('LeptonNumber', 'total, list')

    @property
    def leptonNumber(self):
        leptonnumber = [0,0,0]
        for index, family in enumerate(TransformationChannel.leptonDict):
            for name in self.names:
                try:
                    leptonnumber[index] += TransformationChannel.leptonDict[index][name]
                except:
                    leptonnumber[index] += 0
        return TransformationChannel.LeptonNumber(sum(leptonnumber),leptonnumber)

    def isLeptonNeutrino(self):
        if self.length == 2:
            lepton = 0
            neutrino = 0
            for name in self.names:
                if name in TransformationChannel.leptonList:
                    lepton =1
                elif name in TransformationChannel.neutrinoList:
                    neutrino =1
            leptonneutrino = [lepton,neutrino] == [1,1]
            return leptonneutrino
        else:
            return False

class TransformationChannels(object):
    '''
    TCS class includes ALL the channels of a particular transformation
    TCS = TransformationChannels.from_decaylist([(0.5,[1,2]),(0.5,[3,4])])
    TCS = TransformationChannels.from_decaylistNames([(0.5,['e-','nu_ebar']),(0.5,['mu-','nu_mubar'])])
    TCS.all = [TC1,TC2]
    TCS.length = 2
    TCS.mostProbable: the TC with higher BR
    TCS.getChannel(1) = TC2
    TCS.getChannel(['mu-','nu_mubar']) = TC2
    TCS.lengthCut(3) -> TCs with number of output particles <= 3
    TCS.lengthSelection(3) -> TCs with number of output particles = 3
    '''
    EXCLUDED = set(['rndmflavgbar','rndmflavg'])

    def __init__(self, tclist):
        self._tclist = tclist

    @classmethod
    def from_decaylist(cls, decaylist):
        '''
        We only accept 2body and 3body channels
        '''
        tclist = []
        for channel in decaylist:
            TC = TransformationChannel(channel[0],channel[1])
            if all([
                TC.length in [2,3],
                TC.nameSet.intersection(TransformationChannels.EXCLUDED) == set([])
            ]):
                tclist.append(TC)
        return cls(tclist)

    @classmethod
    def from_decaylistNames(cls, decaylist):
        tclist = []
        for channel in decaylist:
            TC = TransformationChannel(channel[0],map(ParticleDataSource.getPDGId,channel[1]))
            if all([
                TC.length in [2,3],
                TC.nameSet.intersection(TransformationChannels.EXCLUDED) == set([])
            ]):
                tclist.append()
        return cls(tclist)

    @property
    def all(self):
        return self._tclist

    @property
    def length(self):
        return len(self._tclist)

    @property
    def mostProbable(self):
        return sorted(self._tclist, key=lambda x: x.BR)[-1]

    def getChannel(self, *arg):
        if isinstance(arg[0],(int, long)):
            return self.getChannelfromId(arg[0])
        elif isinstance(arg[0],list):
            return self.getChannelfromParticles(arg[0])

    def getChannelfromId(self, id):
        try:
            return self.all[id]
        except:
            return []

    def getChannelfromParticles(self, particles):
        try:
            return [channel for channel in self.all if channel.nameSet==set(particles) and channel.length == len(particles)]
        except:
            return []

    def lengthCut(self, len):
        return [channel for channel in self._tclist if channel.length<=len]

    def lengthSelection(self, len):
        return [channel for channel in self._tclist if channel.length==len]

class AllDecays(object):

    ParticleDecayChannels = namedtuple('ParticleDecayChannels', 'name decayChannels')
    OriginOptions = namedtuple('OriginOptions', 'name BR')

    typical_particles = ['B+','B-','B0','D+','D-','D0','J/psi','K*-','K*+','K*0','K+','K-','K0','Lambda0','Sigma+','Sigma-','Sigma0','Upsilon','W+','W-','Xi-','Xi0','Z0','u','ubar','s','sbar','t','tbar','b','bbar','c','cbar','d','dbar','e+','e-','eta\'','eta','g','gamma','h0(H_1)','mu+','mu-','n0','nu_e','nu_ebar','nu_mu','nu_mubar','nu_tau','nu_taubar','omega','p+','phi','pi+','pi-','pi0','rho+','rho-','rho0','tau+','tau-']

    def __init__(self):
        self._buildList()

    def _buildList(self):
        all = []
        for item in ParticleDataToolFetcher.getParticleList():
            channels = ParticleDataToolFetcher.getDecayChannels(item[0])
            all.append(AllDecays.ParticleDecayChannels(item[1].name,TransformationChannels.from_decaylist(channels)))
        self._allDecaysinDB = all

    def getParticlesfromDecay(self,decay):
        selected_particles = []
        for partchannel in self._allDecaysinDB:
            for channel in partchannel.decayChannels.getChannel(decay):
                if all([set(decay) == channel.nameSet,
                        channel.BR > 0.,
                        ParticleDataSource.getCharge(partchannel.name)== channel.totalCharge,
                        partchannel.name in AllDecays.typical_particles
                        ]):
                    if channel.isLeptonNeutrino():
                        if partchannel.name in ['W+','W-']: selected_particles.append(AllDecays.OriginOptions(partchannel.name,channel.BR))
                    else:
                        selected_particles.append(AllDecays.OriginOptions(partchannel.name,channel.BR))
        return selected_particles
