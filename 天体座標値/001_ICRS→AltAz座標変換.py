# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:00:20 2020

@author: PC
"""

from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time


# 天体座標値取得(ICRS座標系)
m33 = SkyCoord.from_name('M33')
print(m33)
print("ra : ", m33.ra)
print("dec : ", m33.dec)

# 時刻設定
utcoffset = -4*u.hour  # ニューヨークなのでアメリカ東部標準時（UTC-4h）を設定
time = Time('2012-7-12 23:00:00') - utcoffset

# ICRS->AltAz座標変換
bear_mountain = EarthLocation(lat=41.3*u.deg, lon=-74*u.deg, height=390*u.m)
m33altaz = m33.transform_to(AltAz(obstime=time, location=bear_mountain))
print(m33altaz)
print("az : ", m33altaz.az)
print("alt : ", m33altaz.alt)
