# -*- coding: utf-8 -*-
"""
Created on Sun May 29 20:42:06 2016

@author: reuben
"""
from scipy import*
from scipy import interpolate
from pylab import *
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
import sys

ah=0.01
an=500
aalpha=pi/2
aomega=0
at=0


def f(a):
    beta=9.81
    return (-beta*sin(a))
def fub(a,b):
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
        l1.append(product)
    for i in a:
        r=1
        for h in l:
            if h(i)!=0:
                r*=h(i)
        l2.append(r)
    u,=a.shape
    for i in range (u):
        l3.append(l1[i]/l2[i])
    lgp=0
    for i in range (u):
        lgp+=l3[i]*b[i]
    return lgp    


def fubar(h,alpha,omega,n,t):
    """Trapezoidal interpolation of second order differential equation.
    f = second derivative with respect to the original integral.(input=fn)
    Omega = first derivative in numerical basis.(input=init val)
    Alpha = function being interpolated.(input=init val)
    """
    v=array([alpha,omega,t])
    l=[alpha]
    l1=[omega]
    l2=[t]

    alphaobst=-pi/3
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
        t1,t2,t3=l2[i-2],l2[i-1],l2[i]
        a1,a2,a3=l[i-2],l[i-1],l[i]
        falpha=fub(array([t1,t2,t3]),array([a1,a2,a3]))

        fsolve1=falpha
        if falpha(t)<=alphaobst:
            omega=-omega
            alpha=alphaobst
#        if fub(array([t1,t2,t3]),array([a1,a2,a3]))(t)<=alphaobst:
#            omega=-omega
#            alpha=alphaobst
        v=vstack((v,(alpha,omega,t)))
        i+=1
    return v,l,l1,l2
#index taking two same values from list. Change indexing such that the code runs.
figure()
plot(fubar(ah,aalpha,aomega,an,at)[3],fubar(ah,aalpha,aomega,an,at)[1],linewidth=3.0)
scatter(fubar(ah,aalpha,aomega,an,at)[3],fubar(ah,aalpha,aomega,an,at)[2])
v=[0,5,-6,6]
axis(v)

def plotsplit(f):
    n=0
    
    for i in range(len(f[1])-1):
        print(sign(f[2][i]))
        if sign(f[1][i])!=sign(f[1][i+1]):
            pass
        else:
            print(f[2][i])
            if (n*i+i)<=len(f[1]):
                
                plot(f[3][n*i:n*i+i],f[1][n*i:n*i+i])
                plot(f[3][n*i:n*i+i],f[2][n*i:n*i+i])
#plotsplit(fubar(ah,aalpha,aomega,an,at))