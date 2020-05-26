# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:03:38 2020
https://qiita.com/nishimuraatsushi/items/f422c624027dcd34b820
@author: PC
"""

import numpy
import astropy.coordinates
import astropy.wcs
import astropy.io.fits
fits = astropy.io.fits.open('http://www.astro.s.osakafu-u.ac.jp/~nishimura/Orion/data/Orion.CO1221.Osaka.beam204.mom0.fits.gz')
header = fits[0].header
data = fits[0].data

maxind = numpy.unravel_index(numpy.nanargmax(data), data.shape)
wcs = astropy.wcs.WCS(fits[0].header)
maxworld = wcs.wcs_pix2world([maxind[::-1]], 0) 
        # wcs_pix2world の要求するインデックスの軸の順は x, y(, z)
        # fits[0].data の軸の順は、(z,) y, x
        # この 2 つの向きが逆なので、maxind[::-1] で反転させている
galx, galy = maxworld[0]
# >>> (208.99999963578261, -19.383371004831144)

# 銀河座標で作成
coord = astropy.coordinates.SkyCoord(galx, galy, frame='galactic', unit='deg')
# >>> <SkyCoord (Galactic): (l, b) in deg
#         (208.99999964, -19.383371)>

# 星座を確認
coord.get_constellation()
