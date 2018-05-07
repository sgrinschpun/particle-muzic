import socket
import sys
from phenomena.connection.commons import PORT
from phenomena.connection.commons import PetitionHandler

class MessageSender:

    def __init__(self, host):
        # Create a TCP/IP socket
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the port where the server is listening
        server_address = (host, PORT)
        self._socket.connect(server_address)
        self._petition_handler = PetitionHandler(self._socket)

    def sendMessage(self, petition):
        return self._petition_handler.sendPetition(petition)


