# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:59:43 2020
https://qiita.com/phyblas/items/a801b0f319742245ad2e
@author: PC
"""

from astropy.coordinates import SkyCoord


# 北極(天球上の各領域の星座取得)
hokkyoku = SkyCoord(ra=0, dec=90, unit='deg')
print(hokkyoku.get_constellation())

# 南極(天球上の各領域の星座取得)
nankyoku = SkyCoord(ra=0, dec=-90, unit='deg')
print(nankyoku.get_constellation())
