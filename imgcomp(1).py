# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:36:19 2016

@author: reuben
"""

from scipy import misc
import numpy as np
from PIL import Image


im = array(Image.open('kalle.jpg').convert('L'),'f')

def HWTGen(a):
    u,v = a.shape
    for i in range (u-1):
        a[i][2*i:2*i+2]=1/sqrt(2)
    for i in range (u/2):    
        a[i+u/2][2*i]=-1/sqrt(2)
        a[i+u/2][2*i+1]=1/sqrt(2)
    return a
    
def imfix(a):
    u,v=a.shape
    if u%2!=0:
        a=np.delete(a,(u-1),axis=0)
    if v%2!=0:
        a=np.delete(a,(v-1),axis=1)
        return a
    else:
        return a
def zerosgen(a):
    u,v=a.shape
    h=zeros((u,u))
    i=zeros((v,v))
    return h,i
def imcomp (a):
    ac=imfix(a)
    u,v=ac.shape
    i,j=zerosgen(ac)
    HWT=HWTGen(i)
    HWTT=transpose(HWTGen(j))
    cim=dot(dot(HWT,ac),HWTT)
    
    return cim
def bananasplit(a):
    u,v=a.shape
    w=a[0:u/2,0:v/2]
    x=a[(u/2):u,0:v/2]
    y=a[0:u/2,(v/2):v]
    z=a[(u/2):u,(v/2):v]
    return w,x,y,z
def bananaunsplit(a,b,c,d):
    h=vstack((a,b))
    r=vstack((c,d))
    return hstack((h,r))

def inversetrans(a):
    u,v=a.shape
    ac=imfix(a)
    u,v=ac.shape
    i,j=zerosgen(ac)
    HWT=transpose(HWTGen(i))
    HWTT=HWTGen(j)
    cim=dot(dot(HWT,ac),HWTT)
    return cim
def badway(a):
    x,y=a.shape
    l=[]
    l1=[]
    l2=[]
    l3=[]
    for i in range(x):
        for j in range(1,y):
            v1=a[i][j-1]
            v2=a[i][j]
            if j%2==0:
                l.append((v1+v2)/sqrt(2))
                l1.append((v2-v1)/sqrt(2))
    r=array(l)
    z=array(l1)
    r1=r.reshape(x,-1)
    z1=z.reshape(x,-1)
    HT=column_stack((r1,z1))
   
    
    a,b=HT.shape
    for i in range(a-1):
        for j in range(b):
            v1=HT[i][j]
            v2=HT[i+1][j]
            if i%2==0:
                l2.append((v1+v2)/sqrt(2))
                l3.append((v2-v1)/sqrt(2))
    L2=array(l2)
    L3=array(l3)
    a,=L2.shape
    if a%x!=0:
        for i in reversed(range(a-(a%x),a)):
            L2=np.delete(L2,i)
            L3=np.delete(L3,i)
    HTW=vstack((L2.reshape(x/2,-1),L3.reshape(x/2,-1)))
    return HTW
def decomp (a,h):
    k=0
    w=a
    while k<h:
        k+=1
        i,j=w.shape
        r=np.zeros((i,j))
        w=inversetrans(bananaunsplit(w,r,r,r))
    return w
def recomp(a,h):
    u,v=a.shape
    i=0
    im4=a
    while i<h:
        i+=1
        w,x,y,z=bananasplit(imcomp(im4))
        im4=w
    return im4

misc.imsave('kvinnacomp.jpg',imcomp(im))
misc.imsave('kvinnabadway.jpg',badway(im))
it=3
u=np.count_nonzero(im)
v=np.count_nonzero(imcomp(im))
print(u)
print(v)
#v=np.count_nonzero(z)
#print(float(v)/float(u))
#misc.imsave('recomp1.jpg',z)
#misc.imsave('decomp1.jpg',decomp(z,it))


    