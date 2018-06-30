#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 10:32:51 2018

@author: Developer
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# setup the figure and axes
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# fake data
_x = np.arange(4)
_y = np.arange(5)
print(_x)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
print(x)
top = x + y
bottom = np.zeros_like(top)
width = depth = 1

x = [1-0.1,2,3,4]  #x coordinates of each bar
y = [1,2,3,3]  #y coordinates of each bar
z = [0,0,0,0]  #z coordinates of each bar
dx = [0.5, 0.5, 0.5,0.5]  #width of each bar
dy = [0.5, 0.5, 0.5,0.5]  #depth of each bar
dz = [1, 20, 30, 10]  #height of each bar

ax1.bar3d(x, y, z, dx, dy, dz)
ax1.set_title('Shaded')

plt.show()