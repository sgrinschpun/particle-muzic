from phenomena.connection.phenomena_client import MessageSender
from phenomena.connection.phenomena_message import IncomingMessage, OutcomingMessage

HOST = '127.0.0.1'

class Phenomena:

    _command_id = 0

    @staticmethod
    def getCommandId():
        Phenomena._command_id += 1
        return Phenomena._command_id

    def addParticle(self, particle):
        message = IncomingMessage.fromData(command_id=Phenomena.getCommandId(), command_name="ADD", module_path="node", params={'particle_name': particle})
        received_message = self._sendMessage(message)
        return received_message

    def _sendMessage(self, message):
        message_sender = MessageSender(HOST)
        return message_sender.sendMessage(message)


if __name__ == '__main__':
    import time
    phenomena = Phenomena()
    begin_time = time.time()
<<<<<<< HEAD:phenomena/phenomena_client.py
    for i in range(2):
=======
    for i in range(1):
>>>>>>> 2084da8f3662d093c66d6455021c7929cb6f73a7:python/phenomena/phenomena_client.py
        print phenomena.addParticle("K-")
        #time.sleep()
    print "Total time: {0}".format(time.time() - begin_time)
