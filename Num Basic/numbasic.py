# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:03:32 2016

@author: reuben
"""

from scipy import *
from pylab import *
from scipy.integrate import quad
import sys
"""
x=linspace(0.8,1.8,50)
y=linspace(-0.5,0.6,50)
figure(1)
M=200.
plot(y,1/2-1/(1+M*abs(x-1.05)))
title("fig M")
figure(2)
N=200000.
plot(y,1/2-1/(1+N*abs(x-1.05)))
title("fig N")
"""
x=range(-1,3)
y=[2,6,4,30]
p2=polyfit(x,y,3)
print(p2)
xx=linspace(-2,4,200)
plot(xx,polyval(p2,xx))

x=rand(4)
print(x)