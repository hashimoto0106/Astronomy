# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:00:20 2020

@author: PC
"""

from astropy.coordinates import SkyCoord


# 天体座標値取得(ICRS座標系)

# 太陽系の外にある天体 Sesame name resolver
# http://cds.u-strasbg.fr/cgi-bin/Sesame
star = SkyCoord.from_name('M33')
print(star)
print("ra : ", star.ra)
print("dec : ", star.dec)

star = SkyCoord.from_name('HCG 7')
print(star)
print("ra : ", star.ra)
print("dec : ", star.dec)
