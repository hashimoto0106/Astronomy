# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:00:20 2020

@author: PC
"""

from astropy.coordinates import SkyCoord


# 天体座標値取得(ICRS座標系)
m33 = SkyCoord.from_name('M33')
print(m33)
print("ra : ", m33.ra)
print("dec : ", m33.dec)
