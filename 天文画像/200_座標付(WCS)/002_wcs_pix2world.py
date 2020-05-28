# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:44:39 2020

@author: PC
"""

import astropy.wcs
import astropy.io.fits


fits = astropy.io.fits.open('http://www.astro.s.osakafu-u.ac.jp/~nishimura/Orion/data/Orion.CO1221.Osaka.beam204.mom0.fits.gz')

wcs = astropy.wcs.WCS(fits[0].header)
print(wcs)

# 画像座標系[pix]→WCS[geg]変換
print(wcs.wcs_pix2world([[0, 0]], 0))
print(wcs.wcs_pix2world([[100, 50]], 0))
print(wcs.wcs_pix2world([[200, 100]], 0))
print(wcs.wcs_pix2world([[300, 150]], 0))
print(wcs.wcs_pix2world([[400, 200]], 0))
print(wcs.wcs_pix2world([[500, 250]], 0))
print(wcs.wcs_pix2world([[600, 300]], 0))
print(wcs.wcs_pix2world([[700, 350]], 0))
