# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:31:05 2020

@author: PC
"""

import ephem
import datetime
from math import degrees as deg

# Body(天体)クラスのインスタンスを作成。

moon = ephem.Moon()

# Observer(観測者)クラスのインスタンスを作成。

shinjuku = ephem.Observer()
shinjuku.lat = '35.6846'
shinjuku.lon = '139.7106'
shinjuku.elevation = 60
shinjuku.date = datetime.datetime.utcnow() # 任意の年月日の位置を求められる

# 観測者から見た天体を計算。

moon.compute(shinjuku)
print(deg(moon.alt)) # 20.88288333068003(地平線からの仰角(degで度に変換))
print(deg(moon.az)) # 218.0421642706897(北を0度とした方角)
print(moon.moon_phase) # 0.2820702016225599(月相)
print(shinjuku.date - ephem.previous_new_moon(shinjuku.date)) # 24.138740752328886(月齢)
