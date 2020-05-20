# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:07:28 2019

@author: PC
"""

import folium
import pandas as pd
# from CAL_RHO import CAL_RHO
from tqdm import tqdm
import geocoder
import numpy as np

CSV_FILE = "TelescopeDB.csv"


def main():
    csv_telescope = pd.read_csv(filepath_or_buffer=CSV_FILE,
                            encoding="ms932", sep=",")
#    print(csv_telescope[["No.", "High School", "Address"]])

    koshien_location = [34.7211538, 135.3617240]  # 地図の基準として甲子園野球場を設定

    # 基準地点と初期の倍率を指定し、地図を作成する
    map = folium.Map(location=koshien_location, zoom_start=5)

    # 自宅(〒662-0843 兵庫県西宮市神祇官町６−２７ ジオ西宮北口ガーデンズ)マーカー設置
    home_location = [34.7401233, 135.35423200000002]
    marker = folium.Marker(home_location,
                           popup="Home",
                           icon=folium.Icon(color='red', icon='home'))
    map.add_child(marker)

    # Officeマーカー設置
    office_location = [34.76460823577404, 135.42264612647]
    marker = folium.Marker(office_location,
                           popup="Office",
                           icon=folium.Icon(color='black', icon='office'))
    map.add_child(marker)

    # 基準地点にマーカーを設置する
    marker = folium.Marker(koshien_location,
                           popup='甲子園',
                           icon=folium.Icon(color='green', icon='ball'))
    map.add_child(marker)

    df_lat_lon = pd.DataFrame(np.arange(300).reshape(150, 2),columns=['緯度', '経度'])
    
    # 地図マーキング
#    for no in tqdm(csv_telescope["No."]):
    for no in (csv_telescope["No."]):
        # 高校位置情報取得
        ret = geocoder.osm(csv_telescope.iat[no-1, 6], timeout=5.0)
        df_lat_lon.iat[no, 0] = ret.lat
        df_lat_lon.iat[no, 1] = ret.lng
        print(ret.lat)
        # print(ret.lng)

        # 甲子園からの距離算出
        telescope_location = [csv_telescope.iat[no-1, 7], csv_telescope.iat[no-1, 8]]
        # distance_from_koshien = CAL_RHO(telescope_location, koshien_location)
        # print('Distance={0:10.3f} km'.format(distance_from_koshien))

        # 家からの距離算出
        # distance_from_home = CAL_RHO(telescope_location, home_location)
        # print('Distance={0:10.3f} km'.format(distance_from_koshien))

        # 各高校にマーカーを設置
        marker = folium.Marker(telescope_location,  # 高校位置
                               popup=csv_telescope.iat[no-1, 1],  # 高校名
                               icon=folium.Icon(color='blue', icon='school')
                               )

        # 地図マーキング
        map.add_child(marker)


    # 地図をhtml形式で出力
    map.save(outfile="TelescopeMap.html")
    
    # csvファイル上書き
    # df_lat_lon.to_csv(CSV_FILE, columns=['緯度'])

if __name__ == '__main__': main()
