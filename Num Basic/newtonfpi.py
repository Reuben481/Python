# -*- coding: utf-8 -*-
"""
Created on Tue May 31 13:06:31 2016

@author: reuben
"""
from scipy import*
from scipy import interpolate
from pylab import *
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
import sys

ah=0.1
an=100
aalpha=pi/2
aomega=0
at=0
def f(a):
    beta=9.81
    return (-beta*sin(a))
    
def fu(h,alpha,omega,n,t):
    """Trapezoidal interpolation of second order differential equation.
    f = second derivative with respect to the original integral.(input=fn)
    Omega = first derivative in numerical basis.(input=init val)
    Alpha = function being interpolated.(input=init val)
    """
    v=array([alpha,omega,t])
    l=[alpha]
    l1=[omega]
    l2=[t]
    for i in range(1,n):
        k1a=h*omega
        k1b=h*f(alpha)
        k2a=h*(omega+k1b)
        k2b=h*f(alpha+k1a)
        alpha+=(k1a+k2a)/2
        omega+=(k1b+k2b)/2
        t+=h
        l.append(alpha)
        l1.append(omega)
        l2.append(t)
        v=vstack((v,(alpha,omega,t)))
        i+=1
    return v,l,l1,l2

print(fu(ah,an,aalpha,aomega,at))
def newtonfpi(h,alpha,omega,t):
    l2=[t]
    for i in range(100):
        k1a=h*omega
        k1b=h*f(alpha)
        k2a=h*(omega+k1b)
        k2b=h*f(alpha+k1a)
        alpha=(k1a+k2a)/2
        h=(k1b+k2b)/2
        t-=h
        l2.append(t)
    return l2
def newtonfpi(h,alpha,omega,t):
    l2=[t]
    for i in range(10):
        k1a=h*omega
        k1b=h*f(alpha)
        k2a=h*(omega+k1b)
        k2b=h*f(alpha+k1a)
        alpha=(k1a+k2a)/2
        alpha/omega=(k1b+k2b)/2
        h=omega
        
        t-=h
        l2.append(t)

#print(newtonfpi(29,pi/2,0,0))
#plot(newtonfpi(0.1,pi/2,0,0)[1])