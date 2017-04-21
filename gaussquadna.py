# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:58:16 2017

@author: reuben
"""

from math import sqrt
from numpy import*
from scipy.linalg import *
import matplotlib.pyplot as plt
from scipy import*
from scipy.integrate import quad

class gaussquadr(object):
    """
    Coded the Three Term Recurrence relation for educational purposes. However, 
    as has been mentioned before, the GS method has a large degree of error.
    This orthogonal polynomial only takes w(x)=1. 
    Increase in polynomial compared to the polynomial being approximated appears
    increase the accuracy. 
    All roots are real and are in (a,b)
    """

    def __init__(self,interval,fcn,n,disc):
        self.i=interval
        self.f=fcn
        self.n=n
        self.d=disc
        self.xl=None
        self.yl=None
        self.lg=None
        self.phil=None
        self.counter=0

#Hardcoded version of alpha gen.
    def hcalpha(self):
        self.phil=[self.one]
        a,b=self.i
        x=linspace(a,b,self.d)
        i=self.counter
        phi=self.phil[i](x)
        return norm(phi*x**2,1)/norm(phi*x,1)

#general version of alpha gen(sort of, no weight function included as of yet).. 
    def alpha(self):
        a,b=self.i
        x=linspace(a,b,self.d)
        i=self.counter
        phi=self.phil[i](x)
        return norm((phi**2)*x,1)/norm(phi**2,1)


#general version of beta gen (sort of, see alpha )
    def beta(self):
        a,b=self.i
        i=self.counter
        phi1=self.phil[i-1]
        phi2=self.phil[i]
        x=linspace(a,b,self.d)
        return norm(phi2(x)**2,1)/norm(phi1(x)**2,1)


    def one(self,a):
        return poly1d([1])(a)


#Three term Recurrence relation
    def TTRR(self):
        if self.phil==None:
            self.phil=[self.one]
            self.phil.append(poly1d([1,-self.alpha()]))
            self.counter+=1
        self.phi=1
        a,b=self.i
        while self.counter < self.n:
            alpha=self.alpha()
            beta=self.beta()
            phil=self.phil
            i=self.counter
            if i==1:
                phinew=poly1d([1,-alpha])*phil[i]-beta
                self.phil.append(phinew)
                self.counter+=1
                if self.n==2:
                    return self.phil[self.counter]
                
            i=self.counter
            phinew=poly1d([1,-alpha])*phil[i]-phil[i-1]*beta
            self.phil.append(phinew)
            self.counter+=1
        return self.phil[self.counter]
    #pats lagrange method, modified to only return the unadded lg pols

    def lagrange(self):# returns the lagrange interpolating polynomial
        self.xl=self.TTRR().r
        self.lg=[]
        tmp = poly1d([0])
        x=self.xl
        for i in range(len(x)): # create a basis polynomial for each point
            numerator=poly1d([1]) #create empty 1st order polynomial 
            denom = 1.0     #set denominator equal 1.0
            for j in range(len(x)): #for each of the x values 
                if (x[i] != x[j]): # use all other x values
                    tmp = poly1d([1,-x[j]]) # create polynomical x-xj
                    numerator = numerator * tmp #multiply by numerator
                    denom = denom * (x[i] - x[j]) # multiply denominator by (xi-xj)
                    tmp = (numerator/denom)
            self.lg.append(tmp) 
            
    def quadr(self):
        if self.lg==None:
            self.lagrange()
        cl=[]
        a,b=self.i
        for i in self.lg:
            cl.append(quad(i,a,b)[0])
        return sum(cl*self.f(self.xl))
        
    def initref(self):
        a,b=self.i
        l=[]
        n=self.n
        for i in range(0,n+1):
            l.append((a+b)/2+((b-a)/2)*cos(((2*i-1)/(2*n))*pi))
        return(sort(l))      
        
#%%
#==============================================================================
# Cell-1- plots and plot functions. 
#==============================================================================


def rn(x):
    return 1/sqrt(log(x))
#print(gaussquadr((0,1),poly1d([0,1]),5,10000).TTRR().r)
phi=gaussquadr((1,30),rn,5,1000).TTRR()
#print(phi.r)
print(phi)
xx=linspace(0,1,1000)
#print("dotproduct",phi(xx)@poly1d([1,2,3,0,0])(xx)/1000)
def r(x):
    return abs(1/(1+25*x**2))
    
poly=poly1d([1,2,3,4,5])
print("gaussquadrature:",0.765*gaussquadr((1,30),rn,5,10000).quadr())
print("quad in-built",0.765*quad(rn,1,30)[0])

def fcn(x):
    return sin(x)+cos(x)


print(gaussquadr((pi/3,5*pi/3),fcn,4,1000).TTRR())
xx=linspace(pi/3,5*pi/3,1000)
a, = plt.plot(xx,fcn(xx),label='sin(x)+cos(x)', color='blue')

def lagrange(x,y): # accepts lists of x and y coordinates
                    # returns the lagrange interpolating polynomial
    tmp = poly1d([0])
    result=poly1d([0])

    for i in range(len(x)): # create a basis polynomial for each point
        numerator=poly1d([1]) #create empty 1st order polynomial 
        denom = 1.0     #set denominator equal 1.0
        for j in range(len(x)): #for each of the x values 

            if (x[i] != x[j]): # use all other x values
                tmp = poly1d([1,-x[j]]) # create polynomical x-xj
                numerator = numerator * tmp #multiply by numerator
                denom = denom * (x[i] - x[j]) # multiply denominator by (xi-xj)
        tmp = (numerator/denom) * y[i] # multiply basis polynomial with corresponding y value
        result = result + tmp # sum all basis polynomials
    return result

xg=[pi-(sqrt(2)*pi/3),pi,pi+(sqrt(2)*pi/3)]
yg=[sin(i)+cos(i) for i in xg]
print(lagrange(xg,yg))

b, = plt.plot(xx,lagrange(xg,yg)(xx),label='p*(x)', color='orange')

def signcount(xx,xxx):
    l=[]
    l1=[]
    signcount=0
    for i in range(1,len(xx)):
        if sign(xx[i])!=sign(xx[i-1]):
            signcount+=1
            l.append(xxx[i])
            l1.append(i)
    return l,l1

ly=sin(xx)+cos(xx)-lagrange(xg,yg)(xx)
print(signcount(ly,xx))
sgn=signcount(ly,xx)[0]
sgny=lagrange(xg,yg)(sgn)
print(sgny)
arsgn=array(sgn)
arsgny=array(sgny)
plt.plot(arsgn,arsgny,'ro')
plt.legend(handles=[a,b])
plt.ylabel("y")
plt.xlabel("x")

print(quad(lagrange(xg,yg),pi/3,sgn[0])[0]-quad(lagrange(xg,yg),sgn[0],sgn[1])[0]+quad(lagrange(xg,yg),sgn[1],sgn[2])[0]-quad(lagrange(xg,yg),sgn[2],5*pi/3)[0])
print(sum(abs(sgny)))
#%%

#%%
def polist(n):
    l=[]
    l1=[]
    l2=[]
    for i in range(n):
        pl=hstack((array([1]),zeros(i,)))
        l.append(poly1d(pl))
        l1.append(abs(gaussquadr((0,1),l[i],i+2,1000).quadr()-quad(l[i],0,1)[0]))
        l2.append(quad(l[i],0,1)[1])
    return sum(l1)/len(l1),sum(l2)/l2
polist(5)



#%%
