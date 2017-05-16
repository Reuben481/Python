# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:00:03 2016

@author: reuben
"""
#Task 1(b-d)
from scipy import*
from scipy import interpolate
from pylab import *
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
import sys

def f(a):
    beta=9.81
    return (-beta*sin(a))
#variables

ah=0.01
an=500
aalpha=pi/2
aomega=0
at=0
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

print(fu(ah,aalpha,aomega,an,at)[0])
plot(fu(ah,aalpha,aomega,an,at)[3],fu(ah,aalpha,aomega,an,at)[1],linewidth=3.0)
scatter(fu(ah,aalpha,aomega,an,at)[3],fu(ah,aalpha,aomega,an,at)[2])
v=[0,5,-5,5]
axis(v)
#hobs=0.1
#nobs=100
#alphaobs=pi/2
#omegaobs=0
#tobs=0
#print(fu(hobs,alphaobs,omegaobs,nobs,tobs)[0])
#plot(fu(hobs,alphaobs,omegaobs,nobs,tobs)[1])
#plot(fu(hobs,alphaobs,omegaobs,nobs,tobs)[2]) 

#Task 2        
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

r=array(fu(ah,aalpha,aomega,an,at)[3])#t
a=array(fu(ah,aalpha,aomega,an,at)[2])#omega
b=array(fu(ah,aalpha,aomega,an,at)[1])#alpha

z=[fub(a[0:3],r[0:3])]
#for i in range(1,len(a)-2):
#    fi=fub(a[i:i+3],r[i:i+3])
#    z.append(fi)
#
#y=[fub(a[0:3],b[0:3])]
#for i in range(1,len(a)-2):
#    fi=fub(a[i:i+3],r[i:i+3])
#    y.append(fi)

def fuba(x,y):
    alphaobs=2*pi/3
    for i in range(1,len(a)-2):
        t=x[i]
        fi=fub(x[i:i+3],y[i:i+3])
        if abs(fi(t)-alphaobs)<=1.e-2:

            return abs(fub(x[i:i+3],y[i:i+3])(t)-alphaobs),i
    



#def newtonfpi(h,alpha,omega,t):
#    l1=[alpha]
#    l2=[t]
#    for i in range(30):
#        k1a=h*omega
#        k1b=h*f(alpha)
#        k2a=h*(omega+k1b)
#        k2b=h*f(alpha+k1a)
#        alpha+=(k1a+k2a)/2
#        omega+=(k1b+k2b)/2
#        h+=alpha/-omega
#        
#        t+=h
#        l1.append(alpha)
#        l2.append(t)
    return l2,l1
def fpir(h,alphainit,alphanew,omegainit,omeganew,n):
    alpha=alphanew
    omega=omeganew
    g=-9.81
    l=1
    v=array([alpha,omega])
    l1=[alpha]
    l2=[omega]    
    for i in range(1,n):
        alphanew=alpha-(h/2)*omega-alphainit-(h/2)*omegainit
        omeganew=omega+(h/2)*(g/l)*sin(alpha)-omegainit+(h/2)*(g/l)*sin(alphainit)
        if abs(alphanew-alpha)<=1.e-3:
            return omega, alpha
        alphainit=alpha
        omegainit=omega
        alpha=alphanew
        omega=omeganew
        v=vstack((v,(alphanew,omeganew)))
        l1.append(alpha)
        l2.append(omega)
        v=vstack((v,(alpha,omega)))
        i+=1
    return v, l1,l2
xx=fu(ah,aalpha,aomega,an,at)[1]
xy=fu(ah,aalpha,aomega,an,at)[2]

i=0
def fpirit(n,h):
    l=[]
    l1=[]
    for i in range(n):
        l.app
        
        
print(fpir(0.1, pi/2,pi/2,0,-0.981,  100)[0])
#plot(fpir(0.1, pi/2,pi/2,0,0,  200)[2])
#plot(fpir(0.1, pi/2,pi/2,0,0,  200)[1])

    
#xx=linspace(0,0.1,100)
#for i in xx:
#    print(fpir(0.1, pi/2,1.52,0,-0.981,  100))
#plot(fpir(0.1, pi/2,1.52,0,-0.981,  1000)[1])
#print(sqrt((1.13**2)+(2.81**2))/sqrt((0.3**2)+(0.6)**2))

        
        
        

        
