# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:34:36 2020
https://rhodesmill.org/pyephem/tutorial.html#first-steps
@author: PC
"""

import ephem


def hpos(body): return body.hlon, body.hlat


yh = ephem.readdb("C/2002 Y1 (Juels-Holvorcem),e,103.7816," +
   "166.2194,128.8232,242.5695,0.0002609,0.99705756,0.0000," +
   "04/13.2508/2003,2000,g  6.5,4.0")
yh.compute('2003/4/11')
print(yh.name)
print("%s %s" % (yh.ra, yh.dec))
print("%s %s" % (ephem.constellation(yh), yh.mag))
print(yh) 

iss = ephem.readtle("ISS (ZARYA)",
 "1 25544U 98067A   03097.78853147  .00021906  00000-0  28403-3 0  8652",
 "2 25544  51.6361  13.7980 0004256  35.6671  59.2566 15.58778559250029")
gatech = ephem.Observer()
gatech.date = '2003/3/23'
iss.compute(gatech)
print("%s %s %s" % (iss.rise_time, iss.transit_time, iss.set_time))

gatech.date = '2003/3/23 8:00'
iss.compute(gatech)
print("%s %s %s" % (iss.rise_time, iss.transit_time, iss.set_time))
