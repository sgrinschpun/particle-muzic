import json
from twisted.internet import reactor, protocol
from copy import deepcopy
from node_controller import NodeController
from muzik_exception import DeserializationException, MessageFormatError

PORT = 16180

class IncomingMessage():

    @staticmethod
    def deserialize(serialized_string):
        try:
            value = json.dumps(serialized_string)
        except:
            raise DeserializationException()
        _incoming_message = IncomingMessage()
        try:
            _incoming_message._command_id = value["COMMAND_ID"]
            _incoming_message._command_name = value["COMMAND_NAME"]
            _incoming_message._module_path = value["MODULE_PATH"]
            _incoming_message._params = deepcopy(value["PARAMS"])
        except:
            raise DeserializationException()
        return _incoming_message

    def __init__(self):
        self._command_id = 0
        self._command_name = ""
        self._module_path=""
        self._params = {}

    def getCommandID(self):
        return self._commandid

    def getModulePath(self):
        return self._module_path

    def getParams(self):
        return self._params

class OutcomingMessage:

    def __init__(self):
        pass

    def getCommandID(self):
        return self._commandid

    def serialize(self):
        pass

class MuzikServer(protocol.Protocol):

    def dataReceived(self, data):
        try:
            value = json.dumps(data)
        except Exception, ex:
            pass
        else:
            print value
            self._return_message(value)

    def _return_message(self, message):
        print message
        value = json.loads(message)
        send_value = value.encode("ascii")
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