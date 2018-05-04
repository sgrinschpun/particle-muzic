from phenomena.connection.phenomena_message import IncomingMessage, OutcomingMessage
from phenomena.utils.log import get_logger

PORT = 16180
DATASIZE = 5

class PetitionHandler:

    def __init__(self, conn):
        self._conn = conn
        self._log = get_logger()

    def attendPetition(self):
        data = self._receiveData()
        self._treatData(data)

    def sendPetition(self, incoming_message):
        assert isinstance(incoming_message, IncomingMessage)
        self._sendData(incoming_message.serialize())
        data = self._receiveData()
        return OutcomingMessage.deserialize(data)

    def _receiveData(self):
        try:
            str_size = self._receive(DATASIZE)
            size = int(str_size)
            return self._receive(size)
        except Exception, ex:
            self._log.exception("Failed receiving data: {0}".format(ex.message))

    def _sendData(self, message):
        try:
            self._send(str(len(message)).zfill(5))
            self._send(message)
        except Exception, ex:
            self._log.exception("Failed sending data: {0}".format(ex.message))

    def _treatData(self, data):
        try:
            new_message = IncomingMessage.deserialize(data)
        except Exception, ex:
            out_message = OutcomingMessage.errorSerializeMessage(ex.message)
            self._sendData(out_message.serialize())
        else:
            self._log.info("Received Command!")
            out_message = OutcomingMessage.okMessage(new_message, new_message.params)
            self._sendData(out_message.serialize())

    def _send(self, msg):
        total_sent = 0
        message_length = len(msg)
        while total_sent < message_length:
            sent = self._conn.send(msg[total_sent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            total_sent = total_sent + sent

    def _receive(self, message_length):
        chunks = []
        bytes_recd = 0
        while bytes_recd < message_length:
            chunk = self._conn.recv(min(message_length - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)