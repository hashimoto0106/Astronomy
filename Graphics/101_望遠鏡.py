# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:43:05 2020
https://qiita.com/phyblas/items/d3fdca7c42b798e65b89
@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import astropy.units as u
from astropy.coordinates import SkyCoord,EarthLocation,AltAz,Angle
from astropy.time import Time


koko_keido = Angle('133° 35′ 48.3″') # 観測値の経度
koko_ido = Angle('34° 34′ 36.5″') # 観測値の緯度
# 観測の位置を決めるオブジェクト
koko = EarthLocation(lat=koko_ido,lon=koko_keido)
# 観測時間、日本の20時に始まるが、๊UTCにする必要があるので9時間でひく
toki = Time('2019-09-15 20:00:00') - 9*u.hour + np.arange(0,1,0.5)*u.hour
now = Time('2019-09-15 20:00:00') - 9*u.hour

# 観測天体位置(赤道座標)
hoshi_sekkei = Angle('22h 57m 39.04625s')  # 赤経
hoshi_sekii = Angle('-29° 37′ 20.0533″')  # 赤緯
hoshi_sekidou = SkyCoord(ra=hoshi_sekkei, dec=hoshi_sekii)

# 地平座標のグリッド
az,alt = np.meshgrid(np.arange(0,360.1,3),np.arange(0,90.1,3))
chihei_grid = SkyCoord(az=az,alt=alt,unit='deg',frame='altaz').cartesian.xyz

# その時間のその場所の地平座標を示すオブジェクト
kokoima = AltAz(obstime=now,location=koko)

# 赤道座標のグリッド
ra,dec = np.meshgrid(np.arange(0,360.1,1),np.arange(-90,90.1,15))
sekidou_grid = SkyCoord(ra=ra,dec=dec,unit='deg')

# 描画
fig = plt.figure(figsize=[6,6],dpi=80)
# 地平座標グリッド描画
ax = plt.axes([0,0,1,1],projection='3d',xlim=[-0.6,0.6],ylim=[-0.6,0.6],zlim=[-0.4,1],facecolor='k')
ax.plot_wireframe(*chihei_grid,rstride=10,cstride=10,color='#dddddd',alpha=0.4)

# 地平座標で赤道座標のグリッド描画
sekidou_grid_xyz = sekidou_grid.transform_to(kokoima).cartesian.xyz
sekidou_grid_xyz[:,sekidou_grid_xyz[2]<0] = np.nan # 地面より低いところを除外
ax.plot_wireframe(*sekidou_grid_xyz,cstride=30,color='#ff7777',linestyle='--',alpha=0.6)

# 観測天体位置(赤道座標)描画
hoshi_chihei = hoshi_sekidou.transform_to(kokoima)
hoshi_xyz = hoshi_chihei.cartesian.xyz  # 直交座標変換
ax.scatter(*hoshi_xyz, s=250,marker='*', color='#9999ff')  # 天体位置マーク(地平座標)

# 望遠鏡描画
ax.plot(*np.stack([(0,0,0),hoshi_xyz],1),color='#99bbff',ls='--')  # 望遠鏡から天体までの線
ax.plot(*np.stack([(0,0,0),hoshi_xyz],1)*0.2,color='#99bbff',lw=10)  # 望遠鏡描画
ax.plot([0,0],[0,0],[0,1],color='#ffffdd',alpha=0.6)  # 望遠鏡から天頂までの線

plt.axis('off')
ax.view_init(30, 105)
fig.canvas.draw()
plt.savefig('101_望遠鏡.png')
plt.close()
