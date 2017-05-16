# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 01:01:27 2016

@author: reuben
"""
from scipy import *
from pylab import *
import numpy as np
from scipy.integrate import quad
from matplotlib.pyplot import *
import sys

def adaptive_simpsons (a,b,f):
    """
    takes in end points as well as function to produce simpsons 
    expression for integral Î[a,b] =ish quad(f(x))
    """
    b=float(b)
    a=float(a)
    return ((b-a)/6)*(f(a)+4*(f((a+b)/2)+f(b)))
    
def tpgr(a,b,f):
    a=float(a)
    b=float(b)
    c1=(b-a)/2
    c2=(b-a)/2
    x1=(1/-sqrt(3))
    x2=(1/+sqrt(3))
    return((b-a)/2)* f(x1)+f(x2)    
def tfs(a):
    return sqrt(abs(a))    
def tfe(a):
    return exp(a**2)
def tfsi(a):
    return sin(a)

def tf2(a):
    return 16*(a**2)+2*a+1
def tf3(a):
    return 3*(a**3)+6*(a**2)+3*a+1
def polynomcheck(a,b,f,i):
    l=[]
    for z in range (i):
        l.append(np.poly1d([1,1]))
    product=1
    for z in l:
        product*=z
    return f(a,b,product)
        
    
def tf1(a):
    return a+1
def rectangleform(a,b,f):
    a=float(a)
    b=float(b)
    return (b-a)*f(a)
fs=tf2
i=-1
j=1
print("rectangle form=",rectangleform(i,j,fs))
print("mpqr=",adaptive_simpsons(i,j,fs))
print("tpgr=",tpgr(i,j,fs))
print("scipy.quad=",quad(fs,i,j))
print("scipy.quad=",quad(poly1d([1,4,6,4,1]),i,j))
print(polynomcheck(i,j,adaptive_simpsons,4))



    


    