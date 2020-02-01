# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:59:43 2020
https://qiita.com/phyblas/items/a801b0f319742245ad2e
@author: PC
"""

import astropy.coordinates
from astropy.table import Table
import os
import matplotlib.pyplot as plt
from tqdm import tqdm

dat_path = os.path.join(astropy.coordinates.__path__[0],'data','constellation_data_roman87.dat')
ctable = Table.read(dat_path,format='ascii')
print(ctable)

cmap = plt.get_cmap('jet')
col4 = ctable.field(3) # 星座の略号
dic = {n:i for i,n in enumerate(set(col4))} # 星座の略号を数字にする辞書
plt.figure(figsize=[7,4])
ax = plt.gca(xlim=[0,360],ylim=[-90,90],aspect=1)
for c in tqdm(reversed(ctable)): # 上の行は優先なので最後の行から描き始める
    ral = c[0]*15 # 赤経の下限
    rau = c[1]*15 # 赤経の上限
    decl = c[2] # 赤緯の下限
    p = plt.Rectangle([ral,decl],rau-ral,90-decl,fc=cmap(dic[c[3]]/87.))
    ax.add_patch(p)
plt.show()
