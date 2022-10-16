#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:56:36 2022

@author: steven
"""
import numpy as np
import math
import matplotlib.pyplot as plt

# %% zone de l'exo1
def Exo1():
    a = np.arange(10)
    print(a)
    print(type(a))
    L = np.arange(2,15,3)
    print(L)
    p1 = np.array([1,2,3])
    print(p1)
    print(type(p1))
    l2 = [10,12,13]
    l1 = [1,2,3]
    print(l1+l2)
    p2 = np.array(l2)
    print(p1+p2)
    
    N = 50
    x1 = np.linspace(0,10,N,endpoint=True)
    print(x1)
    x2 = np.linspace(0,10,N,endpoint=False)
    print(x2)
    
    plt.plot([1,2,3,4],[1,4,2,3])
    plt.show()

# %% zone de l'exo2
def Exo2():
    sinus(0,2*math.pi,100)
    
def sinus2():
    #a = list(range(0,math.ceil(2*math.pi)))
    a = [x*0.01 for x in range(0,math.ceil(2*math.pi*100))]
    b = [math.sin(x) for x in a]
    plt.plot(a,b)
    plt.show()
    
def sinus(a,b,n):
    tab = []
    index = []
    h = (b-a)/n
    #va servir pour calculer le nmbre de point
    i = 0
    
    while i <= b:
        tab.append(math.sin(i))
        index.append(i)
        i += h
        
    plt.plot(index,tab)
    plt.show()

# %% zone de l'exo3
def Exo3():
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)
    plt.plot(x,y)
    plt.show()

# %% zone de l'exo4
def Exo4():
    p0=np.array([0.,0.,0.])
    p1=np.array([0.,-1.,0.])
    m=1.0
    k=0.1
    amort=0.1
    deltat=0.01
    time_sim=100

    v,x,t = Euler(0,time_sim,F,1,100,p0,p1,amort,k,m)
    plt.plot(t,x)
    plt.show()
    
def F(v,x,p1,p0,amort,k):        
    return - amort*v - k*(x - p1[1])    

def Euler(a,b,F,v0,N,p0,p1,amort,k,m):
    dt=(b-a)/N
    v=[v0]
    x=[p1[1]]
    t=[a]
    for i in range(1,b):
        v.append(v[i-1]+(F(v[i-1],x[i-1],p1,p0,amort,k)*dt)/(m*abs(p1[1]-p0[0])))      
        x.append(x[i-1]+v[i]*dt)
        t.append(t[i-1]+dt)
    return v,x,t

# %% zone de l'exo5
def Exo5():
    
# %% zone du main
if __name__ == '__main__' :
    #Exo1()
    #Exo2()
    #Exo3()
    #Exo4()
    Exo5()