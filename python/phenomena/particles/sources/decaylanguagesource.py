import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

from decaylanguage.particle import Particle
from skhep.math  import width_to_lifetime
from skhep import units as u
from phenomena.particles.particle import Particle as P

class DecayLanguageFetcher(object):

    @staticmethod
    def getMass(pdgid):
        return Particle.from_pdgid(pdgid).mass  * u.GeV

    @staticmethod
    def getCharge(pdgid):
        return Particle.from_pdgid(pdgid).charge

    @staticmethod
    def getName(pdgid):
        return Particle.from_pdgid(pdgid).name

    @staticmethod
    def getWidth(pdgid):
        return Particle.from_pdgid(pdgid).width * u.GeV

    @staticmethod
    def getTau(pdgid):
        width = Particle.from_pdgid(pdgid).width * u.GeV / u.MeV
        if width != 0.0:
            tau = width_to_lifetime(width) * u.nanosecond / u.picosecond
        else:
            tau = P.STABLE
        return tau

    @staticmethod
    def getPDGId(name):
        return Particle.from_search(name=name).val

    @staticmethod
    def getComposition(pdgid):
        quarks = list(Particle.from_pdgid(pdgid).quarks)
        quarkdict = {'U':'ubar', 'D':'dbar', 'C':'cbar', 'S':'sbar', 'T':'tbar', 'B':'bbar'}
        for n, quark in enumerate(quarks):
            if quark in quarkdict.keys():
                quarks[n] = quarkdict[quark]
        return quarks

    @staticmethod
    def getRadius(pdgid):
        return Particle.from_pdgid(pdgid).radius

    @staticmethod
    def getAnti(pdgid):
        if pdgid in [12,14,16,-12,-14,-16]:
            return -1*pdgid
        else:
            return Particle.from_pdgid(pdgid).invert().val

    @staticmethod
    def getLatex(pdgid):
        return Particle.from_pdgid(pdgid).latex

    @staticmethod
    def getLatexName(pdgid):
        return Particle.from_pdgid(pdgid).latex

    @staticmethod
    def getHTMLName(pdgid):
        return Particle.from_pdgid(pdgid).html_name

    @staticmethod
    def getQuantumNumbrers(pdgid):
        QN={}
        QN["I"]=Particle.from_pdgid(pdgid).I # Isospin
        QN["J"]=Particle.from_pdgid(pdgid).J # Total angular momentum
        QN["G"]=Particle.from_pdgid(pdgid).G # Parity: '', +, -, or ?
        QN["P"]=Particle.from_pdgid(pdgid).P # Space parity
        QN["C"]=Particle.from_pdgid(pdgid).C # Charge conjugation parity
        return QN

    @staticmethod
    def getMassLimits(pdgid):
        return [Particle.from_pdgid(pdgid).mass_lower,Particle.from_pdgid(pdgid).mass_upper]

    @staticmethod
    def getWidthLimits(pdgid):
        return [Particle.from_pdgid(pdgid).width_lower,Particle.from_pdgid(pdgid).wodth_upper]

    @staticmethod
    def getSpinType(pdgid):
        return Particle.from_pdgid(pdgid).spin_type.name

    @staticmethod
    def getStatus(pdgid):
        return Particle.from_pdgid(pdgid).status.name
