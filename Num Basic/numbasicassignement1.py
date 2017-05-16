# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:08:43 2016

@author: reuben
"""
from scipy import *
from pylab import *
import numpy as np
from matplotlib.pyplot import *
import sys

x=array([-1.,0.,2.,3.])
y=array([2.,6,4,30])
"""
print(x.shape)
z,=x.shape
p=np.poly1d([1,2])
u=np.poly1d([1,1,4])
print(u*p)
"""
def polyr(a,b):
    """
    input: array of x values and y values of the function. Returns 
    as many nodes as there are values in the arrays.
    Array should be of the same dimensions, and always (1,n) in shape. 
    """
    
    l=[]
    l1=[]
    l2=[]
    l3=[]
    for i in a:
        l.append(np.poly1d([1,-i]))
    for h in l:
        product=1   
        for z in l:
            if h!=z:
                product*=z
        print(product)
        l1.append(product)
    for i in a:
        r=1
        for h in l:
            if h(i)!=0:
                r*=h(i)
        l2.append(r)
        print(l2)
    u,=a.shape
    for i in range (u):
        l3.append(l1[i]/l2[i])
    lgp=0
    for i in range (u):
        lgp+=l3[i]*b[i]
    return lgp 

print(polyr(x,y))
xxa=linspace(-1,1,5)
xxb=linspace(-1,1,12)
xxc=linspace(-1,1,15)
xxd=linspace(-1,1,21)
x1=linspace(-1,1,100)
y1=e**(-4*xxa**2)
y2=e**(-4*xxb**2)
y3=1/(1+25*xxc**2)
y4=1/(1+25*xxd**2)

p1=polyr(xxa,y1).c
p2=polyr(xxb,y2).c
p3=polyr(xxc,y3).c
p4=polyr(xxd,y4).c
print("p2=",p2)
plot(x1,polyval(p1,x1))
plot(x1,polyval(p2,x1))
figure()
title('easy as 1,2,3')
plot(x1,polyval(p3,x1))
#plot(x1,polyval(p4,x1),label='yourmother')
          
        

        

        

    