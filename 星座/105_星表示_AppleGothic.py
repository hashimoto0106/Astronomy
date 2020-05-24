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

# 夏の大三角を形成するはくちょう座とわし座とこと座
plt.gca(facecolor='k',aspect=1)
o = (seiza=='Lyra')
plt.scatter(ra[o],dec[o],c='#ffffaa',s=s[o])
vega = ra[o][s[o].argmax()].value,dec[o][s[o].argmax()].value
o = (seiza=='Aquila')
plt.scatter(ra[o],dec[o],c='#aaffff',s=s[o])
altair = ra[o][s[o].argmax()].value,dec[o][s[o].argmax()].value
o = (seiza=='Cygnus')
plt.scatter(ra[o],dec[o],c='#aaffaa',s=s[o])
deneb = ra[o][s[o].argmax()].value,dec[o][s[o].argmax()].value
plt.plot([vega[0],altair[0],deneb[0],vega[0]],[vega[1],altair[1],deneb[1],vega[1]],'--w',lw=0.5)
plt.title('夏の大三角',fontname='AppleGothic')
plt.show()
