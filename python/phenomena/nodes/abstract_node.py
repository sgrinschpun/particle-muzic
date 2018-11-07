# Author: Cristobal Pio
# Company: IFAE
# Date: 4 November 2018
# Mail: cgarcia@ifae.es
# Information:

from abc import ABCMeta, abstractmethod

class Node():
    __metaclass__ = ABCMeta
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def configure(self, configure_message):
        pass
    