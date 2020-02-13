# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 23:50:28 2020
https://qiita.com/phyblas/items/9a087ad1f73aca5dcbe5
@author: PC
"""

from astropy.coordinates import EarthLocation

koko = EarthLocation(lat='35 40 30.78',lon='139 32 17.1')
print(koko.geodetic)
print(koko.lon)
print(koko.lat)
print(koko.height)
