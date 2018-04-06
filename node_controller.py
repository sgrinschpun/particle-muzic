from particle_action import ParticleAccumulatorNode, ParticleEntryNode
from particle import Particle, ParticleDT
from nodes import get_save_node

class NodeController:

    def __init__(self):
        self._root_node = ParticleEntryNode()
        self._last_node = ParticleAccumulatorNode()
        _node = get_save_node()
        _node.setInitNode(self._root_node)
        self._root_node.setNextNode(self._last_node)

    def addParticle(self, particle):
        assert issubclass(type(particle), Particle)
        self._root_node.addParticle(particle)



if __name__ == "__main__":
    node_controller = NodeController()
    particle = ParticleDT("pi+")
    node_controller.addParticle(particle)
