import xarray as xr
import numpy as np
from eofs.standard import Eof
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import cartopy.mpl.ticker as cticker
def contour_map(fig,img_extent,spec):
    fig.set_extent(img_extent, crs=ccrs.PlateCarree())
    fig.add_feature(cfeature.COASTLINE.with_scale('50m')) 
    fig.add_feature(cfeature.LAKES, alpha=0.5)
    fig.set_xticks(np.arange(leftlon,rightlon+spec,spec), crs=ccrs.PlateCarree())
    fig.set_yticks(np.arange(lowerlat,upperlat+spec,spec), crs=ccrs.PlateCarree())
    lon_formatter = cticker.LongitudeFormatter()
    lat_formatter = cticker.LatitudeFormatter()
    fig.xaxis.set_major_formatter(lon_formatter)
    fig.yaxis.set_major_formatter(lat_formatter)
f = xr.open_dataset("out.nc" )
dot = np.array(f['cspath'].loc[:,0:90,:])
lat = f['lat'].loc[0:90]
lon = f['lon']
years = range(1979, 2018)
solver = Eof(dot)
eof = solver.eofsAsCorrelation(neofs=2)
pc = solver.pcs(npcs=2, pcscaling=1)
var = solver.varianceFraction()
fig = plt.figure(figsize=(15,15))
proj = ccrs.PlateCarree(central_longitude=80) #投影
leftlon, rightlon, lowerlat, upperlat = (0,160,10,90) #地图边界
img_extent = [leftlon, rightlon, lowerlat, upperlat]
f_ax1 = fig.add_axes([0.1, 0.32, 0.3, 0.4],projection = proj)#EOF1
contour_map(f_ax1,img_extent,20) #利用前边自定义的绘图函数，目的是省去绘制相同图形时需要再次设置地形，湖泊，轴刻度等参数
f_ax1.set_title('(a) EOF1',loc='left')#左标题
f_ax1.set_title( '%.2f%%' % (var[0]*100),loc='right')#右标题，解释方差
f_ax1.contourf(lon,lat, eof[0,:,:], levels=np.arange(-0.9,1.0,0.1), zorder=0, extend='both',transform=ccrs.PlateCarree(), cmap=plt.cm.RdBu_r)#绘制填色
f_ax2 = fig.add_axes([0.1, 0.1, 0.3, 0.4],projection = proj)#EOF2
contour_map(f_ax2,img_extent,20)
f_ax2.set_title('(c) EOf',loc='left')
f_ax2.set_title( '%.2f%%' % (var[1]*100),loc='right')
c2=f_ax2.contourf(lon,lat, eof[1,:,:], levels=np.arange(-0.9,1.0,0.1), zorder=0, extend='both', transform=ccrs.PlateCarree(), cmap=plt.cm.RdBu_r)
#绘制色标
position=fig.add_axes([0.1, 0.17, 0.3, 0.017])
fig.colorbar(c2,cax=position,orientation='horizontal',format='%.1f',)
f_ax3 = fig.add_axes([0.45, 0.44, 0.3, 0.156])#绘制PC1
f_ax3.set_title('(b) PC1',loc='left')
f_ax3.set_ylim(-3,3)#y轴上下限
f_ax3.axhline(0,linestyle="-",c='k')#水平参考线
f_ax3.plot(years,pc[:,0],c='k')#绘制折线
pc1_9 = np.convolve(pc[:,0], np.repeat(1/9, 9), mode='valid')#计算九年滑动平均
f_ax3.plot(years[4:-4],pc1_9,c='r',lw=2)#绘制滑动平均
f_ax4 = fig.add_axes([0.45, 0.22, 0.3, 0.156])#绘制PC2
f_ax4.set_title('(d) PC2',loc='left')
f_ax4.set_ylim(-3,3)
f_ax4.axhline(0,linestyle="-",c='k')
f_ax4.plot(years,pc[:,1],c='k')
pc2_9 = np.convolve(pc[:,1], np.repeat(1/9, 9), mode='valid')
f_ax4.plot(years[4:-4],pc2_9,c='r',lw=2)
#plt.show()
plt.savefig("eof.pdf")