#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:37:16 2024

@author: brettnakao
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rng

data = rng(1000)

plt.figure()
plt.hist(data)

counts, bin_edges, _ = plt.hist(data)
counts, bin_edges = np.histogram(data)

bin_size = bin_edges[1] - bin_edges[0]
new_widths = bin_size * counts/counts.max()

plt.figure()
plt.bar(bin_edges[:-1], counts, width=new_widths, color=['r', 'g', 'b', 'y'])