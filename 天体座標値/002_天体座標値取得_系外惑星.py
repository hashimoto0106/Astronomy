# -*- coding: utf-8 -*-
"""
Created on Mon May 25 21:49:15 2020

@author: PC
"""

from astropy.coordinates import SkyCoord


# 天体座標値取得(ICRS座標系)
# 系外惑星 IAU names for exoplanets
# https://www.iau.org/public/themes/naming_exoplanets/
star = SkyCoord.from_name('Arion')
print(star)
print("ra : ", star.ra)
print("dec : ", star.dec)
