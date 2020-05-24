# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:23:58 2020

@author: PC
"""

from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt

simbad = Simbad()
simbad.add_votable_fields('flux(V)')

# simbadのデータは星の他に星団や銀河や星雲も含まれていますが、otype='star'を指定することで星だけに絞ります
# simbadから等級5以下の星を取
hoshi = simbad.query_criteria('Vmag<5', otype='star')
print(hoshi)

print(hoshi[hoshi['FLUX_V']<0.2])

sc = SkyCoord(ra=hoshi['RA'],dec=hoshi['DEC'],unit=['hourangle','deg'])
seiza = sc.get_constellation()
ra,dec = sc.ra,sc.dec
z = (seiza[:,None]==np.unique(seiza)).argmax(1)
iro = np.stack([z/87,z%5/4,1-z%4/4],1)
s = (5-hoshi['FLUX_V'])*3

x,y,z = sc.cartesian.xyz
fig = plt.figure(figsize=[6,6])
ax = plt.axes([0,0,1,1],projection='3d',xlim=[-0.6,0.6],ylim=[-0.6,0.6],zlim=[-0.6,0.6],facecolor='k')
ax.scatter(x,y,z,c=iro,s=s)
ra,dec = np.meshgrid(np.linspace(0,360,25),np.linspace(-90,90,13))
gx,gy,gz = SkyCoord(ra=ra,dec=dec,unit='deg').cartesian.xyz
ax.plot_wireframe(gx,gy,gz,color='#444444',linestyle='-') # 赤経と赤緯の線
ax.plot([0,0],[0,0],[-1.2,1.2],'#444444') # 中央の軸
plt.axis('off')
gif = []
for i in range(50):
    ax.view_init(30,i*360/50)
    fig.canvas.draw()
    gif.append(np.array(fig.canvas.renderer._renderer))
plt.close()
imageio.mimsave('seiza.gif',gif,fps=4)
