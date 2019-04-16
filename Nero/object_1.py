
from __future__ import division
import numpy as np
import os
import sys

# method template
method = dict(name = 'method1',
              statediff = 1.0,
              funcalls = [],
              parametercalls = [])

class method_encap(object):
    def __init__(self,methodlist=None):
        if methodlist is None:
            self.name = 'method1'
        else:
            self.name = 'method' + str(len(methodlist))
        self.statediff = 0
        self.funccalls = []
        self.parametercalls = []

    def addcall(self,func,paramlist):
        self.funccalls.append(func)
        self.parametercalls.append(paramlist)

class ObjectOne(object):
    def __init__(self):
        self.__param_1__ = 0
        self.max_val = 100
        self.log_method = True
        dirname = os.path.dirname(__file__)
        try:
            self.methods = np.load(os.path.join(dirname,'methods.npy'))
        except Exception:
            self.methods = [] # (listofDict)
        self.currentmethod = method_encap()
    
    def addnm(self, list):
        if self.log_method:
            self.currentmethod.addcall('addnm',list)
        if len(list) >1:
            # try:
            return lambda x,y: x+y, list
            # except Exception:
            #     pass
        else:
            # try:
            return list[0]+1
            # except Exception:
            #     pass

    def subnm(self,list):
        if self.log_method:
            self.currentmethod.addcall('subnm',list)
        if len(list)>1:
            try:
                return list[0] - list[1]
            except Exception:
                pass
        else:
            return list[0]-1

    def setattr(self,list):
        if self.log_method:
            self.currentmethod.addcall('setattr',list)
        setattr(self,list[0],list[1])

    def cns(self):
        exit_condition = False
        prev_state = self.state()
        prev_parameter = self.__param_1__
        self.__param_1__ = getattr(self, 'subnm')(['__param_1__'])
        new_state_1 = self.state()
        self.__param_1__ = getattr(self, 'addnm')([prev_parameter])
        new_state_2 = self.state()
        if max(new_state_1,new_state_2,prev_state) ==prev_state:
            return
        elif new_state_1 > new_state_2:
            func = 'subnm'
        else:
            func = 'addnm'

        while not exit_condition:
            self.__param_1__ = getattr(self,func)([self.__param_1__])
            if self.state() >= self.max_val:
                print('exit condition reached.')
                print('parameter ' + str(self.__param_1__))
                print('state ' + str(self.state()))
                exit_condition = True



    def state(self):
        return 0.1*self.__param_1__

object1 = ObjectOne()
object1.cns()