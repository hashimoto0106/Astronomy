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
