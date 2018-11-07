import threading
import time

from abstract_node import Node
from main_controller_fsm import FSMMainController, FFFreeRide
from phenomena.particles import ServerParticle
from phenomena.nodes.main_controller_fsm import NonStep
from particle_accumulator import ParticleAccumulator
from saver_node import SaverNode

def getNodeController():
    global _node_controller
    if _node_controller == None: _node_controller = MainController()
    return _node_controller

class NodesAvailable():
    
    def __init__(self):
        self._nodes = []
    
    def addNode(self, node):
        self._nodes.append(node)
    
    def addNodes(self, node_iterable):
        for node in node_iterable:
            self.addNode(node)
            
    def findNode(self, node_name):
        node_list = [node for node in self._nodes if node.name == node_name]
        if len(node_list) != 1: raise Exception("Invalid node name")
        return node_list[0]

class Updater():
    def __init__(self, main_controller):
        self._FPS = 20.0
        self._main_controller = main_controller
        self._exit = False
    
    def start(self):
        threading.Timer(1/self._FPS, self.update).start()
        
    def end(self):
        self._exit = True
    
    def update(self):
        self._init_time_stamp = time.time()
        self._main_controller.execute()
        if not self._exit:
            self._recalculateTime()
    
    def _recalculateTime(self):
        actual_time_stamp = time.time()
        delta_time = actual_time_stamp - self._init_time_stamp
        launch_time =  (1/self._FPS) - delta_time
        print "Launch time: ", 1/self._FPS, delta_time, launch_time
        if delta_time <= 0:
            #TODO: Send warning message
            threading.Thread(self.update).start()
        else: threading.Timer(launch_time, self.update).start()

    @property
    def fps(self):
        return self._FPS

    @fps.setter
    def fps(self, value):
        if value > 60 | value < 20:
            raise ValueError("Non valid FPS Value. Should be between 20 and 60")
        self._FPS = value

class MainController(Node, FSMMainController):
    _commands = {'ADD': "_addParticle",
                 "CHANGE_FPS": "_changeFPS",
                 "STEP_FORDWARD": "_stepFordward",
                 "STEP_BACKWARD": "_stepBackward",
                 "SET_MODE": "_setMode"}
    
    def __init__(self):
        Node.__init__(self, "Main")
        self._fsm = FFFreeRide()
        self._nodes = NodesAvailable()
        self._stepper = NonStep()
        self._nodes.addNodes([self, SaverNode])
        self._index = 0
        self._updater = Updater(self)
        self._particles_accumulator = ParticleAccumulator()
        
    def start(self):
        self._updater.start()
    
    def attendMessage(self, message):
        pass
     
    def configure(self, configuration_message):
        assert isinstance(configuration_message, configuration_message)
        exec_method = getattr(self, MainController._commands[configuration_message.command_name])
        exec_method(**configuration_message.params)
            
    def execute(self):
        print self._index, time.time()
        self._index += 1
    
    def end(self):
        self._updater.end()
        
    def _addParticle(self, **kwargs):
        #TODO: this should be only in FREERIDE MODE
        particle_str = kwargs['particle_name']
        particle = ServerParticle.init(particle_str,**kwargs)
        self._particles_accumulator.addParticle(particle)
    
    def _changeFPS(self, **kwargs):
        new_fps = kwargs['fps']
        self._updater.fps = new_fps
    
    def _setMode(self, **kwargs):
        new_mode = kwargs['new_mode']
        self._fsm._setMode(new_mode)
    
    def _stepForward(self, **kwargs):
        self._stepper._stepForward()
    
    def _stepBackward(self, **kwargs):
        self._stepper._stepBackward()
    
    
if __name__ == "__main__":
    main_controller = MainController()
    main_controller.start()
    time.sleep(10)
    main_controller.end()