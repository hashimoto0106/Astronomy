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

wcs.wcs_world2pix([[210, -19]], 0)   # (l=210, b=-19) の index を取得

wcs.wcs_pix2world([[150, 60]], 0)   # (x=150, y=60) の物理座標を取得
