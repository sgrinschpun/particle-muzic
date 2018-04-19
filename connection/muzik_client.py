from twisted.internet.protocol import Protocol, ClientFactory
from muzik_message import IncomingMessage

class Echo(Protocol):
    def dataReceived(self, data):
        print "data: ",data

    def connectionMade(self):
        incoming_message = IncomingMessage.fromData(command_id=1, command_name="test", module_path="x.y.z", params = [1,2])
        send_message = incoming_message.serialize()
        self.transport.write(send_message)

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