# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:09:39 2020

@author: PC
"""

import matplotlib.pyplot
import astropy.io.fits
import aplpy

# FITS ファイルを web からダウンロードする場合
# fits = astropy.io.fits.open('http://www.astro.s.osakafu-u.ac.jp/~nishimura/Orion/data/Orion.CO1221.Osaka.beam204.mom0.fits.gz')
# fig = aplpy.FITSFigure(fits)

# FITS ファイルが local に保存されている場合
fig = aplpy.FITSFigure('Orion.CO1221.Osaka.beam204.mom0.fits.gz')

fig.show_colorscale()
fig.add_colorbar()
fig.save('Orion.CO1221.Osaka.beam204.mom0.png')  # 画像を保存する場合
