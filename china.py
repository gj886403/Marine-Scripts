#!/usr/bin/python
# -*- coding: utf8 -*-

from fonction import *
from jules_download import *
from Split_times_Marine import *

save_directory='C:/Users/qw919026/Desktop/Marine_scripts/plots/Shanghai'

save_plot='yes'

#legende_variable='Latent Heat  $W.m^{-2}$'
#name_variable_JULES='latent_heat'
#name_file_plot='Latent_heat_'

#legende_variable='Sensible heat  $W.m^{-2}$'
#name_variable_JULES='ftl_gb'
#name_file_plot='Sensible_heat_'

#legende_variable='net allwave  $W.m^{-2}$'
#name_variable_JULES='rad_net'
#name_file_plot='Q_star'

legende_variable='LWup  $W.m^{-2}$'
name_variable_JULES='lw_up'
name_file_plot='Outgoing_longwave_'

site='Shanghai'
#site='Beijing'


#### Here are the files that we want to study : (NetCDF files)

##########################  OBS
#Var_OBS=extract_variable(extract_txt('/glusterfs/micromet/users/micromet/JULES/SUEWSEvaluationData/Kc/Obs/'+'Kc1_Obs.csv',nomber_header=0), 'qh')
#Var_OBS=quite_modif(Var_OBS,-500,1500,value_missing=-999.)
#Time_OBS=extract_variable(extract_txt('/glusterfs/micromet/users/micromet/JULES/SUEWSEvaluationData/Kc/Obs/'+'Kc1_Obs.csv',nomber_header=0), 'DateTime',date=True)

########################## JULES




#Shanghai
save_directory='C:/Users/qw919026/Desktop/Marine_scripts/plots/Shanghai'
moruses_version=93186
best_version=93552
moruses_folder='C:/Users/qw919026/Desktop/JULES/JULES runs/MORUSES/u-bb996/'
best_folder='C:/Users/qw919026/Desktop/JULES/JULES runs/Best/u-bc091/'
local_time='Asia/Shanghai'
Start= datetime.datetime(2012, 01, 01,01,00,00)
year_study='2012-2013'
year_study_short='12-13'
site='Shanghai'


#Beijing
#save_directory='C:/Users/qw919026/Desktop/Marine_scripts/plots/Beijing'
#moruses_version=93224
#best_version=93350
#moruses_folder='C:/Users/qw919026/Desktop/JULES/JULES runs/MORUSES/u-bc002/'
#best_folder='C:/Users/qw919026/Desktop/JULES/JULES runs/Best/u-bc035/'
#local_time='Asia/Beijing'
#local_time='Asia/Shanghai'
#year_study='2014-2015'
#year_study_short='14-15'
#site='Beijing'
#Start= datetime.datetime(2014, 01, 01,01,00,00)

#print moruses_folder+str(moruses_version)+'/jules.all.nc'
#f = Dataset(moruses_folder+str(moruses_version)+'/jules.all.nc', 'r')

#for v in f.variables : print("****") ; print(v) ; print(f.variables[v])
#plt.figure()
#plt.show()



Var_moruses=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES,Start)[0]
Var_best=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[0]



Time_moruses=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES,Start)[1]
Time_moruses=convert_UTC_to_local(Time_moruses,local_time)
Time_best=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[1]
Time_best=convert_UTC_to_local(Time_best,local_time)
#print Time_moruses



lon=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc','longitude',Start)[0]
lat=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc','latitude',Start)[0]

if  (Time_moruses!=Time_best) : print 'MORUSES and Best are not the same size'
print 'lon',lon,'lat',lat

#plt.figure()
#plt.show()

#Var_missing_OBS=missing_measurement(Time_moruses,Var_OBS,Time_OBS,value_nan=-999.)[1]
#missing_OBS=missing_measurement(Time_moruses,Var_OBS,Time_OBS,value_nan=-999.)[0]


#Var_saison_OBS=divide_periode_day('season',Var_missing_OBS,Time_moruses)
Var_saison_m=divide_periode_day('season',Var_moruses,Time_moruses)
Var_saison_b=divide_periode_day('season',Var_best,Time_moruses)
Time_saison=divide_periode_day('season',Time_moruses,Time_moruses)

#Var_saison_3h_OBS=divide_periode_day('season',Var_missing_OBS,Time_moruses,which_day=3)
Var_saison_3h_b=divide_periode_day('season',Var_best,Time_moruses,which_day=3)
Var_saison_3h_m=divide_periode_day('season',Var_moruses,Time_moruses,which_day=3)
Time_saison_3h=divide_periode_day('season',Time_moruses,Time_moruses,which_day=3)

#Var_saison_h_OBS=divide_periode_day('season',Var_missing_OBS,Time_moruses,which_day=1)
Var_saison_h_b=divide_periode_day('season',Var_best,Time_moruses,which_day=1)
Var_saison_h_m=divide_periode_day('season',Var_moruses,Time_moruses,which_day=1)
#Time_saison_h=divide_periode_day('season',Time_JULES,Time_JULES,which_day=1)

#Var_h_OBS=divide_periode_day('month',Var_missing_OBS,Time_moruses,which_day=1)
Var_h_b=divide_periode_day('month',Var_best,Time_moruses,which_day=1)
Var_h_m=divide_periode_day('month',Var_moruses,Time_moruses,which_day=1)
######################Usefull information

max_T=max([Var_best.max(),Var_moruses.max()])
min_T=min([Var_best.min(),Var_moruses.min()])
#Var_99=np.nanpercentile(np.array([Var_best,Var_moruses]),99)
position_title=max_T-(max_T-min_T)*0.10

print min_T

#plt.figure()
#plt.show()

#print Var_99
#print max_T

#plt.figure()
#plt.show()

#max_T=max([max(Var_missing_OBS),Var_best.max(),Var_moruses.max()])
#min_T=min([min(Var_missing_OBS),Var_best.min(),Var_moruses.min()])
heure_3h=['0h','3h','6h','9h','12h','15h','18h','21h']
mois=['J','F','M','A','M','J','J','A','S','O','N','D']
season=['Winter DJF','Spring MAM','Summer JJA','Autumn SON']
heure=['']*24
for i in range(0,len(heure)):
	if (i%3==0) : heure[i]=str(i)
#for i in range(0,24): heure.extend([str(i)])
row_labels_MAE=['24h','T','M','A','N']
count_figure=1
######################

##########################################################
############ Evolution over the Period

#count_figure=1
#color_value=(1.,.0,.0)#red
#color_missing=(0.,0.,1.)#blue
#colors=[color_value,color_missing]
#n_bin=2
#cm = LinearSegmentedColormap.from_list('color_value_missing', colors, N=2)

#plt.figure(figsize=(14,3))
#plt.pcolor(Time_moruses,[1,2,3],np.array([missing_OBS,missing_OBS]),cmap=cm)
#plt.yticks([1,2,3], ['Kc']+['',' '])
#plt.title('Kc OBS 2011-2013')
#cbar=plt.colorbar(ticks=[0, 1])
#cbar.ax.set_yticklabels([ 'missing', 'available'])
##plt.savefig(save_directory+str(count_figure)+'.png')
#count_figure=count_figure+1

#plt.figure(figsize=(17,11))
#plt.plot(Time_moruses,Var_moruses,color='k',label='Hourly')
##case[2].plot(daily_mean(Var_best,Time_moruses,val_min=15)[1],daily_mean(Var_best,Time_moruses,val_min=15)[0],color='b',label='Daily mean')
#plt.ylabel(legende_variable)
#plt.xlabel('Time (day)')
#plt.title('moruses')
##case[2].set_xticks(range(0,len(Time_moruses)),Time_moruses)
#plt.ylim(min_T,max_T)
##plt.title('Sensible Heat 2012-2013 over'+site)
#plt.legend(loc='best')


fig=plt.figure(figsize=(17,11)) #We now want to plot
#ax1 = fig.add_subplot(311)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
epaisseur_percentile=0.8
transparance=0.1

#fig.add_subplot(311)
##plt.plot(range(0,len(Time_moruses)),Var_best,color='k',label='Hourly')
#plt.plot(Time_moruses,Var_OBS,color='k',label='Hourly',linewidth=0.5,alpha=0.7)
##plt.plot(daily_mean(Var_OBS,Time_moruses,val_min=15)[1],daily_mean(Var_OBS,Time_moruses,val_min=15)[0],color='b',label='Daily mean',marker='+',markeredgecolor='r')
#plt.scatter(daily_mean(Var_OBS,Time_moruses,val_min=15)[1],daily_mean(Var_OBS,Time_moruses,val_min=15)[0],color='r',label='Daily mean',marker='+')
#plt.text(min(Time_moruses),position_title,  'OBS '+site+' '+year_study, fontsize='smaller')
#plt.ylabel(legende_variable)
##plt.title('best')
#plt.ylim(min_T,max_T)
plt.xticks([])


fig.add_subplot(211)
#plt.plot(range(0,len(Time_moruses)),Var_best,color='k',label='Hourly')
plt.plot(Time_moruses,Var_moruses,color='k',label='Hourly',linewidth=0.5,alpha=0.7)
#plt.plot(daily_mean(Var_moruses,Time_moruses,val_min=15)[1],daily_mean(Var_moruses,Time_moruses,val_min=15)[0],color='b',label='Daily mean',marker='+',markeredgecolor='r')
plt.scatter(daily_mean(Var_moruses,Time_moruses,val_min=15)[1],daily_mean(Var_moruses,Time_moruses,val_min=15)[0],color='r',label='Daily mean',marker='+')
plt.text(min(Time_moruses),position_title,  'MORUSES '+site+' '+year_study+' v='+str(moruses_version), fontsize='smaller')
plt.ylabel(legende_variable)
#plt.title('best')
plt.ylim(min_T,max_T)
plt.xticks([])

fig.add_subplot(212)
plt.plot(Time_moruses,Var_best,color='k',label='Hourly',linewidth=0.5,alpha=0.7)
plt.scatter(daily_mean(Var_best,Time_moruses,val_min=15)[1],daily_mean(Var_best,Time_moruses,val_min=15)[0],color='r',label='Daily mean',marker='+')
plt.text(min(Time_moruses),position_title,   'Best '+site+' '+year_study+' v='+str(best_version), fontsize='smaller')
plt.ylabel(legende_variable)
plt.xlabel('Time (day)')
#plt.title('moruses')
#case[2].set_xticks(range(0,len(Time_moruses)),Time_moruses)
plt.ylim(min_T,max_T)
plt.legend(loc='best')
fig.suptitle('Outgoing longwave 2012-2013 over '+site)

if (save_plot=='yes') :plt.savefig(save_directory+name_file_plot+str(count_figure)+'.png')
count_figure=count_figure+1

plt.show()




##fig=plt.figure(figsize=(14,6))
#f, case = plt.subplots(3,1, sharex='col', sharey='row',figsize=(17,11))
#plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
##case[0].plot(Time_moruses,Var_missing_OBS,color='k',label='Hourly')
##case[0].plot(daily_mean(Var_missing_OBS,Time_moruses,val_min=12)[1],daily_mean(Var_missing_OBS,Time_moruses,val_min=12)[0],color='b',label='Daily mean')
##for i in range(0,len(flux_periode_s)) : plt.plot(list_date_s,flux_periode_s[i],label=name_sensor[6+i])
##case[0].set_ylabel(legende_variable)
##case[0].legend(loc='best')
##case[0].set_ylim(min_T,max_T)

##case[1].plot(range(0,len(Time_moruses)),Var_best,color='k',label='Hourly')
#case[1].plot(Time_moruses,Var_best,color='k',label='Hourly')
##case[1].plot(daily_mean(Var_moruses,Time_moruses,val_min=15)[1],daily_mean(Var_moruses,Time_moruses,val_min=15)[0],color='b',label='Daily mean')
#case[1].text(734500,400,  'toto', fontsize=12)
#case[1].set_ylabel(legende_variable)
#case[1].set_title('best')
#case[1].set_ylim(min_T,max_T)

#case[2].plot(Time_moruses,Var_moruses,color='k',label='Hourly')
##case[2].plot(daily_mean(Var_best,Time_moruses,val_min=15)[1],daily_mean(Var_best,Time_moruses,val_min=15)[0],color='b',label='Daily mean')
#case[2].set_ylabel(legende_variable)
#case[2].set_xlabel('Time (day)')
#case[2].set_title('moruses')
##case[2].set_xticks(range(0,len(Time_moruses)),Time_moruses)
#case[2].set_ylim(min_T,max_T)
#f.suptitle('Sensible Heat 2012-2013 over '+site)
#case[2].legend(loc='best')

#if (save_plot=='yes') :plt.savefig(save_directory+str(count_figure)+'.png')
#count_figure=count_figure+1






plt.figure(figsize=(12,6))
#plt.plot(daily_mean(Var_missing_OBS,Time_moruses,val_min=12)[1],daily_mean(Var_missing_OBS,Time_moruses,val_min=12)[0],color='b',label='OBS')
plt.scatter(daily_mean(Var_best,Time_moruses,val_min=15)[1],daily_mean(Var_best,Time_moruses,val_min=15)[0],color='k',label='best',marker='+')
plt.scatter(daily_mean(Var_moruses,Time_moruses,val_min=15)[1],daily_mean(Var_moruses,Time_moruses,val_min=15)[0],color='r',label='moruses',marker='+')
plt.title('Outgoing longwave, daily mean -2012-2013 over'+site)
plt.legend(loc='best')
plt.ylabel(legende_variable)
plt.xlabel('Time (day)')
if (save_plot=='yes') :plt.savefig(save_directory+name_file_plot+str(count_figure)+'.png')
count_figure=count_figure+1


#plt.show()

###############################################
############ Boxplot

##OBS
#f, case = plt.subplots(1,4, sharex='col', sharey='row',figsize=(18,9))
#plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
#for i in range(0,4):#for each month
#	plot_evolution_boxplot(case[i],Var_saison_h_OBS[i],heure,season[i],min_T,max_T)
#	case[i].set_xlabel('Hours')
#	if (i==0 or i==6) :case[i].set_ylabel(legende_variable)
#f.suptitle('OBS - KC - 2011-2013')
#if (save_plot=='yes') : plt.savefig(save_directory+name_file_plot+str(count_figure)+'.png')
#count_figure=count_figure+1

#best
f, case = plt.subplots(1,4, sharex='col', sharey='row',figsize=(18,9))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
for i in range(0,4):#for each month
	plot_evolution_boxplot(case[i],Var_saison_h_b[i],heure,season[i],min_T,max_T)
	case[i].set_xlabel('Time (h)')
	if (i==0 or i==6) :case[i].set_ylabel(legende_variable)
case[0].text(0,position_title,   'Best '+site+' '+year_study+' v='+str(best_version), fontsize='smaller')
#f.suptitle('Best - 2012-2013 - Shanghai' )
if (save_plot=='yes') :plt.savefig(save_directory+name_file_plot+str(count_figure)+'.png')
count_figure=count_figure+1



#moruses
f, case = plt.subplots(1,4, sharex='col', sharey='row',figsize=(18,9))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
for i in range(0,4):#for each month
	plot_evolution_boxplot(case[i],Var_saison_h_m[i],heure,season[i],min_T,max_T)
	case[i].set_xlabel('Time (h)')
	if (i==0 or i==6) :case[i].set_ylabel(legende_variable)
case[0].text(0,position_title,   'MORUSES '+site+' '+year_study+' v='+str(moruses_version), fontsize='smaller')
#f.suptitle('Moruses - 2012-2013 - Shanghai')
if (save_plot=='yes') :plt.savefig(save_directory+name_file_plot+str(count_figure)+'.png')
count_figure=count_figure+1




f, case = plt.subplots(2,6, sharex='col', sharey='row',figsize=(18,9))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
for i in range(0,12):#for each month
	plot_evolution_boxplot(case[i/6,i%6],Var_h_b[i],heure,mois[i],min_T,max_T)
	if (i>5) : case[i/6,i%6].set_xlabel('Time (h)')
	if (i==0 or i==6) :case[i/6,i%6].set_ylabel(legende_variable)
case[0,0].text(0,position_title,   'B '+site+' '+year_study+' v='+str(best_version), fontsize='smaller')
#f.suptitle('Best - Shanghai - 2011-2013')
if (save_plot=='yes') :plt.savefig(save_directory+name_file_plot+str(count_figure)+'.png')
count_figure=count_figure+1

f, case = plt.subplots(2,6, sharex='col', sharey='row',figsize=(18,9))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
for i in range(0,12):#for each month
	plot_evolution_boxplot(case[i/6,i%6],Var_h_m[i],heure,mois[i],min_T,max_T)
	if (i>5) : case[i/6,i%6].set_xlabel('Time (h)')
	if (i==0 or i==6) :case[i/6,i%6].set_ylabel(legende_variable)
case[0,0].text(0,position_title,   'M '+site+' '+year_study+' v='+str(moruses_version), fontsize='smaller')
#f.suptitle('MORUSES - Shanghai - 2011-2013')
if (save_plot=='yes') :plt.savefig(save_directory+name_file_plot+str(count_figure)+'.png')
count_figure=count_figure+1



col_labels=['B-M','B-OBS','M-OBS']

fig=plt.figure(figsize=(16,6)) #We now want to plot
ax1 = fig.add_subplot(141)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
epaisseur_percentile=0.8
transparance=0.1
toto=[0,2,4,8]
for i in range(0,4):#For each season
	k=i
	split_hour=split_times(float(lat),float(lon),Time_saison[k],Var_saison_b[k],Var_saison_b[k],Var_saison_m[k], param_UTC=8)
	MAE_night=[MAE(split_hour[11],split_hour[15]),MAE(split_hour[11],split_hour[7]),MAE(split_hour[15],split_hour[7])]
	MAE_transit=[MAE(split_hour[8],split_hour[12]),MAE(split_hour[8],split_hour[4]),MAE(split_hour[12],split_hour[4])]
	MAE_morning=[MAE(split_hour[9],split_hour[13]),MAE(split_hour[9],split_hour[5]),MAE(split_hour[13],split_hour[5])]
	MAE_afternoon=[MAE(split_hour[10],split_hour[14]),MAE(split_hour[10],split_hour[6]),MAE(split_hour[14],split_hour[6])]
	fig.add_subplot(141+i)
	plot_line_bloxplot(Var_saison_h_b[i],heure,case_plot=plt,str_color='k',str_label='B'+' V'+str(best_version))
	plot_line_bloxplot(Var_saison_h_m[i],heure,case_plot=plt,str_color='r',str_label='M'+' V'+str(moruses_version))
	#plot_line_bloxplot(Var_saison_h_OBS[i],heure,case_plot=plt,str_color='b',str_label='OBS 11-13')
	#table_vals=[[MAE(Var_saison_b[k],Var_saison_m[k]),MAE(Var_saison_b[k],Var_saison_OBS[k]),MAE(Var_saison_m[k],Var_saison_OBS[k])], MAE_transit, MAE_morning, MAE_afternoon,MAE_night]
	table_vals=[[MAE(Var_saison_b[k],Var_saison_m[k]),MAE(Var_saison_b[k],Var_saison_b[k]),MAE(Var_saison_m[k],Var_saison_b[k])], MAE_transit, MAE_morning, MAE_afternoon,MAE_night]
	the_table = plt.table(cellText=table_vals,colWidths = [0.15]*3, rowLabels=row_labels_MAE, colLabels=col_labels,loc='best')
	plt.xticks(range(0,len(heure)+1),heure+['Mean'],rotation='vertical')
	plt.title(season[i])
	plt.ylim(min_T-1,max_T+1)
	plt.xlabel('Time (h)')
	if(i==0) : plt.text(0,position_title,   site+year_study, fontsize='smaller')
	if(i!=0) : plt.yticks([])
	else : 	plt.ylabel(legende_variable)
#plt.suptitle('MORUSES')
#case[0].text(0,position_title,   site+year_study+' MORUSES and Best ', fontsize='smaller')
plt.legend(loc='upper left')
print count_figure
if (save_plot=='yes') :plt.savefig(save_directory+name_file_plot+str(count_figure)+'.png')
count_figure=count_figure+1




#############################################
############ Distribution

#fig=plt.figure(figsize=(10,6))
couleur=['b','orange','g','r']
f, case = plt.subplots(1,2, sharex='col', sharey='row',figsize=(17,7))
for i in range(0,4):
	print int(min_T)
	print int(max_T)
#	case[0].hist(remove_nanVar_saison_OBS[i]),histtype = 'step', normed=1,label=season[i],color=couleur[i])
#	case[0].hist(remove_nan(Var_saison_OBS)[i],histtype = 'step', normed=1,bins=range(-200,500,20),label=season[i])
	case[0].hist(Var_saison_b[i],histtype = 'step', normed=1,bins=range(-200,500,20),label=season[i])
	case[1].hist(Var_saison_m[i],histtype = 'step', normed=1,bins=range(-200,500,20),label=season[i])
	case[0].set_xlabel(legende_variable)
	case[1].set_xlabel(legende_variable)
	#case[0].set_xlabel(legende_variable)
#plt.xlim(min_T-1,max_T+1)
case[0].text(-200,0.0165,   site+' '+year_study+' '+'M '+' v='+str(moruses_version), fontsize='smaller')
case[1].text(-200,0.0165,   site+' '+year_study+' '+'B '+' v='+str(best_version), fontsize='smaller')
#plt.xlabel(legende_variable)
plt.legend()
if (save_plot=='yes') :plt.savefig(save_directory+name_file_plot+str(count_figure)+'.png')
count_figure=count_figure+1


f, case = plt.subplots(4,8, sharex='col', sharey='row',figsize=(18,9))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)

for i in range(0,4):
	for j in range(0,len(heure_3h)) :
#		case[i,j].hist(remove_nan(Var_saison_3h_OBS[i])[j],histtype = 'step', normed=1,bins=range(-200,500,20))
		case[i,j].hist(remove_nan(Var_saison_3h_b[i])[j],histtype = 'step', normed=1,bins=range(-200,500,20),label='B')
		case[i,j].hist(remove_nan(Var_saison_3h_m[i])[j],histtype = 'step', normed=1,bins=range(-200,500,20),label='M')
		case[i,0].set_ylabel(season[i])
		case[0,j].set_title(heure_3h[j])
		case[3,j].set_xlabel(legende_variable)
case[0,(len(heure_3h)-1)].legend()
f.suptitle(site+' '+year_study+' '+'M '+' v='+str(moruses_version)+' B '+' v='+str(best_version))
if (save_plot=='yes') :plt.savefig(save_directory+name_file_plot+str(count_figure)+'.png')
count_figure=count_figure+1



plt.show()
