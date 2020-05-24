# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 23:50:28 2020
https://qiita.com/phyblas/items/9a087ad1f73aca5dcbe5
@author: PC
"""

import datetime
import astropy.time
import astropy.units as u
from astropy.coordinates import get_sun

tz = astropy.time.TimezoneInfo(9*u.hour) # グリニッジ標準時間
toki = datetime.datetime(2019,5,16,17,0,0,tzinfo=tz)
toki = astropy.time.Time(toki)
taiyou = get_sun(toki)
print(taiyou)
print(taiyou.get_constellation())
