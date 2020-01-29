# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:03:38 2020

@author: PC
"""

import astropy.io.fits


fits = astropy.io.fits.open('http://www.astro.s.osakafu-u.ac.jp/~nishimura/Orion/data/Orion.CO1221.Osaka.beam204.mom0.fits.gz')
hdu = fits[0]

# データ部
data = hdu.data
print(data[0][0]) # ピクセル値

# ヘッダ部
header = hdu.header

# ヘッダ情報を確認
print(repr(header))
naxis = header['NAXIS']   # 辞書のように扱える
naxis1 = header.get('NAXIS1')
print(naxis)


# データ構造を確認
type(data)
print(data.ndim)
