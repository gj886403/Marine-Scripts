#!/usr/bin/python
# -*- coding: utf8 -*-

from fonction import *
from jules_download import *
from Split_times_Marine import *
from rotate_landuse import *


from mpl_toolkits.basemap import Basemap
from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

save_plot='no'
with_obs='no'
save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/CLIMATE/'


#name_var_clim='surface_downwelling_shortwave_flux_in_air'
name_var_clim='stratiform_rainfall_flux'
#name_var_clim='surface_upward_latent_heat_flux'
name_var_clim='UM_m01s03i217_vn1006'
#name_var_clim='air_temperature'
name_var_clim='surface_air_pressure'



#name_var_clim='northward_wind'
#name_var_clim='UM_m01s08i208_vn1006'# Soil moisture
#name_var_clim='UM_m01s05i205_vn1006'# Convective rainfall
name_var_clim='UM_m01s05i216_vn1006'# Total previpitation
#name_var_clim='UM_m01s04i203_vn1006'# Large Scale
#name_var_clim='UM_m01s00i024_vn1006'# Surface Temperature after timestep

#ap9
name_var_clim='UM_m01s00i409_vn1006'# P
name_var_clim='UM_m01s03i236_vn1006'# Tair
#name_var_clim='wind'

#ape
#name_var_clim='UM_m01s03i223_vn1006'# surface total moisture flux

#ap1
###name_var_clim='UM_m01s00i266_vn1006'# cloud
#name_var_clim='UM_m01s03i217_vn1006'# QH
##name_var_clim='UM_m01s03i261_vn1006'# gross primary productivity
##name_var_clim='UM_m01s03i262_vn1006'# net primary productivity
##############name_var_clim='UM_m01s08i225_vn1006'# 
#name_var_clim='UM_m01s08i234_vn1006'# surface runoff
#name_var_clim='UM_m01s03i234_vn1006'# QE

#apd
###name_var_clim='UM_m01s00i266_vn1006'# cloud
#name_var_clim='UM_m01s03i217_vn1006'# QH
#name_var_clim='UM_m01s03i234_vn1006'# QE
#name_var_clim='UM_m01s01i235_vn1006'# SW down
#name_var_clim='UM_m01s01i201_vn1006'# SW net
#name_var_clim='UM_m01s02i207_vn1006'# L down
#name_var_clim='UM_m01s02i201_vn1006'# L net
#name_var_clim='UM_m01s03i245_vn1006'# Hu
#name_var_clim='UM_m01s03i237_vn1006'# q


#year=[2006,2007,2008,2009,2010]
year=[2007,2008,2009,2010]
year=[2009]

vect_month=['J','F','M','A','M','J','J','A','S','O','N','D']

[s +' '+ str(year[0]) for s in vect_month]

vect_month_year=[]
for i in range(0, len(year)):
	vect_month_year.extend([s +' '+ str(year[i]) for s in vect_month])

if(name_var_clim=='UM_m01s08i208_vn1006') :
	legend_axes_var='Soil Moisture $kg.m^{-2}$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apa/'
	climat_file='u-aj981.apa.london.'
	name_file='Hu_soil'
elif(name_var_clim=='UM_m01s05i205_vn1006') :
	legend_axes_var='Conv RR $kg.m^{-2}.s^{-1}$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apa/'
	climat_file='u-aj981.apa.london.'
	name_file='RRconv'
elif(name_var_clim=='UM_m01s05i216_vn1006') :
	legend_axes_var='Total Precipitation $kg.m^{-2}.s^{-1}$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apa/'
	climat_file='u-aj981.apa.london.'
	name_file='Precip'
elif(name_var_clim=='UM_m01s04i203_vn1006') :
	legend_axes_var='Large Scale $kg.m^{-2}.s^{-1}$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apa/'
	climat_file='u-aj981.apa.london.'
	name_file='PrecipLarge'
elif(name_var_clim=='UM_m01s00i024_vn1006') :
	legend_axes_var='$T_{surf}$ $K$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apa/'
	climat_file='u-aj981.apa.london.'
	name_file='Tsurf'
elif(name_var_clim=='UM_m01s00i024_vn1006') :
	legend_axes_var='$T_{surf}$ $K$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apa/'
	climat_file='u-aj981.apa.london.'
	name_file='Tsurf'
elif(name_var_clim=='UM_m01s00i409_vn1006'):
	year=[2006,2007]
	legend_axes_var='$P$  $Pa$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/ap9/'
	climat_file='u-aj981.ap9.london.'
	name_file='P'
elif(name_var_clim=='UM_m01s03i236_vn1006'):
	year=[2007]
	legend_axes_var='$T_{air}$  $C$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/ap9/'
	climat_file='u-aj981.ap9.london.'
	name_file='Tair'
elif(name_var_clim=='wind'):
	name_var_climU='UM_m01s03i209_vn1006_true_latitude_longitude'
	name_var_climV='UM_m01s03i210_vn1006_true_latitude_longitude'
	year=[2009]
	legend_axes_var='$Wind Speed$   $m.s^{-1}$'
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/ap9/'
	climat_file='u-aj981.ap9.london.'
	name_file='V'
elif(name_var_clim=='UM_m01s03i223_vn1006'):
	year=[2006,2007,2008,2009,2010]
	legend_axes_var='$Surf HU flux$  $-$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/ape/'
	climat_file='u-aj981.ape.london.'
	name_file='Tair'

elif(name_var_clim=='UM_m01s03i234_vn1006'):
	year=[2009]
	legend_axes_var='$Q_{E}$  $W$ $m^{-2}$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apd/'
	climat_file='u-aj981.apd.london.'
	name_file='QE'
elif(name_var_clim=='UM_m01s08i234_vn1006'):
	year=[2006,2007,2008,2009,2010]
	legend_axes_var='$Runoff$  $-$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/ap1/'
	climat_file='u-aj981.ap1.london.'
	name_file='Runoff'
elif(name_var_clim=='UM_m01s03i217_vn1006'):
	year=[2009]
	legend_axes_var='$Q_{H}$  $W$ $m^{-2}$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apd/'
	climat_file='u-aj981.apd.london.'
	name_file='QH'
elif(name_var_clim=='UM_m01s01i235_vn1006'):
	year=[2009]
	legend_axes_var='$K_{\downarrow}$  $W$ $m^{-2}$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apd/'
	climat_file='u-aj981.apd.london.'
	name_file='Kdown'
elif(name_var_clim=='UM_m01s01i201_vn1006'):
	year=[2009]
	legend_axes_var='$K_{*}$  $W$ $m^{-2}$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apd/'
	climat_file='u-aj981.apd.london.'
	name_file='Kstar'
elif(name_var_clim=='UM_m01s02i207_vn1006'):
	year=[2009]
	legend_axes_var='$L_{\downarrow}$  $W$ $m^{-2}$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apd/'
	climat_file='u-aj981.apd.london.'
	name_file='Ldown'
elif(name_var_clim=='UM_m01s02i201_vn1006'):
	year=[2009]
	legend_axes_var='$L_{*}$  $W$ $m^{-2}$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apd/'
	climat_file='u-aj981.apd.london.'
	name_file='Lstar'
elif(name_var_clim=='UM_m01s03i245_vn1006'):
	year=[2009]
	legend_axes_var='$Hu$  $-$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apd/'
	climat_file='u-aj981.apd.london.'
	name_file='Hu'
elif(name_var_clim=='UM_m01s03i237_vn1006'):
	year=[2009]
	legend_axes_var='$q$  $-$'   
	climat_folder='/storage/shared/research/met/micromet/JULES/Marine/Climate_run/apd/'
	climat_file='u-aj981.apd.london.'
	name_file='q'



#############################################################################
######################### JULES
moruses_folder='/storage/shared/research/met/micromet/JULES/u-av612_MORUSES_London_KSSW/'
version_plot='' #OBS and AnthroOff
#var=['SW_up','QH','Q_star','K_star','K_down','L_up','L_down']
var=['QH']

for var_i in var :
	if (var_i=='QH') :
		legende_variable='$Q_{H}$  $W$ $m^{-2}$'
		name_variable_JULES='ftl_gb'
		name_variable_OBS='qh'
		name_file_plot='QH'
		name_variable_SUEWS='QH'
	if(version_plot==''):
		moruses_version=76930# Anthropogenic Flux OFF
	Start= datetime.datetime(2011, 01, 01,00,00,00)
	Var_moruses=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES,Start)[0]
	Time_moruses=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES,Start)[1]
	lon_JULES=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc','longitude',Start)[0]
	lat_JULES=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc','latitude',Start)[0]

#############################################################################
######################### CLIMATE

#f = Dataset(climat_folder+climat_file+str(2007)+'.nc', 'r')
#for v in f.variables : print v, f.variables[v]
#plt.figure()
#plt.show()

############################# Read Climate
Time_CLIM=[]
Var_CLIM=[]
print Time_CLIM
for i in range(0,len(year)):
	print climat_folder+climat_file+str(year[i])+'.nc'
	f = Dataset(climat_folder+climat_file+str(year[i])+'.nc', 'r')
	Time_memory=(i*360.+np.squeeze(f.variables['time'][:])).tolist()
	if(name_var_clim=='wind'):
		V_CLIM= np.squeeze(f.variables[name_var_climV][:])
		U_CLIM= np.squeeze(f.variables[name_var_climU][:])
		U_CLIM_scalar=U_CLIM[:,:,0:U_CLIM.shape[2]-1]*0
		for i in range (0,(U_CLIM.shape[2]-1)):
			U_CLIM_scalar[:,:,i]=(U_CLIM[:,:,i]+U_CLIM[:,:,i+1])/2
		V_CLIM_scalar=V_CLIM[:,0:V_CLIM.shape[1],:]*0
		for i in range (0,(V_CLIM.shape[1]-1)):
			V_CLIM_scalar[:,i+1,:]=(V_CLIM[:,i,:]+V_CLIM[:,i+1,:])/2
		WS_CLIM_scalar=np.sqrt(V_CLIM_scalar*V_CLIM_scalar+U_CLIM_scalar*U_CLIM_scalar)
		Var_memory=WS_CLIM_scalar
	elif(name_var_clim=='UM_m01s03i236_vn1006'):
		Var_memory=(np.squeeze(f.variables[name_var_clim][:])-273.14).tolist()
	else :
		Var_memory=(np.squeeze(f.variables[name_var_clim][:])).tolist()
	print i,Time_CLIM
	Time_CLIM.extend(Time_memory)
	Var_CLIM.extend(Var_memory)

Var_CLIM=np.array(Var_CLIM)
Time_CLIM=np.array(Time_CLIM)
print '****'
print Time_CLIM
print np.array(Var_CLIM).shape

############################## Get longitude and latitude
lon_CLIM=np.squeeze(f.variables['longitude'][:])
lat_CLIM=np.squeeze(f.variables['latitude'][:])


for i in range(0,21):
	for j in range(0,30):
#		print(sum(x is not None for x in Var_CLIM[:,i,j].tolist()))
		if (sum(x is not None for x in Var_CLIM[:,i,j].tolist())==0) : 
#			print Var_CLIM[:,i,j]
			Var_CLIM[:,i,j]=[float('nan')]*len(Var_CLIM[:,i,j].tolist())
#			print Var_CLIM[:,i,j]
#			print '****'
		
Var_CLIM[Var_CLIM ==0.] = float('nan')
#plt.figure()
#plt.show()


lon_GRID= np.append(np.squeeze(f.variables['longitude_bounds'][:])[:,0].tolist(),np.squeeze(f.variables['longitude_bounds'][:])[(lon_CLIM.shape[0]-1),1])
delta_lon_GRID=lon_GRID[1]-lon_GRID[0]

lat_GRID= np.append(np.squeeze(f.variables['latitude_bounds'][:])[:,0].tolist(),np.squeeze(f.variables['latitude_bounds'][:])[(lat_CLIM.shape[0]-1),1])
delta_lat_GRID=lat_GRID[1]-lat_GRID[0]
#print type(lon_CLIM)
#print lon_CLIM.shape[0]
#print np.squeeze(f.variables['longitude_bounds'][:])[(lon_CLIM.shape[0]-1),1]
#print lon_CLIM


################################################### Monthly mean on each gridbox
Monthly_mean=[]
for j in range(0,int(max(Time_CLIM))/30+1):
	index_1_month=[i for i,x in enumerate(Time_CLIM) if int(x)/30 == j]
	#print Var_CLIM[index_1_month,:,:]
	#print Var_CLIM[index_1_month,:,:].shape
	#print Var_CLIM[index_1_month,:,:]==Var_CLIM[0:720,:,:]
	#print np.mean(Var_CLIM[index_1_month,:,:], axis=0)
	#print np.mean(Var_CLIM[index_1_month,:,:], axis=0).shape
	#print j
	#print Var_CLIM[index_1_month,:,:]
	Monthly_mean.append(np.nanmean(Var_CLIM[index_1_month,:,:], axis=0))
#	print np.extract(np.array(int(Time_CLIM))/30==i, np.array(Var_CLIM))

Monthly_mean=np.array(Monthly_mean)



lon_min=lon_GRID.min()
lon_max=lon_GRID.max()
lat_min=lat_GRID.min()
lat_max=lat_GRID.max()

################################### We want to extract 3 regions

index_lat=[] # List of the 3 lat of LONDON and WEST
for j in range(0,len(lat_GRID)) :
	if((lat_GRID[j]>lat_JULES-2*delta_lat_GRID and lat_GRID[j]<lat_JULES+2*delta_lat_GRID)) : index_lat.append(j)

index_lon=[]# List of the 3 lon of LONDON
for j in range(0,len(lon_GRID)) :
	if((lon_GRID[j]>lon_JULES-2*delta_lon_GRID and lon_GRID[j]<lon_JULES+2*delta_lon_GRID)) : index_lon.append(j)

index_lon_ruralwest=[] # List of the 3 lon of WEST
for j in range(0,len(lon_GRID)) :
	if((lon_GRID[j]>-1.6 and lon_GRID[j]<-1.0)) : index_lon_ruralwest.append(j)

index_lon_north=[] # List of the 3 lon of NORTH
for j in range(0,len(lon_GRID)) :
	if((lon_GRID[j]>0.5 and lon_GRID[j]<1.0)) : index_lon_north.append(j)

index_lat_north=[] # List of the 3 lat of NORTH
for j in range(0,len(lat_GRID)) :
	if((lat_GRID[j]>51.8 and lat_GRID[j]<52.2)) : index_lat_north.append(j)


print index_lat

############################################# Extraction of the 3 regions
lat_CITY=np.array(lat_CLIM)[index_lat[0]:(index_lat[-1])]
lon_CITY=np.array(lon_CLIM)[index_lon[0]:(index_lon[-1])]
Var_CITY=Var_CLIM[:,index_lat[0]:(index_lat[-1]),index_lon[0]:(index_lon[-1])]
Monthly_mean_CITY=Monthly_mean[:,index_lat[0]:(index_lat[-1]),index_lon[0]:(index_lon[-1])]

lon_RURALWEST=np.array(lon_CLIM)[index_lon_ruralwest[0]:(index_lon_ruralwest[-1])]
Var_RURALWEST=Var_CLIM[:,index_lat,index_lon_ruralwest]
Var_RURALWEST=Var_CLIM[:,index_lat[0]:(index_lat[-1]),index_lon_ruralwest[0]:(index_lon_ruralwest[-1])]
Monthly_mean_RURALWEST=Monthly_mean[:,index_lat[0]:(index_lat[-1]),index_lon_ruralwest[0]:(index_lon_ruralwest[-1])]

lon_NORTH=np.array(lon_CLIM)[index_lon_north[0]:(index_lon_north[-1])]
lat_NORTH=np.array(lat_CLIM)[index_lat_north[0]:(index_lat_north[-1])]
Var_NORTH=Var_CLIM[:,index_lat_north,index_lon_north]
Var_NORTH=Var_CLIM[:,index_lat_north[0]:(index_lat_north[-1]),index_lon_north[0]:(index_lon_north[-1])]
Monthly_mean_NORTH=Monthly_mean[:,index_lat_north[0]:(index_lat_north[-1]),index_lon_north[0]:(index_lon_north[-1])]


########################################### Division in each season and each hour
Var_saison_h_city=divide_periode_day_climate('season',np.mean(np.mean(Var_CITY,axis=1),axis=1),Time_CLIM,which_day=1)
Var_saison_h_north=divide_periode_day_climate('season',np.mean(np.mean(Var_NORTH,axis=1),axis=1),Time_CLIM,which_day=1)
Var_saison_h_west=divide_periode_day_climate('season',np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),Time_CLIM,which_day=1)

min_Var=min([Var_CITY.min(),Var_NORTH.min(),Var_RURALWEST.min()])
max_Var=max([Var_CITY.max(),Var_NORTH.max(),Var_RURALWEST.max()])



#############################################################
########################################### OBS
if(with_obs=='yes'):
	if(name_var_clim=='UM_m01s05i216_vn1006'):name_file_obs='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/Hearthrow_2007_2010_Precip.txt'
	#elif(name_var_clim=='UM_m01s08i208_vn1006'):
	#elif(name_var_clim=='UM_m01s05i205_vn1006'):
	#elif(name_var_clim=='UM_m01s04i203_vn1006'):
	#elif(name_var_clim=='UM_m01s00i024_vn1006'):
	dataframe_obs=pd.read_table(name_file_obs, sep = ',', header=0)
	Var_obs=np.array(dataframe_obs[u' Amt'].tolist())
	for i in range (0,len(Var_obs)) : 
		if (Var_obs[i]==999.9) : Var_obs[i]=float('nan')
	Var_obs=Var_obs/3600/6
	Time_obs=convert_time_obs_datetime(dataframe_obs[ u'  Date'].tolist(),heure=dataframe_obs[u'     HrMn'].tolist())

#name_file_obs='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/City_2007.txt'
#name_file_obs='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/Hearthrow_2007_Tair.txt'
#name_file_obs='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/Hearthrow_2007_P.txt'
#name_file_obs='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/STJAMESPARK_2010_Tair.txt'
#dataframe_obs=pandas.read_table(name_file_obs, sep = ',', header=0)
#Var_obs=dataframe_obs[u'  Temp'].tolist()
#Var_obs=np.array(dataframe_obs[u' Amt'].tolist())*100
#Time_obs=convert_time_obs_datetime(dataframe_obs[ u'  Date'].tolist(),heure=dataframe_obs[u'     HrMn'].tolist())

#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################


###################################################################################
######################################## Plot evolution
plt.figure(figsize=(18, 5))
plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)

#plt.figure()
#plt.show()
#vect_day=['01-01']+['']*29+['01-02']+['']*29+['01-03']+['']*29+['01-04']+['']*29+['01-05']+['']*29+['01-06']+['']*29+['01-07']+['']*29+['01-08']+['']*29+['01-09']+['']*29+['01-10']+['']*29+['01-11']+['']*29+['01-12']+['']*29

plt.plot(Time_CLIM,Var_NORTH[:,1,1],'blue',label='Rural North')
plt.fill_between(Time_CLIM.tolist(), np.min(np.min(Var_NORTH,axis=1),axis=1).tolist(), np.max(np.max(Var_NORTH,axis=1),axis=1).tolist(),color='blue',alpha=0.3)

plt.plot(Time_CLIM,Var_RURALWEST[:,1,1],'green',label='Rural West')
plt.fill_between(Time_CLIM.tolist(), np.min(np.min(Var_RURALWEST,axis=1),axis=1).tolist(), np.max(np.max(Var_RURALWEST,axis=1),axis=1).tolist(),color='green',alpha=0.3)

plt.plot(Time_CLIM,Var_CITY[:,1,1],'red',label='London')
plt.fill_between(Time_CLIM.tolist(), np.min(np.min(Var_CITY,axis=1),axis=1).tolist(), np.max(np.max(Var_CITY,axis=1),axis=1).tolist(),color='red',alpha=0.3)

plt.ylabel(legend_axes_var,fontsize=15)
plt.xlabel('Time (day - year)',fontsize=15)
plt.xlim(min(Time_CLIM), max(Time_CLIM))
#plt.xticks(Time_CLIM,vect_day,rotation='vertical')
plt.legend(fontsize=12)
if (save_plot=='yes') :plt.savefig(save_directory+name_file+'_evolution.png',dpi=300)



#plt.figure(figsize=(14, 6))
#plt.plot(Time_CLIM,np.mean(np.mean(Var_NORTH,axis=1),axis=1),'blue',label='Rural North')
#plt.plot(Time_CLIM,np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),'green',label='Rural West')
#plt.plot(Time_CLIM,np.mean(np.mean(Var_CITY,axis=1),axis=1),'red',label='London, mean over 9 gridboxs')
#plt.plot(Time_CLIM,Var_CITY[:,1,1],'red', linestyle='--',label='London, central gridbox')
#plt.ylabel(legend_axes_var,fontsize=15)
#plt.xlabel('Time (num. day)',fontsize=15)
#plt.xlim(min(Time_CLIM), max(Time_CLIM))
#plt.legend(fontsize=15)





print Monthly_mean_NORTH[:,1,1].shape[0]
print len(range(0,Monthly_mean_NORTH[:,1,1].shape[0]))


###################################################################################
######################################## Plot evolution - Monthly mean

plt.figure(figsize=(18, 5))
plt.plot(range(0,Monthly_mean_NORTH[:,1,1].shape[0]),Monthly_mean_NORTH[:,1,1],'blue',label='Rural North')
plt.fill_between(range(0,Monthly_mean_NORTH[:,1,1].shape[0]), np.min(np.min(Monthly_mean_NORTH,axis=1),axis=1).tolist(), np.max(np.max(Monthly_mean_NORTH,axis=1),axis=1).tolist(),color='blue',alpha=0.3)
print np.min(np.min(Monthly_mean_NORTH,axis=1),axis=1)
print np.max(np.max(Monthly_mean_NORTH,axis=1),axis=1)
print min(np.min(np.min(Monthly_mean_NORTH,axis=1),axis=1).tolist())
print max(np.min(np.min(Monthly_mean_NORTH,axis=1),axis=1).tolist())
print min(np.max(np.max(Monthly_mean_NORTH,axis=1),axis=1).tolist())
print max(np.max(np.max(Monthly_mean_NORTH,axis=1),axis=1).tolist())


plt.plot(range(0,Monthly_mean_NORTH[:,1,1].shape[0]),Monthly_mean_RURALWEST[:,1,1],'green',label='Rural West')
plt.fill_between(range(0,Monthly_mean_NORTH[:,1,1].shape[0]), np.min(np.min(Monthly_mean_RURALWEST,axis=1),axis=1).tolist(), np.max(np.max(Monthly_mean_RURALWEST,axis=1),axis=1).tolist(),color='green',alpha=0.3)

plt.plot(range(0,Monthly_mean_NORTH[:,1,1].shape[0]),Monthly_mean_CITY[:,1,1],'red',label='London')
plt.fill_between(range(0,Monthly_mean_NORTH[:,1,1].shape[0]), np.min(np.min(Monthly_mean_CITY,axis=1),axis=1).tolist(), np.max(np.max(Monthly_mean_CITY,axis=1),axis=1).tolist(),color='red',alpha=0.3)

plt.ylabel(legend_axes_var,fontsize=15)
plt.xlabel('Time (num. month)',fontsize=15)
plt.legend(fontsize=15)

#plt.show()

##############################################################
############################################ OBS
#print month_mean(Var_obs,Time_obs,val_min=23,missing=-9999.9)[1]
if(with_obs=='yes'):plt.plot(range(0,Monthly_mean_NORTH[:,1,1].shape[0]),month_mean(Var_obs,Time_obs,val_min=23,missing=-9999.9)[0],'k',label='London')

if (save_plot=='yes') :plt.savefig(save_directory+name_file+'_evolution_monthly_mean.png',dpi=300)

if(with_obs=='yes'):
	plt.figure(figsize=(14, 6))
	plt.plot(Time_obs,Var_obs,'k',label='London')
############################
# Scattered plot around the city center

#plt.figure()
#couleur=['red','orange','yellow','greenyellow','black','darkgreen','darkblue','cyan','magenta']
#plt.plot([np.min(Var_CITY), np.max(Var_CITY)],[np.min(Var_CITY), np.max(Var_CITY)],color='grey',alpha=1.)
#for i in range(0,9):
#	plt.scatter(Var_CITY[:,1,1], Var_CITY[:,i%3,i/3],label=str(i%3)+str(i/3),marker='+',color=couleur[i],alpha=0.7)
#plt.xlabel(legend_axes_var+' CENTER')
#plt.ylabel(legend_axes_var+' 1 gridbox')
#plt.legend()
#plt.ylim(np.min(Var_CITY), np.max(Var_CITY))
#plt.xlim(np.min(Var_CITY), np.max(Var_CITY))



#plt.show()

############################
# Scattered plot between rural and urban

#plt.figure()
#couleur=['red','orange','yellow','greenyellow','black','darkgreen','darkblue','cyan','magenta']
#plt.plot([np.min(Var_CITY), np.max(Var_CITY)],[np.min(Var_CITY), np.max(Var_CITY)],color='grey',alpha=1.)
#plt.scatter(np.mean(np.mean(Var_CITY,axis=1),axis=1), np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),label='Rural West'+' COR='+str(correlation(np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),np.mean(np.mean(Var_CITY,axis=1),axis=1))),marker='+',color='blue',alpha=0.7)
#plt.scatter(np.mean(np.mean(Var_CITY,axis=1),axis=1), np.mean(np.mean(Var_NORTH,axis=1),axis=1),label='Rural North'+' COR='+str(correlation(np.mean(np.mean(Var_NORTH,axis=1),axis=1),np.mean(np.mean(Var_CITY,axis=1),axis=1))),marker='+',color='green',alpha=0.7)
#plt.ylabel(legend_axes_var+' RURAL')
#plt.xlabel(legend_axes_var+' URBAN')
#plt.annotate('COR NORTH-CITY='+str(correlation(np.mean(np.mean(Var_NORTH,axis=1),axis=1),np.mean(np.mean(Var_CITY,axis=1),axis=1)))+'\n'+'COR WEST-CITY='+str(correlation(np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),np.mean(np.mean(Var_CITY,axis=1),axis=1))), xycoords = 'axes fraction',xy=(0.005,    0.8))
#plt.annotate('COR NORTH-CITY='+str(correlation(np.mean(np.mean(Var_NORTH,axis=1),axis=1),np.mean(np.mean(Var_CITY,axis=1),axis=1))+'\n'+'COR WEST-CITY='+str(correlation(np.mean(np.mean(Var_WEST,axis=1),axis=1),np.mean(np.mean(Var_CITY,axis=1),axis=1))), xycoords = 'axes fraction',xy=(0.005,    0.8))
#plt.legend()
#plt.ylim(np.min(Var_CITY), np.max(Var_CITY))
#plt.xlim(np.min(Var_CITY), np.max(Var_CITY))



print len(np.mean(np.mean(Var_RURALWEST,axis=1),axis=1)), len (Var_CITY[:,1,1])
print np.mean(np.mean(Var_RURALWEST,axis=1),axis=1)
print Var_CITY[:,1,1]
df=pd.DataFrame({'list1':np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),'list2':Var_CITY[:,1,1]})
#	return np.around(df.corr()['list2']['list1'],num_round)
print 'df'
print df
print 'corr'
print type(df['list1'][1])
#print df['list1']
#print df['list2']
#print df['list1'].corr(df['list2'])
#print df.corr()['list2']['list1']

print type(np.mean(np.mean(Var_RURALWEST,axis=1),axis=1)),type(np.mean(np.mean(Var_RURALWEST,axis=1),axis=1)[0]), type(Var_CITY[:,1,1]),type(Var_CITY[:,1,1][0])
print np.mean(np.mean(Var_RURALWEST,axis=1),axis=1).shape, Var_CITY[:,1,1].shape
print np.mean(np.mean(Var_RURALWEST,axis=1),axis=1)[:].shape
#print np.corrcoef(np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),np.mean(np.mean(Var_RURALWEST,axis=1),axis=1))
print np.corrcoef(Var_CITY[:,1,1].tolist(),Var_CITY[:,1,1].tolist())
print np.corrcoef(np.mean(np.mean(Var_RURALWEST,axis=1),axis=1).tolist(),Var_CITY[:,1,1].tolist())
print np.corrcoef(np.mean(np.mean(Var_RURALWEST,axis=1),axis=1).tolist(),Var_CITY[:,1,1].tolist())[1,0]
#print correlation(np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),Var_CITY[:,1,1])












###################################################################################
######################################## Scatterred plot - rural vs urban

figsize = plt.figaspect(float(2 * 1) / float(2 * 3))
fig= plt.figure(figsize=figsize)
#ax1 = fig.add_subplot(311)
plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
epaisseur_percentile=0.8
transparance=0.1

fig.add_subplot(131)
plt.plot([np.nanmin(Var_CITY), np.nanmax(Var_CITY)],[np.nanmin(Var_CITY), np.nanmax(Var_CITY)],color='k',alpha=1., linestyle = ':',label='y= x')
plt.scatter(Var_CITY[:,1,1], np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),label='Rural West'+' COR='+str(np.around(np.corrcoef(np.mean(np.mean(Var_RURALWEST,axis=1),axis=1).tolist(),Var_CITY[:,1,1].tolist())[1,0],4)),marker='+',color='green',alpha=0.5)
plt.scatter(Var_CITY[:,1,1], np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),marker='+',color='green',alpha=0.5)
idx = np.isfinite(Var_CITY[:,1,1]) & np.isfinite(np.mean(np.mean(Var_RURALWEST,axis=1),axis=1))
fit=np.polyfit(Var_CITY[idx,1,1].tolist(), np.mean(np.mean(Var_RURALWEST,axis=1),axis=1)[idx].tolist(), deg=1)
plt.plot(np.array([np.nanmin(Var_CITY),np.nanmax(Var_CITY)]), fit[0] * np.array([np.nanmin(Var_CITY),np.nanmax(Var_CITY)]) + fit[1], color='k', linestyle = 'solid',label='y= '+str(round(fit[1],3))+' + '+str(round(fit[0],3))+' x')
plt.ylabel(legend_axes_var+' RURAL')
plt.xlabel(legend_axes_var+' URBAN')
plt.legend(loc='upper left')


fig.add_subplot(132)
plt.plot([np.nanmin(Var_CITY), np.nanmax(Var_CITY)],[np.nanmin(Var_CITY), np.nanmax(Var_CITY)],color='k',alpha=1., linestyle = ':',label='y= x')
plt.scatter(Var_CITY[:,1,1], np.mean(np.mean(Var_CITY,axis=1),axis=1),label='London'+' COR='+str(np.around(np.corrcoef(np.mean(np.mean(Var_CITY,axis=1),axis=1).tolist(),Var_CITY[:,1,1].tolist())[1,0],4)),marker='+',color='red',alpha=0.5)
idx = np.isfinite(Var_CITY[:,1,1]) & np.isfinite(np.mean(np.mean(Var_CITY,axis=1),axis=1))
fit =np.polyfit(Var_CITY[idx,1,1].tolist(), np.mean(np.mean(Var_CITY,axis=1),axis=1)[idx].tolist(), deg=1)
plt.plot(np.array([np.nanmin(Var_CITY),np.nanmax(Var_CITY)]), fit[0] * np.array([np.nanmin(Var_CITY),np.nanmax(Var_CITY)]) + fit[1], color='k', linestyle = 'solid',label='y= '+str(round(fit[1],3))+' + '+str(round(fit[0],3))+' x')
plt.ylabel(legend_axes_var+' RURAL')
plt.xlabel(legend_axes_var+' URBAN')
plt.legend(loc='upper left')

fig.add_subplot(133)
plt.plot([np.nanmin(Var_CITY), np.nanmax(Var_CITY)],[np.nanmin(Var_CITY), np.nanmax(Var_CITY)],color='k',alpha=1., linestyle = ':',label='y= x')
plt.scatter(Var_CITY[:,1,1], np.mean(np.mean(Var_NORTH,axis=1),axis=1),label='Rural North'+' COR='+str(np.around(np.corrcoef(np.mean(np.mean(Var_NORTH,axis=1),axis=1).tolist(),Var_CITY[:,1,1].tolist())[1,0],4)),marker='+',color='blue',alpha=0.5)
idx = np.isfinite(Var_CITY[:,1,1]) & np.isfinite(np.mean(np.mean(Var_NORTH,axis=1),axis=1))
fit =np.polyfit(Var_CITY[idx,1,1].tolist(), np.mean(np.mean(Var_NORTH,axis=1),axis=1)[idx].tolist(), deg=1)
plt.plot(np.array([np.nanmin(Var_CITY),np.nanmax(Var_CITY)]), fit[0] * np.array([np.nanmin(Var_CITY),np.nanmax(Var_CITY)]) + fit[1], color='k', linestyle = 'solid',label='y= '+str(round(fit[1],3))+' + '+str(round(fit[0],3))+' x')
plt.ylabel(legend_axes_var+' RURAL')
plt.xlabel(legend_axes_var+' URBAN')
plt.legend(loc='upper left')

if (save_plot=='yes') :plt.savefig(save_directory+name_file+'_scattered_urban_rural.png',dpi=300)










###################################################################################
######################################## Scatterred plot - rural vs urban and rural vs rural

#fig=plt.figure(figsize=(17,11)) #We now want to plot
figsize = plt.figaspect(float(2 * 1) / float(2 * 3))
fig= plt.figure(figsize=figsize)
#ax1 = fig.add_subplot(311)
plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
epaisseur_percentile=0.8
transparance=0.1

ax=fig.add_subplot(131)
plt.plot([np.nanmin(Var_CITY), np.nanmax(Var_CITY)],[np.nanmin(Var_CITY), np.nanmax(Var_CITY)],color='k',alpha=1., linestyle = ':',label='y= x')
plt.scatter(Var_CITY[:,1,1], np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),label='WEST/LONDON'+' COR='+str(np.around(np.corrcoef(np.mean(np.mean(Var_RURALWEST,axis=1),axis=1).tolist(),Var_CITY[:,1,1].tolist())[1,0],4)),marker='+',color='green',alpha=0.5)
plt.scatter(Var_CITY[:,1,1], np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),marker='+',color='green',alpha=0.5)
idx = np.isfinite(Var_CITY[:,1,1]) & np.isfinite(np.mean(np.mean(Var_RURALWEST,axis=1),axis=1))
fit=np.polyfit(Var_CITY[idx,1,1].tolist(), np.mean(np.mean(Var_RURALWEST,axis=1),axis=1)[idx].tolist(), deg=1)
plt.plot(np.array([np.nanmin(Var_CITY),np.nanmax(Var_CITY)]), fit[0] * np.array([np.nanmin(Var_CITY),np.nanmax(Var_CITY)]) + fit[1], color='k', linestyle = 'solid',label='y= '+str(round(fit[1],3))+' + '+str(round(fit[0],3))+' x')
plt.ylabel(legend_axes_var+' RURAL',fontsize=14)
plt.xlabel(legend_axes_var+' URBAN',fontsize=14)
plt.annotate('Pvalue', xycoords = 'axes fraction',xy=(0.75,    0.21))
plt.ylim(min([np.nanmin(Var_CITY),np.nanmin(Var_RURALWEST),np.nanmin(Var_NORTH)]), max([np.nanmax(Var_CITY),np.nanmax(Var_RURALWEST),np.nanmax(Var_NORTH)]))
#plt.xlim(min([np.nanmin(Var_CITY),np.nanmin(Var_RURALWEST),np.nanmin(Var_NORTH)]), max([np.nanmax(Var_CITY),np.nanmax(Var_RURALWEST),np.nanmax(Var_NORTH)]))
plt.legend(loc='upper left', fontsize=11)
pvalue_gridbox=[]
for j in range(0,20):
	pvalue_gridbox.append(stat.ttest_ind(random.sample(Var_CITY[:,1,1], 30),random.sample(Var_RURALWEST[:,1,1], 30))[1])
#ax2 = case[2-i%3,i/3].add_axes([0.8, 0., 0.2, 0.2])
inset_ax = inset_axes(ax, height="30%",width="30%",loc=4)
inset_ax.bar(range(0,20), pvalue_gridbox,align='center',color='k')
inset_ax.plot(range(0,20), [0.05]*20,color='red',linewidth=0.7,linestyle='--')
inset_ax.set_ylim([0, 1.])
inset_ax.set_xticks([])
#inset_ax.set_yticks([])


ax=fig.add_subplot(132)
plt.plot([np.nanmin(Var_CITY), np.nanmax(Var_CITY)],[np.nanmin(Var_CITY), np.nanmax(Var_CITY)],color='k',alpha=1., linestyle = ':',label='y= x')
plt.scatter(Var_CITY[:,1,1], np.mean(np.mean(Var_NORTH,axis=1),axis=1),label='NORTH/LONDON'+' COR='+str(np.around(np.corrcoef(np.mean(np.mean(Var_NORTH,axis=1),axis=1).tolist(),Var_CITY[:,1,1].tolist())[1,0],4)),marker='+',color='blue',alpha=0.5)
idx = np.isfinite(Var_CITY[:,1,1]) & np.isfinite(np.mean(np.mean(Var_NORTH,axis=1),axis=1))
fit =np.polyfit(Var_CITY[idx,1,1].tolist(), np.mean(np.mean(Var_NORTH,axis=1),axis=1)[idx].tolist(), deg=1)
plt.plot(np.array([np.nanmin(Var_CITY),np.nanmax(Var_CITY)]), fit[0] * np.array([np.nanmin(Var_CITY),np.nanmax(Var_CITY)]) + fit[1], color='k', linestyle = 'solid',label='y= '+str(round(fit[1],3))+' + '+str(round(fit[0],3))+' x')
#plt.ylabel(legend_axes_var+' RURAL')
plt.xlabel(legend_axes_var+' URBAN',fontsize=14)
plt.yticks([])
plt.legend(loc='upper left',fontsize=11)
plt.ylim(min([np.nanmin(Var_CITY),np.nanmin(Var_RURALWEST),np.nanmin(Var_NORTH)]), max([np.nanmax(Var_CITY),np.nanmax(Var_RURALWEST),np.nanmax(Var_NORTH)]))
plt.xlim(min([np.nanmin(Var_CITY),np.nanmin(Var_RURALWEST),np.nanmin(Var_NORTH)]), max([np.nanmax(Var_CITY),np.nanmax(Var_RURALWEST),np.nanmax(Var_NORTH)]))
plt.annotate('Pvalue', xycoords = 'axes fraction',xy=(0.75,    0.21))
pvalue_gridbox=[]
for j in range(0,20):
	pvalue_gridbox.append(stat.ttest_ind(random.sample(Var_CITY[:,1,1], 30),random.sample(Var_NORTH[:,1,1], 30))[1])
#ax2 = case[2-i%3,i/3].add_axes([0.8, 0., 0.2, 0.2])
inset_ax = inset_axes(ax, height="30%",width="30%",loc=4)
inset_ax.bar(range(0,20), pvalue_gridbox,align='center',color='k')
inset_ax.plot(range(0,20), [0.05]*20,color='red',linewidth=0.7,linestyle='--')
inset_ax.set_ylim([0, 1.])
inset_ax.set_xticks([])


ax=fig.add_subplot(133)
plt.plot([np.nanmin(Var_CITY), np.nanmax(Var_CITY)],[np.nanmin(Var_CITY), np.nanmax(Var_CITY)],color='k',alpha=1., linestyle = ':',label='y= x')
plt.scatter(Var_RURALWEST[:,1,1], np.mean(np.mean(Var_NORTH,axis=1),axis=1),label='NORTH/WEST'+' COR='+str(np.around(np.corrcoef(np.mean(np.mean(Var_NORTH,axis=1),axis=1).tolist(),Var_RURALWEST[:,1,1].tolist())[1,0],4)),marker='+',color='grey',alpha=0.5)
idx = np.isfinite(Var_RURALWEST[:,1,1]) & np.isfinite(np.mean(np.mean(Var_NORTH,axis=1),axis=1))
fit =np.polyfit(Var_RURALWEST[idx,1,1].tolist(), np.mean(np.mean(Var_NORTH,axis=1),axis=1)[idx].tolist(), deg=1)
plt.plot(np.array([np.nanmin(Var_CITY),np.nanmax(Var_CITY)]), fit[0] * np.array([np.nanmin(Var_CITY),np.nanmax(Var_CITY)]) + fit[1], color='k', linestyle = 'solid',label='y= '+str(round(fit[1],3))+' + '+str(round(fit[0],3))+' x')
#plt.ylabel(legend_axes_var+' RURAL',fontsize=15)
plt.xlabel(legend_axes_var+' WEST',fontsize=14)
plt.yticks([])
plt.legend(loc='upper left',fontsize=11)
plt.ylim(min([np.nanmin(Var_CITY),np.nanmin(Var_RURALWEST),np.nanmin(Var_NORTH)]), max([np.nanmax(Var_CITY),np.nanmax(Var_RURALWEST),np.nanmax(Var_NORTH)]))
plt.xlim(min([np.nanmin(Var_CITY),np.nanmin(Var_RURALWEST),np.nanmin(Var_NORTH)]), max([np.nanmax(Var_CITY),np.nanmax(Var_RURALWEST),np.nanmax(Var_NORTH)]))
plt.annotate('Pvalue', xycoords = 'axes fraction',xy=(0.75,    0.21))
pvalue_gridbox=[]
for j in range(0,20):
	pvalue_gridbox.append(stat.ttest_ind(random.sample(Var_RURALWEST[:,1,1], 30),random.sample(Var_NORTH[:,1,1], 30))[1])
#ax2 = case[2-i%3,i/3].add_axes([0.8, 0., 0.2, 0.2])
inset_ax = inset_axes(ax, height="30%",width="30%",loc=4)
inset_ax.bar(range(0,20), pvalue_gridbox,align='center',color='k')
inset_ax.plot(range(0,20), [0.05]*20,color='red',linewidth=0.7,linestyle='--')
inset_ax.set_ylim([0, 1.])
inset_ax.set_xticks([])


if (save_plot=='yes') :plt.savefig(save_directory+name_file+'_scattered_rural.png', bbox_inches='tight',dpi=300)












#plt.show()



###################################################################################
######################################## Scatterred plot - central gridbox vs local gridbox


figsize = plt.figaspect(float(2 * 3) / float(2 * 3))
f, case = plt.subplots(3,3,sharex='col', sharey='row',figsize=figsize)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
couleur=['red','orange','yellow','greenyellow','black','darkgreen','darkblue','cyan','magenta']
for i in range(0,9):
	idx = np.isfinite(Var_CITY[:,1,1]) & np.isfinite(Var_CITY[:,i%3,i/3])
	case[2-i%3,i/3].plot([np.nanmin(Var_CITY[idx,:,:]), np.nanmax(Var_CITY[idx,:,:])],[np.nanmin(Var_CITY[idx,:,:]), np.nanmax(Var_CITY[idx,:,:])],color='grey',alpha=0.7, linestyle = ':')
	case[2-i%3,i/3].scatter(Var_CITY[:,1,1], Var_CITY[:,i%3,i/3],label=' COR='+str(np.around(np.corrcoef(Var_CITY[idx,1,1].tolist(),Var_CITY[idx,i%3,i/3].tolist())[1,0],4)),marker='+',color='red')
	case[2-i%3,i/3].set_ylim(np.nanmin(Var_CITY), np.nanmax(Var_CITY))
	case[2-i%3,i/3].set_xlim(np.nanmin(Var_CITY), np.nanmax(Var_CITY))
	#case[2-i%3,i/3].legend(loc='upper left')
	#case[2-i%3,i/3].get_xticklabels().set_rotation(90)
	#case[2-i%3,i/3].set_xticks(rotation='vertical')
	fit =np.polyfit(Var_CITY[idx,1,1],  Var_CITY[idx,i%3,i/3], deg=1)
	case[2-i%3,i/3].plot(np.array([np.nanmin(Var_CITY[idx,1,1]),np.nanmax(Var_CITY[idx,1,1])]), fit[0] * np.array([np.nanmin(Var_CITY[idx,1,1]),np.nanmax(Var_CITY[idx,1,1])]) + fit[1], color='k', linestyle = 'solid',label='y= '+str(round(fit[1],3))+' + '+str(round(fit[0],3))+' x')
	#case[2-i%3,i/3].annotate(' COR='+str(np.around(np.corrcoef(Var_CITY[idx,1,1].tolist(),Var_CITY[idx,i%3,i/3].tolist())[1,0],4))+'\n Pvalue='+str(round(stat.ttest_ind(random.sample(Var_CITY[idx,i%3,i/3], 30),random.sample(Var_CITY[idx,1,1], 30))[1],4)), xycoords = 'axes fraction',xy=(0.005,    0.7))
	case[2,1].set_xlabel(legend_axes_var+' CENTER')
	case[2-i%3,i/3].annotate(' COR='+str(np.around(np.corrcoef(Var_RURALWEST[idx,1,1].tolist(),Var_RURALWEST[idx,i%3,i/3].tolist())[1,0],4)), xycoords = 'axes fraction',xy=(0.005,    0.9))
	case[2-i%3,i/3].annotate('Pvalue', xycoords = 'axes fraction',xy=(0.63,    0.35))
	case[1,0].set_ylabel(legend_axes_var+' 1 gridbox')
	case[2-i%3,0].yaxis.set_tick_params(labelsize=9)
	case[2,i/3].xaxis.set_tick_params(labelsize=9)
	pvalue_gridbox=[]
	for j in range(0,20):
		pvalue_gridbox.append(stat.ttest_ind(random.sample(Var_CITY[idx,i%3,i/3], 30),random.sample(Var_CITY[idx,1,1], 30))[1])
	#ax2 = case[2-i%3,i/3].add_axes([0.8, 0., 0.2, 0.2])
	inset_ax = inset_axes(case[2-i%3,i/3], height="30%",width="30%",loc=4)
	inset_ax.bar(range(0,20), pvalue_gridbox,align='center',color='k')
	inset_ax.plot(range(0,20), [0.05]*20,color='red',linewidth=0.7,linestyle='--')
	inset_ax.set_ylim([0, 1.])
	inset_ax.set_xticks([])
	#inset_ax.set_yticks([])

#f.suptitle('LONDON')

if (save_plot=='yes') :plt.savefig(save_directory+name_file+'_scattered_LONDON.png',dpi=300)
print np.min(Var_CITY), np.max(Var_CITY)
print np.min(Var_CITY[:,:,:]), np.max(Var_CITY[:,:,:])
print np.min(Var_CITY[idx,:,:]), np.max(Var_CITY[idx,:,:])



#plt.show()


#plt.figure()
figsize = plt.figaspect(float(2 * 3) / float(2 * 3))
f, case = plt.subplots(3,3,sharex='col', sharey='row',figsize=figsize)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
couleur=['red','orange','yellow','greenyellow','black','darkgreen','darkblue','cyan','magenta']
for i in range(0,9):
	case[2-i%3,i/3].plot([np.min(Var_RURALWEST), np.max(Var_RURALWEST)],[np.min(Var_RURALWEST), np.max(Var_RURALWEST)],color='grey',alpha=0.7, linestyle = ':')
	case[2-i%3,i/3].scatter(Var_RURALWEST[:,1,1], Var_RURALWEST[:,i%3,i/3],label=' COR='+str(np.around(np.corrcoef(Var_CITY[idx,1,1].tolist(),Var_CITY[idx,i%3,i/3].tolist())[1,0],4)),marker='+',color='green')
	case[2-i%3,i/3].set_ylim(np.nanmin(Var_RURALWEST), np.nanmax(Var_RURALWEST))
	case[2-i%3,i/3].set_xlim(np.nanmin(Var_RURALWEST), np.nanmax(Var_RURALWEST))
	#case[2-i%3,i/3].legend(loc='upper left')
	#case[2-i%3,i/3].get_xticklabels().set_rotation(90)
	#case[2-i%3,i/3].set_xticks(rotation='vertical')#
	idx = np.isfinite(Var_RURALWEST[:,1,1]) & np.isfinite(Var_RURALWEST[:,i%3,i/3])

	fit =np.polyfit(Var_RURALWEST[idx,1,1],  Var_RURALWEST[idx,i%3,i/3], deg=1)
	case[2-i%3,i/3].plot(np.array([np.nanmin(Var_RURALWEST[idx,:,:]),np.nanmax(Var_RURALWEST[idx,:,:])]), fit[0] * np.array([np.nanmin(Var_RURALWEST[idx,:,:]),np.nanmax(Var_RURALWEST[idx,:,:])]) + fit[1], color='k', linestyle = 'solid')#,label='y= '+str(round(fit[1],3))+' + '+str(round(fit[0],3))+' x')

	case[2-i%3,i/3].annotate(' COR='+str(np.around(np.corrcoef(Var_RURALWEST[idx,1,1].tolist(),Var_RURALWEST[idx,i%3,i/3].tolist())[1,0],4)), xycoords = 'axes fraction',xy=(0.005,    0.9))
	case[2,1].set_xlabel(legend_axes_var+' CENTER')
	#case[2-i%3,i/3].annotate(' COR='+str(np.around(np.corrcoef(Var_RURALWEST[idx,1,1].tolist(),Var_RURALWEST[idx,i%3,i/3].tolist())[1,0],4)), xycoords = 'axes fraction',xy=(0.005,    0.7))
	case[2-i%3,i/3].annotate('Pvalue', xycoords = 'axes fraction',xy=(0.63,    0.35))

	case[1,0].set_ylabel(legend_axes_var+' 1 gridbox')
	case[2-i%3,0].yaxis.set_tick_params(labelsize=9)
	case[2,i/3].xaxis.set_tick_params(labelsize=9)
	pvalue_gridbox=[]
	for j in range(0,20):
		pvalue_gridbox.append(stat.ttest_ind(random.sample(Var_RURALWEST[idx,i%3,i/3], 30),random.sample(Var_RURALWEST[idx,1,1], 30))[1])
	#ax2 = case[2-i%3,i/3].add_axes([0.8, 0., 0.2, 0.2])
	inset_ax = inset_axes(case[2-i%3,i/3], height="30%",width="30%",loc=4)
	inset_ax.bar(range(0,20), pvalue_gridbox,align='center',color='k')
	inset_ax.plot(range(0,20), [0.05]*20,color='red',linewidth=0.7,linestyle='--')
	inset_ax.set_ylim([0, 1.])
	inset_ax.set_xticks([])
	inset_ax.set_yticks([])
#f.suptitle('WEST')

if (save_plot=='yes') :plt.savefig(save_directory+name_file+'_scattered_WEST.png',dpi=300)

#plt.figure()
figsize = plt.figaspect(float(2 * 3) / float(2 * 3))
f, case = plt.subplots(3,3,sharex='col', sharey='row',figsize=figsize)
#case.set_aspect(aspect='equal')
print type(case)
print type(case[0,0])
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
couleur=['red','orange','yellow','greenyellow','black','darkgreen','darkblue','cyan','magenta']
for i in range(0,9):
	case[2-i%3,i/3].plot([np.min(Var_NORTH), np.max(Var_NORTH)],[np.min(Var_NORTH), np.max(Var_NORTH)],color='grey',alpha=0.7, linestyle = ':')
	case[2-i%3,i/3].scatter(Var_NORTH[:,1,1], Var_NORTH[:,i%3,i/3],label=' COR='+str(np.around(np.corrcoef(Var_CITY[idx,1,1].tolist(),Var_CITY[idx,i%3,i/3].tolist())[1,0],4)),marker='+',color='blue')
	case[2-i%3,i/3].set_ylim(np.nanmin(Var_NORTH), np.nanmax(Var_NORTH))
	case[2-i%3,i/3].set_xlim(np.nanmin(Var_NORTH), np.nanmax(Var_NORTH))
	#case[2-i%3,i/3].legend(loc='upper left')
	#case[2-i%3,i/3].set_aspect(aspect='equal')
	#case[2-i%3,i/3].imshow(aspect='equal')
	#case[2-i%3,i/3].get_xticklabels().set_rotation(90)
	#case[2-i%3,i/3].set_xticks(rotation='vertical')
	idx = np.isfinite(Var_NORTH[:,1,1]) & np.isfinite(Var_NORTH[:,i%3,i/3])

	fit =np.polyfit(Var_NORTH[idx,1,1],  Var_NORTH[idx,i%3,i/3], deg=1)
	case[2-i%3,i/3].plot(np.array([np.nanmin(Var_NORTH[idx,:,:]),np.nanmax(Var_NORTH[idx,:,:])]), fit[0] * np.array([np.nanmin(Var_NORTH[idx,:,:]),np.nanmax(Var_NORTH[idx,:,:])]) + fit[1], color='k', linestyle = 'solid')#,label='y= '+str(round(fit[1],3))+' + '+str(round(fit[0],3))+' x')

	case[2-i%3,i/3].annotate(' COR='+str(np.around(np.corrcoef(Var_NORTH[idx,1,1].tolist(),Var_NORTH[idx,i%3,i/3].tolist())[1,0],4)), xycoords = 'axes fraction',xy=(0.005,    0.9))
	#case[2-i%3,i/3].annotate(' COR='+str(np.around(np.corrcoef(Var_NORTH[idx,1,1].tolist(),Var_NORTH[idx,i%3,i/3].tolist())[1,0],4)), xycoords = 'axes fraction',xy=(0.005,    0.7))
	case[2-i%3,i/3].annotate('Pvalue', xycoords = 'axes fraction',xy=(0.63,    0.35))
	case[2,1].set_xlabel(legend_axes_var+' CENTER')
	case[1,0].set_ylabel(legend_axes_var+' 1 gridbox')
	case[2-i%3,0].yaxis.set_tick_params(labelsize=9)
	case[2,i/3].xaxis.set_tick_params(labelsize=9)
	pvalue_gridbox=[]
	for j in range(0,20):
		pvalue_gridbox.append(stat.ttest_ind(random.sample(Var_NORTH[idx,i%3,i/3], 30),random.sample(Var_NORTH[idx,1,1], 30))[1])
	#ax2 = case[2-i%3,i/3].add_axes([0.8, 0., 0.2, 0.2])
	inset_ax = inset_axes(case[2-i%3,i/3], height="30%",width="30%",loc=4)
	inset_ax.bar(range(0,20), pvalue_gridbox,align='center',color='k')
	inset_ax.plot(range(0,20), [0.05]*20,color='red',linewidth=0.7,linestyle='--')
	inset_ax.set_ylim([0, 1.])
	inset_ax.set_xticks([])
	#inset_ax.set_yticks([])
#f.suptitle('NORTH')

if (save_plot=='yes') :plt.savefig(save_directory+name_file+'_scattered_NORTH.png',dpi=300)
































###################################################################################
######################################## Scatterred plot - central gridbox vs local gridbox

figsize = plt.figaspect(float(2 * 3) / float(2 * 3))
f, case = plt.subplots(3,3,sharex='col', sharey='row',figsize=figsize)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
couleur=['red','orange','yellow','greenyellow','black','darkgreen','darkblue','cyan','magenta']
for i in range(0,9):
	idx = np.isfinite(Var_CITY[:,1,1]) & np.isfinite(Var_CITY[:,i%3,i/3])
	case[2-i%3,i/3].plot([np.nanmin(Var_CITY[idx,:,:]), np.nanmax(Var_CITY[idx,:,:])],[np.nanmin(Var_CITY[idx,:,:]), np.nanmax(Var_CITY[idx,:,:])],color='grey',alpha=0.7, linestyle = ':')
	case[2-i%3,i/3].scatter(Var_CITY[:,1,1], Var_CITY[:,i%3,i/3],label=' COR='+str(np.around(np.corrcoef(Var_CITY[idx,1,1].tolist(),Var_CITY[idx,i%3,i/3].tolist())[1,0],4)),marker='+',color='red')
	case[2-i%3,i/3].set_ylim(np.nanmin(Var_CITY), np.nanmax(Var_CITY))
	case[2-i%3,i/3].set_xlim(np.nanmin(Var_CITY), np.nanmax(Var_CITY))
	#case[2-i%3,i/3].legend(loc='upper left',fontsize=8)
	#case[2-i%3,i/3].get_xticklabels().set_rotation(90)
	#case[2-i%3,i/3].set_xticks(rotation='vertical')
	fit =np.polyfit(Var_CITY[idx,1,1],  Var_CITY[idx,i%3,i/3], deg=1)
	case[2-i%3,i/3].plot(np.array([np.nanmin(Var_CITY[idx,1,1]),np.nanmax(Var_CITY[idx,1,1])]), fit[0] * np.array([np.nanmin(Var_CITY[idx,1,1]),np.nanmax(Var_CITY[idx,1,1])]) + fit[1], color='k', linestyle = 'solid',label='y= '+str(round(fit[1],3))+' + '+str(round(fit[0],3))+' x')
	case[2-i%3,i/3].annotate(' COR='+str(np.around(np.corrcoef(Var_CITY[idx,1,1].tolist(),Var_CITY[idx,i%3,i/3].tolist())[1,0],4)), xycoords = 'axes fraction',xy=(0.005,    0.9))
	case[2,1].set_xlabel(legend_axes_var+' CENTER')
	#case[2-i%3,i/3].annotate(' COR='+str(np.around(np.corrcoef(Var_CITY[idx,1,1].tolist(),Var_CITY[idx,i%3,i/3].tolist())[1,0],4)), xycoords = 'axes fraction',xy=(0.005,    0.7))
	#case[2-i%3,i/3].annotate('Pvalue', xycoords = 'axes fraction',xy=(0.75,    0.35))
	case[1,0].set_ylabel(legend_axes_var+' 1 gridbox')
	case[2-i%3,0].yaxis.set_tick_params(labelsize=9)
	case[2,i/3].xaxis.set_tick_params(labelsize=9)

#f.suptitle('LONDON')

if (save_plot=='yes') :plt.savefig(save_directory+name_file+'_scattered_LONDON_withoutpvalue.png',dpi=300)
print np.min(Var_CITY), np.max(Var_CITY)
print np.min(Var_CITY[:,:,:]), np.max(Var_CITY[:,:,:])
print np.min(Var_CITY[idx,:,:]), np.max(Var_CITY[idx,:,:])



#plt.show()


#plt.figure()
figsize = plt.figaspect(float(2 * 3) / float(2 * 3))
f, case = plt.subplots(3,3,sharex='col', sharey='row',figsize=figsize)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
couleur=['red','orange','yellow','greenyellow','black','darkgreen','darkblue','cyan','magenta']
for i in range(0,9):
	case[2-i%3,i/3].plot([np.min(Var_RURALWEST), np.max(Var_RURALWEST)],[np.min(Var_RURALWEST), np.max(Var_RURALWEST)],color='grey',alpha=0.7, linestyle = ':')
	case[2-i%3,i/3].scatter(Var_RURALWEST[:,1,1], Var_RURALWEST[:,i%3,i/3],label=' COR='+str(np.around(np.corrcoef(Var_CITY[idx,1,1].tolist(),Var_CITY[idx,i%3,i/3].tolist())[1,0],4)),marker='+',color='green')
	case[2-i%3,i/3].set_ylim(np.nanmin(Var_RURALWEST), np.nanmax(Var_RURALWEST))
	case[2-i%3,i/3].set_xlim(np.nanmin(Var_RURALWEST), np.nanmax(Var_RURALWEST))
	#case[2-i%3,i/3].legend(loc='upper left')
	#case[2-i%3,i/3].get_xticklabels().set_rotation(90)
	#case[2-i%3,i/3].set_xticks(rotation='vertical')#
	idx = np.isfinite(Var_RURALWEST[:,1,1]) & np.isfinite(Var_RURALWEST[:,i%3,i/3])

	fit =np.polyfit(Var_RURALWEST[idx,1,1],  Var_RURALWEST[idx,i%3,i/3], deg=1)
	case[2-i%3,i/3].plot(np.array([np.nanmin(Var_RURALWEST[idx,:,:]),np.nanmax(Var_RURALWEST[idx,:,:])]), fit[0] * np.array([np.nanmin(Var_RURALWEST[idx,:,:]),np.nanmax(Var_RURALWEST[idx,:,:])]) + fit[1], color='k', linestyle = 'solid')#,label='y= '+str(round(fit[1],3))+' + '+str(round(fit[0],3))+' x')

	case[2-i%3,i/3].annotate(' COR='+str(np.around(np.corrcoef(Var_RURALWEST[idx,1,1].tolist(),Var_RURALWEST[idx,i%3,i/3].tolist())[1,0],4)), xycoords = 'axes fraction',xy=(0.005,    0.9))
	case[2,1].set_xlabel(legend_axes_var+' CENTER')
	#case[2-i%3,i/3].annotate(' COR='+str(np.around(np.corrcoef(Var_RURALWEST[idx,1,1].tolist(),Var_RURALWEST[idx,i%3,i/3].tolist())[1,0],4)), xycoords = 'axes fraction',xy=(0.005,    0.7))
	#case[2-i%3,i/3].annotate('Pvalue', xycoords = 'axes fraction',xy=(0.75,    0.35))
	case[2-i%3,0].yaxis.set_tick_params(labelsize=9)
	case[2,i/3].xaxis.set_tick_params(labelsize=9)
	case[1,0].set_ylabel(legend_axes_var+' 1 gridbox')
#f.suptitle('WEST')

if (save_plot=='yes') :plt.savefig(save_directory+name_file+'_scattered_WEST_withoutpvalue.png',dpi=300)

#plt.figure()

figsize = plt.figaspect(float(2 * 3) / float(2 * 3))
f, case = plt.subplots(3,3,sharex='col', sharey='row',figsize=figsize)
#case.set_aspect(aspect='equal')
print type(case)
print type(case[0,0])
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
couleur=['red','orange','yellow','greenyellow','black','darkgreen','darkblue','cyan','magenta']
for i in range(0,9):
	case[2-i%3,i/3].plot([np.min(Var_NORTH), np.max(Var_NORTH)],[np.min(Var_NORTH), np.max(Var_NORTH)],color='grey',alpha=0.7, linestyle = ':')
	case[2-i%3,i/3].scatter(Var_NORTH[:,1,1], Var_NORTH[:,i%3,i/3],label=' COR='+str(np.around(np.corrcoef(Var_CITY[idx,1,1].tolist(),Var_CITY[idx,i%3,i/3].tolist())[1,0],4)),marker='+',color='blue')
	case[2-i%3,i/3].set_ylim(np.nanmin(Var_NORTH), np.nanmax(Var_NORTH))
	case[2-i%3,i/3].set_xlim(np.nanmin(Var_NORTH), np.nanmax(Var_NORTH))
	#case[2-i%3,i/3].legend(loc='upper left')
	#case[2-i%3,i/3].set_aspect(aspect='equal')
	#case[2-i%3,i/3].imshow(aspect='equal')
	#case[2-i%3,i/3].get_xticklabels().set_rotation(90)
	#case[2-i%3,i/3].set_xticks(rotation='vertical')
	idx = np.isfinite(Var_NORTH[:,1,1]) & np.isfinite(Var_NORTH[:,i%3,i/3])

	fit =np.polyfit(Var_NORTH[idx,1,1],  Var_NORTH[idx,i%3,i/3], deg=1)
	case[2-i%3,i/3].plot(np.array([np.nanmin(Var_NORTH[idx,:,:]),np.nanmax(Var_NORTH[idx,:,:])]), fit[0] * np.array([np.nanmin(Var_NORTH[idx,:,:]),np.nanmax(Var_NORTH[idx,:,:])]) + fit[1], color='k', linestyle = 'solid')#,label='y= '+str(round(fit[1],3))+' + '+str(round(fit[0],3))+' x')

	case[2-i%3,i/3].annotate(' COR='+str(np.around(np.corrcoef(Var_NORTH[idx,1,1].tolist(),Var_NORTH[idx,i%3,i/3].tolist())[1,0],4)), xycoords = 'axes fraction',xy=(0.005,    0.9))
	#case[2-i%3,i/3].annotate(' COR='+str(np.around(np.corrcoef(Var_NORTH[idx,1,1].tolist(),Var_NORTH[idx,i%3,i/3].tolist())[1,0],4)), xycoords = 'axes fraction',xy=(0.005,    0.7))
	#case[2-i%3,i/3].annotate('Pvalue', xycoords = 'axes fraction',xy=(0.75,    0.35))
	case[2,1].set_xlabel(legend_axes_var+' CENTER')
	case[1,0].set_ylabel(legend_axes_var+' 1 gridbox')
	case[2-i%3,0].yaxis.set_tick_params(labelsize=9)
	case[2,i/3].xaxis.set_tick_params(labelsize=9)


#f.suptitle('NORTH')
#axis.set_xticklabels(labels, fontsize='small')

if (save_plot=='yes') :plt.savefig(save_directory+name_file+'_scattered_NORTH_withoutpvalue.png',dpi=300)





















###################################################################################
######################################## Statistical Test 


import scipy.stats as stat
import random

print type(Var_CITY[:,1,1])
print Var_CITY[:,1,1].shape
print Var_NORTH[:,1,1].shape
dt = np.array([24,43,58,71,43,49,61,44,67,49,53,56,59,52,62,54,57,33,46,43,57])
print type(dt)
print dt.shape
dc = np.array([42,43,55,26,62,37,33,41,19,54,20,85,46,10,17,60,53,42,37,42,55,28,48])
toto=Var_NORTH[:,1,1]
titi=Var_CITY[:,1,1]
#print stat.ttest_ind(dc,dt) # (2.3109, 0.0264)

print 'CITY vs WEST : ',stat.ttest_ind(Var_CITY[:,1,1],Var_RURALWEST[:,1,1]) # (2.3109, 0.0264)
print 'CITY vs NORTH : ',stat.ttest_ind(Var_NORTH[:,1,1],Var_CITY[:,1,1]) # (2.3109, 0.0264)
print 'NORTH vs WEST : ',stat.ttest_ind(Var_NORTH[:,1,1],Var_RURALWEST[:,1,1]) # (2.3109, 0.0264)
print '***'
print 'CITY vs WEST : ',stat.ttest_ind(Var_CITY[:,1,1],np.mean(np.mean(Var_RURALWEST,axis=1),axis=1)) # (2.3109, 0.0264)
print 'CITY vs NORTH : ',stat.ttest_ind(np.mean(np.mean(Var_NORTH,axis=1),axis=1),Var_CITY[:,1,1]) # (2.3109, 0.0264)
print 'NORTH vs WEST : ',stat.ttest_ind(np.mean(np.mean(Var_NORTH,axis=1),axis=1),np.mean(np.mean(Var_RURALWEST,axis=1),axis=1)) # (2.3109, 0.0264)
print '***'

print 'CITY vs WEST : ',stat.ttest_ind(np.mean(np.mean(Var_CITY,axis=1),axis=1),np.mean(np.mean(Var_RURALWEST,axis=1),axis=1)) # (2.3109, 0.0264)
print 'CITY vs NORTH : ',stat.ttest_ind(np.mean(np.mean(Var_NORTH,axis=1),axis=1),np.mean(np.mean(Var_CITY,axis=1),axis=1)) # (2.3109, 0.0264)
print 'NORTH vs WEST : ',stat.ttest_ind(np.mean(np.mean(Var_NORTH,axis=1),axis=1),np.mean(np.mean(Var_RURALWEST,axis=1),axis=1)) # (2.3109, 0.0264)
tir_city=random.sample(Var_CITY[:,1,1], 30)
tir_west=random.sample(Var_RURALWEST[:,1,1], 30)
tir_north=random.sample(Var_NORTH[:,1,1], 30)



for i in range(0,9):
	print i%3, i/3
	print lat_CITY[i%3], lon_CITY[i/3]

###################################################################################
######################################## Histogram

plt.figure()

idx = np.isfinite(Var_NORTH[:,1,1]) & np.isfinite(Var_CITY[:,1,1])& np.isfinite(Var_RURALWEST[:,1,1])
plt.hist(Var_NORTH[idx,1,1],color='blue',alpha=0.5,bins=20)
plt.hist(Var_RURALWEST[idx,1,1],color='green',alpha=0.5,bins=20)
plt.hist(Var_CITY[idx,1,1],color='red',alpha=0.5,bins=20)




if (name_var_clim=='UM_m01s03i236_vn1006' or name_var_clim=='wind'):

#	name_file_obs='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/Hearthrow_2009_Tair.txt'
#	dataframe_obs=pandas.read_table(name_file_obs, sep = ',', header=0)
#	Var_obs=dataframe_obs[u'  Temp'].tolist()
#	Time_obs=convert_time_obs_datetime(dataframe_obs[ u'  Date'].tolist(),heure=dataframe_obs[u'     HrMn'].tolist())

#	Var_saison_h_obs=divide_periode_day('season',Var_obs,Time_obs,which_day=1)
#	min_Var=min(Var_obs)
#	max_Var=max(Var_obs)

	
	Var_saison_h_city=divide_periode_day_climate('season',np.mean(np.mean(Var_CITY,axis=1),axis=1),Time_CLIM,which_day=1)
	Var_saison_h_north=divide_periode_day_climate('season',np.mean(np.mean(Var_NORTH,axis=1),axis=1),Time_CLIM,which_day=1)
	Var_saison_h_west=divide_periode_day_climate('season',np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),Time_CLIM,which_day=1)

	min_Var=min([Var_CITY.min(),Var_NORTH.min(),Var_RURALWEST.min()])
	max_Var=max([Var_CITY.max(),Var_NORTH.max(),Var_RURALWEST.max()])


	season=['Winter DJF','Spring MAM','Summer JJA','Autumn SON']
	heure=['']*24
	for i in range(0,len(heure)):
		if (i%3==0) : heure[i]=str(i)
		col_labels=['B-M','B-OBS','M-OBS']
	fig=plt.figure(figsize=(16,6)) #We now want to plot
	ax1 = fig.add_subplot(141)
	plt.subplots_adjust(left=0.05, bottom=0.15, right=0.95, top=None,wspace=0.05, hspace=0.05)
	epaisseur_percentile=0.8
	transparance=0.1
	toto=[0,2,4,8]
	for i in range(0,4):#For each season
		k=i
		fig.add_subplot(141+i)
		plot_line_bloxplot(Var_saison_h_city[i],heure,case_plot=plt,str_color='r',str_label='LONDON')
		plot_line_bloxplot(Var_saison_h_west[i],heure,case_plot=plt,str_color='g',str_label='WEST')
		plot_line_bloxplot(Var_saison_h_north[i],heure,case_plot=plt,str_color='b',str_label='NORTH')
		#plot_line_bloxplot(Var_saison_h_obs[i],heure,case_plot=plt,str_color='k',str_label='OBS')
		plt.xticks(range(0,len(heure)+1),heure+['Mean'],rotation='vertical')
		plt.title(season[i])
		plt.ylim(min_Var,max_Var)
		plt.xlabel('Time (h)', fontsize=15)
		if(i!=0) : plt.yticks([])
		if(i==0) : plt.ylabel(legend_axes_var, fontsize=15)
	plt.legend(loc='best', fontsize=12)
	if (save_plot=='yes') :plt.savefig(save_directory+name_file+'_diurnalcycle.png',dpi=300)


if (name_var_clim=='UM_m01s03i236_vn1006' or name_var_clim=='wind'):

	name_file_obs='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/Hearthrow_2007_Tair.txt'
	#name_file_obs='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/City_2009_2_Tair.txt'
	dataframe_obs=pandas.read_table(name_file_obs, sep = ',', header=0)
	Var_obs=dataframe_obs[u'  Temp'].tolist()
	Time_obs=convert_time_obs_datetime(dataframe_obs[ u'  Date'].tolist(),heure=dataframe_obs[u'     HrMn'].tolist())

	Var_saison_h_obs=divide_periode_day('season',Var_obs,Time_obs,which_day=1)
	min_Var=min(Var_obs)
	max_Var=max(Var_obs)

	
	Var_saison_h_city=divide_periode_day_climate('season',np.mean(np.mean(Var_CITY,axis=1),axis=1),Time_CLIM,which_day=1)
	Var_saison_h_north=divide_periode_day_climate('season',np.mean(np.mean(Var_NORTH,axis=1),axis=1),Time_CLIM,which_day=1)
	Var_saison_h_west=divide_periode_day_climate('season',np.mean(np.mean(Var_RURALWEST,axis=1),axis=1),Time_CLIM,which_day=1)

	min_Var=min([Var_CITY.min(),Var_NORTH.min(),Var_RURALWEST.min()])
	max_Var=max([Var_CITY.max(),Var_NORTH.max(),Var_RURALWEST.max()])


	season=['Winter DJF','Spring MAM','Summer JJA','Autumn SON']
	heure=['']*24
	for i in range(0,len(heure)):
		if (i%3==0) : heure[i]=str(i)
		col_labels=['B-M','B-OBS','M-OBS']
	fig=plt.figure(figsize=(16,6)) #We now want to plot
	ax1 = fig.add_subplot(141)
	plt.subplots_adjust(left=0.05, bottom=0.15, right=0.95, top=None,wspace=0.05, hspace=0.05)
	epaisseur_percentile=0.8
	transparance=0.1
	toto=[0,2,4,8]
	for i in range(0,4):#For each season
		k=i
		fig.add_subplot(141+i)
		plot_line_bloxplot(Var_saison_h_city[i],heure,case_plot=plt,str_color='r',str_label='LONDON')
		plot_line_bloxplot(Var_saison_h_west[i],heure,case_plot=plt,str_color='g',str_label='WEST')
		plot_line_bloxplot(Var_saison_h_north[i],heure,case_plot=plt,str_color='b',str_label='NORTH')
		plot_line_bloxplot(Var_saison_h_obs[i],heure,case_plot=plt,str_color='k',str_label='OBS')
		plt.xticks(range(0,len(heure)+1),heure+['Mean'],rotation='vertical')
		plt.title(season[i])
		plt.ylim(min_Var,max_Var)
		plt.xlabel('Time (h)', fontsize=15)
		if(i!=0) : plt.yticks([])
		if(i==0) : plt.ylabel(legend_axes_var, fontsize=15)
	plt.legend(loc='best', fontsize=12)
	if (save_plot=='no') :plt.savefig(save_directory+name_file+'_diurnalcycle_withobs_2007.png',dpi=300)









plt.show()
