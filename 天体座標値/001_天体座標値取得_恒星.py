# -*- coding: utf-8 -*-
"""
Created on Mon May 25 21:48:37 2020

@author: PC
"""

from astropy.coordinates import SkyCoord


# 天体座標値取得(ICRS座標系)
# 恒星 IAU names for stars
# https://www.iau.org/public/themes/naming_stars/
star = SkyCoord.from_name('Gudja')
print(star)
print("ra : ", star.ra)
print("dec : ", star.dec)
