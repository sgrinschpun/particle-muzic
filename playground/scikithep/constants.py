from __future__ import print_function, division
import path
import math

from skhep.constants import c_light
from skhep import units as u


from phenomena.particles.sources import ParticleDataToolFetcher, SciKitHEPFetcher, DecayLanguageFetcher, ParticleDataSource

if __name__ == '__main__':
    #tau_Bs = 1.5 * picosecond    # a particle lifetime, say the Bs meson's
    #ctau_Bs = c_light * tau_Bs   # ctau of the particle, ~450 microns
    #print (ctau_Bs)                # result in HEP units, so mm ;-)
    #print (ctau_Bs / micrometer)  # result in micrometers
    #print (c_light/(u.cm/u.s))
    #print (c_light)
    particle = 'pi0'
    id = ParticleDataToolFetcher.getPDGId(particle)
    print (ParticleDataToolFetcher.getTau(id))
    print (SciKitHEPFetcher.getTau(id))
    print (DecayLanguageFetcher.getTau(id))
    print (ParticleDataSource.getTau(particle))

    print (ParticleDataToolFetcher.getMass(id))
    print (SciKitHEPFetcher.getMass(id))
    print (DecayLanguageFetcher.getMass(id))
    print (ParticleDataSource.getMass(particle))


    #print (ParticleDataToolFetcher.getWidth(id))
    #print (SciKitHEPFetcher.getWidth(id))
    #print (DecayLanguageFetcher.getWidth(id))
