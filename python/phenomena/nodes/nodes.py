import abc

_savenodes = None

def get_save_node():
    global _savenodes
    if not _savenodes: _savenodes = ListSaveNodes()
    return _savenodes

class Node(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def findModule(self, module_path):
        pass

    @abc.abstractmethod
    def getIdentifier(self):
        pass

class ExecutableNode(Node):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def execute(self, incoming_message):
        pass

class ConfigurableNode(ExecutableNode):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def setNextNode(self, n_node):
        pass

    @abc.abstractmethod
    def setPastNode(self, p_node):
        pass

class ListSaveNodes:

    def __init__(self):
        self._nodes = []

    def setInitNode(self, node):
        self._nodes.insert(0, node)

    def getInitNode(self):
        return self._nodes[0]

    def getNextNode(self, actual_node):
        index = self._nodes.index(actual_node)
        next_index = index + 1
        if next_index >= len(self._nodes):return self._nodes[0]
        return self._nodes[next_index]

    def getPastNode(self, actual_node):
        index = self._nodes.index(actual_node)
        past_index = index - 1
        if past_index <= 0: return self._nodes[-1]

    def setNextNode(self, actual_node, add_node):
        assert issubclass(type(add_node), Node)
        index = self._nodes.index(actual_node) + 1
        self._nodes.insert(index, add_node)
        print self._nodes

    def setPastNode(self, actual_node, add_node):
        assert issubclass(type(add_node), Node)
        index = self._nodes.index(actual_node) - 1
        self._nodes.insert(index, add_node)