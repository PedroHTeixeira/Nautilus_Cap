import numpy
import random

class Signal():
    
    def __init__(self,label):
        self.label = label
        self.waves = numpy.random.normal(-1,1,size=50)
        self.tx=5
        self.amp= sum(list(self.waves))/len(list(self.waves))

    def __repr__(self):
        return "The signal {} has {} of amplitude and {} of recording tax. The signal is {}{}".format(self.label,self.amp,self.tx,self.waves,"\n")

    def __sub__(self,other):
        if type(self)==type(other):
            w = Signal(self.label + "-" + other.label)
            w.waves=self.waves - other.waves
            return w

    def __add__(self,other):
        if type(self)==type(other):
            w = Signal(self.label + "+" + other.label)
            w.waves=self.waves + other.waves
            return w

    def __gt__(self,other):
        if type(self)==type(other):
            return self.amp > other.amp

    def __mul__(self, other):
        if type(self)==type(other):
            w = Signal(self.label + "*" + other.label)
            w.waves = numpy.array(list(self.waves) + list(other.waves))
            return w

    def __lt__(self,other):
        if type(self)==type(other):
            return self.amp < other.amp

    def __eq__(self,other):
        if type(self)==type(other):
            return self.amp == other.amp

    def __ne__(self,other):
        if type(self)==type(other):
            return self.amp != other.amp

    def __getitem__(self, index):
        a=list(self.waves)
        self.waves = a[index]
        return self


signal1=Signal("Track 1")
signal2=Signal("Track 2")
signal3=signal1+signal2
signal4=signal1-signal2
signal5=signal1*signal2
signals = [signal1,signal2,signal3,signal4,signal5]
signals.sort()
print(signal1)
print(signal2)
print(signal3)
print(signal4)
print(signal5)
print(signals)
print('This is slicing: {}'.format(signal1[3:9]))