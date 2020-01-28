# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:09:39 2020

@author: PC
"""

import astropy.io.fits as iofits
import matplotlib.pyplot as plt

list = iofits.open("WFPC2u5780205r_c0fx.fits")
print(list)

pic = list[0]
data = pic.data
header = pic.header
print(header)

# データ構造を確認
type(data)
print(data.ndim) # 3次元だと表示でエラーとなる

#plt.imshow(data)
#plt.show()
