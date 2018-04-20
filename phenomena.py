from connection.muzik_client import MessageSender
from connection.muzik_message import IncomingMessage, OutcomingMessage

class Phenomena:

    _command_id = 0

    @staticmethod
    def getCommandId():
        Phenomena._command_id += 1
        return Phenomena._command_id

    def __init__(self):
        self._message_sender = MessageSender()

    def addParticle(self, particle):
        message = IncomingMessage.fromData(command_id=Phenomena.getCommandId(), command_name="ADD", module_path="node", params={'particlename': particle})
        received_message = self._sendMessage(message)
        outcoming_message = OutcomingMessage.deserialize(received_message)
        #print outcoming_message

    def _sendMessage(self, message):
        return self._message_sender.sendMessage(message.serialize())

    def endConnection(self):
        self._message_sender.disconnect()


if __name__ == '__main__':
    import time
    phenomena = Phenomena()
    begin_time = time.time()
    for i in range(100000):
        phenomena.addParticle("pi+")
    print "Total time: {0}".format(time.time() - begin_time)
    phenomena.endConnection()
