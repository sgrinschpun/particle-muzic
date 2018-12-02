#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from random import shuffle

from phenomena.particles.transformations.selections import TypeSelector, ChannelSelector
from kinematicscontroller import KinematicsController
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
        self._setTime()

    def _setTransformationList(self, classlist):
        '''
        Sets list of all transformation objects
        '''
        objectlist = []
        for transformationclass in classlist:
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

        # if decay values list is [] keep NoTransformation
        # if decay values list is not [] get rid of Notransformaton
        #spaghetti
        # if not any('Decay' in item['type'] for item in allTransformations):
        #     allTransformations.append({'type':'NoTransformation'})

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
            channel = ChannelSelector(self._selectedType.list).value
        except:
            channel = []
        finally:
            self._selectedChannel = channel

    def _buildOutput(self):
        '''
        Get de list of output particles boosted values
        '''
        return KinematicsController(self._particle).getFinalState() if self.selectedType != 'NoTransformation'else []

    def _setTime(self):
        self._time = TimeController.getTime()

    @property
    def allTypes(self):
        return self._allTransformations

    @property
    def selectedType(self):
        return self._selectedType.type

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
            channel = self._selectedChannel.particles
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
                print transf.name
                self._selectedType = self._selectByType(transf.name)
                self._selectChannel()
                output = self.output
                break
        return output
