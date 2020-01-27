# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:34:36 2020
https://rhodesmill.org/pyephem/tutorial.html#first-steps
@author: PC
"""

import ephem


def hpos(body): return body.hlon, body.hlat


d = ephem.Date('1984/12/21 15:00')
ephem.localtime(d)
print(ephem.localtime(d).ctime())

d = ephem.Date('1950/2/28')
print(d + 1)
print(ephem.Date(d + 1))

d = ephem.Date(34530.34375)
d = ephem.Date('1994/7/16.84375')
d = ephem.Date('1994/7/16 20:15')
d = ephem.Date((1994, 7, 16.84375))
d = ephem.Date((1994, 7, 16, 20, 15, 0))

print('as a float: %f\nas a string: "%s"' % (d, d))
print(d.triple())
print(d.tuple())
