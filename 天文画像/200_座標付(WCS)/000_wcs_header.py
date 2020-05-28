# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:03:38 2020
https://qiita.com/nishimuraatsushi/items/f422c624027dcd34b820
@author: PC
"""

import astropy.wcs
import astropy.io.fits


fits = astropy.io.fits.open('http://www.astro.s.osakafu-u.ac.jp/~nishimura/Orion/data/Orion.CO1221.Osaka.beam204.mom0.fits.gz')

wcs = astropy.wcs.WCS(fits[0].header)
print(wcs)
