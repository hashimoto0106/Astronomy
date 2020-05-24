# -*- coding: utf-8 -*-
"""
Created on Sun May  3 01:35:30 2020

@author: PC
"""

import ephem
from datetime import datetime 
from pytz import timezone

def lunar_date_calc(year, month, day, hour, min, sec):

    # 指定時刻をUTCに変換
    jst = datetime(year, month, day, hour, min, sec)
    local_tz = timezone('Asia/Tokyo')
    jst = local_tz.localize(jst)
    utc = jst.astimezone(timezone('UTC'))

    # 前回新月時刻を求め結果をJSTに変換
    previous_new_moon_time = ephem.previous_new_moon(utc).datetime()
    previous_new_moon_time = timezone('UTC').localize(previous_new_moon_time)
    previous_new_moon_time_jst = previous_new_moon_time.astimezone(timezone('Asia/Tokyo'))

    # 前回新月時刻から指定時刻までの経過時間から月齢を求める（小数点２位以下は四捨五入）
    lunar_date = jst - previous_new_moon_time_jst
    lunar_date = round(lunar_date.days + lunar_date.seconds/(60*60*24.), 1)
    return lunar_date


# 月齢を求めたい日時の正午時刻を与え「正午月齢」を求めてみる。
# 正午時刻以外を与えると、その時刻での月齢になります。
year=2018
month=10
day=4
hour=12
min=0
sec=0

lunar_date = lunar_date_calc(year, month, day, hour, min, sec)
print('月齢=', lunar_date)
