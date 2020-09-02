# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:10:54 2020

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
import GraphPoint
import GraphVektor


# ==========自衛星とデブリの絶対座標==========
p0 = np.array([0, 0, 0])  # 地球
p1 = np.array([1, 0, 0])  # 自衛星
p2 = np.array([0, 5, 2])  # デブリ
p3 = np.array([-2, -3, -1])
p4 = np.array([1, 2, 3])
p5 = np.array([4, 5, 6])
p6 = np.array([6, 5, 4])
p7 = np.array([3, 2, 1])
p8 = np.array([-1, -5, -2])
fig = plt.figure(figsize = (6, 6))  # FigureとAxes
ax = fig.add_subplot(111, projection='3d')
GraphPoint.coordinate_3d(ax, 'Absolute coordinates of own satellite and debris', "X[km]", "Y[km]", "X[km]", grid = True)  # 座標設定
GraphPoint.plot_3D(ax, "Point0", p0, "r", ".")
GraphPoint.plot_3D(ax, "Point1", p1, "r", ",")
GraphPoint.plot_3D(ax, "Point2", p2, "g", "o")
GraphPoint.plot_3D(ax, "Point3", p3, "b", "s")
GraphPoint.plot_3D(ax, "Point4", p4, "b", "s")
GraphPoint.plot_3D(ax, "Point5", p5, "b", "p")
GraphPoint.plot_3D(ax, "Point6", p6, "b", "*")
GraphPoint.plot_3D(ax, "Point7", p7, "b", "+")
GraphPoint.plot_3D(ax, "Point8", p8, "b", "x")


# ==========自衛星基準のデブリ相対座標==========
p0 = np.array([0, 0, 0])  # 自衛星
p1 = np.array([1, 7, -2])  # デブリ
fig = plt.figure(figsize = (6, 6))  # FigureとAxes
ax = fig.add_subplot(111, projection='3d')
GraphPoint.coordinate_3d(ax, 'Debris relative coordinates based on own satellite', "X[km]", "Y[km]", "X[km]", grid = True)  # 座標設定
GraphPoint.plot_3D(ax, "Point0", p0, "black", ".")
GraphPoint.plot_3D(ax, "Point1", p1, "r", ",")


# ==========相対座標と相対速度の外積==========
pos = np.array([1, 0, 0])  # 相対座標
vel = np.array([0, 5, 0])  # 相対速度

# 外積
cross = np.cross(pos, vel)
print(cross)

# 3Dベクトル可視化
org = [0, 0, 0]  # 始点(自衛星)
fig = plt.figure(figsize = (6, 6))  # FigureとAxes
ax = fig.add_subplot(111, projection='3d')
GraphVektor.coordinate_3d(ax, 'Cross product of relative coordinates and relative velocity', [-5, 5], [-5, 5], [-5, 5], grid = True)  # 座標設定
GraphVektor.plot_3D(ax, "Relative coordinates", org, pos, "red")  # 相対座標
GraphVektor.plot_3D(ax, "Relative speed", org, vel, "blue")  # 相対速度
#GraphVektor.plot_3D(ax, "Cross product", org, cross1, "black")  # 相対座標と相対速度の外積 
GraphVektor.plot_3D(ax, "Cross product", org, cross, "black")  # 相対座標と相対速度の外積 ※python衝突計算結果


# ==========B-Plane X-Y軸==========
B_Plane_X = np.array([100, 0, 0])  # B-Plane X軸
B_Plane_Y = np.array([0, 100, 0])  # B-Plane Y軸
B_Plane_Z = np.array([0, 0, 100])  # B-Plane Z軸

# 3Dベクトル可視化
org = [0, 0, 0]  # 始点(自衛星)
fig = plt.figure(figsize = (6, 6))  # FigureとAxes
ax = fig.add_subplot(111, projection='3d')
GraphVektor.coordinate_3d(ax, 'B-Plane coordinates', [-100, 100], [-100, 100], [-100, 100], grid = True)  # 座標設定
GraphVektor.plot_3D(ax, "B-Plane X Axis", org, B_Plane_X, "r")  # B-Plane X軸
GraphVektor.plot_3D(ax, "B-Plane Y Axis", org, B_Plane_Y, "g")  # B-Plane Y軸
GraphVektor.plot_3D(ax, "B-Plane Z Axis", org, B_Plane_Z, "b")  # B-Plane Z軸


# ==========B-Plane座標系での相対座標と共分散行列==========

# ==========★誤差楕円(共分散行列の固有値)==========
# ==========★誤差楕円の長/短半径==========
# ==========★誤差楕円の方向ベクトル==========
# ==========誤差楕円の長半径ベクトルとB-Plane X軸のなす角度==========

# ==========共分散行列の行列式/逆行列==========


# ==========衝突確率==========


