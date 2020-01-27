# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:34:36 2020
https://rhodesmill.org/pyephem/tutorial.html#first-steps
@author: PC
"""

import ephem


def hpos(body): return body.hlon, body.hlat


polaris = ephem.readdb("Polaris,f|M|F7,2:31:48.704,89:15:50.72,2.02,2000")
# print(polaris.dec)

polaris.compute()    # uses the current time by default
print(polaris.a_dec)
print(ephem.degrees(ephem.degrees('90') - polaris.a_dec))

polaris.compute(epoch='2100')
print(polaris.a_dec)

thuban = ephem.readdb("Thuban,f|V|A0,14:4:23.3,64:22:33,3.65,2000")
thuban.compute()
print(thuban.a_dec)

print(thuban.a_dec)
polaris.compute(epoch='-2800')
print(polaris.a_dec)

j = ephem.Jupiter()
j.compute(epoch=ephem.now())   # so both date and epoch are now
print("%s %s" % (j.a_ra, j.a_dec))

j.compute('2003/3/25', epoch='2003/3/25')
print("%s %s" % (j.a_ra, j.a_dec))

j1, j2 = ephem.Jupiter(), ephem.Jupiter()
j1.compute('2003/3/1')
j2.compute('2003/4/1')
print(ephem.separation(
    (j1.a_ra, j1.a_dec),
    (j2.a_ra, j2.a_dec)))   # coordinates are both epoch 2000
j1.compute('2003/3/1', '2003/3/1')
j2.compute('2003/4/1', '2003/4/1')
print(ephem.separation(
    (j1.a_ra, j1.a_dec),
    (j2.a_ra, j2.a_dec)))   # coordinates are both epoch-of-date
