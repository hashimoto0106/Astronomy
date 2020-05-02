# -*- coding: utf-8 -*-
"""
Created on Sun May  3 01:35:30 2020

@author: PC
"""

import ephem
import datetime


# 観測者
osaka = ephem.Observer()
osaka.lat = '34.6914'
osaka.lon = '135.4917'
osaka.date = datetime.datetime.utcnow()

# 月インスタンス作成
moon = ephem.Moon()

print("次の月の出　 : ", ephem.localtime(osaka.next_rising(moon)))
print("次の月の入り : ", ephem.localtime(osaka.next_setting(moon)))

print("次の新月 : ", ephem.localtime(ephem.next_new_moon(osaka.date)))
print("次の上弦 : ", ephem.localtime(ephem.next_first_quarter_moon(osaka.date)))
print("次の満月 : ", ephem.localtime(ephem.next_full_moon(osaka.date)))
print("次の下弦 : ", ephem.localtime(ephem.next_last_quarter_moon(osaka.date)))
print("現在の月齢 : ", osaka.date - ephem.previous_new_moon(osaka.date))
