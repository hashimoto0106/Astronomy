# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:01:05 2020

['altaz', 'barycentrictrueecliptic', 'cirs', 'fk4', 
'fk4noeterms', 'fk5', 'galactic', 'galacticlsr', 
'galactocentric', 'gcrs', 'geocentrictrueecliptic', 
'hcrs', 'heliocentrictrueecliptic', 'icrs', 'itrs', 
'lsr', 'precessedgeocentric', 'supergalactic']

@author: PC
"""

from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time

# 天体座標値取得(ICRS座標系)
c = SkyCoord('22h50m0.19315s', '+24d36m05.6984s', frame='icrs')
loc = EarthLocation(lat = 31.7581*u.deg, lon = -95.6386*u.deg, height = 147*u.m)

# 時刻設定
time = Time('1991-06-06 12:00:00')

# ICRS(赤道座標とほぼ同じ)->AltAz(地平座標)座標変換
cAltAz = c.transform_to(AltAz(obstime = time, location = loc))
print(cAltAz)
print("az : ", cAltAz.az)
print("alt : ", cAltAz.alt)
