# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 18:20:34 2016

@author: reuben
"""

xx=trapfunc(ah,aalpha,aomega,an,at)[1]
xy=trapfunc(ah,aalpha,aomega,an,at)[2]
for i in range(len(xx)):
        fpir(0.1,pi/2,xx[i],0,xy[i],100)