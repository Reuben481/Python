# -*- coding: utf-8 -*-
"""
Created on Tue May  3 16:15:18 2016

@author: reuben
"""

from scipy import *
from pylab import *
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
import sys

def x(a):
    return e**-100*a
def y(a):
    return (1/99)*((e**-99*a)+(100/e**a))
def expEulera(a,b,f,h):
    c=0    
    l=[]
    yi=f(a)
    while c*h+a<b:
        yi=yi+h*-100*e**-100*(a+(c-1)*h)
        l.append(yi)
        c+=1
    return l

xs=expEulera(0,1,x,0.1)
plot(linspace(0,1,len(xs)),xs)
def impEulera(a,b,f,h):
    c=0    
    l=[]
    yi=f(a)
    while c*h+a<b:
        yi=yi+h*-100*e**-100*(a+c*h)
        l.append(yi)
        c+=1
    return l
xy=impEulera(0,1,x,0.1)
print("ea=",expEulera(0,1,x,0.1))
print("ia=",impEulera(0,1,x,0.1))
plot(linspace(0,1,len(xy)),xy)
xx=linspace(0,1,len(xy))
l=[]
for i in xx:
    l.append(x(i))
plot(xx,l)
def derivatron(a):
    return (-100/99)*e**(-100*a)*((e**100*a)+1)
def expEulerb(a,b,f,h):
    c=0    
    l=[]
    yi=f(a)
    while c*h+a<b:
        yi=yi+h*derivatron((a+(c)*h))
        l.append(yi)
        c+=1
    return l 
def impEulerb(a,b,f,h):
    c=0    
    l1=[]
    yi=f(a)
    while c*h+a<b:
        yi=yi+h*derivatron(a+(c+1)*h)
        l1.append(yi)
        c+=1
    return l1
print(expEulerb(0,1,y,0.1))
print(impEulerb(0,1,y,0.1))

figure()
xs=expEulerb(0,1,x,0.1)
plot(linspace(0,1,len(xs)),xs)
xy=impEulerb(0,1,x,0.1)
#plot(linspace(0,1,len(xy)),xy)
l=[]
for i in xx:
    l.append(y(i))
#plot(xx,l)

    
        
    