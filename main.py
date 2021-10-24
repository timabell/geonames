#!/usr/bin/env python

# source: https://stackoverflow.com/questions/32424670/python-matplotlib-drawing-3d-sphere-with-circumferences/32427177#32427177

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('auto')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

#for i in range(2):
#    ax.plot_surface(x+random.randint(-5,5), y+random.randint(-5,5), z+random.randint(-5,5),  rstride=4, cstride=4, color='b', linewidth=0, alpha=0.5)

elev = 10.0
rot = 80.0 / 180 * np.pi

# surface of sphere
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b', linewidth=0, alpha=0.25)

#calculate vectors for "vertical" circle
a = np.array([-np.sin(elev / 180 * np.pi), 0, np.cos(elev / 180 * np.pi)])
b = np.array([0, 1, 0])
b = b * np.cos(rot) + np.cross(a, b) * np.sin(rot) + a * np.dot(a, b) * (1 - np.cos(rot))

# dotted horizontal line
ax.plot(np.sin(u),np.cos(u),0,color='k', linestyle = 'dashed')

horiz_front = np.linspace(0, np.pi, 100)

# solid horizontal line at front
ax.plot(np.sin(horiz_front),np.cos(horiz_front),0,color='k')

vert_front = np.linspace(np.pi / 2, 3 * np.pi / 2, 100)

# dotted vertical line
ax.plot(a[0] * np.sin(u) + b[0] * np.cos(u), b[1] * np.cos(u), a[2] * np.sin(u) + b[2] * np.cos(u),color='k', linestyle = 'dashed')

# solid vertical line at front
ax.plot(a[0] * np.sin(vert_front) + b[0] * np.cos(vert_front), b[1] * np.cos(vert_front), a[2] * np.sin(vert_front) + b[2] * np.cos(vert_front),color='k')

ax.view_init(elev = elev, azim = 0)


plt.show()
