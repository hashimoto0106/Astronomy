# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:09:42 2020

@author: PC
"""

from astropy import units as u
from astropy.units import imperial

# Standard units
print(u.g.find_equivalent_units())

# Enabling other units
imperial.enable()
print(u.m.find_equivalent_units())
