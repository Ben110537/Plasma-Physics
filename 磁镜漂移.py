# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:11:01 2017

@author: msi
"""

from matplotlib import pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

qm=2#float(input("Input q/m:\n"))

ar=[0]
afi=[0]
b=[0]
az=[0]
vr=[0]
vfi=[0]
oe=[0]
vz=[1]
r=[10]
fi=[0]
th=[0]
z=[0]

x=[]
y=[]

k=0.0003           #磁场梯度尽可能小
a=0.001       
t=np.arange(0,20,a)
#Bz=0.01*z, Br=-0.5*r
j=0
for i in t:
    ar.append(qm*vfi[j]*k*abs(z[j]))
    vr.append(vr[j]+a*ar[j+1])
    r.append(r[j]+a*vr[j+1])
    
    afi.append(-qm*(vz[j]*0.5*r[j]+k*abs(z[j])*vr[j]))
    vfi.append(vfi[j]+a*afi[j+1])
    b.append(afi[j+1]/r[j+1])
    oe.append(oe[j]+a*b[j+1])
    th.append(th[j]+a*oe[j+1])
    
    az.append(qm*vfi[j]*0.5*r[j]*k)
    vz.append(vz[j]+a*az[j+1])
    z.append(z[j]+a*vz[j+1])
    
    j+=1

j=0
ak=[0]
k=1
for i in t:
    x.append(math.cos(th[j])*r[j])
    y.append(math.sin(th[j])*r[j])
    
    if j>0 and vz[j]*vz[j-1]<=0:
        ak.append(j)
        k+=1
    j+=1
ak.append(j-1)
print(k)
print(len(ak))
x.append(math.cos(th[j])*r[j])
y.append(math.sin(th[j])*r[j])

xa=[[]]
ya=[[]]
za=[[]]
if k==1:
    xa.append(x)
    ya.append(y)
    za.append(z)
else:
    for i in range(0,k):
        xa.append(x[ak[i]:ak[i+1]])
        ya.append(y[ak[i]:ak[i+1]])
        za.append(z[ak[i]:ak[i+1]])

fig = plt.figure(figsize=(20,10))
axe = Axes3D(fig)

axe.view_init(elev=30, azim=30)
if k==1:
    axe.plot(xa[0],ya[0],za[0],'b')
else:
    for i in range(0,k):
        if i%2==1:
            axe.plot(xa[i],ya[i],za[i],'b')
        else:
            axe.plot(xa[i],ya[i],za[i],'r')
axe.set_zlabel('z')
axe.set_ylabel('y')
axe.set_xlabel('x')

plt.show()