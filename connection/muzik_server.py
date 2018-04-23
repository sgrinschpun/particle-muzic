import json
from twisted.internet import reactor, protocol

from muzik_message import IncomingMessage, OutcomingMessage
from utils.log import get_logger

PORT = 16180

class MuzikServer(protocol.Protocol):

    def __init__(self):
        self._log = get_logger()
    def dataReceived(self, data):
        try:
            new_message = IncomingMessage.deserialize(data)
        except Exception, ex:
            out_message = OutcomingMessage.errorSerializeMessage(ex.message)
            self._return_message(out_message)
        else:
            print "Received Command: ", new_message.command_name
            self._log.info("Received Command!")
            out_message = OutcomingMessage.okMessage(new_message, new_message.params)
            self._return_message(out_message)

    def _return_message(self, outcoming_message):
        send_value = outcoming_message.serialize()
        self.transport.write(send_value)

class MyServerFactory(protocol.Factory):
    protocol = MuzikServer


if __name__ == '__main__':
    factory = MyServerFactory()
    reactor.listenTCP(PORT, factory)
    reactor.run()


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