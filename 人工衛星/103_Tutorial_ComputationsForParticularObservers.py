# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:34:36 2020
https://rhodesmill.org/pyephem/tutorial.html#first-steps
@author: PC
"""

import ephem


def hpos(body): return body.hlon, body.hlat


gatech = ephem.Observer()
gatech.lon, gatech.lat = '-84.39733', '33.775867'

gatech.date = '1984/5/30 16:22:56'   # 12:22:56 EDT
sun, moon = ephem.Sun(), ephem.Moon()
sun.compute(gatech)
moon.compute(gatech)
print("%s %s" % (sun.alt, sun.az))
print("%s %s" % (moon.alt, moon.az))
print(ephem.separation((sun.az, sun.alt), (moon.az, moon.alt)))
print("%.8f %.8f %.11f" % (sun.size, moon.size, sun.size - moon.size))

gatech.date = '1984/5/31 00:00'   # 20:00 EDT
sun.compute(gatech)
for i in range(8):
    old_az, old_alt = sun.az, sun.alt
    gatech.date += ephem.minute * 5.
    sun.compute(gatech)
    sep = ephem.separation((old_az, old_alt), (sun.az, sun.alt))
    print("%s %s %s" % (gatech.date, sun.alt, sep))

print(gatech.next_setting(sun))
print("%s %s" % (sun.alt, sun.az))
