#!/usr/bin/python
# -*- coding: utf8 -*-

from fonction import *
from jules_download import *
from Split_times_Marine import *



save_plot='no'
#version_plot='' #OBS and AnthroOff
#version_plot='AnthroOn_' #OBS and AnthroOn
#version_plot='WFDEI_AnthroOff_' #WFDEI and AnthroOff
version_plot='WFDEI_AnthroOn_' #WFDEI and AnthroOn

#var=['SW_up','QH','Q_star','K_star','K_down','L_up','L_down']
var=['Q_star']




#legende_variable='$Q_{E}$  $W.m^{-2}$'
#name_variable_JULES='latent_heat'
#name_variable_OBS='qe'
#name_file_plot='Latent_heat'

for var_i in var :
	if (var_i=='QH') :
		legende_variable='$Q_{H}$  $W.m^{-2}$'
		name_variable_JULES='ftl_gb'
		name_variable_OBS='qh'
		name_file_plot='QH'
		#name_file_plot_A='AnthroOn_QH'
		name_variable_SUEWS='QH'

	if (var_i=='SW_up') :
		name_file_plot='SW_up'
		#name_file_plot='AnthroOn_SW_up'
		legende_variable='SW up $W.m^{-2}$'
		name_variable_JULES='sw_net'
		name_variable_JULES2='sw_down'
		name_variable_OBS='kup'
		name_variable_SUEWS='kup'

	if (var_i=='Q_star') :
		legende_variable='Q* $W.m^{-2}$'
		name_variable_JULES='rad_net'
		name_variable_OBS='kdown'
		name_variable_OBS2='kup'
		name_variable_OBS3='ldown'
		name_variable_OBS4='lup'
		name_variable_SUEWS='kdown'
		name_variable_SUEWS2='kup'
		name_variable_SUEWS3='ldown'
		name_variable_SUEWS4='lup'
		name_file_plot='Q_star'

	if (var_i=='K_star') :
		legende_variable='$K*$  $W.m^{-2}$'
		name_variable_JULES='sw_net'
		name_variable_OBS='kdown'
		name_variable_OBS2='kup'
		name_variable_SUEWS='kdown'
		name_variable_SUEWS2='kup'
		name_file_plot='K_star'

	if (var_i=='K_down') :
		legende_variable='$K down$  $W.m^{-2}$'
		name_variable_JULES='sw_down'
		name_variable_OBS='kdown'
		name_file_plot='K_down'
		name_variable_SUEWS='kdown'

	if (var_i=='L_up') :
		legende_variable='$L up$  $W.m^{-2}$'
		name_variable_JULES='lw_up'
		name_variable_OBS='lup'
		name_file_plot='L_up'
		#name_file_plot='AnthroOn_L_up'
		name_variable_SUEWS='lup'

	if (var_i=='L_down') :
		legende_variable='$L down$  $W.m^{-2}$'
		name_variable_JULES='lw_down'
		name_variable_OBS='ldown'
		name_file_plot='L_down'
		#name_file_plot='AnthroOn_L_down'
		name_variable_SUEWS='ldown'



##	#legende_variable='Albedo '
##	#name_variable_JULES='albedo_land'
##	#name_file_plot='Albedo'
##	#with_obs='no'
##	#with_SUEWS='no'

##	#legende_variable='Emissivity '
##	#name_variable_JULES='emis_gb'
##	#name_file_plot='Emisivity'
##	#with_obs='no'
##	#with_SUEWS='no'

	##LONDON
	##save_directory='/home/sufs1/ru5/sw/fq208733/WORKDIR/FIGURE/AnthroOff/KC/'# Anthropogenic Flux OFF
	##save_directory='/home/sufs1/ru5/sw/fq208733/WORKDIR/FIGURE/AnthroOn/KC/'# Anthropogenic Flux OFF
	#save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/AnthroOff/KC/'# Anthropogenic Flux OFF
	#save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/AnthroOn/KC/'# Anthropogenic Flux ON
	#moruses_version=74899# Anthropogenic Flux OFF
	#best_version=74898# Anthropogenic Flux OFF
	#moruses_version=74930# Anthropogenic Flux ON
	#best_version=74929# Anthropogenic Flux ON
	site='London KC'
	moruses_folder='/storage/shared/research/met/micromet/JULES/u-av612_MORUSES_London_KSSW/'
	best_folder='/storage/shared/research/met/micromet/JULES/u-av588_1-tile_London_KSSW/'
	obs_folder='/storage/shared/research/met/micromet/JULES/SUEWSEvaluationData/Kc/Obs/'
	#suews_folder='/storage/shared/research/met/micromet/JULES/SUEWSEvaluationData/Kc/Output/'
	suews_folder='/storage/shared/research/met/micromet/JULES/SUEWS_Prescribed_Ldn/'
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
		moruses_version=76930# Anthropogenic Flux OFF
		best_version=76922# Anthropogenic Flux OFF
	elif(version_plot=='AnthroOn_'):
		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/AnthroOn/KC/'# Anthropogenic Flux ON
		moruses_version=76956# Anthropogenic Flux ON
		best_version=76913# Anthropogenic Flux ON
	elif(version_plot=='WFDEI_AnthroOff_'):
		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOff/KC/'# Anthropogenic Flux ON
		moruses_version=76919# Anthropogenic Flux ON
		best_version=76940# Anthropogenic Flux ON
	elif(version_plot=='WFDEI_AnthroOn_'):
		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOn/KC/'# Anthropogenic Flux ON
		moruses_version=76907# Anthropogenic Flux ON
		best_version=76948# Anthropogenic Flux ON




#	###Shanghai
#	site='Shanghai'
#	moruses_folder='/storage/shared/research/met/micromet/JULES/u-aw196_MORUSES_Shanghai_XJH/'
#	best_folder='/storage/shared/research/met/micromet/JULES/u-aw195_1-tile_Shanghai_XJH/'
#	#obs_folder=
#	#suews_folder=
#	#name_file_suews=
#	local_time='Asia/Shanghai'
#	Start= datetime.datetime(2012, 01, 01,00,00,00)
#	#Start_SUEWS= 
#	year_study='2012-2013'
#	year_study_short='12-13'
#	with_obs='no'
#	local_hour=8
#	with_SUEWS='no'

#	#if(version_plot==''):
#		#save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/AnthroOff/Shanghai/'# Anthropogenic Flux OFF
#		#moruses_version=74899# Anthropogenic Flux OFF
#		#best_version=74898# Anthropogenic Flux OFF
#	#elif(version_plot=='AnthroOn_'):
#		#save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/AnthroOn/Shanghai/'# Anthropogenic Flux ON
#		#moruses_version=74930# Anthropogenic Flux ON
#		#best_version=74929# Anthropogenic Flux ON
#	if(version_plot=='WFDEI_AnthroOff_'):
#		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOff/Shanghai/'# Anthropogenic Flux ON
#		moruses_version=76910# Anthropogenic Flux ON
#		best_version=76924# Anthropogenic Flux ON
#	elif(version_plot=='WFDEI_AnthroOn_'):
#		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOn/Shanghai/'# Anthropogenic Flux ON
#		moruses_version=76921# Anthropogenic Flux ON
#		best_version=76915# Anthropogenic Flux ON


#	#Beijing
#	site='Beijing'
#	moruses_folder='/storage/shared/research/met/micromet/JULES/u-aw219_MORUSES_Beijing_IAP/'
#	best_folder='/storage/shared/research/met/micromet/JULES/u-aw217_1-tile_Beijing_IAP/'
#	#obs_folder=
#	#suews_folder=
#	#name_file_suews=
#	local_time='Asia/Shanghai'
#	Start= datetime.datetime(2014, 01, 01,00,00,00)
#	#Start_SUEWS= 
#	year_study='2014-2015'
#	year_study_short='14-15'
#	with_obs='no'
#	local_hour=8
#	with_SUEWS='no'

#	#if(version_plot==''):
#		#save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/AnthroOff/Beijing/'# Anthropogenic Flux OFF
#		#moruses_version=74899# Anthropogenic Flux OFF
#		#best_version=74898# Anthropogenic Flux OFF
#	#elif(version_plot=='AnthroOn_'):
#		#save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/AnthroOn/Beijing/'# Anthropogenic Flux ON
#		#moruses_version=74930# Anthropogenic Flux ON
#		#best_version=74929# Anthropogenic Flux ON
#	if(version_plot=='WFDEI_AnthroOff_'):
#		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOff/Beijing/'# Anthropogenic Flux ON
#		moruses_version=76908# Anthropogenic Flux ON
#		best_version=76923# Anthropogenic Flux ON
#	elif(version_plot=='WFDEI_AnthroOn_'):
#		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOn/Beijing/'# Anthropogenic Flux ON
#		moruses_version=76920# Anthropogenic Flux ON
#		best_version=76914# Anthropogenic Flux ON


	#### Here are the files that we want to study : (NetCDF files)


	########################## JULES

	#name_variable_JULES='ftl_gb'


	Var_moruses=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_best=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[0]

	#if(name_file_plot=='AnthroOn_SW_up' or name_file_plot=='SW_up'):
	Var_moruses_1=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc','sw_net',Start)[0]
	Var_best_1=jules_download(best_folder+str(best_version)+'/jules.all.nc','sw_net',Start)[0]
#		Var_best_1=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_moruses_2=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc','lw_down',Start)[0]
	Var_best_2=jules_download(best_folder+str(best_version)+'/jules.all.nc','lw_down',Start)[0]
#		Var_best_2=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES2,Start)[0]
	Var_moruses_3=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc','lw_up',Start)[0]
	Var_best_3=jules_download(best_folder+str(best_version)+'/jules.all.nc','lw_up',Start)[0]
	Var_moruses_calcul=Var_moruses_1+Var_moruses_2-Var_moruses_3
	Var_best_calcul=Var_best_1+Var_best_2-Var_best_3
#		Var_best=Var_best_2-Var_best_1






	Time_moruses=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES,Start)[1]
	if(local_time!='Europe/London') : Time_moruses=convert_UTC_to_local(Time_moruses,local_time)
	Time_best=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[1]
	if(local_time!='Europe/London') : Time_best=convert_UTC_to_local(Time_best,local_time)

	lon=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc','longitude',Start)[0]
	lat=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc','latitude',Start)[0]

	#if  (Time_moruses!=Time_best) : print 'MORUSES and Best are not the same size'
	#print 'lon',lon,'lat',lat


	fig=plt.figure(figsize=(17,11)) #We now want to plot
	#ax1 = fig.add_subplot(311)
	#plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
	#epaisseur_percentile=0.8
	#transparance=0.1

	#fig.add_subplot(312)
	plt.plot(Time_moruses,Var_moruses,color='k',label='rad_net',linewidth=0.5,alpha=0.7)
	plt.plot(Time_moruses,Var_moruses_calcul,color='r',label='Calcul',linewidth=0.5,alpha=0.7)
	plt.plot(Time_moruses,np.array(Var_moruses)-np.array(Var_moruses_calcul),color='b',label='diff',linewidth=0.5,alpha=0.7)
	#plt.scatter(daily_mean(Var_moruses,Time_moruses,val_min=15)[1],daily_mean(Var_moruses,Time_moruses,val_min=15)[0],color='r',label='Daily mean',marker='+')
	plt.annotate(site +'\n'+'MORUSES '+'v='+str(moruses_version)+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction')
	plt.ylabel(legende_variable)
	plt.legend(loc='best')
	#if(name_file_plot!='Albedo'and name_file_plot!='Emisivity') : plt.ylim(min_T,max_T)
	#plt.xticks([])


	fig=plt.figure(figsize=(17,11)) #We now want to plot
	plt.plot(Time_moruses,np.array(Var_moruses)-np.array(Var_moruses_calcul),color='b',label='diff',linewidth=0.5,alpha=0.7)
	#plt.scatter(daily_mean(Var_moruses,Time_moruses,val_min=15)[1],daily_mean(Var_moruses,Time_moruses,val_min=15)[0],color='r',label='Daily mean',marker='+')
	plt.annotate(site +'\n'+'MORUSES '+'v='+str(moruses_version)+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction')
	plt.ylabel('diff'+legende_variable)
	#if(name_file_plot!='Albedo'and name_file_plot!='Emisivity') : plt.ylim(min_T,max_T)
	#plt.xticks([])


	fig=plt.figure(figsize=(17,11)) #We now want to plot
	#ax1 = fig.add_subplot(311)
	#plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
	#epaisseur_percentile=0.8
	#transparance=0.1

	#fig.add_subplot(312)
	plt.plot(Time_moruses,Var_best,color='k',label='rad_net',linewidth=0.5,alpha=0.7)
	plt.plot(Time_moruses,Var_best_calcul,color='r',label='Calcul',linewidth=0.5,alpha=0.7)
	plt.plot(Time_moruses,np.array(Var_best)-np.array(Var_best_calcul),color='b',label='diff',linewidth=0.5,alpha=0.7)
	#plt.scatter(daily_mean(Var_moruses,Time_moruses,val_min=15)[1],daily_mean(Var_moruses,Time_moruses,val_min=15)[0],color='r',label='Daily mean',marker='+')
	plt.annotate(site +'\n'+'BEST '+'v='+str(best_version)+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction')
	plt.ylabel(legende_variable)
	plt.legend(loc='best')
	#if(name_file_plot!='Albedo'and name_file_plot!='Emisivity') : plt.ylim(min_T,max_T)
	#plt.xticks([])


	fig=plt.figure(figsize=(17,11)) #We now want to plot
	plt.plot(Time_moruses,np.array(Var_best)-np.array(Var_best_calcul),color='b',label='diff',linewidth=0.5,alpha=0.7)
	#plt.scatter(daily_mean(Var_moruses,Time_moruses,val_min=15)[1],daily_mean(Var_moruses,Time_moruses,val_min=15)[0],color='r',label='Daily mean',marker='+')
	plt.annotate(site +'\n'+'Best '+'v='+str(best_version)+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction')
	plt.ylabel('diff'+legende_variable)
	#if(name_file_plot!='Albedo'and name_file_plot!='Emisivity') : plt.ylim(min_T,max_T)
	#plt.xticks([])

plt.show()

