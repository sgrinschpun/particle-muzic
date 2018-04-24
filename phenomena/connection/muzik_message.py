import json
from copy import deepcopy
from phenomena.connection.muzik_exception import DeserializationException

class IncomingMessage:

    @staticmethod
    def deserialize(serialized_string):
        value = {}
        try:
            value = json.loads(serialized_string)
        except Exception, ex:
            raise DeserializationException(ex.message)
        _incoming_message = IncomingMessage()
        try:
            _incoming_message._command_id = value["COMMAND_ID"]
            _incoming_message._command_name = value["COMMAND_NAME"]
            _incoming_message._module_path = value["MODULE_PATH"]
            _incoming_message._params = deepcopy(value["PARAMS"])
        except Exception, ex:
            raise DeserializationException(ex.message)
        return _incoming_message

    @staticmethod
    def fromData(command_id = 0, command_name = "", module_path="", params = {}):
        incoming_message = IncomingMessage()
        incoming_message._command_id = command_id
        incoming_message._command_name = command_name
        incoming_message._module_path = module_path
        incoming_message._params = deepcopy(params)
        return incoming_message

    def __init__(self):
        self._command_id = 0
        self._command_name = ""
        self._module_path=""
        self._params = {}

    @property
    def command_id(self):
        return self._command_id

    @property
    def command_name(self):
        return self._command_name

    @property
    def module_path(self):
        return self._module_path

    @property
    def params(self):
        return self._params

    def serialize(self):
        ret_dict = {}
        ret_dict["COMMAND_ID"] = self.command_id
        ret_dict["COMMAND_NAME"] = self._command_name
        ret_dict["MODULE_PATH"] = self._module_path
        ret_dict["PARAMS"] = deepcopy(self._params)
        return json.dumps(ret_dict).encode("ascii")

    def __str__(self):
        return "Incoming message: id {0} Name: {1} Module Path: {2} ".format(self._command_id,
                                                                             self._command_name,
                                                                             self._module_path)

class OutcomingMessage:
    ERROR = 0
    OK = 1

    @staticmethod
    def deserialize(serialized_string):
        value = {}
        try:
            value = json.loads(serialized_string)
        except Exception, ex:
            raise DeserializationException(ex.message)
        try:
            return OutcomingMessage(value["COMMAND_ID"],
                                    value["COMMAND_NAME"],
                                    value["MODULE_PATH"],
                                    value["RETURN"],
                                    value["TYPE"])

        except Exception, ex:
            raise DeserializationException(ex.message)

    @staticmethod
    def errorMessage(incoming_message, message):
        return OutcomingMessage(incoming_message.command_id,
                                incoming_message.command_name,
                                incoming_message.module_path,
                                message,
                                OutcomingMessage.ERROR)

    @staticmethod
    def errorSerializeMessage(message):
        return OutcomingMessage(-1, "UNKNOWN", "UNKNOWN", message, OutcomingMessage.ERROR)

    @staticmethod
    def okMessage(incoming_message, ret):
        return OutcomingMessage(incoming_message.command_id,
                                incoming_message.command_name,
                                incoming_message.module_path,
                                ret,
                                OutcomingMessage.OK)

    def __init__(self, command_id, command_name, module_path, return_info, type):
        self._command_id = command_id
        self._module_path = module_path
        self._command_name = command_name
        self._return = return_info
        self._type = type

    @property
    def command_id(self):
        return self._command_id

    @property
    def command_name(self):
        return self._command_name

    @property
    def module_path(self):
        return self._module_path

    @property
    def return_info(self):
        return self._return

    @property
    def type(self):
        return self._type

    def serialize(self):
        ret_dict = {}
        ret_dict["COMMAND_ID"] = self._command_id
        ret_dict["COMMAND_NAME"] = self._command_name
        ret_dict["MODULE_PATH"] = self._module_path
        ret_dict["RETURN"] = self._return
        ret_dict["TYPE"] = self._type
        return json.dumps(ret_dict).encode("ascii")

    def __str__(self):
        return "Outcoming message: type: {0} id {1} Name: {2} Module Path: {3} ".format(self._type,
                                                                                        self._command_id,
                                                                                        self._command_name,
                                                                                        self._module_path)