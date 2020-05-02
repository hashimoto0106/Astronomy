# -*- coding: utf-8 -*-
"""
Created on Sun May  3 01:35:30 2020

@author: PC
"""

import ephem
import datetime
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 観測地設定
osaka = ephem.Observer()
osaka.lat = '34.6914'
osaka.lon = '135.4917'
osaka.date = datetime.datetime.utcnow()

# 月
moon = ephem.Moon()

# 次回　月の出・月の入り等を表示
print("次の月の出　 : ", ephem.localtime(osaka.next_rising(moon)))
print("次の月の入り : ", ephem.localtime(osaka.next_setting(moon)))

print("次の新月 : ", ephem.localtime(ephem.next_new_moon(osaka.date)))
print("次の上弦 : ", ephem.localtime(ephem.next_first_quarter_moon(osaka.date)))
print("次の満月 : ", ephem.localtime(ephem.next_full_moon(osaka.date)))
print("次の下弦 : ", ephem.localtime(ephem.next_last_quarter_moon(osaka.date)))
print("現在の月齢 : ", osaka.date - ephem.previous_new_moon(osaka.date))

# 月と太陽の離角を計算
moon.compute(osaka)
moon_elong = np.rad2deg(moon.elong)

# 描画領域を準備
fig = plt.figure(figsize=(5, 5))
ax = fig.gca(projection='3d')

# x, y, z軸の範囲設定
ax.set_xlim([-1., 1.])
ax.set_ylim([-1., 1.])
ax.set_zlim([-1., 1.])

# x, y, z軸や目盛を非表示に
for a in [ax.xaxis, ax.yaxis, ax.zaxis]:
    a.set_ticklabels([])
    a._axinfo['grid']['linewidth'] = 0
    a._axinfo['tick']['linewidth'] = 0

# 背景の x, y, z面を非表示に
for a in [ax.w_xaxis, ax.w_yaxis, ax.w_zaxis]:
    a.line.set_linewidth(0)
    a.set_pane_color((0., 0., 0., 0.))

# 背面を灰色に
ax.set_facecolor('lightgray')

# メッシュ状の球面 (u, v) を準備し、(x, y, z) 値を計算
u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]  # u:接線方向　v:動経方向
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)

# メッシュの球面に貼りつける色を準備（半分だけ黄色に）
colors = np.zeros((50, 25, 3))
for i in range(0, 25):
    for j in range(0, 25):
        colors[i][j][0] = 1
        colors[i][j][1] = 1
        colors[i][j][2] = 0

# 球面をプロット
ax.plot_surface(x, y, z, facecolors = colors, shade = False)
# グラフを見る方向を設定
ax.view_init(elev = 0, azim = moon_elong - 90)

plt.show()
