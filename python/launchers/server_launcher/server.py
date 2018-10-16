from __future__ import print_function
import path
from phenomena.connection.phenomena_server import PhenomenaServer


if __name__ == '__main__':
    print ('starting server')
    server = PhenomenaServer()
    server.startServer()
