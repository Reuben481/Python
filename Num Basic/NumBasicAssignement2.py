# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:21:46 2016

@author: reuben
"""
from scipy import *
from pylab import *
from scipy.integrate import quad
import sys


def adaptive_simpsons (a,b,f):
    """
    takes in end points as well as function to produce simpsons 
    expression for integral Î[a,b] =ish quad(f(x))
    """
    b=float(b)
    a=float(a)
    return ((b-a)/6)*(f(a)+4*(f((a+b)/2)+f(b)))
def testfunction(x):
    return sqrt(abs(x))
print("adaptive_Simpsons =", adaptive_simpsons(-1,1,testfunction))
print("quad =",quad(testfunction,-1,1))

def composite1 (a,b,i,f):
    a=float(a)
    b=float(b)
    
#print(composite1(-1,1,9,testfunction))

def composite2 (a,b,i,f):
    xx=linspace(a,b,i)
    u,=xx.shape
    A=0
    B=0
    if i>500:
        for z in range(0,u-1):
            A+=adaptive_simpsons(xx[z],xx[z+1],f)
        return A
        
    else:
        i+=1
        for z in range(0,u-1):
            B+=adaptive_simpsons(xx[z],xx[z+1],f)
        return composite2(a,b,i,f)
print(composite2(-1,1,1,testfunction))

def composite(a,b,er):
    intervalList=[]
    
    a=float(a)
    b=float(b)
    f=testfunction
    A=adaptive_simpsons(a,b,f)
    B=adaptive_simpsons(a,(a+b)/2,f)+adaptive_simpsons((a+b)/2,b,f)
    #run formula to estimate integral with simpsons (I(f))
    # result = A
    
    #run formula to estimate integral with simpsons with split interval (Q(f))
    # result = B
    error = abs(B-A)

    if error < 15*er:
        return error,intervalList
    else:
        a=(a+b)/2
        error += (composite(a,(a+b)/2,er/2)[0] + composite((a+b)/2,b,er/2)[0])
        intervalList.append(composite(a,(a+b)/2,er/2)[1] + composite((a+b)/2,b,er/2)[1])
        print(a)        
        return error,intervalList
#print(composite(-1,1,1.e-5))

            
        
        
  

    
    
    
    