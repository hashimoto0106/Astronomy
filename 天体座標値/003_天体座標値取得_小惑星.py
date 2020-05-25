# -*- coding: utf-8 -*-
"""
Created on Mon May 25 21:49:58 2020

@author: PC
"""

from astropy.coordinates import SkyCoord


# 天体座標値取得(ICRS座標系)
# NG
# 小惑星 Minor Planet Center (MPC) database
# https://www.minorplanetcenter.net/iau/lists/MPNames.html
star = SkyCoord.from_name('APL')
print(star)
print("ra : ", star.ra)
print("dec : ", star.dec)
