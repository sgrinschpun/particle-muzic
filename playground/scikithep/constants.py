from __future__ import print_function
import path
import math

from skhep.constants import c_light
from skhep.units     import picosecond, micrometer

if __name__ == '__main__':
    tau_Bs = 1.5 * picosecond    # a particle lifetime, say the Bs meson's
    ctau_Bs = c_light * tau_Bs   # ctau of the particle, ~450 microns
    print (ctau_Bs)                # result in HEP units, so mm ;-)
    print (ctau_Bs / micrometer)  # result in micrometers
