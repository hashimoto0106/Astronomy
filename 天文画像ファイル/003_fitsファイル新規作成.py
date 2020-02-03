# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 18:30:56 2020
https://qiita.com/eriksoon/items/c90d9738cfe1c1c83f3e
@author: PC
"""

import astropy.io.fits as fits

fits = fits.open('http://www.astro.s.osakafu-u.ac.jp/~nishimura/Orion/data/Orion.CO1221.Osaka.beam204.mom0.fits.gz')
hdu = fits[0]
data = hdu.data  # データ部
header = hdu.header  # ヘッダ部

hdu_new = fits.PrimaryHDU(data, header)
hdulist = fits.HDUList([hdu_new])
hdulist.writeto('new.fits',overwrite=True)
