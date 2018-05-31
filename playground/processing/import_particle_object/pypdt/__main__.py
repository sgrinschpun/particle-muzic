# -*- python -*-

from __future__ import print_function

import optparse
op = optparse.OptionParser()
op.add_option("-f", "--dbfile", action="store", dest="FILE", metavar="FILE",
              help="specify the db file to read", default=None)
opts, args = op.parse_args()

import pypdt
t = pypdt.ParticleDataTable(opts.FILE if opts.FILE else None)
for pid in args:
    print(t[pid])
