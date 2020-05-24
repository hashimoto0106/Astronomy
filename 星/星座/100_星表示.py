# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:23:58 2020

@author: PC
"""

from astroquery.simbad import Simbad

simbad = Simbad()
simbad.add_votable_fields('flux(V)')

# simbadのデータは星の他に星団や銀河や星雲も含まれていますが、otype='star'を指定することで星だけに絞ります
# simbadから等級5以下の星を取
hoshi = simbad.query_criteria('Vmag<5', otype='star')
print(hoshi)

print(hoshi[hoshi['FLUX_V']<0.2])
