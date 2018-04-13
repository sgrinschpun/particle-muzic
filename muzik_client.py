from twisted.internet.protocol import Protocol, ClientFactory
import json


class Echo(Protocol):
    def dataReceived(self, data):
        print "data: ",data

    def connectionMade(self):
        self.transport.write(json.dumps("Hello, world!"))

class EchoClientFactory(ClientFactory):
    def startedConnecting(self, connector):
        print 'Started to connect.'

    def buildProtocol(self, addr):
        print "Protocol!"
        return Echo()

    def clientConnectionLost(self, connector, reason):
        print 'Lost connection.  Reason:', reason

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed. Reason:', reason

from twisted.internet import reactor
reactor.connectTCP("localhost", 16180, EchoClientFactory())
reactor.run()