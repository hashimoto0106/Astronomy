# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:04:45 2019

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 3D座標設定関数
def coordinate_3d(axes, title, range_x, range_y, range_z, grid = True):
    axes.set_title(title)
    axes.set_xlabel("x", fontsize = 16)
    axes.set_ylabel("y", fontsize = 16)
    axes.set_zlabel("z", fontsize = 16)
    axes.set_xlim(range_x[0], range_x[1])
    axes.set_ylim(range_y[0], range_y[1])
    axes.set_zlim(range_z[0], range_z[1])
    if grid == True:
        axes.grid()


# 3Dベクトル描画関数
def plot_3D(axes, label, loc, vector, color = "red"):
    axes.quiver(loc[0], loc[1], loc[2],
              vector[0], vector[1], vector[2],
              color = color, length = 1,
              arrow_length_ratio = 0.2, label=label)
    
    axes.legend()  # 凡例

    # ベクトルにテキストを添える
#    txt = "(" + str(vector[0]) + ", " + str(vector[1]) + ")"
#    axes.text(vector[0], vector[1], txt, color = color, size = 9)


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
