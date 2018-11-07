from phenomena.particles import ServerParticle
from phenomena.connection.phenomena_message import IncomingMessage
from phenomena.nodes import get_save_node, ExecutableNode
from phenomena.nodes import JsonRemoteAudioVideoNode

from phenomena.nodes.particle_nodes import ParticleAccumulatorNode, ParticleEntryNode

_node_controller = None

class NodeController(ExecutableNode):

    def __init__(self):
        self._root_node = ParticleEntryNode()
        self._audiovideonode = JsonRemoteAudioVideoNode()
        self._last_node = ParticleAccumulatorNode()
        _node = get_save_node()
        _node.setInitNode(self._root_node)
        self._root_node.setNextNode(self._audiovideonode)
        self._audiovideonode.setNextNode(self._last_node)
        self._identifier = "node"

    def findModule(self, module_path):
        if(module_path == self._identifier): return self
        else:
            next_module_path = module_path.split(' ', 1)
            if(len(next_module_path) == 1): raise Exception("Module Not found!")
            self._root_node.findModule(next_module_path[1])

    def getIdentifier(self):
        return self._identifier

    def execute(self, incoming_message):
        assert isinstance(incoming_message, IncomingMessage)
        exec_method = getattr(self, NodeController._commands[incoming_message.command_name])
        exec_method(**incoming_message.params)



if __name__ == "__main__":
    node_controller = NodeController()
    particle = "pi+"
    node_controller._addParticle(particle = particle)
