#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:28:51 2024

@author: brettnakao
"""

import numpy as np
import matplotlib.pyplot as plt

# Create grid of x and y coordinates
x_vals = np.linspace(-1, 1, 200)
y_vals = np.linspace(-1, 1, 200)
X, Y = np.meshgrid(x_vals, y_vals)

# Generate function values
Z = np.cos(X) * np.sin(Y)

R = X**2 + Y**2

# Plot contour curves
plt.contour(X, Y, Z)
plt.show()

plt.contour(X, Y, R)
plt.show()

# Plot and label contours
plt.figure()
cs = plt.contour(X, Y, Z, 10, linewidths=3, colors='r')
plt.clabel(cs, fontsize = 10)
plt.show()

# Plot surfaces
ax1 = plt.axes(projection='3d')  # Adding subplot with 3D projection
ax1.plot_surface(X, Y, R)
plt.show()

ax3 = plt.axes(projection='3d')
ax3.plot_surface(X, Y, R, rcount=200, ccount=200) # Highly refined 3D plot
plt.show()

# Plot heatmaps
plt.pcolormesh(X, Y, R)
plt.show()

plt.pcolormesh(X, Y, R, cmap = 'jet')