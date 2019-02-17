#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from random import shuffle

from phenomena.particles.transformations.selections import TypeSelector, ChannelSelector
from kinematicscontroller import KinematicsController, VirtualKinematicsController
from phenomena.particles.transformations.types.decaysviavirtual.virtualparticlechannel import VirtualParticleChannel
from phenomena.particles.transformations.time import TimeController

class TransformController(object):
    '''
    Manages a list of transformationtype objects
    Manages the creation and selection of transformations
    Implements online & offline selections
    '''

    def __init__(self, particle, classlist):
        self._particle = particle
        self._setTransformationList(classlist)
        self._buildTransformations() ## las one needed for online selections
        self._selectType()
        self._selectChannel()
        self._useVirtual()
        self._setTime()


    def _setTransformationList(self, classlist):
        '''
        Sets list of all transformation objects
        If self._particle.lifetime == -1, it should not add the Decay tranformation
        If the Decay tranf is in the list, it should not include NoTransformation for self._particle.lifetime != -1 particles. We asume Decay is always present.
        '''
        objectlist = []
        for transformationclass in classlist:
            if all([self._particle.lifetime != -1, transformationclass.__name__ != 'NoTransformation']):
                objectlist.append(transformationclass(self._particle))
            elif all([self._particle.lifetime == -1, transformationclass.__name__ != 'Decay']):
                objectlist.append(transformationclass(self._particle))
        self._transformationlist = objectlist

    def _buildTransformations(self):
        '''
        For each transformation possible for the particle, build list.
        '''
        allTransformations = []
        newtransformationlist =[]
        for transf in self._transformationlist :
            item = transf.values
            if item:
                allTransformations.append(item)
                newtransformationlist.append(transf)
            else:
                pass

        self._transformationlist = newtransformationlist
        self._allTransformations = allTransformations

    def _selectByType(self, type):
        return [element for element in self._allTransformations if element.type == type][0]

    def _selectType(self):
        '''
        From all the possible transformations, choose one
        '''
        self._selectedType = TypeSelector(self._allTransformations).value

    def _selectChannel(self):
        '''
        From all the possible channels, choose one
        '''
        try:
            channel = ChannelSelector(self._selectedType.channels.all).value
        except:
            channel = []
        finally:
            self._selectedChannel = channel

    def _useVirtual(self):
        '''
        If the flag DECAYTHROUGHVIRTUAL is set in the model, check if 3body decay and change self._selectedChannel to 2body with virtual
        '''
        self._virtual = False
        if self._particle.__class__.DECAYTHROUGHVIRTUAL == True:
            if len(self.selectedChannel) == 3 and self._selectedType.type == "Decay":
                virtualchannel = VirtualParticleChannel(self._particle,self._selectedChannel.names).getValues()
                if virtualchannel != []:
                    self._virtual = True
                    self._selectedChannel = virtualchannel
                else:
                    pass
        else:
            pass


    def _buildOutput(self):
        '''
        Get de list of output particles boosted values.
        Different classes if virtual or not.
        '''
        if self.selectedType.type != 'NoTransformation':
            if not self._virtual:
                return KinematicsController(self._particle).getFinalState()
            else:
                return VirtualKinematicsController(self._particle).getFinalState()
        else:
            return []

    def _setTime(self):
        try:
            if self._particle.virtuality==0:
                self._time = TimeController.getTime()
            else:
                self._time = 0.5
        except:
            self._time = TimeController.getTime()


    @property
    def allTypes(self):
        return self._allTransformations

    @property
    def selectedType(self):
        return self._selectedType

    @property
    def target(self):
        try:
            target = self._selectedType.target
        except:
            target = None
        finally:
            return target

    @property
    def selectedChannel(self):
        try:
            channel = self._selectedChannel.names
        except:
            channel = []
        finally:
            return channel

    @property
    def output(self):
        return self._buildOutput()

    @property
    def transformtime(self):
        return self._time

    def query(self, dt=1./60.):
        output = []
        shuffle(self._transformationlist)
        for transf in self._transformationlist:
            probability = transf.getProbability(dt)
            if TypeSelector.getDecision(probability):
                self._selectedType = self._selectByType(transf.name)
                self._selectChannel()
                output = self.output
                break
        return output
