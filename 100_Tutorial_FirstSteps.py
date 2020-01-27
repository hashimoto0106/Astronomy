# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:34:36 2020
https://rhodesmill.org/pyephem/tutorial.html#first-steps
@author: PC
"""

import ephem

u = ephem.Uranus()
u.compute('1781/3/13')
print('%s %s %s' % (u.ra, u.dec, u.mag))
print(ephem.constellation(u))

j = ephem.Jupiter('1612/12/28')
n = ephem.Neptune('1612/12/28')
print("%s %s %s" % (j.ra, j.dec, j.mag))
print("%s %s %s" % (n.ra, n.dec, n.mag))
print(ephem.separation(j, n))


def hpos(body): return body.hlon, body.hlat


ma0 = ephem.Mars('1976/05/21')    # ma: mars near aphelion
ma1 = ephem.Mars('1976/05/22')
print(ephem.separation(hpos(ma0), hpos(ma1)))
mp0 = ephem.Mars('1975/06/13')    # mp: mars near perihelion
mp1 = ephem.Mars('1975/06/14')
print(ephem.separation(hpos(mp0), hpos(mp1)))
