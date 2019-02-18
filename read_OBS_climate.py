#!/usr/bin/python
# -*- coding: utf8 -*-

from fonction import *
from jules_download import *
from Split_times_Marine import *

from mpl_toolkits.basemap import Basemap
from osgeo import gdal

from rotate_landuse import *
import pandas as pd

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


#name_file='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/City_2007_daily.txt'
#name_file='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/City_2007.txt'
name_file='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/Hearthrow_2010_Tair.txt'

dataframe_obs = pd.read_table(name_file, sep = ',', header=0)

print dataframe_obs

print dataframe_obs.head()

print dataframe_obs.columns
print len(dataframe_obs.columns)

Var_obs=dataframe_obs[u'  Temp'].tolist()
print Var_obs[0:10]

H_obs=dataframe_obs[u'     HrMn'].tolist()
print H_obs[0:10]

for i in range(0,10):
	print H_obs[i], H_obs[i]/100,H_obs[i]%100


#print dataframe_obs[u'   TEMP']

#Var_obs=dataframe_obs[u'   TEMP'].tolist()
#Time_obs=dataframe_obs[ u' YEARMODA'].tolist()

#Var_obs=dataframe_obs[u'   TEMP'].tolist()





#print Time_obs[36]
#print str(Time_obs[36])[0:4]
#print Time_obs[36]/10000
#print Time_obs[36]/100%(Time_obs[36]/10000)
#print Time_obs[36]%(Time_obs[36]/100)

#print datetime.datetime(Time_obs[36]/10000, Time_obs[36]/100%(Time_obs[36]/10000), Time_obs[36]%(Time_obs[36]/100), 00, 00)




#print Time_obs[10:20]
#print '**'
#print Time_obs[10:20][1]
#datetime_return=[]
#for i in range(0,len(Time_obs[10:20])):
#			print Time_obs[10:20][i]
#			datetime_return.append(datetime.datetime(Time_obs[10:20][i]/10000, Time_obs[10:20][i]/100%(Time_obs[10:20][i]/10000),Time_obs[10:20][i]%(Time_obs[10:20][i]/100), 00, 00))


#def monthly_mean_obs(time_obs,var_obs)

def convert_time_obs_datetime(date,heure=None):
	datetime_return=[]
	if (heure==None):
		for i in range(0,len(date)):
			datetime_return.append(datetime.datetime(date[i]/10000, date[i]/100%(date[i]/10000), date[i]%(date[i]/100), 00, 00))
	else :
		for i in range(0,len(date)):
			datetime_return.append(datetime.datetime(date[i]/10000, date[i]/100%(date[i]/10000), date[i]%(date[i]/100), heure[i]/100,heure[i]%100))
		
	return (datetime_return)

#print Time_obs[10:20]
#print convert_time_obs_datetime(Time_obs[10:20],heure=None)

Time_obs=convert_time_obs_datetime(dataframe_obs[ u'  Date'].tolist(),heure=dataframe_obs[u'     HrMn'].tolist())
print len(Time_obs)
print Time_obs[0]

print Time_obs[0:20]

#plt.figure()
#plt.show()

#Start= datetime.datetime(2007, 01, 01,00,00,00)
#End= datetime.datetime(2007, 12, 31,00,00,00)
#num_day=(End-Start).days
#Time_all=[]
#for i in range(0,num_day):
#	Time_all.append(Start+datetime.timedelta(days=i))





plt.plot(Time_obs,Var_obs)





print len(month_mean(Var_obs,Time_obs,val_min=23,missing=9999.9)[0])
print month_mean(Var_obs,Time_obs,val_min=23,missing=9999.9)[1]
print month_mean(Var_obs,Time_obs,val_min=23,missing=9999.9)[0]

plt.plot(month_mean(Var_obs,Time_obs,val_min=23,missing=9999.9)[1],month_mean(Var_obs,Time_obs,val_min=23,missing=9999.9)[0])
#plt.show()



Var_saison_h_obs=divide_periode_day('season',Var_obs,Time_obs,which_day=1)
min_Var=min(Var_obs)
max_Var=max(Var_obs)



season=['Winter DJF','Spring MAM','Summer JJA','Autumn SON']
heure=['']*24
for i in range(0,len(heure)):
	if (i%3==0) : heure[i]=str(i)
	col_labels=['B-M','B-OBS','M-OBS']
fig=plt.figure(figsize=(16,6)) #We now want to plot
ax1 = fig.add_subplot(141)
plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
epaisseur_percentile=0.8
transparance=0.1
toto=[0,2,4,8]
for i in range(0,4):#For each season
	k=i
	fig.add_subplot(141+i)
	plot_line_bloxplot(Var_saison_h_obs[i],heure,case_plot=plt,str_color='r',str_label='HEATHROW')
	plt.xticks(range(0,len(heure)+1),heure+['Mean'],rotation='vertical')
	plt.title(season[i])
	plt.ylim(min_Var,max_Var)
	plt.xlabel('Time (h)')
	if(i!=0) : plt.yticks([])
plt.legend(loc='best')






name_file_obs='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/STJAMESPARK_2010_Tair.txt'
#name_file_obs='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/City_2007.txt'
dataframe_obs=pd.read_table(name_file_obs, sep = ',', header=0)
Var_obs=dataframe_obs[u'  Temp'].tolist()
Time_obs=convert_time_obs_datetime(dataframe_obs[ u'  Date'].tolist(),heure=dataframe_obs[u'     HrMn'].tolist())

#plt.plot(month_mean(Var_obs,Time_obs,val_min=23,missing=9999.9)[1],month_mean(Var_obs,Time_obs,val_min=23,missing=9999.9)[0])


Var_saison_h_obs=divide_periode_day('season',Var_obs,Time_obs,which_day=1)
min_Var=min(Var_obs)
max_Var=max(Var_obs)


season=['Winter DJF','Spring MAM','Summer JJA','Autumn SON']
heure=['']*24
for i in range(0,len(heure)):
	if (i%3==0) : heure[i]=str(i)
	col_labels=['B-M','B-OBS','M-OBS']
#fig=plt.figure(figsize=(16,6)) #We now want to plot
ax1 = fig.add_subplot(141)
plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
epaisseur_percentile=0.8
transparance=0.1
toto=[0,2,4,8]
for i in range(0,4):#For each season
	k=i
	fig.add_subplot(141+i)
	plot_line_bloxplot(Var_saison_h_obs[i],heure,case_plot=plt,str_color='k',str_label='STJAMESPARK')
	plt.xticks(range(0,len(heure)+1),heure+['Mean'],rotation='vertical')
	plt.title(season[i])
	plt.ylim(min_Var,max_Var)
	plt.xlabel('Time (h)')
	if(i!=0) : plt.yticks([])
plt.legend(loc='best')
















name_file_obs='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/City_2010_Tair.txt'
#name_file_obs='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/STJAMESPARK_2010_Tair.txt'
#name_file_obs='/storage/shared/research/met/micromet/JULES/Marine/Obs_climate/City_2007.txt'
dataframe_obs=pandas.read_table(name_file_obs, sep = ',', header=0)
Var_obs=dataframe_obs[u'  Temp'].tolist()
Time_obs=convert_time_obs_datetime(dataframe_obs[ u'  Date'].tolist(),heure=dataframe_obs[u'     HrMn'].tolist())

#plt.plot(month_mean(Var_obs,Time_obs,val_min=23,missing=9999.9)[1],month_mean(Var_obs,Time_obs,val_min=23,missing=9999.9)[0])


Var_saison_h_obs=divide_periode_day('season',Var_obs,Time_obs,which_day=1)
#min_Var=min(Var_obs)
#max_Var=max(Var_obs)


season=['Winter DJF','Spring MAM','Summer JJA','Autumn SON']
heure=['']*24
for i in range(0,len(heure)):
	if (i%3==0) : heure[i]=str(i)
	col_labels=['B-M','B-OBS','M-OBS']
#fig=plt.figure(figsize=(16,6)) #We now want to plot
ax1 = fig.add_subplot(141)
plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
epaisseur_percentile=0.8
transparance=0.1
toto=[0,2,4,8]
for i in range(0,4):#For each season
	k=i
	fig.add_subplot(141+i)
	plot_line_bloxplot(Var_saison_h_obs[i],heure,case_plot=plt,str_color='b',str_label='CITY')
	plt.xticks(range(0,len(heure)+1),heure+['Mean'],rotation='vertical')
	plt.title(season[i])
	plt.ylim(min_Var,max_Var)
	plt.xlabel('Time (h)')
	if(i!=0) : plt.yticks([])
plt.legend(loc='best')






plt.show()









plt.show()


