# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:53:22 2020

@author: PC
"""

import matplotlib as mpl

toki = astropy.time.Time('2019-5-16') - 9*u.hour
toki += np.linspace(0,24,1441)*u.hour
taiyou = get_sun(toki).transform_to(AltAz(obstime=toki,location=koko))
plt.plot((toki+9*u.hour).datetime,taiyou.alt.value,'r')
plt.gca().xaxis.set_major_formatter(mpl.dates.DateFormatter('%H:%M'))
plt.axhline(0,ls='--',color='k') # 日の出と日没の線
takasa = taiyou.alt.max().value # 一番高い高さ
takai_toki = (toki[taiyou.alt.argmax()]+9*u.hour).datetime # 一番高い時間
plt.scatter(takai_toki,takasa)
plt.text(takai_toki,takasa,'%s\n%.2f[deg]'%(takai_toki.strftime('%H:%M'),takasa),fontname='AppleGothic',va='top',ha='center')
plt.xlabel(u'Time',fontname='AppleGothic')
plt.ylabel(u'EL[deg]',fontname='AppleGothic')
plt.show()
