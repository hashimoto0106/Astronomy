# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:07:43 2020
https://rhodesmill.org/pyephem/quick.html#phases-of-the-moon
@author: PC
"""

import ephem

d1 = ephem.next_full_moon('1984')
print(d1)
d2 = ephem.next_new_moon(d1)
print(d2)

print(ephem.previous_new_moon('2020'))
print(ephem.next_new_moon('2020'))

print(ephem.previous_first_quarter_moon('2020'))
print(ephem.next_first_quarter_moon('2020'))

print(ephem.previous_full_moon('2020'))
print(ephem.next_full_moon('2020'))

print(ephem.previous_last_quarter_moon('2020'))
print(ephem.next_last_quarter_moon('2020'))
