from __future__ import print_function
import path
from phenomena.phenomena_client import Phenomena

if __name__ == '__main__':
    phenomena = Phenomena()
    for i in range(2):
        print (phenomena.addParticle("K+"))
