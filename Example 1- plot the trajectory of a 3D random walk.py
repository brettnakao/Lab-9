#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:59:25 2024

@author: brettnakao
"""

import numpy as np

rng = np.random.default_rng()

# x-step
x_step = 2 * (rng.random(500) > .5) - 1
x_coord = np.cumsum(x_step)

# y-step
y_step = 2 * (rng.random(500) > .5) - 1
y_coord = np.cumsum(y_step)

# z-step
z_step = 2 * (rng.random(500) > .5) - 1
z_coord = np.cumsum(z_step)

# Plot 3D random walk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

ax1 = fig.add_subplot(111, projection='3d')
ax1.plot(x_coord, y_coord, z_coord)
plt.show()