#!/usr/bin/python
# -*- coding: utf8 -*-

from fonction import *
from jules_download import *
from Split_times_Marine import *




from mpl_toolkits.basemap import Basemap
from osgeo import gdal



version_plot='WFDEI_AnthroOff_' #WFDEI and AnthroOff
legende_variable='$Q_{H}$  $W.m^{-2}$'
name_variable_JULES='ftl_gb'
name_variable_OBS='qh'
name_file_plot='QH'
#name_file_plot_A='AnthroOn_QH'
name_variable_SUEWS='QH'




site='London KC'
moruses_folder='/storage/shared/research/met/micromet/JULES/u-av612_MORUSES_London_KSSW/'
best_folder='/storage/shared/research/met/micromet/JULES/u-av588_1-tile_London_KSSW/'
obs_folder='/storage/shared/research/met/micromet/JULES/SUEWSEvaluationData/Kc/Obs/'
suews_folder='/storage/shared/research/met/micromet/JULES/SUEWSEvaluationData/Kc/Output/'
name_file_suews=['Kc1_2011_60.txt','Kc1_2012_60.txt','Kc1_2013_60.txt']
local_time='Europe/London'
Start= datetime.datetime(2011, 01, 01,00,00,00)
Start_SUEWS= datetime.datetime(2011, 01, 01,00,00,00)
year_study='2011-2013'
year_study_short='11-13'
with_obs='yes'
local_hour=0
with_SUEWS='yes'

if(version_plot==''):
	save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/AnthroOff/KC/'# Anthropogenic Flux OFF
	moruses_version=74899# Anthropogenic Flux OFF
	best_version=74898# Anthropogenic Flux OFF
elif(version_plot=='AnthroOn_'):
	save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/AnthroOn/KC/'# Anthropogenic Flux ON
	moruses_version=74930# Anthropogenic Flux ON
	best_version=74929# Anthropogenic Flux ON
elif(version_plot=='WFDEI_AnthroOff_'):
	save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOff/KC/'# Anthropogenic Flux ON
	moruses_version=74885# Anthropogenic Flux ON
	best_version=74884# Anthropogenic Flux ON
elif(version_plot=='WFDEI_AnthroOn_'):
	save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOn/KC/'# Anthropogenic Flux ON
	moruses_version=74281# Anthropogenic Flux ON
	best_version=74280# Anthropogenic Flux ON

Var_moruses=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES,Start)[0]
Var_best=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[0]

if(name_file_plot=='AnthroOn_SW_up' or name_file_plot=='SW_up'):
	Var_moruses_1=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_best_1=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_moruses_2=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES2,Start)[0]
	Var_best_2=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES2,Start)[0]
	Var_moruses=Var_moruses_2-Var_moruses_1
	Var_best=Var_best_2-Var_best_1

Time_moruses=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES,Start)[1]
if(local_time!='Europe/London') : Time_moruses=convert_UTC_to_local(Time_moruses,local_time)
lon_moruses=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc','longitude',Start)[0]
lat_moruses=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc','latitude',Start)[0]




name_file='/storage/shared/research/met/micromet/JULES/Marine/maps_WFDEI/WFDEI-copie.txt'

variable=['Longitude','Latitude','Ht(m)','glon','glat']


dataset_panda=pandas.read_table(name_file, sep="\s+", header=0, index_col =False)

#print toto[0:10]
#print toto.size
#print toto.shape


lon=dataset_panda[variable[0]].tolist()
lat=dataset_panda[variable[1]].tolist()
alt=dataset_panda[variable[2]].tolist()
glon=dataset_panda[variable[3]].tolist()
glat=dataset_panda[variable[4]].tolist()

data=np.array([lon,lat,alt,glon,glat])

print lon[0:10]
print lat[0:10]
print type(lon)
print len(lon)

print data.shape
print data[0,:][0:10]
print data[0,0:10]

print data[1,:][0:10]
print data[1,0:10]

print data[:,1:11]

lon_min=-1.220088
lon_max=0.790410
lat_max=51.949409
lat_min=51.108762

print data[:,[0,1,3]]


#print range(0,len(lon))

#index=[i for i, j in range(0,len(lon)) if (lat[j]>lat_min and lat[j]<lat_max and lon[j]>lon_min and lon[j]<lon_max)]
#print index


#j2 = [i for i in j if i >= 5]

index=[]
for j in range(0,len(lon)) :
	if((lat[j]>lat_min and lat[j]<lat_max and lon[j]>lon_min and lon[j]<lon_max)) : index.append(j)

print index

print data[:,index]

fig = plt.figure(figsize=(7, 8))

m = Basemap(llcrnrlon=lon_min-1, llcrnrlat=lat_min-1, urcrnrlon=lon_max+1, urcrnrlat=lat_max+1, projection='lcc',lon_0=-0.132442,lat_0=51.513937)		
m.shadedrelief()
#m.drawcoastlines(color='gray')
#m.drawcountries(color='gray')

m.drawcoastlines()
m.drawstates()
m.drawcountries()

# draw parallels.
parallels = data[1,index]
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
# draw meridians
meridians = data[0,index]
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)
ny = data.shape[0]; nx = data.shape[1]
lons, lats = m.makegrid(nx, ny) # get lat/lons of ny by nx evenly space grid.
x, y = m(lons, lats) # compute map proj coordinates.



m.scatter(lon_moruses, lat_moruses, latlon=True,c=([0]))
m.scatter(-0.117, 51.51, latlon=True,c=([1]))

save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/Input/'



#for i in range(0,len(data[2,index].tolist())):
#	plt.annotate(  data[2,index][i]   ,xytext=(data[1,index][i], data[0,index][i]),  xycoords='data')

for i in range(0,len(data[2,index].tolist())):
	print data[0,index][i],(lat_max+1), data[1,index][i],data[2,index][i], data[1,index][i]/(lat_max+1), data[0,index][i]/(lon_max+1)
	plt.annotate(data[2,index][i], xy=((data[0,index][i]-(lon_min-1))/((lon_max+1)-(lon_min-1)),(data[1,index][i]-(lat_min-1))/((lat_max+1)-(lat_min-1))),xycoords='axes fraction',horizontalalignment='right', verticalalignment='bottom')
	#plt.text(data[0,index][i], data[1,index][i],  data[2,index][i])

plt.savefig(save_directory+'maps_WFDEI_OBS.png',dpi=200)

plt.show()
	
