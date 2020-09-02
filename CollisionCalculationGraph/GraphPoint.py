# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:04:45 2019

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5]
y = [1, 8, 3, 6, 5]
z = [1, 5, 3, 8, 9]

ax.scatter(x, y, z, c='r', marker='^', label='test')
ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


# 3D座標設定関数
def coordinate_3d(axes, title, xlabel, ylabel, zlabel, grid = True):
    axes.legend()
    axes.set_title(title)
    axes.set_xlabel(xlabel, fontsize = 9)
    axes.set_ylabel(ylabel, fontsize = 9)
    axes.set_zlabel(zlabel, fontsize = 9)
    if grid == True:
        axes.grid()


# 3Dベクトル描画関数
def plot_3D(axes, label, p, color, mark):
    axes.scatter(p[0], p[1], p[2], c=color, marker=mark, label=label)
    axes.legend()  # 凡例

    # ポイントに数値表示
    txt = "(" + str(p[0]) + ", " + str(p[1]) + ", " + str(p[2]) + ")"
    axes.text(p[0], p[1], p[2], txt, color = color, size = 9)


# 2D座標設定関数
def coordinate_2d(axes, title, range_x, range_y):
    axes.set_title(title)
    axes.set_xlabel("x", fontsize = 16)
    axes.set_ylabel("y", fontsize = 16)
    axes.set_xlim(range_x[0], range_x[1])
    axes.set_ylim(range_y[0], range_y[1])
    axes.grid()


# 2Dベクトル描画関数
def plot_2D(axes, label, loc, vector, color = "red"):
    axes.quiver(loc[0], loc[1],
              vector[0], vector[1], color = color,
              angles = 'xy', scale_units = 'xy', scale = 1, label=label)

    axes.legend()  # 凡例
    
    # ベクトルにテキストを添える
    txt = "(" + str(vector[0]) + ", " + str(vector[1]) + ")"
    axes.text(vector[0], vector[1], txt, color = color, size = 9)
