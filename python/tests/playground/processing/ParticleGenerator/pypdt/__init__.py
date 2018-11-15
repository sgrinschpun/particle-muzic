# -*- python -*-

"""
Pythonic access to high energy particle data tables and ID codes.

This is a rethink in Python of the commonly used HepPDT/HepPID packages for accessing
particle data tables and PDG scheme particle ID codes. Version 0.7.0 onwards should be
compatible with Python 3.


Particle data table functions (cf. HepPDT)
------------------------------------------

HepPDT has no native Python interface, and it is not easy
to naturally wrap its C++ interface for Python, so PyPDT is written from scratch
in Python, with a lighter class count than the original: it's just a convenience
interface to a small ASCII data file, so who needs lots of classes?

Examples:

>>> import pypdt
>>> pypdt.get(2212) # print out proton particle data
>>> p = pypdt.get(2112) # get the neutron particle data object
>>> tbl = pypdt.ParticleDataTable() # make a particle data table
>>> # or tbl = pypdt.ParticleDataTable() # to read from AFS default db
>>> # or tbl = pypdt.PDT() # if you prefer minimal keystrokes to clarity :)
>>> print tbl[13] # print a summary of muon information
>>> tbl[6].mass # access the top mass in GeV
>>> tbl[23].width # access the Z width in GeV
>>> tbl[310].lifetime # access the K0S lifetime in ps
>>> tbl[310].ctau # access the K0S lifetime in mm
>>> tbl[310].mean_disp(10.) # get the mean flight distance of a 10 GeV K0S in mm
>>> for p in tbl: print p # print summaries for all known particles
>>> # print info for all particles in asc lifetime order:
>>> for t, p in sorted((p.ctau, p) for p in tbl): print p

The world is your bivalve of choice.

For maximum convenience, you can even use PyPDT from the command line:

    $ python -m pypdt 13 310
    mu^-: ID=13, m=1.06e-01 GeV, 3*q=-3, width=9.99e-19 GeV, tau=6.59e+05 ps, ctau=1.97e+05 mm
    K_S^0: ID=310, m=4.98e-01 GeV, 3*q=0, width=2.46e-14 GeV, tau=2.68e+01 ps, ctau=8.02e+00 mm


Particle ID functions (cf. HepPID)
----------------------------------

PyPDT also contains Python versions of the HepPID library of functions for
interpreting particle ID codes in the PDG scheme. The code of these functions
has been directly translated to Python from HepPID's ParticleIdMethods -- please
notify the author of this package in case of inaccuracies or evolution of the
PID scheme.

Examples:

>>> pypdt.isSUSY(2010011)
True


TODO:
 * Use doctest
"""

__author__ = "Andy Buckley <andy.buckley@cern.ch>"
__version__ = "0.7.4"

from .pdt import *
from .pid import *

__all__ = ("lifetime_to_width", "width_to_lifetime",
           "LorentzViolation", "ParticleData", "ParticleDataTable", "PDT",
           "isValid", "hasFundamentalAnti",
           "isMeson", "isBaryon", "isDiQuark",
           "isHadron", "isLepton", "isNucleus",
           "isPentaquark", "isSUSY", "isRhadron", "isDyon", "isQBall",
           "hasDown", "hasUp", "hasStrange", "hasCharm", "hasBottom", "hasTop",
           "jSpin", "lSpin", "sSpin",
           "threeCharge", "charge",
           "ionZ", "ionA", "ionNlambda")
