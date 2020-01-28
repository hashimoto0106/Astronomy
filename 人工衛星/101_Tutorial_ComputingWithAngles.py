# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:34:36 2020
https://rhodesmill.org/pyephem/tutorial.html#first-steps
@author: PC
"""

import ephem


def hpos(body): return body.hlon, body.hlat


u = ephem.Uranus('1871/3/13')
print(str(u.dec))
print('%.12f' % float(u.dec))
print('%.11f' % (u.dec + 1))

print(ephem.degrees('90.0'))
print(ephem.degrees(3.141593))

print("as a string: %s, as a float: %f" % (u.dec, u.dec))
ma0 = ephem.Mars('1976/05/21')    # ma: mars near aphelion
ma1 = ephem.Mars('1976/05/22')
mp0 = ephem.Mars('1975/06/13')    # mp: mars near perihelion
mp1 = ephem.Mars('1975/06/14')

aph_angle = ephem.separation(hpos(ma0), hpos(ma1))
aph_distance = aph_angle * ma0.sun_distance
print('%.13f' % aph_distance)

aph_area = aph_distance * ma0.sun_distance / 2.
print('%.13f' % aph_area)

peri_angle = ephem.separation(hpos(mp0), hpos(mp1))
peri_distance = peri_angle * mp0.sun_distance
peri_area = peri_distance * mp0.sun_distance / 2.
print('%.13f' % peri_area)    # the area, to high precision, is the same!

print('%.13f' % (peri_angle * 2))
print(ephem.degrees(peri_angle * 2))

deg = ephem.degrees
print(deg(deg('270') + deg('180')))
print(deg(deg('270') + deg('180')).norm)
