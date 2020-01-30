# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 22:08:42 2020
https://qiita.com/phyblas/items/d3fdca7c42b798e65b89
@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import astropy.units as u
from astropy.coordinates import SkyCoord,EarthLocation,AltAz
from astropy.coordinates import Angle
from astropy.time import Time
import imageio
from tqdm import tqdm


koko_keido = Angle('133° 35′ 48.3″')
koko_ido = Angle('34° 34′ 36.5″')
koko = EarthLocation(lat=koko_ido,lon=koko_keido)
toki = Time('2019-09-15 20:00:00')-9*u.hour + np.arange(0,8,0.5)*u.hour

az,alt = np.meshgrid(np.arange(0,360.1,3),np.arange(0,90.1,3))
chihei_grid = SkyCoord(az=az,alt=alt,unit='deg',frame='altaz').cartesian.xyz

ra,dec = np.meshgrid(np.arange(0,360.1,1),np.arange(-90,90.1,30))
sekidou_grid = SkyCoord(ra=ra,dec=dec,unit='deg')

hoshi_sekkei = Angle('22h 57m 39.04625s')
hoshi_sekii = Angle('-29° 37′ 20.0533″')
hoshi_sekidou = SkyCoord(ra=hoshi_sekkei,dec=hoshi_sekii)

lis_parang = [] # 視差角を納めるリスト
gif = []
for ima in tqdm(toki):
    kokoima = AltAz(obstime=ima,location=koko)

    fig = plt.figure(figsize=[6,6],dpi=80)
    ax = plt.axes([0,0,1,1],projection='3d',xlim=[-0.6,0.6],ylim=[-0.6,0.6],zlim=[-0.1,1.1],facecolor='k')
    ax.plot_wireframe(*chihei_grid,rstride=10,cstride=10,color='#dddddd',alpha=0.4)

    sekidou_grid_xyz = sekidou_grid.transform_to(kokoima).cartesian.xyz
    sekidou_grid_xyz[:,sekidou_grid_xyz[2]<0] = np.nan
    ax.plot_wireframe(*sekidou_grid_xyz,cstride=None,color='#ff7777',linestyle='--',alpha=0.6)

    hoshi_chihei = hoshi_sekidou.transform_to(kokoima)
    hoshi_xyz = hoshi_chihei.cartesian.xyz
    ax.scatter(*hoshi_xyz,s=250,marker='*',color='#9999ff')

    # 赤道座標の北極から天体を経過して南極まで曲線
    kyoku_chihei = SkyCoord(ra=hoshi_sekkei,dec=np.arange(-90,90.1,1),unit=('hourangle','deg')).transform_to(kokoima)
    kyoku_xyz = kyoku_chihei.cartesian.xyz
    kyoku_xyz[2][kyoku_xyz[2]<0] = np.nan
    ax.plot(*kyoku_xyz,color='#ffff99')
    ax.view_init(hoshi_chihei.alt.value,hoshi_chihei.az.value)

    # 天頂から天体までの曲線
    tenchou_chihei = SkyCoord(az=hoshi_chihei.az,alt=np.linspace(hoshi_chihei.alt.value,90,101),unit='deg',frame='altaz')
    tenchou_xyz = tenchou_chihei.cartesian.xyz
    ax.plot(*tenchou_xyz,color='#9999ff')

    # 時間と方位角と仰俯角と視差角を書く
    az = hoshi_chihei.az.to_string(unit=u.degree, sep=['° ','′ ','″'])
    alt = hoshi_chihei.alt.to_string(unit=u.degree, sep=['° ','′ ','″'])
    parang = np.degrees(np.arcsin(np.sin(hoshi_chihei.az.radian)*np.cos(koko.lat.radian)/np.cos(hoshi_sekidou.dec.radian)))
    ax.text(0,0,1.2,f'{(ima+9*u.hour).datetime}\naz = {az}\nalt = {alt}\nparang= {parang:.3f}',color='#ccffcc',size=18,ha='center')

    plt.axis('off')
    fig.canvas.draw()
    gif.append(np.array(fig.canvas.renderer._renderer))
    plt.close()
    lis_parang.append(parang)

# 図1を保存
imageio.mimsave('fomalhaut_20190915_parang.gif',gif,fps=4)

# 図2を描く
plt.figure(figsize=[7,8],dpi=60)
for i,(parang,ima) in enumerate(zip(lis_parang,toki)):
    plt.subplot(4,4,1+i,xlim=[-1,1],ylim=[-1,1],xticks=[],yticks=[],facecolor='k')
    plt.plot([0,0],[0,1],color='#9999ff')
    plt.text(0,0,'$\Delta$',color='#ffff99',size=70,ha='center',va='center',rotation=-parang)
    plt.title(f'{(ima+9*u.hour).datetime:%H:%M}',size=18)
    plt.xlabel('%.1f°'%parang,size=18)
plt.tight_layout()
plt.savefig('fomalhaut_20190915_parang1.png')
plt.close()

# 図3を描く
plt.figure(figsize=[7,8],dpi=60)
for i,(parang,ima) in enumerate(zip(lis_parang,toki)):
    plt.subplot(4,4,1+i,xlim=[-1,1],ylim=[-1,1],xticks=[],yticks=[],facecolor='k')
    plt.plot([0,-np.tan(np.radians(parang))],[0,1],color='#9999ff')
    plt.text(0,0,'$\Delta$',color='#ffff99',size=70,ha='center',va='center')
    plt.title(f'{(ima+9*u.hour).datetime:%H:%M}',size=18)
    plt.xlabel('%.1f°'%parang,size=18)
plt.tight_layout()
plt.savefig('fomalhaut_20190915_parang2.png')
plt.close()
