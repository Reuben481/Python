# -*- coding: utf-8 -*-
"""
Created on Sun May 29 16:44:27 2016

@author: reuben
"""

def fu(h,alpha,omega,n,t):
    """Trapezoidal interpolation of second order differential equation.
    f = second derivative with respect to the original integral.(input=fn)
    Omega = first derivative in numerical basis.(input=init val)
    Alpha = function being interpolated.(input=init val)
    """
    v=array([alpha,omega,t])
    l=[]
    l1=[]
    l2=[]
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