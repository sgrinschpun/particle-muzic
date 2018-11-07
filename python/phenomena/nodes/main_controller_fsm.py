# Author: Cristobal Pio
# Company: IFAE
# Date: 6 November 2018
# Mail: cgarcia@ifae.es
# Information:

from abc import ABCMeta, abstractmethod

class MainControllerStates:
    FF_FREERIDE = 0
    RW_RIDE = 1
    USERCONTROL = 2
    
class FSMMainController():
    __metaclass__ = ABCMeta

    def __init__(self, main_controller):
        self._main_controller = main_controller
        
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def _playBackward(self, **kwargs):
        pass
    
    @abstractmethod
    def _playFordward(self, **kwargs):
        pass

    @abstractmethod
    def _setMode(self, **kwargs):
        pass
    
class FFFreeRide(FSMMainController):
    
    def __init__(self, main_controller):
        FSMMainController.__init__(self, main_controller)
        
    def execute(self):
        pass

    def _playBackward(self, **kwargs):
        pass
    
    def _playFordward(self, **kwargs):
        pass

    def _setMode(self, **kwargs):
        pass
    
class RWRide(FSMMainController):
    
    def __init__(self, main_controller):
        FSMMainController.__init__(self, main_controller)
        
    
    def execute(self):
        pass

    def _playBackward(self, **kwargs):
        raise Exception("Unable to playBackward in this mode")
    
    def _playFordward(self, **kwargs):
        raise Exception("Unable to playForward in this mode")

    def _setMode(self, **kwargs):
        pass
    
class UserControl(FSMMainController):
    def __init__(self, main_controller):
        FSMMainController.__init__(self, main_controller)
        
    def execute(self):
        pass

    def _playBackward(self, **kwargs):
        pass
    
    def _playFordward(self, **kwargs):
        pass

    def _setMode(self, **kwargs):
        pass
    
class Stepper():
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def _stepForward(self, **kwargs):
        pass
    
    @abstractmethod
    def _stepBackward(self, **kwargs):
        pass
    
class NonStep(Stepper):
    
    def _stepForward(self, **kwargs):
        raise Exception("Unable to stepForward in this mode")
    
    def _stepBackward(self, **kwargs):
        raise Exception("Unable to stepBackward in this mode")
    