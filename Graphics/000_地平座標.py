# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:43:05 2020
https://qiita.com/phyblas/items/d3fdca7c42b798e65b89
@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt


# 地平座標のグリッド
az,alt = np.meshgrid(np.arange(0,360.1,3),np.arange(0,90.1,3))
chihei_grid = SkyCoord(az=az,alt=alt,unit='deg',frame='altaz').cartesian.xyz

fig = plt.figure(figsize=[6,6],dpi=80)
# 地平座標のグリッドを描く
ax = plt.axes([0,0,1,1],projection='3d',xlim=[-0.6,0.6],ylim=[-0.6,0.6],zlim=[-0.4,1],facecolor='k')
ax.plot_wireframe(*chihei_grid, rstride=10, cstride=10, color='#dddddd', alpha=0.4)

plt.axis('off')
ax.view_init(30, 105)
fig.canvas.draw()
plt.savefig('000_地平座標.png')
plt.close()
