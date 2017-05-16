# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 18:57:31 2016

@author: reuben
"""

def fpir(h,alphainit,alphanew,omegainit,omeganew,n):
    alpha=alphanew
    omega=omeganew
    g=-9.81
    l=1
    v=array([alpha,omega])
    l1=[alpha]
    l2=[omega]    
    for i in range(1,n):
        alphanew=alpha-omega-alphainit-(h/2)*omegainit
        omeganew=omega+(g/l)*sin(alpha)-omegainit+(h/2)*(g/l)*sin(alphainit)
        if abs(omega-omeganew)<=1.e-3:
            print("bingo")            
            print (omega,alpha)
        alphainit=alpha
        omegainit=omega
        alpha=alphanew
        omega=omeganew
        v=vstack((v,(alphanew,omeganew)))
        l1.append(alpha)
        l2.append(omega)
        i+=1
    return v 