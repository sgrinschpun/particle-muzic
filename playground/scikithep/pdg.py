from __future__ import print_function
import path
import math

from skhep.pdg import ParticleDataTable
from skhep.pdg import ParticleData
if __name__ == '__main__':
    tbl = ParticleDataTable()
    print( tbl[9000221].name )
    print( tbl('f(0)(500)0').id )
    print( tbl('f(0)(500)0').name )
    print( tbl('f(0)(500)0').mass )
