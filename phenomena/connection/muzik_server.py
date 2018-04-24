import socket
import sys
import threading

from phenomena.utils.log import get_logger
from phenomena.connection.commons import PORT, PetitionHandler


HOST = '0.0.0.0'

class PhenomenaServer:

    def __init__(self):
        self._log = get_logger()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.settimeout(2.0)
        self._out = False

    def startServer(self):
        self._server_thread = threading.Thread(target = self._startServer)
        self._server_thread.start()

    def _startServer(self):
        # Bind socket to local host and port
        try:
            self._socket.bind((HOST, PORT))
        except socket.error as msg:
            self._log.exception('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()
        self._log.info('Socket bind complete')
        # Start listening on socket
        self._socket.listen(10)
        # now keep talking with the client
        while not self._out:
            # wait to accept a connection - blocking call
            try:
                conn, addr = self._socket.accept()
                self._log.info('New petition from: ' + addr[0] + ':' + str(addr[1]))
                petition_handler = PetitionHandler(conn)
                petition_handler.attendPetition()
            except socket.timeout:
                self._log.info("Server petition timeout")

    def stopServer(self):
        self._out = True
        self._server_thread.join()
        self._socket.close()
        self._log.info("Server closed")



if __name__ == '__main__':
    import time
    server = PhenomenaServer()
    server.startServer()
    while(True):
        pass


"""
Json:
MESSAGE:
{
"MODULE_PATH": "x.y.z",
"COMMAND_NAME": CMD_NAME,
"COMMAND_ID": ID,
"PARAMS" : {}
}

RETURN:
{
"TYPE": OK//FAILED
"COMMAND_NAME": CMD_NAME,
"COMMAND_ID": ID,
"MODULE_PATH": "x.y.z",
"RETURN": message
}

[
{"CMD": "ADD",
"PARAMS": { "name":"pi+",
            "id": 1
            "mass":2E-16,
            "charge":3E-3,
            "lifetime":10E-12,
},

# COMMANDS_AVAILABLE:
{"CMD": "TRANSFORM",
"PARAMS": { "id": 1
                    "particles": [ { "name":"e-",
                       "id": 2
                      "mass":2E-16,
                      "charge":3E-3,
                      "lifetime":10E-12,
                    },
                      { "name":"mu+",
                       "id": 3
                      "mass":2E-16,
                      "charge":3E-3,
                      "lifetime":10E-12,
                    },

{"CMD": "REMOVE",
"PARAMS": { "id": 2},
],
]
"""