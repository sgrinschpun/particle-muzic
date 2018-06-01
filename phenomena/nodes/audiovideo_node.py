import json
import socket
import time
from phenomena.mappings import MappingsController
from phenomena.nodes import get_save_node
from phenomena.particles.particle_action import ParticleActionNodeChain
from phenomena.particles import Particle
from phenomena.utils import get_logger

class JsonRemoteAudioVideoNode(ParticleActionNodeChain):
    _IP =  "172.16.7.12"
    _PORT = 1234
    def __init__(self):
        super(ParticleActionNodeChain, self).__init__()
        self._mapping_controller = MappingsController()
        self._log = get_logger()
        self._node = get_save_node()

    def addParticle(self, particle):
        assert issubclass(type(particle), Particle)
        try:
            msg = self._addParticlesMessage([particle])
            #self._sendMessage(msg)
        except Exception, ex:
            self._log.exception("Failed adding Particle on {0}".format(self.__class__.__name__))
            print ex
        finally:
            self._node.getNextNode(self).addParticle(particle)

    def removeParticle(self, particle):
        assert issubclass(type(particle), Particle)
        try:
            msg = self._removeParticlesMessage(particle)
            #self._sendMessage(msg)
        except:
            self._log.exception("Failed removing Particle on {0}".format(self.__class__.__name__))
        finally:
            self._node.getNextNode(self).removeParticle(particle)

    def transformParticle(self, particle, new_particles):
        rm_message = self._removeParticlesMessage([particle])
        add_message = self._addParticlesMessage(new_particles)
        all_messages = rm_message + add_message
        self._node.getNextNode(self).transformParticle(particle, new_particles)
        #self._sendMessage(all_messages)

    def getIdentifier(self):
        return "AudioVideoController"

    def setNextNode(self, n_node):
        self._node.setNextNode(self, n_node)

    def setPastNode(self, p_node):
        self._node.setPastNode(self, p_node)

    def execute(self, incoming_message):
        pass

    def _addParticlesMessage(self, particles_list):
        new_messages = []
        for particle in particles_list:
            new_message = {}
            new_particle = self._mapping_controller.translateParticle(particle)
            new_message['CMD'] = "ADD"
            new_message['PARAMS'] = new_particle.toDictionary()
            new_messages.append(new_message)
            self._sendMessage(new_message)
            time.sleep(0.2)
        return new_messages


    def _removeParticlesMessage(self, particles_list):
        new_messages = []
        for particle in particles_list:
            new_message = {}
            new_message['CMD'] = "REMOVE"
            new_message['PARAMS'] = {'id':particle.id};
            new_messages.append(new_message)
            self._sendMessage(new_message)
        return new_messages

    def _sendMessage(self, messages):
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (JsonRemoteAudioVideoNode._IP, JsonRemoteAudioVideoNode._PORT)
        send_socket.connect(server_address)
        print "Going to send: " + json.dumps(messages).encode("ascii")
        send_socket.sendall(json.dumps(messages).encode("ascii"))
        send_socket.close()