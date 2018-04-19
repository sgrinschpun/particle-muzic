from particle_action import ParticleAccumulatorNode, ParticleEntryNode
from particle import Particle, ParticleDT
from nodes import get_save_node, ExecutableNode
from connection.muzik_message import IncomingMessage


class NodeController(ExecutableNode):
    def __init__(self):
        self._root_node = ParticleEntryNode()
        self._last_node = ParticleAccumulatorNode()
        _node = get_save_node()
        _node.setInitNode(self._root_node)
        self._root_node.setNextNode(self._last_node)
        self._identifier = "node"

    def _addParticle(self, **kwargs):
        particle_str = kwargs['particle']
        assert issubclass(type(particle_str), str)
        particle = ParticleDT(particle_str)
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


if __name__ == "__main__":
    node_controller = NodeController()
    particle = "pi+"
    node_controller._addParticle(particle = particle)
