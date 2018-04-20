from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor
from Queue import Queue
from threading import Thread
from muzik_message import IncomingMessage, OutcomingMessage


class SendMessageProtocol(Protocol):

    def __init__(self, message_queue):
        self._message_queue = message_queue

    def dataReceived(self, received_data):
        self._message_queue.put(received_data)

    def connectionMade(self):
        self._message_queue.put(True)

    def sendMessage(self, _message):
        self.transport.write(_message)

class ClientFactory(ClientFactory):

    def __init__(self, message_queue):
        self._protocol = SendMessageProtocol(message_queue)

    def startedConnecting(self, connector):
        pass

    def buildProtocol(self, addr):
        return self._protocol

    def getProtocol(self):
        return self._protocol

    def clientConnectionLost(self, connector, reason):
        pass
        #print 'Lost connection.  Reason:', reason

    def clientConnectionFailed(self, connector, reason):
        pass
        #print 'Connection failed. Reason:', reason


class MessageSender:

    def __init__(self):
        self._return_message_queue = Queue()
        self._factory = ClientFactory(self._return_message_queue)
        self._connector = reactor.connectTCP("localhost", 16180, self._factory)
        self._thread_connector = Thread(target=reactor.run, args=(False,))
        self._thread_connector.start()
        self._return_message_queue.get()

    def sendMessage(self, message):
        protocol = self._factory.getProtocol()
        protocol.sendMessage(message)
        return self._return_message_queue.get()

    def disconnect(self):
        self._connector.disconnect()
        reactor.stop()
        self._thread_connector.join()