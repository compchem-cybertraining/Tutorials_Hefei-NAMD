#!/usr/bin/env python
############################################################
import os, re
import numpy as np
from glob import glob

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('agg')
mpl.rcParams['axes.unicode_minus'] = False

############################################################
# load FSSH result files
############################################################
dt       = 1.0
bmin     = 324
bmax     = 335
namdTime = 1000
potim    = 1.0
inpFiles = glob('./SHPROP.*')
pop      = np.average(
    np.array([np.loadtxt(F) for F in inpFiles]),
    axis=0
)
############################################################


############################################################
fig = plt.figure(
    figsize=(4.0, 2.4),
    dpi=300,
)

ax  = plt.subplot()
############################################################
t0 = np.arange(pop.shape[0]) * dt
for ii in range(bmax - bmin):
    ax.plot(t0, pop[:,ii+2])

############################################################
# ax.set_xlim(0, namdTime)
# ax.set_ylim(-1.0, 1.0)

ax.set_xlabel('Time [fs]',  labelpad=5)
ax.set_ylabel('Population', labelpad=5)

########################################
plt.tight_layout(pad=0.2)
plt.savefig('pop_line_plot.png')
