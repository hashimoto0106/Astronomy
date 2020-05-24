# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:23:58 2020

@author: PC
"""

from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt

simbad = Simbad()
simbad.add_votable_fields('flux(V)')

# simbadのデータは星の他に星団や銀河や星雲も含まれていますが、otype='star'を指定することで星だけに絞ります
# simbadから等級5以下の星を取
hoshi = simbad.query_criteria('Vmag<5', otype='star')
print(hoshi)

print(hoshi[hoshi['FLUX_V']<0.2])

sc = SkyCoord(ra=hoshi['RA'],dec=hoshi['DEC'],unit=['hourangle','deg'])
seiza = sc.get_constellation()
ra,dec = sc.ra,sc.dec
z = (seiza[:,None]==np.unique(seiza)).argmax(1)
iro = np.stack([z/87,z%5/4,1-z%4/4],1)
s = (5-hoshi['FLUX_V'])*3

plt.figure(figsize=[8,4])

# 北斗七星を含むおおぐま座
plt.gca(facecolor='k',aspect=1,title='Ursa Major')
o = (seiza=='Ursa Major')
plt.scatter(ra[o],dec[o],c='w',s=s[o])
plt.show()
