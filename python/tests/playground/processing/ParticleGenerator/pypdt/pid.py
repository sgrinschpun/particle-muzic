## -*- python -*-

"""
Access to information about fundamental particles and hadrons from PDG ID codes.

A Python version of the HepPID library of functions for processing particle
physics particle ID codes, in the PDG scheme. Code directly translated to Python
from HepPID's ParticleIdMethods -- please notify the author of this package in
case of inaccuracies or evolution of the PID scheme.
"""


## DIGIT HELPER FUNCTIONS

## Human readable digit indices
NJ = 1
NQ3 = 2
NQ2 = 3
NQ1 = 4
NL = 5
NR = 6
N = 7
N8 = 8
N9 = 9
N10 = 10

def _digit(loc, pid):
    "Find the loc'th digit in the given PID, starting from the RHS with index = 1"
    spid = str(abs(pid))
    if len(spid) < loc:
        return 0
    return int(spid[-loc])


def _extraBits(pid):
    "Return everything beyond the 7th digit, i.e. outside the defined numbering scheme."
    return abs(pid) // 10000000


def _fundamentalID(pid):
    """Return the first two digits if this is a 'fundamental' particle.
    ID = 100 is a special case (internal generator ID's are 81-100).
    Returns 0 if not fundamental or non-standard."""
    if _extraBits(pid) > 0:
        return 0
    if _digit(NQ2, pid) == 0 and _digit(NQ1, pid) == 0:
        return abs(pid) % 10000
    elif abs(pid) <= 100:
        return abs(pid)
    return 0



## BOOLEAN FUNCTIONS

def isValid(pid):
    "Check to see if this is a valid PID"
    if abs(pid) == 0: # illegal
        return None
    if _extraBits(pid) > 0:
        return isNucleus(pid) or isQBall(pid)
    if any(f(pid) for f in (isSUSY, isRhadron, isDyon, isMeson, isBaryon, isDiQuark, isPentaquark)):
        return True
    if _fundamentalID(pid) > 0:
        if pid > 0:
            return True
        return hasFundamentalAnti(pid)
    return False


def hasFundamentalAnti(pid):
    "If this is a fundamental particle, does it have a valid antiparticle?"
    ## These are defined by the generator and therefore are always valid
    fpid = _fundamentalID(pid)
    if fpid in range(80, 101):
        return True
    ## Check IDs from 1 to 79
    if fpid in range(1, 80) and fpid not in [21,22,23,32,33,35,36,39,41] and isValid(abs(pid)):
        return True
    return False


def isMeson(pid):
    "Check to see if this is a valid meson"
    if _extraBits(pid) or abs(pid) <= 100 or _fundamentalID(pid) in range(1, 101) or isRhadron(pid):
        return False
    ## Special meson cases
    if abs(pid) in (130, 310, 210):
        return True
    ## EvtGen uses some odd numbers
    if abs(pid) in (150, 350, 510, 530):
        return True
    ## Treat Regge particles (pomeron, etc.) as valid mesons
    if pid in (110, 990, 9990):
        return True
    if _digit(NJ, pid) > 0 and _digit(NQ3, pid) > 0 and _digit(NQ2, pid) > 0 and _digit(NQ1, pid) == 0:
        ## Check for illegal antiparticles
        return not (_digit(NQ3, pid) == _digit(NQ2, pid) and pid < 0)
    return False


def isBaryon(pid):
    "Check to see if this is a valid baryon"
    if _extraBits(pid) > 0 or abs(pid) <= 100 or _fundamentalID(pid) in range(1, 101) or isRhadron(pid) or isPentaquark(pid):
        return False
    if abs(pid) in (2110, 2210):
        return True
    if _digit(NJ, pid) > 0 and _digit(NQ3, pid) > 0 and _digit(NQ2, pid) > 0 and _digit(NQ1, pid) > 0:
        return True
    return False


def isDiQuark(pid):
    "Check to see if this is a valid diquark"
    if _extraBits(pid) > 0 or abs(pid) <= 100 or _fundamentalID(pid) in range(1, 101):
        return False
    if _digit(NJ, pid) > 0 and _digit(NQ3, pid) == 0 and _digit(NQ2, pid) > 0 and _digit(NQ1, pid) > 0:
        ## diquark signature
        return True
    return False


def isHadron(pid):
    "Is this a valid hadron ID?"
    if _extraBits(pid) > 0:
        return False
    return any(f(pid) for f in (isMeson, isBaryon, isPentaquark, isRhadron))


def isLepton(pid):
    "Is this a valid lepton ID?"
    if _extraBits(pid) > 0:
        return False
    return _fundamentalID(pid) in range(11, 19)


def isNucleus(pid):
    """This implements the 2006 Monte Carlo nuclear code scheme.
    Ion numbers are +/- 10LZZZAAAI.
    AAA is A - total baryon number
    ZZZ is Z - total charge
    L is the total number of strange quarks.
    I is the isomer number, with I=0 corresponding to the ground state.
    """
    ## A proton can also be a hydrogen nucleus
    if abs(pid) == 2212:
        return True
    ## new standard: +/- 10LZZZAAAI
    if _digit(N10, pid) == 1 and _digit(n9, pid) == 0:
        ## charge should always be less than or equal to baryon number. Check A >= Z
        return (abs(pid)//10) % 1000 >= (abs(pid)//10000) % 1000
    return False


def isPentaquark(pid):
    """Check to see if this is a valid pentaquark.

    A pentaquark code is of the form 9abcdej, where j is the spin and a-e are
    quarks.
    """
    if _extraBits(pid) > 0 or _digit(N, pid) != 9 or _digit(NR, pid) in (0,9):
        return False
    if _digit(NJ, pid) == 9 or _digit(NL, pid) == 0:
        return False
    if _digit(NQ1,pid) == 0 or _digit(NQ2,pid) == 0 or _digit(NQ3,pid) == 0 or _digit(NJ,pid) == 0:
        return False
    ## check ordering
    if _digit(NQ2, pid) > _digit(NQ1, pid) or _digit(NQ1, pid) > _digit(NL, pid) or _digit(NL, pid) > _digit(NR, pid):
        return False
    return True


def isSUSY(pid):
    """Is this a SUSY particle?
    Fundamental SUSY particles have n = 1 or 2 and nr = 0.
    """
    if _extraBits(pid) > 0:
        return False
    if _digit(N, pid) not in (1,2) or _digit(NR, pid) != 0:
        return False
    return _fundamentalID(pid) != 0


def isRhadron(pid):
    """Is this an R-hadron?

    An R-hadron code is of the form 10abcdj, 100abcj, or 1000abj where j is the
    spin, b, c, and d are quarks or gluons, and a (the digit following the
    zeros) is a SUSY particle.
    """
    if _extraBits(pid) > 0 or _digit(N, pid) != 1 or _digit(NR, pid) != 0:
        return False
    ## Make sure this isn't a fundamental SUSY particle
    if isSUSY(pid):
        return False
    ## All R-hadrons have at least 3 core digits
    if _digit(NQ2, pid) == 0 or _digit(NQ3, pid) == 0 or _digit(NJ,pid) == 0:
        return False
    return True


def isDyon(pid):
    """Is this a Dyon (magnetic monopole)?

    Magnetic monopoles and Dyons are assumed to have one unit of Dirac monopole
    charge and a variable integer number xyz units of electric charge.

    Codes 411xyz0 are then used when the magnetic and electrical charge sign
    agree and 412xyz0 when they disagree, with the overall sign of the particle
    set by the magnetic charge.  For now no spin information is provided.
    """
    if _extraBits(pid) > 0 or _digit(N, pid) != 4 or _digit(NR, pid) != 1 or _digit(NL, pid) not in (1,2):
        return False
    ## All Dyons have at least 1 core digit
    if _digit(NQ3, pid) == 0:
        return False
    ## Dyons have spin zero for now
    if _digit(NJ, pid) != 0:
        return False
    return True


def isQBall(pid):
    """Check for QBalls

    The ad-hoc numbering for such particles is 100xxxx0, where xxxx is the charge in tenths.
    """
    if _extraBits(pid) != 1 or _digit(N, pid) != 0 or _digit(NR, pid) != 0:
        return False
    ## Check the core number
    if (abs(pid)//10) % 10000 == 0:
        return False
    ## These particles have spin zero for now
    if _digit(NJ, pid) != 0:
        return False
    return True


## QUARK CONTENT

def _hasXXX(pid, q):
    "Internal function used by hasXXX methods"
    if _extraBits(pid) > 0 or _fundamentalID(pid) > 0:
        return False
    if isDyon(pid):
        return False
    if isRhadron(pid):
        iz = 7
        for i in reversed(range(2, 7)):
            if _digit(i, pid) == 0:
                iz = i
            elif i == iz - 1:
                pass ## ignore squark or gluino
            else:
                if _digit(i, pid) == q:
                    return True
        return False
    if q in [_digit(NQ3, pid), _digit(NQ2, pid), _digit(NQ1, pid)]:
        return True
    if isPentaquark(pid):
        if q in [_digit(NL, pid), _digit(NR, pid)]:
            return True
    return False


def hasDown(pid):
    "Does this particle contain a down quark?"
    return _hasXXX(pid, 1)

def hasUp(pid):
    "Does this particle contain an up quark?"
    return _hasXXX(pid, 2)

def hasStrange(pid):
    "Does this particle contain an strange quark?"
    return _hasXXX(pid, 3)

def hasCharm(pid):
    "Does this particle contain a charm quark?"
    return _hasXXX(pid, 4)

def hasBottom(pid):
    "Does this particle contain a bottom quark?"
    return _hasXXX(pid, 5)

def hasTop(pid):
    "Does this particle contain a top quark? Really?!"
    return _hasXXX(pid, 6)



## SPIN/ANGULAR MOMENTUM INFORMATION

def jSpin(pid):
    "Returns 2J+1, where J is the total angular momentum."
    if not isValid(pid):
        return None
    f = _fundamentalID(pid)
    if f > 0:
        ## some of these are known
        if f in range(1, 7): # quarks
            return 2
        if f == 9: ## ?
            return 3
        if f in range(11, 17): ## leptons
            return 2
        if f in range(21, 25): ## vector bosons
            return 3
        return 0
    elif _extraBits(pid) > 0:
        return 0
    return abs(pid) % 10


def sSpin(pid):
    "Returns 2S+1, where S is the spin."
    if not isValid(pid):
        return None
    # TODO: Can't we also handle spins for fundamentals (and baryons?)
    if not isMeson(pid):
        return None
    if _digit(N, pid) == 9:
        return 0
    inl = _digit(NL, pid)
    js = _digit(NJ, pid)
    if js == 1 or js >= 3:
        if inl == 0:
            return 0 if js == 1 else 1
        elif inl == 1:
            return 1 if js == 1 else 0
        elif inl in (2,3) and js >= 3:
            return 1
    return 0


def lSpin(pid):
    "Returns 2L+1, where L is the orbital angular momentum"
    if not isValid(pid):
        return None
    # TODO: Why meson-specific? This should be 0 for most (all?) fundamentals, not None
    if not isMeson(pid):
        return None
    if _digit(N, pid) == 9:
        return 0
    inl = _digit(NL, pid)
    js = _digit(NJ, pid)
    if inl == 0:
        if js == 1: return 0
        if js == 3: return 0
        if js == 5: return 1
        if js == 7: return 2
        if js == 9: return 3
    elif inl == 1:
        if js == 1: return 1
        if js == 3: return 1
        if js == 5: return 2
        if js == 7: return 3
        if js == 9: return 4
    elif inl == 2:
        if js == 3: return 1
        if js == 5: return 2
        if js == 7: return 3
        if js == 9: return 4
    elif inl == 3:
        if js == 3: return 2
        if js == 5: return 3
        if js == 7: return 4
        if js == 9: return 5
    ## default to zero
    return 0



## CHARGE

def charge3(pid):
    "3 times the charge (so that it can always be returned as an int)"
    if not isValid(pid):
        return None
    charge = None
    q1 = _digit(NQ1, pid)
    q2 = _digit(NQ2, pid)
    q3 = _digit(NQ3, pid)
    ql = _digit(NL, pid)
    ch100 = [-1,  2, -1, 2, -1, 2, -1, 2, 0, 0,
             -3,  0, -3, 0, -3, 0, -3, 0, 0, 0,
              0,  0,  0, 3,  0, 0,  0, 0, 0, 0,
              0,  0,  0, 3,  0, 0,  3, 0, 0, 0,
              0, -1,  0, 0,  0, 0,  0, 0, 0, 0,
              0,  6,  3, 6,  0, 0,  0, 0, 0, 0,
              0,  0,  0, 0,  0, 0,  0, 0, 0, 0,
              0,  0,  0, 0,  0, 0,  0, 0, 0, 0,
              0,  0,  0, 0,  0, 0,  0, 0, 0, 0,
              0,  0,  0, 0,  0, 0,  0, 0, 0, 0]
    if isQBall(pid): ## Qball
        charge = 3 * ((abs(pid)//10) % 10000)
    elif _extraBits(pid) > 0: ## ion
        return 0
    elif isDyon(pid): ## Dyon
        charge = 3 * ((abs(pid)//10) % 1000)
        ## The charge sign will be changed below if pid < 0
        if nl == 2:
            charge = -charge
    elif _fundamentalID(pid) in range(1, 101): ## use lookup table
        charge = ch100[_fundamentalID(pid) - 1]
        if abs(pid) in (1000017, 1000018, 1000034, 1000052, 1000053, 1000054): ## ?
            charge = 0
        elif abs(pid) in (5100061, 5100062): ## ?
            charge = 6
    elif _digit(NJ, pid) == 0: ## KL, KS, or undefined
        return 0
    elif isMeson(pid): ## mesons
        charge = ch100[q3-1] - ch100[q2-1] if q2 in (3,5) else ch100[q2-1] - ch100[q3-1]
    elif isRhadron(pid): ## Rhadron
        if q1 == 0 or q1 == 9:
            charge = ch100[q3-1] - ch100[q2-1] if q2 == 3 or q2 == 5 else ch100[q2-1] - ch100[q3-1]
        elif ql == 0:
            charge = ch100[q3-1] + ch100[q2-1] + ch100[q1-1]
        elif _digit(NR, pid) == 0:
            charge = ch100[q3-1] + ch100[q2-1] + ch100[q1-1] + ch100[ql-1]
    elif isDiQuark(pid): ## diquarks
        charge = ch100[q2-1] + ch100[q1-1]
    elif isBaryon(pid): ## baryons
        charge = ch100[q3-1] + ch100[q2-1] + ch100[q1-1]

    ## Return (inverted) charge
    if not charge: ## None or 0
        return charge
    if pid < 0:
        charge = -charge
    return charge

## Alias
threeCharge = charge3

def abscharge3(pid):
    "Absolute value of 3 x charge"
    return abs(charge3(pid))


def charge(pid):
    "The actual charge"
    if isQBall(pid):
        return threeCharge(pid)/30.0
    return threeCharge(pid)/3.0

def abscharge(pid):
    "Absolute value of charge"
    return abs(charge(pid))


## ION FUNCTIONS

def ionZ(pid):
    "Get the ion Z number. Ion numbers are +/- 10LZZZAAAI. Returns None if not an ion."
    ## A proton can also be a hydrogen nucleus.
    if pid == 2212:
        return 1
    if isNucleus(pid):
        return (abs(pid)//10000) % 1000
    return None


def ionA(pid):
    "Get the ion A number. Ion numbers are +/- 10LZZZAAAI. Returns None if not an ion."
    ## A proton can also be a hydrogen nucleus.
    if pid == 2212:
        return 1
    if isNucleus(pid):
        return (abs(pid)//10) % 1000
    return None


def ionNlambda(pid):
    "Get the ion nLambda number. Ion numbers are +/- 10LZZZAAAI. Returns None if not an ion."
    ## A proton can also be a hydrogen nucleus
    if abs(pid) == 2212:
        return 0
    if isNucleus(pid):
        return _digit(n8, pid)
    return None
