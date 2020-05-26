# -*- coding: utf-8 -*-
"""
Created on Tue May 26 21:54:24 2020
https://ja.coder.work/so/python/2628834
@author: PC
"""

from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time

c = SkyCoord('22h50m0.19315s', '+24d36m05.6984s', frame='icrs')
loc = EarthLocation(lat = 31.7581*u.deg, lon = -95.6386*u.deg, height = 147*u.m)
time = Time('1991-06-06 12:00:00')
cAltAz = c.transform_to(AltAz(obstime = time, location = loc))

x = 5 # why not?
newAltAzcoordiantes = SkyCoord(alt = cAltAz.alt.deg, az = cAltAz.az.deg + x*u.deg, obstime = time, frame = 'altaz')
newAltAzcoordiantes.transform_to('icrs')
