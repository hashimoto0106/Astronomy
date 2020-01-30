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
import imageio
from tqdm import tqdm


koko_keido = Angle('133° 35′ 48.3″') # 観測値の経度
koko_ido = Angle('34° 34′ 36.5″') # 観測値の緯度
# 観測の位置を決めるオブジェクト
koko = EarthLocation(lat=koko_ido,lon=koko_keido)
# 観測時間、日本の20時に始まるが、๊UTCにする必要があるので9時間でひく
toki = Time('2019-09-15 20:00:00') - 9*u.hour + np.arange(0,8,0.5)*u.hour

# 地平座標のグリッド
az,alt = np.meshgrid(np.arange(0,360.1,3),np.arange(0,90.1,3))
chihei_grid = SkyCoord(az=az,alt=alt,unit='deg',frame='altaz').cartesian.xyz

# 赤道座標のグリッド
ra,dec = np.meshgrid(np.arange(0,360.1,1),np.arange(-90,90.1,15))
sekidou_grid = SkyCoord(ra=ra,dec=dec,unit='deg')

# 観測したい天体の赤道による位置
hoshi_sekkei = Angle('22h 57m 39.04625s') # 赤経
hoshi_sekii = Angle('-29° 37′ 20.0533″') # 赤緯
hoshi_sekidou = SkyCoord(ra=hoshi_sekkei,dec=hoshi_sekii)

gif = [] # 絵のフレームを納めるリスト
# フレーム毎に繰り返し絵を描く
for ima in tqdm(toki):
    # その時間のその場所の地平座標を示すオブジェクト
    kokoima = AltAz(obstime=ima,location=koko)

    fig = plt.figure(figsize=[6,6],dpi=80)
    # 地平座標のグリッドを描く
    ax = plt.axes([0,0,1,1],projection='3d',xlim=[-0.6,0.6],ylim=[-0.6,0.6],zlim=[-0.4,1],facecolor='k')
    ax.plot_wireframe(*chihei_grid,rstride=10,cstride=10,color='#dddddd',alpha=0.4)

    # 地平座標で赤道座標のグリッドを描く
    sekidou_grid_xyz = sekidou_grid.transform_to(kokoima).cartesian.xyz
    sekidou_grid_xyz[:,sekidou_grid_xyz[2]<0] = np.nan # 地面より低いところを除外
    ax.plot_wireframe(*sekidou_grid_xyz,cstride=30,color='#ff7777',linestyle='--',alpha=0.6)

    # 地平座標における天体の位置
    hoshi_chihei = hoshi_sekidou.transform_to(kokoima)
    # 直交座標に変換する
    hoshi_xyz = hoshi_chihei.cartesian.xyz
    # 地平座標で天体の位置をマーク
    ax.scatter(*hoshi_xyz,s=250,marker='*',color='#9999ff')
    # 望遠鏡から天体までの線
    ax.plot(*np.stack([(0,0,0),hoshi_xyz],1),color='#99bbff',ls='--')
    # 望遠鏡を描く
    ax.plot(*np.stack([(0,0,0),hoshi_xyz],1)*0.2,color='#99bbff',lw=10)
    # 望遠鏡から天頂までの線
    ax.plot([0,0],[0,0],[0,1],color='#ffffdd',alpha=0.6)

    plt.axis('off')
    # 時間と方位角と仰俯角を書く
    az = hoshi_chihei.az.to_string(unit=u.degree, sep=['° ','′ ','″'])
    alt = hoshi_chihei.alt.to_string(unit=u.degree, sep=['° ','′ ','″'])
    ax.text(0,0,1.2,f'{(ima+9*u.hour).datetime}\naz = {az}\nalt = {alt}',color='#ccffcc',size=18,ha='center')
    ax.view_init(30,105)
    fig.canvas.draw()
    gif.append(np.array(fig.canvas.renderer._renderer))
    plt.close()

# .gifファイル保存
imageio.mimsave('fomalhaut_20190915.gif',gif,fps=4)
