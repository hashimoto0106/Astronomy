# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:03:38 2020
https://qiita.com/nishimuraatsushi/items/f422c624027dcd34b820
@author: PC
"""

import astropy.units

# 1: 5km/s で動く分子雲コアが 5pc 移動するのにかかる時間を計算してみる
v = 5 * astropy.units.kilometer / astropy.units.second
# >>> <Quantity 5.0 km / s>

d = 5 * astropy.units.pc
# >>> <Quantity 5.0 pc>

(d/v).to('megayear')
# >>> <Quantity 0.9777922216731284 Myr>

# 2: 10^-6 Mo/yr の質量降着率を、kg/sec にしてみる
(1e-6 * astropy.units.solMass / astropy.units.year).to('kg/second')
