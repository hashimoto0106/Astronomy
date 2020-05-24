# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:59:43 2020
https://qiita.com/phyblas/items/a801b0f319742245ad2e
@author: PC
"""

from astropy.coordinates import SkyCoord,PrecessedGeocentric

b1875 = PrecessedGeocentric(equinox='B1875')

b1875_hokkyoku = SkyCoord(ra=0,dec=90,unit='deg',frame=b1875)
print(b1875_hokkyoku)

b1875_hokkyoku_icrs = b1875_hokkyoku.transform_to('icrs')
print(b1875_hokkyoku_icrs)
