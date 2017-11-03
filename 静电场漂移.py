# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:33:56 2017

@author: msi
"""

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

qm=0.2#float(input("Input q/m:\n"))
Bz=10#float(input("Input Bz:\n"))
E=[1,0,1]
w=Bz*qm

ax=[0]
ay=[0]
az=[0]
vx=[0]
vy=[0]
vz=[0]
x=[0]
y=[0]
z=[0]

a=0.01
t=np.arange(0,50,a)
j=0

for i in t:
    ax.append(qm*E[0]+w*vy[j])
    vx.append(vx[j]+a*ax[j+1])
    x.append(x[j]+a*vx[j+1])
    
    ay.append(-w*vx[j])
    vy.append(vy[j]+a*ay[j+1])
    y.append(y[j]+a*vy[j+1])
    
    az.append(qm*E[2])
    vz.append(vz[j]+a*az[j+1])
    z.append(z[j]+a*vz[j+1])
    
    j+=1

fig = plt.figure(figsize=(20,10))
axe = Axes3D(fig)

axe.view_init(elev=0, azim=0)
axe.plot(x,y,z)
axe.set_zlabel('z')
axe.set_ylabel('y')
axe.set_xlabel('x')

plt.show()