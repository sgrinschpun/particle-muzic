from phenomena.particles import ParticleDT, ParticleBoosted
from phenomena.connection.phenomena_message import IncomingMessage
from phenomena.nodes import get_save_node, ExecutableNode
from phenomena.nodes import JsonRemoteAudioVideoNode

from phenomena.particles.particle_action import ParticleAccumulatorNode, ParticleEntryNode

_node_controller = None

def getNodeController():
    global _node_controller
    if _node_controller == None: _node_controller = NodeController()
    return _node_controller



class NodeController(ExecutableNode):
    _commands = {'ADD': "_addParticle"}

    def __init__(self):
        self._root_node = ParticleEntryNode()
        self._audiovideonode = JsonRemoteAudioVideoNode()
        self._last_node = ParticleAccumulatorNode()
        _node = get_save_node()
        _node.setInitNode(self._root_node)
        self._root_node.setNextNode(self._audiovideonode)
        self._audiovideonode.setNextNode(self._last_node)
        self._identifier = "node"

    def _addParticle(self, **kwargs):
        particle_str = kwargs['particle_name']
        theta = kwargs['theta']
        p = kwargs['p']
        E = kwargs['E']
        print "THIS: ", particle_str, type(particle_str)
        particle = ParticleBoosted(particle_str,theta,p)
        self._root_node.addParticle(particle)

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
