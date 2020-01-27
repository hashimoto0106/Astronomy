# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 21:31:07 2019

@author: PC
"""

import ephem
import datetime
import math
import numpy as np


def main():
    # 観測者
    osaka = ephem.Observer()
    osaka.lat = '34.6883'
    osaka.lon = '135.4933'
    osaka.date = datetime.datetime.utcnow()
    print(osaka)

    # 国際宇宙ステーション軌道要素
    iss = ephem.readtle('ISS',
                    '1 25544U 98067A   19251.51298924  .00000370  00000-0  14350-4 0  9995',
                    '2 25544  51.6453 307.9614 0007973  18.9504 129.2301 15.50436909188185')

    # 大阪で現在時刻において、国際宇宙ステーションが見える方向を計算
    iss.compute(osaka)
    print("方位角 : " + str(math.degrees(iss.az)) + "[deg]")
    print("仰角  : " + str(math.degrees(iss.alt)) + "[deg]")

    # 大阪上空を通るパスを計算
    # （出現時刻、出現方位角、最大高度となる時刻、最大高度、没時刻、没方向）
    rise_t, az_rise, max_t, alt_max, set_t, az_set = osaka.next_pass(iss)
    print(u"見え始め時刻: %s 方位角: %.1f" % (ephem.localtime(rise_t), np.rad2deg(az_rise)))
    print(u"最大迎角時刻: %s 最大迎角: %.1f" % (ephem.localtime(max_t), np.rad2deg(alt_max)))
    print(u"見え終わり時刻: %s 方位角: %.1f" % (ephem.localtime(set_t), np.rad2deg(az_set)))


if __name__ == '__main__':
    main()
