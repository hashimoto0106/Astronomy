# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:53:22 2020

@author: PC
"""

from astropy.coordinates import AltAz

toki = astropy.time.Time(datetime.datetime(2019,5,16,17,0,0)) - 9*u.hour
taiyou = get_sun(toki).transform_to(AltAz(obstime=toki,location=koko))
print(taiyou)
print(taiyou.az) # 天球での方位角(北では0度で西では270度)
print(taiyou.alt) # 天球での仰俯角
print(taiyou.distance) # 距離
print(taiyou.distance.au) # au単位での距離
