# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:59:43 2020
https://qiita.com/phyblas/items/a801b0f319742245ad2e
@author: PC
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import imageio
from tqdm import tqdm

ra,dec = np.meshgrid(np.linspace(0,360,361),np.linspace(-90,90,181))
tenkyuu = SkyCoord(ra=ra,dec=dec,unit='deg')
seiza = tenkyuu.ravel().get_constellation().reshape(*ra.shape) # 星座の名前を求める
z = (seiza[:,:,None]==np.unique(seiza)).argmax(2) # 星座の名前を数字に変換
plt.figure(figsize=[7,4])
plt.gca(aspect=1)
plt.contour(ra,dec,z,88,colors='k',linestyles=':',linewidths=0.1)
plt.pcolormesh(ra,dec,z,cmap='jet')
plt.show()

mx,my,mz = tenkyuu.cartesian.xyz # xyz座標に変換
iro = np.stack([z/87,z%5/4,1-z%4/4],2) # できるだけ各星座に違う色をつける
fig = plt.figure(figsize=[6,6])
ax = plt.axes([0,0,1,1],projection='3d',xlim=[-0.6,0.6],ylim=[-0.6,0.6],zlim=[-0.6,0.6],facecolor='k')
ax.plot_surface(mx,my,mz,facecolors=iro,rstride=1,cstride=1,alpha=0.9)
plt.axis('off') # 軸を隠す

gif = [] # どんどん回してアニメーションgifを作る
for i in tqdm(range(24)):
    ax.view_init(30*np.sin(i*np.pi/12),i*15) # 眺める角度を変える
    fig.canvas.draw()
    gif.append(np.array(fig.canvas.renderer._renderer))
plt.close()
imageio.mimsave('seiza_kubun.gif',gif,fps=5) # 保存
