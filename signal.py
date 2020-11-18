import numpy
import random

class Signal():
    
    def __init__(self,label):
        self.label = label
        self.amp = numpy.random.normal(-1,1,size="50")
        self.tx=5

    def __repr__(self):
        return "The signal {} has {} of amplitude and {} of recording tax ".format(self.label,self.amp,self.tx)

    def __sub__(self,other):
        if type(self)==type(other):
            self.label= self.label + "-" + other.label
            return self.amp - other.amp

    def __add__(self,other):
        if type(self)==type(other):
            self.label= self.label + "+" + other.label
            return self.amp + other.amp

    def __gt__(self,other):
        if type(self)==type(other):
            return self.amp > other.amp

    def __mul__(self, other):
        if type(self)==type(other):
            self.label= self.label + "*" + other.label
            return self.amp + other.amp

    def __lt__(self,other):
        if type(self)==type(other):
            return self.amp < other.amp

    def __eq__(self,other):
        if type(self)==type(other):
            return self.amp == other.amp

    def __ne__(self,other):
        if type(self)==type(other):
            return self.amp != other.amp


signal1=Signal("Track 1")

print(signal1)