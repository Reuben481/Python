# -*- coding: utf-8 -*-
"""
Created on Sun May  1 19:29:49 2016

@author: patrickleacy
"""

from scipy import *
from pylab import *
import numpy as np
from scipy.integrate import quad
from matplotlib.pyplot import *
import sys
#from mpl_toolkits.mplot3d import Axes3D
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')



#a = [0.1,0.2,0.3,0.4,0.5]
#b = [1,1.25,1.5,1.75]
#c = [1,0.5,0.25,0.125,0.0625,0.03125,0.015625,0.0078125]
#
#out = []
#for i in a:
#    e = i
#    for j in b:
#        for k in c:
#            d = math.sqrt((j*k-i)**2)
#            if d<e:
#                e=d
#                bv = j
#                cv = k
#    out.append([bv,cv,e])
#print(out)


def y1(t):
    return ((-1/99)*math.exp(-100*t))+(100/(99*math.exp(t)))
    
def y2(t):
    return math.exp(-100*t)
    
def fun2(t):
    return [y1(t),y2(t)]

def expEuler(y0,f,t0,te,h):
    c = 0
    ti = t0
    yi = array(y0)
    y = [array(y0)]
    while c*h+t0<te:
        print(c)
        z=array([[-1,1],[0,-100]])
        yj = dot(z,yi)
        print(yj)
        yj = [yi[i] + yj[i] * h for i in range(len(yj))] 
        y.append(yj)
        print(h)
        ti += h
        yi = yj
        
        c += 1

    return yj,c,y
    
def impEuler(y0,f,t0,te,h):
    c = 0
    ti = t0
    yi = y0
    y = [y0]
   
    while c*h+t0<te:
        print(c)
        #print(yj)
        #print(yj)
        z=array([[-1,1],[0,-100]])
        yj = np.dot(z,ti)
#        yj = [yi[i] + yj[i] * h for i in range(len(yj))]
        ti += h
        yj=[yj[i] + yi[i] * h for i in range(len(yj))]
        yi=yj
        y.append(yj)
        
        c += 1

    return yj,c,y


#print(expEuler([1,1],fun2,0,1,0.1))
#print(impEuler([1,1],fun2,0,1,0.1))
expeuler=vstack(expEuler([1,1],fun2,0,1,0.1)[2])
impeuler=vstack(impEuler([1,1],fun2,0,1,0.1)[2])
print(expeuler.shape)
print(impeuler.shape)

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100
for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = hstack(expeuler)
    ys = hstack(expeuler)
    zs = linspace(1,3,len(xs))
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

xx=linspace(1,3,20)
z=[]
for i in xx:
    z.append(y1(i))
print(array(z))
h=[]
for i in xx:
    h.append(y2(i))
print(array(h))
    
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#n = 100
#for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#    xs = array(h)
#    ys = array(z)
#    zs = linspace(1,3,len(xs))
#    ax.scatter(xs, ys, zs, c=c, marker=m)
#
#ax.set_xlabel('X Label')
#ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')
#
#plt.show()

