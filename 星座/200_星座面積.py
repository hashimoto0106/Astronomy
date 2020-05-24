# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:23:58 2020

@author: PC
"""

from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt

x,y,z = np.random.randn(3,1000000)
seiza = SkyCoord(x,y,z,representation_type='cartesian').get_constellation()
percent = sorted(('%.4f%%%20s'%(list(seiza).count(c)/10000,c) for c in set(seiza)),reverse=True)
print('\n'.join(percent))
