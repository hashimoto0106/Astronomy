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
import numpy as np
import matplotlib.pyplot as plt

tz = astropy.time.TimezoneInfo(9*u.hour)
toki = datetime.datetime(2019,1,1,12,0,0,tzinfo=tz)
toki = astropy.time.Time(toki) + np.arange(365)*u.day

taiyou = get_sun(toki)
seiza = taiyou.get_constellation()
print('\n'.join(sorted({'%s: %d'%(s,list(seiza).count(s)) for s in set(seiza)},key=lambda x:int(x.split(':')[1]),reverse=True)))
