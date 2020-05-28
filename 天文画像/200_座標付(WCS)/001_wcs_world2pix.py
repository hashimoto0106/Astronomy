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

# WCS[geg]→画像座標系[pix]変換
print(wcs.wcs_world2pix([[215, -13.0]], 0))
print(wcs.wcs_world2pix([[214, -13.2]], 0))
print(wcs.wcs_world2pix([[213, -13.4]], 0))
print(wcs.wcs_world2pix([[212, -13.6]], 0))
print(wcs.wcs_world2pix([[211, -13.8]], 0))
print(wcs.wcs_world2pix([[210, -14.0]], 0))
print(wcs.wcs_world2pix([[209, -14.2]], 0))
print(wcs.wcs_world2pix([[208, -14.4]], 0))
print(wcs.wcs_world2pix([[207, -14.6]], 0))
