#!/usr/bin/python
# -*- coding: utf8 -*-

from fonction import *
from jules_download import *
from Split_times_Marine import *

from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

save_plot='yes'
version_plot='' #OBS and AnthroOff
#version_plot='AnthroOn_' #OBS and AnthroOn
#version_plot='WFDEI_AnthroOff_' #WFDEI and AnthroOff
#version_plot='WFDEI_AnthroOn_' #WFDEI and AnthroOn

var=['SW_up','QH','Q_star','K_star','K_down','L_up','L_down']
#var=['SW_up','QH','Q_star','L_up']
#var=['SW_up']
#var=['QH']
#var=['Emissivity']
#var=['Tsurf']

#var=['Tsoil']
#level=0

#legende_run=['C=2.8E5','C=2.E5','C=1.E5']
legende_run=['C=2.8E5','C=2.E5','C=3.5E5']
#legende_run=[r'$ \alpha = 0.18 $ ',r'$ \alpha = 0.09 $ ',r'$ \alpha = 0.11 $ ']
model=['B','B','B']
third='yes'


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
		legende_variable='$K_{\uparrow}$ $W.m^{-2}$'
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
		legende_variable='$K_{\downarrow}$  $W.m^{-2}$'
		name_variable_JULES='sw_down'
		name_variable_OBS='kdown'
		name_file_plot='K_down'
		name_variable_SUEWS='kdown'

	if (var_i=='L_up') :
		legende_variable='$L_{\uparrow}$  $W.m^{-2}$'
		name_variable_JULES='lw_up'
		name_variable_OBS='lup'
		name_file_plot='L_up'
		#name_file_plot='AnthroOn_L_up'
		name_variable_SUEWS='lup'

	if (var_i=='L_down') :
		legende_variable='$L_{\downarrow}$  $W.m^{-2}$'
		name_variable_JULES='lw_down'
		name_variable_OBS='ldown'
		name_file_plot='L_down'
		#name_file_plot='AnthroOn_L_down'
		name_variable_SUEWS='ldown'

	if (var_i=='Albedo') :
		legende_variable='$Albedo$  $(-)$'
		name_variable_JULES='albedo_land'
		#name_variable_OBS='ldown'
		name_file_plot='Albedo'
		#name_file_plot='AnthroOn_L_down'
		#name_variable_SUEWS='ldown'
		with_obs='no'
		with_SUEWS='no'

	if (var_i=='Emissivity') :
		legende_variable='$Emissivity$  $(-)$'
		name_variable_JULES='emis_gb'
		#name_variable_OBS='ldown'
		name_file_plot='Emissivity'
		#name_file_plot='AnthroOn_L_down'
		#name_variable_SUEWS='ldown'
		with_obs='no'
		with_SUEWS='no'

	if (var_i=='Tsurf') :
		legende_variable='$Tsurf$  $(K)$'
		name_variable_JULES='tstar_gb'
		#name_variable_OBS='ldown'
		name_file_plot='Tsurf'
		#name_file_plot='AnthroOn_L_down'
		#name_variable_SUEWS='ldown'
		with_obs='no'
		with_SUEWS='no'

	if (var_i=='Tsoil') :
		legende_variable='$Tsoil$  $(K)$'
		name_variable_JULES='t_soil'
		#name_variable_OBS='ldown'
		name_file_plot='Tsoil'+str(level)
		#name_file_plot='AnthroOn_L_down'
		#name_variable_SUEWS='ldown'
		with_obs='no'
		with_SUEWS='no'




	##LONDON
	site='London KC'
	#best3_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/2_best_albedo09_C1/'
	#best2_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/4_best_albedo09_C2/'
	#best_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/best_albedo09/'

#	best3_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/2_best_albedo09_C1/'
#	best2_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/5_best_albedo09_c2_anthroON/'
#	best_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/3_best_albedo09_C28_anthroON/'

	# Comparison between != albedo , with Qf
#	best_folder='/storage/shared/research/met/micromet/JULES/u-av588_1-tile_London_KSSW/76913'
#	best3_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/7_best_albedo11_C28_anthroON'
#	best2_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/3_best_albedo09_C28_anthroON/'

	# Comparison between != Cs , with albedo =0.11
	best_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/7_best_albedo11_C28_anthroON/'
	#best3_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/9_best_albedo11_C1_anthropoON/'
	best3_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/10_best_albedo11_C35_anthropoON/'
	best2_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/8_best_albedo11_c2_anthroON/'

	obs_folder='/storage/shared/research/met/micromet/JULES/SUEWSEvaluationData/Kc/Obs/'
	#suews_folder='/storage/shared/research/met/micromet/JULES/SUEWSEvaluationData/Kc/Output/'
	suews_folder='/storage/shared/research/met/micromet/JULES/SUEWS_Prescribed_Ldn/'
	name_file_suews=['Kc1_2011_60.txt','Kc1_2012_60.txt','Kc1_2013_60.txt']
	local_time='Europe/London'
	Start= datetime.datetime(2011, 01, 01,00,00,00)
	Start_SUEWS= datetime.datetime(2011, 01, 01,00,00,00)
	year_study='2011-2013'
	year_study_short='11-13'
	#with_obs='yes'
	local_hour=0
	if (var_i!='Emissivity' and var_i!='Albedo' and var_i!='Tsurf' and var_i!='Tsoil') : with_obs='yes'
	#if (var_i!='Emissivity' and var_i!='Albedo' and var_i!='Tsurf' and var_i!='Tsoil') : with_SUEWS='yes'
	with_SUEWS='no'

	if(version_plot==''):

		#save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/Compare_Best/Capacity_AnthropoOFF/'# Anthropogenic Flux OFF
		#save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/Compare_Best/Albedo_anthropoON/'# Anthropogenic Flux OFF
		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/Compare_Best/Capacity_Albedo11_AnthropoON/'# Anthropogenic Flux OFF

		best2_version=76930# Anthropogenic Flux OFF
		best_version=76922# Anthropogenic Flux OFF
#	elif(version_plot=='AnthroOn_'):
#		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/AnthroOn/KC/'# Anthropogenic Flux ON
#		moruses_version=76956# Anthropogenic Flux ON
#		################best_version=78137# Anthropogenic Flux ON
#	elif(version_plot=='WFDEI_AnthroOff_'):
#		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOff/KC/'# Anthropogenic Flux ON
#		moruses_version=76919# Anthropogenic Flux ON
#		best_version=76940# Anthropogenic Flux ON
#	elif(version_plot=='WFDEI_AnthroOn_'):
#		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOn/KC/'# Anthropogenic Flux ON
#		moruses_version=76907# Anthropogenic Flux ON
#		best_version=76948# Anthropogenic Flux ON




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



	Var_best2=jules_download(best2_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
	print best_folder+str(best_version)+'/jules.all.nc'
	#Var_best=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_best=jules_download(best_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_best3=jules_download(best3_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
	print type(Var_best2)
	print Var_best2.shape
	print Var_best.shape

	if(name_file_plot=='AnthroOn_SW_up' or name_file_plot=='SW_up'):
		Var_best3_1=jules_download(best3_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_best2_1=jules_download(best2_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
		#Var_best_1=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_best_1=jules_download(best_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_best2_2=jules_download(best2_folder+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_best3_2=jules_download(best3_folder+'/jules.all.nc',name_variable_JULES2,Start)[0]
		#Var_best_2=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_best_2=jules_download(best_folder+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_best2=Var_best2_2-Var_best2_1
		Var_best3=Var_best3_2-Var_best3_1
		Var_best=Var_best_2-Var_best_1
	elif(var_i=='Tsoil') :
		Var_best2=Var_best2[:,level]
		Var_best3=Var_best3[:,level]
		Var_best=Var_best[:,level]

	print type(Var_best2)
	print Var_best2.shape

	Time_best2=jules_download(best2_folder+'/jules.all.nc',name_variable_JULES,Start)[1]
	Time_best3=jules_download(best3_folder+'/jules.all.nc',name_variable_JULES,Start)[1]
	if(local_time!='Europe/London') : 
		Time_best2=convert_UTC_to_local(Time_best2,local_time)
		Time_best3=convert_UTC_to_local(Time_best3,local_time)
	#Time_best=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[1]
	Time_best=jules_download(best_folder+'/jules.all.nc',name_variable_JULES,Start)[1]
	if(local_time!='Europe/London') : Time_best=convert_UTC_to_local(Time_best,local_time)

	lon=jules_download(best2_folder+'/jules.all.nc','longitude',Start)[0]
	lat=jules_download(best2_folder+'/jules.all.nc','latitude',Start)[0]

	if  (Time_best2!=Time_best) : print 'Best2 and Best are not the same size'
	print 'lon',lon,'lat',lat


	#for i in range (0, 20) : print 'UTC',Time_best2[i]

	#Time_best2_UTC=Tixme_best2[:]
	#Time_best2_local=convert_UTC_to_local(Time_best2,local_time)

	###for i in range (0, 20) : print 'UTC',Time_best2[i], 'local', Time_best2_local[i],'UTC',Time_best2_UTC[i]

	#for i in range (0, 1000) : print 'UTC',Time_best2[i], 'local', Time_best2_local[i],'sunrise', calculate_time(Time_best2_local[i], lat, lon, 0,0),'sunset', calculate_time(Time_best2_local[i], lat, lon, 1,0),'noon', calculate_time(Time_best2_local[i], lat, lon, 2,0)

	#plt.figure()
	#plt.show()


	#########################  OBS
##	if with_obs=='yes' :
##		Var_OBS=extract_variable(extract_txt('/glusterfs/micromet/users/micromet/JULES/SUEWSEvaluationData/Kc/Obs/'+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS)
##		Var_OBS=quite_modif(Var_OBS,-500,1500,value_missing=-999.)
##		Time_OBS=extract_variable(extract_txt('/glusterfs/micromet/users/micromet/JULES/SUEWSEvaluationData/Kc/Obs/'+'Kc1_Obs.csv',nomber_header=0), 'DateTime',date=True)
##		Time_OBS=convert_UTC_to_local(Time_OBS,local_time)
##		#
##		Var_missing_OBS=missing_measurement(Time_best2,Var_OBS,Time_OBS,value_nan=-999.)[1]
##		missing_OBS=missing_measurement(Time_best2,Var_OBS,Time_OBS,value_nan=-999.)[0]

##	print with_obs, var_i, (var_i!='Emissivity' and var_i!='Albedo')


	if with_obs=='yes' :
		if(name_file_plot=='Q_star' or name_file_plot=='AnthroOn_Q_star'):
			Var_OBS1=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS)),-999.,float('nan'))
			Var_OBS2=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS2)),-999.,float('nan'))
			Var_OBS3=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS3)),-999.,float('nan'))
			Var_OBS4=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS4)),-999.,float('nan'))
			Var_OBS=Var_OBS1-Var_OBS2+Var_OBS3-Var_OBS4
		elif(name_file_plot=='K_star' or name_file_plot=='AnthroOn_K_star'):
			Var_OBS1=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS)),-999.,float('nan'))
			Var_OBS2=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS2)),-999.,float('nan'))
			Var_OBS=Var_OBS1-Var_OBS2
		else : Var_OBS=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS)),-999.,float('nan'))
		#Var_OBS=quite_modif(Var_OBS,-500,900,float('nan'))
		Time_OBS=extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), 'DateTime',date=True)
		if(local_time!='Europe/London') : Time_OBS=convert_UTC_to_local(Time_OBS,local_time)
		Var_missing_OBS=missing_measurement(Time_best2,Var_OBS,Time_OBS,value_nan=-999.)[1]
		missing_OBS=missing_measurement(Time_best2,Var_OBS,Time_OBS,value_nan=-999.)[0]

#	##########################  SUEWS
#	if with_SUEWS=='yes' :
#		if(name_file_plot=='Q_star' or name_file_plot=='AnthroOn_Q_star'):
#			Var_SUEWS1=get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS)
#			Var_SUEWS2=get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS2)
#			Var_SUEWS3=get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS3)
#			Var_SUEWS4=get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS4)
#			Var_SUEWS=np.array(Var_SUEWS1)-np.array(Var_SUEWS2)+np.array(Var_SUEWS3)-np.array(Var_SUEWS4)
#		elif(name_file_plot=='K_star' or name_file_plot=='AnthroOn_K_star'):
#			Var_SUEWS1=get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS)
#			Var_SUEWS2=get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS2)
#			Var_SUEWS=np.array(Var_SUEWS1)-np.array(Var_SUEWS2)
#		else : Var_SUEWS=np.array(get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS))
#		Time_SUEWS=get_time_suews(suews_folder,name_file_suews,Start_SUEWS)
#		if(local_time!='Europe/London') : Time_SUEWS=convert_UTC_to_local(Time_SUEWS,local_time)
#		Var_missing_SUEWS=missing_measurement(Time_best2,Var_SUEWS,Time_SUEWS,value_nan=-999.)[1]






	if with_obs=='yes' : Var_saison_OBS=divide_periode_day('season',Var_missing_OBS,Time_best2)
	if with_SUEWS=='yes' : Var_saison_SUEWS=divide_periode_day('season',Var_missing_SUEWS,Time_best2)
	Var_saison_m=divide_periode_day('season',Var_best2,Time_best2)
	Var_saison_b=divide_periode_day('season',Var_best,Time_best2)
	Var_saison_b3=divide_periode_day('season',Var_best3,Time_best2)
	Time_saison=divide_periode_day('season',Time_best2,Time_best2)

	if with_obs=='yes' : Var_saison_3h_OBS=divide_periode_day('season',Var_missing_OBS,Time_best2,which_day=3)
	if with_SUEWS=='yes' : Var_saison_3h_SUEWS=divide_periode_day('season',Var_missing_SUEWS,Time_best2,which_day=3)
	Var_saison_3h_b=divide_periode_day('season',Var_best,Time_best2,which_day=3)
	Var_saison_3h_b3=divide_periode_day('season',Var_best3,Time_best2,which_day=3)
	Var_saison_3h_m=divide_periode_day('season',Var_best2,Time_best2,which_day=3)
	Time_saison_3h=divide_periode_day('season',Time_best2,Time_best2,which_day=3)

	if with_obs=='yes' : Var_saison_h_OBS=divide_periode_day('season',Var_missing_OBS,Time_best2,which_day=1)
	if with_SUEWS=='yes' : Var_saison_h_SUEWS=divide_periode_day('season',Var_missing_SUEWS,Time_best2,which_day=1)
	Var_saison_h_b=divide_periode_day('season',Var_best,Time_best2,which_day=1)
	Var_saison_h_b3=divide_periode_day('season',Var_best3,Time_best2,which_day=1)
	Var_saison_h_m=divide_periode_day('season',Var_best2,Time_best2,which_day=1)
	#Time_saison_h=divide_periode_day('season',Time_JULES,Time_JULES,which_day=1)

	if with_obs=='yes' : Var_h_OBS=divide_periode_day('month',Var_missing_OBS,Time_best2,which_day=1)
	if with_SUEWS=='yes' : Var_h_SUEWS=divide_periode_day('month',Var_missing_SUEWS,Time_best2,which_day=1)

	if with_obs=='yes' : Var_all_h_OBS=divide_periode_day('all',Var_missing_OBS,Time_best2,which_day=1)
	if with_SUEWS=='yes' : Var_all_h_SUEWS=divide_periode_day('all',Var_missing_SUEWS,Time_best2,which_day=1)
	Var_all_h_b=divide_periode_day('all',Var_best,Time_best2,which_day=1)
	Var_all_h_b3=divide_periode_day('all',Var_best3,Time_best2,which_day=1)
	Var_all_h_m=divide_periode_day('all',Var_best2,Time_best2,which_day=1)

	print len(Var_all_h_m), len(Var_all_h_m[0])



	split_hour_all=split_times(float(lat),float(lon),Time_best2,Var_missing_OBS,Var_best,Var_best2,local_hour)
	if(third=='yes') :split_hour3_all=split_times(float(lat),float(lon),Time_best2,Var_best3,Var_best3,Var_best3,local_hour)

	plt.figure()
	plt.scatter([1,2,3],[MAE(split_hour_all[4],split_hour_all[8]),MAE(split_hour_all[4],split_hour_all[12]),MAE(split_hour_all[4],split_hour3_all[8])], marker='o',color='g',label='T')
	plt.scatter([1,2,3],[MAE(split_hour_all[5],split_hour_all[9]),MAE(split_hour_all[5],split_hour_all[13]),MAE(split_hour_all[5],split_hour3_all[9])], marker='^',color='r',label='M')
	plt.scatter([1,2,3],[MAE(split_hour_all[6],split_hour_all[10]),MAE(split_hour_all[6],split_hour_all[14]),MAE(split_hour_all[6],split_hour3_all[10])], marker='s',color='b',label='A')
	plt.scatter([1,2,3],[MAE(split_hour_all[7],split_hour_all[11]),MAE(split_hour_all[7],split_hour_all[15]),MAE(split_hour_all[7],split_hour3_all[11])], marker='*',color='grey',label='N')
	plt.scatter([1,2,3],[MAE(Var_missing_OBS,Var_best),MAE(Var_missing_OBS,Var_best2),MAE(Var_missing_OBS,Var_best3)], marker='.',color='k',label='24h')
	plt.legend(loc='best')
	plt.xticks([1,2,3],legende_run,rotation='vertical')
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_MAE_year.png',dpi=300)
	#plt.show()


	#plt.figure()
	#plt.text([1]*5, [MAE(split_hour_all[4],split_hour_all[8]),MAE(split_hour_all[5],split_hour_all[9]),MAE(split_hour_all[6],split_hour_all[10]),MAE(split_hour_all[7],split_hour_all[11]),MAE(Var_missing_OBS,Var_best)], ['T','M','A','N','D'])

	#plt.figure()
	#plt.annotate(['T','M','A','N','D'], xy=([1]*5, [MAE(split_hour_all[4],split_hour_all[8]),MAE(split_hour_all[5],split_hour_all[9]),MAE(split_hour_all[6],split_hour_all[10]),MAE(split_hour_all[7],split_hour_all[11]),MAE(Var_missing_OBS,Var_best)]))

	#plt.scatter([2]*5,[MAE(split_hour_all[4],split_hour_all[12]),MAE(split_hour_all[5],split_hour_all[13]),MAE(split_hour_all[6],split_hour_all[14]),MAE(split_hour_all[7],split_hour_all[15]),MAE(Var_missing_OBS,Var_best2)], marker=r"$ {} $".format(['T','M','A','N','D']))



	#####################Usefull information
	vect_all=[Var_best,Var_best2,Var_best3]
	if with_obs=='yes' : vect_all.append(Var_missing_OBS)
	if with_SUEWS=='yes' : vect_all.append(Var_missing_SUEWS)
	centile_99=float(np.nanpercentile(np.array(vect_all),99))
	centile_1=float(np.nanpercentile(np.array(vect_all),1))

	max_T=max([Var_best.max(),Var_best2.max(),Var_best3.max()])
	min_T=min([Var_best.min(),Var_best2.min(),Var_best3.min()])
	if with_obs=='yes' : 
		max_T=max([max_T,max(Var_missing_OBS)])
		min_T=min([min_T,min(Var_missing_OBS)])
	if with_SUEWS=='yes' : 
		max_T=max([max_T,max(Var_missing_SUEWS)])
		min_T=min([min_T,min(Var_missing_SUEWS)])

	position_title=max_T-(max_T-min_T)*0.10

	#plt.figure()
	#plt.show()

	heure_3h=['0h','3h','6h','9h','12h','15h','18h','21h']
	mois=['J','F','M','A','M','J','J','A','S','O','N','D']
	season=['Winter DJF','Spring MAM','Summer JJA','Autumn SON']
	heure=['']*24
	for i in range(0,len(heure)):
		if (i%3==0) : heure[i]=str(i)
	#for i in range(0,24): heure.extend([str(i)])
	row_labels_coef=['24h','T','M','A','N']
	count_figure=1


	print 'max',max_T
	print 'min',min_T
	print 500
	print '99',centile_99, type(centile_99), float(centile_99), type(float(centile_99)), round(centile_99)
	print -200
	print '1', centile_1, type(centile_1), round(centile_1)

	print range(int(centile_1),int(centile_99)+19,20)

	#plt.figure()
	#plt.show()

	#####################

	#########################################################
	########### Evolution over the Periode


#	count_figure=1
#	color_value=(1.,.0,.0)#red
#	color_missing=(0.,0.,1.)#blue
#	colors=[color_value,color_missing]
#	n_bin=2
#	cm = LinearSegmentedColormap.from_list('color_value_missing', colors, N=2)

#	if with_obs=='yes' :
#		plt.figure(figsize=(14,3))
#		plt.pcolor(Time_best2,[1,2,3],np.array([missing_OBS,missing_OBS]),cmap=cm)
#		plt.yticks([1,2,3], ['Kc']+['',' '])
#		plt.title('Kc OBS 2011-2013')
#		cbar=plt.colorbar(ticks=[0, 1])
#		cbar.ax.set_yticklabels([ 'missing', 'available'])
#		if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_missing_obs.png',dpi=200)
#		count_figure=count_figure+1

#	print save_directory+version_plot+name_file_plot+'_missing_obs.png'
	#plt.show()

#	fig=plt.figure(figsize=(17,11)) #We now want to plot
#	ax1 = fig.add_subplot(311)
#	plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
#	epaisseur_percentile=0.8
#	transparance=0.1

#	fig.add_subplot(311)
#	if with_obs=='yes' :
#		plt.plot(Time_best2,Var_missing_OBS,color='k',label='Hourly',linewidth=0.5,alpha=0.7)
#		plt.scatter(daily_mean(Var_missing_OBS,Time_best2,val_min=15)[1],daily_mean(Var_missing_OBS,Time_best2,val_min=15)[0],color='r',label='Daily mean',marker='+')
#		#plt.text(min(Time_best2),position_title,  'OBS '+site+' '+year_study, fontsize='smaller')
#		#plt.text(min(Time_best2),position_title,  'OBS \n'+site+' '+year_study, fontsize='smaller')
#		plt.annotate(site +'\n'+'OBS '
#	+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction')
#		plt.ylabel(legende_variable)
#		#plt.title('best')
#		if(name_file_plot!='Albedo' or name_file_plot=='Emissivity') : plt.ylim(min_T,max_T)
#		plt.xticks([])

#	fig.add_subplot(312)
#	plt.plot(Time_best2,Var_best2,color='k',label='Hourly',linewidth=0.5,alpha=0.7)
#	plt.scatter(daily_mean(Var_best2,Time_best2,val_min=15)[1],daily_mean(Var_best2,Time_best2,val_min=15)[0],color='r',label='Daily mean',marker='+')
#	plt.annotate(site +'\n'+'Best 0.09 '+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction')
#	plt.ylabel(legende_variable)
#	if(name_file_plot!='Albedo'or name_file_plot=='Emissivity') : plt.ylim(min_T,max_T)
#	plt.xticks([])

#	fig.add_subplot(313)
#	plt.plot(Time_best2,Var_best,color='k',label='Hourly',linewidth=0.5,alpha=0.7)
#	plt.scatter(daily_mean(Var_best,Time_best2,val_min=15)[1],daily_mean(Var_best,Time_best2,val_min=15)[0],color='r',label='Daily mean',marker='+')
#	plt.annotate(site +'\n'+'Best 0.18 '+'v='+str(best_version)+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction')
#	plt.ylabel(legende_variable)
#	plt.xlabel('Time (day)')
#	if(name_file_plot!='Albedo' or name_file_plot!='Emissivity') : plt.ylim(min_T,max_T)
#	plt.legend(loc='best')


#	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_variations.png',dpi=300)
#	count_figure=count_figure+1




#	if with_SUEWS=='yes' :
#		fig=plt.figure(figsize=(17,3)) #We now want to plot
#		plt.plot(Time_best2,Var_missing_SUEWS,color='k',label='Hourly',linewidth=0.5,alpha=0.7)
#		plt.scatter(daily_mean(Var_missing_SUEWS,Time_best2,val_min=15)[1],daily_mean(Var_missing_SUEWS,Time_best2,val_min=15)[0],color='r',label='Daily mean',marker='+')
#		plt.annotate(site +'\n'+'SUEWS '+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction')
#		plt.ylabel(legende_variable)
#		if(name_file_plot!='Albedo' or name_file_plot=='Emissivity') : plt.ylim(min_T,max_T)
#		plt.xticks([])
#		if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_variations_SUEWS.png',dpi=300)
#		count_figure=count_figure+1



	plt.figure(figsize=(12,6))
	plt.subplots_adjust(left=0.06, bottom=None, right=0.94, top=None,wspace=0.05, hspace=0.05)
	if with_obs=='yes' : plt.scatter(daily_mean(Var_missing_OBS,Time_best2,val_min=15)[1],daily_mean(Var_missing_OBS,Time_best2,val_min=15)[0],color='k',label='OBS',marker='+')
	if with_SUEWS=='yes' : plt.scatter(daily_mean(Var_missing_SUEWS,Time_best2,val_min=15)[1],daily_mean(Var_missing_SUEWS,Time_best2,val_min=15)[0],color='g',label='SUEWS',marker='+')
	plt.scatter(daily_mean(Var_best,Time_best2,val_min=15)[1],daily_mean(Var_best,Time_best2,val_min=15)[0],color='r',label=str(model[0])+'1 '+legende_run[0],marker='+')
	plt.scatter(daily_mean(Var_best2,Time_best2,val_min=15)[1],daily_mean(Var_best2,Time_best2,val_min=15)[0],color='b',label=str(model[1])+'2 '+legende_run[1],marker='+')
	if(third=='yes') : plt.scatter(daily_mean(Var_best3,Time_best2,val_min=15)[1],daily_mean(Var_best2,Time_best2,val_min=15)[0],color='g',label=str(model[2])+'3 '+legende_run[2],marker='+')
	plt.title('Sensible Heat, daily mean -2011-2013 over London (KC)')
	plt.legend(loc='best')
	plt.ylabel(legende_variable)
	plt.xlabel('Time (day)')
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_daily_mean.png',dpi=300)
	count_figure=count_figure+1

	if (save_plot=='yes') : print 'ok'
	print save_directory+name_file_plot+str(count_figure)+'.png'






	##############################################
	########### Boxplot

#	#OBS
#	if with_obs=='yes' :
#		f, case = plt.subplots(1,4, sharex='col', sharey='row',figsize=(18,9))
#		plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
#		for i in range(0,4):#for each month
#			plot_evolution_boxplot(case[i],Var_saison_h_OBS[i],heure,season[i],min_T,max_T)
#			case[i].set_xlabel('Time (h)')
#			if (i==0 or i==6) :case[i].set_ylabel(legende_variable)
#		case[0].annotate(site +'\n'+'OBS '+'\n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
#		if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_OBS.png',dpi=300)
#		count_figure=count_figure+1

#	#SUEWS
#	if with_SUEWS=='yes' :
#		f, case = plt.subplots(1,4, sharex='col', sharey='row',figsize=(18,9))
#		plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
#		for i in range(0,4):#for each month
#			plot_evolution_boxplot(case[i],Var_saison_h_SUEWS[i],heure,season[i],min_T,max_T)
#			case[i].set_xlabel('Time (h)')
#			if (i==0 or i==6) :case[i].set_ylabel(legende_variable)
#		case[0].annotate(site +'\n'+'SUEWS '+'\n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
#		if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_SUEWS.png',dpi=300)
#		count_figure=count_figure+1



#	#best
#	f, case = plt.subplots(1,4, sharex='col', sharey='row',figsize=(18,9))
#	plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
#	for i in range(0,4):#for each month
#		min_max='yes'
#		if(name_file_plot=='Albedo' or name_file_plot=='Emissivity') : min_max='no'
#		plot_evolution_boxplot(case[i],Var_saison_h_b[i],heure,season[i],min_T,max_T,do_min_max=min_max)
#		case[i].set_xlabel('Time (h)')
#		if (i==0 or i==6) :case[i].set_ylabel(legende_variable)
#	case[0].annotate(site +'\n'+'Best 0.18'+'v='+str(best_version)+'\n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
#	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_Best.png',dpi=300)
#	count_figure=count_figure+1


#	#moruses
#	f, case = plt.subplots(1,4, sharex='col', sharey='row',figsize=(18,9))
#	plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
#	for i in range(0,4):#for each month
#		min_max='yes'
#		if(name_file_plot=='Albedo' or name_file_plot=='Emissivity') : min_max='no'
#		plot_evolution_boxplot(case[i],Var_saison_h_m[i],heure,season[i],min_T,max_T,do_min_max=min_max)
#		case[i].set_xlabel('Time (h)')
#		if (i==0 or i==6) :case[i].set_ylabel(legende_variable)
#	case[0].annotate(site +'\n'+'Best 0.09 '+'\n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
#	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_Best2.png',dpi=300)
#	count_figure=count_figure+1



#	f, case = plt.subplots(2,4, sharex='col', sharey='row',figsize=(18,9))
#	plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.04, hspace=0.04)
#	for i in range(0,4):#for each month
#		min_max='yes'
#		case[0,i].ticklabel_format(useOffset=False)
#		if(name_file_plot=='Albedo' or name_file_plot=='Emissivity') : min_max='no'
#		plot_evolution_boxplot(case[0,i],Var_saison_h_b[i],heure,season[i],min_T,max_T,do_min_max=min_max)
#		case[0,i].set_xlabel('Time (h)')
#		if (i==0 or i==6) :case[0,i].set_ylabel(legende_variable)
#		print type(case[0,i])
#		#case[0,i].get_xaxis().get_major_formatter().set_useOffset(False)
#	case[0,0].annotate(site +'\n'+'Best '+'v='+str(best_version)+'\n'+year_study,xy=(0.01,    0.8), xycoords = 'axes fraction')
#	for i in range(0,4):#for each month
#		min_max='yes'
#		if(name_file_plot=='Albedo' or name_file_plot=='Emissivity') : min_max='no'
#		plot_evolution_boxplot(case[1,i],Var_saison_h_m[i],heure,'',min_T,max_T,do_min_max=min_max)
#		case[1,i].set_xlabel('Time (h)')
#		if (i==0 or i==6) :case[1,i].set_ylabel(legende_variable)
#	case[1,0].annotate(site +'\n'+'Best 0.09+'\n'+year_study,xy=(0.01,    0.8), xycoords = 'axes fraction')
#	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_MORUSES_Best.png',dpi=300)
#	count_figure=count_figure+1







	#plt.show()


#	if with_obs=='yes' :
#		f, case = plt.subplots(2,6, sharex='col', sharey='row',figsize=(18,9))
#		plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)
#		for i in range(0,12):#for each month
#			plot_evolution_boxplot(case[i/6,i%6],Var_h_OBS[i],heure,mois[i],min_T,max_T)
#			if (i>5) : case[i/6,i%6].set_xlabel('Time (h)')
#			if (i==0 or i==6) :case[i/6,i%6].set_ylabel(legende_variable)
#		case[0,0].annotate(site +'\n'+'OBS '+'\n'+year_study,xy=(0.01,    0.8), xycoords = 'axes fraction')
#		f.suptitle('OBS - KC - 2011-2013')
#		if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_OBS_month.png',dpi=300)
#		count_figure=count_figure+1



	###k=2
	###if with_obs=='yes' : split_hour=split_times(float(lat),float(lon),Time_saison[k],Var_saison_OBS[k],Var_saison_b[k],Var_saison_m[k],local_hour)
	###else : split_hour=split_times(float(lat),float(lon),Time_saison[k],[float('nan')]*len(Var_saison_b[k]),Var_saison_b[k],Var_saison_m[k],local_hour)

	####print '********************* transition ************************'
	####for i in range(0,len(split_hour[0])) :  print split_hour[0][i]
	####print '********************* morning ************************'
	####for i in range(0,len(split_hour[1])) :  print split_hour[1][i]
	####print '********************* afternoon ************************'
	####for i in range(0,len(split_hour[2])) :  print split_hour[2][i]
	####print '********************* night ************************'
	####for i in range(0,len(split_hour[3])) :  print split_hour[3][i]


	###print split_hour[14][0:10], len(split_hour[14])
	###print split_hour[6][0:10], len(split_hour[6])
	###print len(split_hour[4]),len(split_hour[0])
	###print len(split_hour[5]),len(split_hour[1])
	###print len(split_hour[6]),len(split_hour[2])
	###print len(split_hour[7]),len(split_hour[3])

	###print len(split_hour[5])+len(split_hour[6])+len(split_hour[7])+len(split_hour[8])
	###print len(split_hour[0])+len(split_hour[1])+len(split_hour[2])+len(split_hour[3])
	###titi=split_hour[14]
	###titi6=split_hour[6]


	####split_hour=split_times(float(lat),float(lon),Time_best2,Var_missing_OBS,Var_best,Var_best2)

	###plt.figure(figsize=(12,6))
	####print len(split_hour[5]),len(split_hour[0])
	###if with_obs=='yes' : plt.scatter(daily_mean(split_hour[4],split_hour[0],val_min=2)[1],daily_mean(split_hour[4],split_hour[0],val_min=2)[0],color='b',label='OBS',marker='+')
	###plt.scatter(daily_mean(split_hour[8],split_hour[0],val_min=2)[1],daily_mean(split_hour[8],split_hour[0],val_min=2)[0],color='k',label='Best 0.18',marker='+')
	###plt.scatter(daily_mean(split_hour[12],split_hour[0],val_min=2)[1],daily_mean(split_hour[12],split_hour[0],val_min=2)[0],color='r',label='Best 0.09',marker='+')
	###plt.title('TRANSITION')
	###plt.legend(loc='best')
	###plt.ylabel(legende_variable)
	####plt.annotate('totot',xy=(0.1,    0.9), xycoords = 'axes fraction')
	###plt.xlabel('Time (day)')

	####plt.show()

	###plt.figure(figsize=(12,6))
	###print len(split_hour[6]),len(split_hour[1])
	###if with_obs=='yes' : plt.scatter(daily_mean(split_hour[5],split_hour[1],val_min=2)[1],daily_mean(split_hour[5],split_hour[1],val_min=2)[0],color='b',label='OBS',marker='+')
	###plt.scatter(daily_mean(split_hour[9],split_hour[1],val_min=2)[1],daily_mean(split_hour[9],split_hour[1],val_min=2)[0],color='k',label='Best',marker='+')
	###plt.scatter(daily_mean(split_hour[13],split_hour[1],val_min=2)[1],daily_mean(split_hour[13],split_hour[1],val_min=2)[0],color='r',label='MORUSES',marker='+')
	###plt.title('MORNING')
	###plt.legend(loc='best')
	###plt.ylabel(legende_variable)
	####plt.annotate('totot',xy=(0.1,    0.9), xycoords = 'axes fraction')
	###plt.xlabel('Time (day)')



	###plt.figure(figsize=(12,6))
	###if with_obs=='yes' : plt.scatter(daily_mean(split_hour[6],split_hour[2],val_min=2)[1],daily_mean(split_hour[6],split_hour[2],val_min=2)[0],color='b',label='OBS',marker='+')
	###plt.scatter(daily_mean(split_hour[10],split_hour[2],val_min=2)[1],daily_mean(split_hour[10],split_hour[2],val_min=2)[0],color='k',label='Best',marker='+')
	###plt.scatter(daily_mean(split_hour[14],split_hour[2],val_min=2)[1],daily_mean(split_hour[14],split_hour[2],val_min=2)[0],color='r',label='MORUSES',marker='+')
	###plt.title('AFTERNOON')
	###plt.legend(loc='best')
	###plt.ylabel(legende_variable)
	####plt.annotate('totot',xy=(0.1,    0.9), xycoords = 'axes fraction')
	###plt.xlabel('Time (day)')



	###plt.figure(figsize=(12,6))
	###if with_obs=='yes' : plt.scatter(daily_mean(split_hour[7],split_hour[3],val_min=2)[1],daily_mean(split_hour[7],split_hour[3],val_min=2)[0],color='b',label='OBS',marker='+')
	###plt.scatter(daily_mean(split_hour[11],split_hour[3],val_min=2)[1],daily_mean(split_hour[11],split_hour[3],val_min=2)[0],color='k',label='Best',marker='+')
	###plt.scatter(daily_mean(split_hour[15],split_hour[3],val_min=2)[1],daily_mean(split_hour[15],split_hour[3],val_min=2)[0],color='r',label='MORUSES',marker='+')
	###plt.title('NIGHT')
	###plt.legend(loc='best')
	###plt.ylabel(legende_variable)
	####plt.annotate('totot',xy=(0.1,    0.9), xycoords = 'axes fraction')
	###plt.xlabel('Time (day)')

	###print 'mean MAE Transition', np.nanmean(abs(np.array(split_hour[12])-np.array(split_hour[4]))),MAE(split_hour[12],split_hour[4])
	###print 'mean MAE Morning', np.nanmean(abs(np.array(split_hour[13])-np.array(split_hour[5]))),MAE(split_hour[13],split_hour[5])
	###print 'mean MAE Afternoon', np.nanmean(abs(np.array(split_hour[14])-np.array(split_hour[6]))),MAE(split_hour[14],split_hour[6])


	###print 'mean MAE Night', np.nanmean(abs(np.array(split_hour[15])-np.array(split_hour[7]))),MAE(split_hour[15],split_hour[7])








	col_labels=[str(model[0])+'-'+str(model[1])+'2',str(model[0])+'-OBS',str(model[1])+'2-OBS',str(model[2])+'3-OBS']
	fig=plt.figure(figsize=(16,6)) #We now want to plot
	ax1 = fig.add_subplot(141)
	plt.subplots_adjust(left=0.05, bottom=0.15, right=0.95, top=None,wspace=0.05, hspace=0.05)
	epaisseur_percentile=0.8
	transparance=0.1
	toto=[0,2,4,8]
	for i in range(0,4):#For each season
		k=i
		fig.add_subplot(141+i)
		plot_line_bloxplot(Var_saison_h_b[i],heure,case_plot=plt,str_color='r',str_label=str(model[0])+'1 '+legende_run[0])
		plot_line_bloxplot(Var_saison_h_m[i],heure,case_plot=plt,str_color='b',str_label=str(model[1])+'2 '+legende_run[1])
		if(third=='yes') : plot_line_bloxplot(Var_saison_h_b3[i],heure,case_plot=plt,str_color='g',str_label=str(model[2])+'3 '+legende_run[2])
		if with_obs=='yes' : plot_line_bloxplot(Var_saison_h_OBS[i],heure,case_plot=plt,str_color='k',str_label='OBS ')
		#table_vals=[MAE_all, MAE_transit, MAE_morning, MAE_afternoon,MAE_night]
		#the_table = plt.table(cellText=table_vals,colWidths = [0.15]*3, rowLabels=row_labels_coef, colLabels=col_labels,loc='lower center')
		plt.xticks(range(0,len(heure)+1),heure+['Mean'],rotation='vertical')
		plt.title(season[i], fontsize=15)
		print (name_file_plot!='Albedo' and name_file_plot!='Emissivity'), name_file_plot
		if(name_file_plot!='Albedo' and name_file_plot!='Emissivity') : 
			print 'NO MAX NO MIN'
			plt.ylim(min_T,max_T)
		#plt.ylim(min_T-1,max_T+1)
		plt.xlabel('Time (h)', fontsize=15)
		if(i==0) : plt.annotate(site +'\n'+year_study+'\n'+'OBS, Best 0.09',xy=(0.01,    0.9), xycoords = 'axes fraction')
		if(i!=0) : plt.yticks([])
		else : 	plt.ylabel(legende_variable, fontsize=15)
	plt.legend(loc='best',fontsize=12)
	print count_figure
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_line.png',dpi=300)
	count_figure=count_figure+1



	split_hour=[]
	split_hour3=[]
	split_hour_SUEWS=[]
	for i in range(0,4):#For each season
		k=i
		#split time
		if with_obs=='yes' : 
			split_hour.append(split_times(float(lat),float(lon),Time_saison[k],Var_saison_OBS[k],Var_saison_b[k],Var_saison_m[k],local_hour))
			if(third=='yes') : split_hour3.append(split_times(float(lat),float(lon),Time_saison[k],Var_saison_OBS[k],Var_saison_b3[k],Var_saison_m[k],local_hour))
			else : split_hour3.append(split_times(float(lat),float(lon),Time_saison[k],Var_saison_OBS[k],[float('nan')]*len(Var_saison_b[k]),Var_saison_m[k],local_hour))
		else : 
			split_hour.append(split_times(float(lat),float(lon),Time_saison[k],[float('nan')]*len(Var_saison_b[k]),Var_saison_b[k],Var_saison_m[k],local_hour))
#		if (with_SUEWS=='yes' and with_obs=='yes') : 
#			split_hour_SUEWS.append(split_times(float(lat),float(lon),Time_saison[k],Var_saison_OBS[k],Var_saison_SUEWS[k],Var_saison_SUEWS[k],local_hour))










	col_labels=[str(model[0])+'-OBS',str(model[1])+'2-OBS',str(model[2])+'3-OBS']
	if (with_SUEWS=='yes' and with_obs=='yes') : col_labels.append('S-OBS')
	fig=plt.figure(figsize=(16,2)) #We now want to plot
	plt.subplots_adjust(left=0.03, bottom=0.01, right=0.97, top=None,wspace=None, hspace=None)
	ax1 = fig.add_subplot(141)
	for i in range(0,4):#For each season
		k=i
		################################################# MAE calculation
		if with_obs=='yes' : 
			MAE_all=[MAE(Var_saison_b[k],Var_saison_OBS[k]),MAE(Var_saison_m[k],Var_saison_OBS[k]),MAE(Var_saison_b3[k],Var_saison_OBS[k])]#,MAE(Var_saison_OBS[k],Var_saison_SUEWS[k])]
			#if (with_SUEWS=='yes' and with_obs=='yes') : MAE_all.append(MAE(Var_saison_OBS[k],Var_saison_SUEWS[k]))
		else :  
			MAE_all=[MAE(Var_saison_b[k],Var_saison_m[k]),'','']
		MAE_night=[MAE(split_hour[i][11],split_hour[i][7]),MAE(split_hour[i][15],split_hour[i][7]),MAE(split_hour3[i][11],split_hour3[i][7])]
		MAE_transit=[MAE(split_hour[i][8],split_hour[i][4]),MAE(split_hour[i][12],split_hour[i][4]),MAE(split_hour3[i][8],split_hour3[i][4])]
		MAE_morning=[MAE(split_hour[i][9],split_hour[i][5]),MAE(split_hour[i][13],split_hour[i][5]),MAE(split_hour3[i][9],split_hour3[i][5])]
		MAE_afternoon=[MAE(split_hour[i][10],split_hour[i][6]),MAE(split_hour[i][14],split_hour[i][6]),MAE(split_hour3[i][10],split_hour3[i][6])]
		ax=fig.add_subplot(141+i)
		table_vals=[MAE_all, MAE_transit, MAE_morning, MAE_afternoon,MAE_night]
		the_table = plt.table(cellText=table_vals,colWidths = [0.20]*len(col_labels), rowLabels=row_labels_coef, colLabels=col_labels,loc='center')
		plt.xticks([])
		plt.annotate(season[i]+' - MAE',xy=(0.2,    0.85), xycoords = 'axes fraction',fontsize=15)
		#plt.title(season[i]+' - MAE')
		#if(i==0) : plt.annotate(site +'\n'+year_study+'\n'+'SUEWS, OBS, MORUSES and Best ',xy=(0.01,    0.9), xycoords = 'axes fraction')
		plt.yticks([])
		ax.axis('off')
	print count_figure
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_MEA.png',dpi=300)
	count_figure=count_figure+1

	print len(split_hour)
	print len(split_hour[i])



	col_labels=[str(model[0])+'-OBS',str(model[1])+'2-OBS',str(model[2])+'3-OBS']
	if (with_SUEWS=='yes' and with_obs=='yes') : col_labels.append('S-OBS')
	fig=plt.figure(figsize=(16,2)) #We now want to plot
	ax1 = fig.add_subplot(141)
	plt.subplots_adjust(left=0.03, bottom=0.01, right=0.97, top=None,wspace=None, hspace=None)
	for i in range(0,4):#For each season
		k=i
		#split time
		#if with_obs=='yes' : 
		#	split_hour=split_times(float(lat),float(lon),Time_saison[k],Var_saison_OBS[k],Var_saison_b[k],Var_saison_m[k],local_hour)
		#else : 
		#	split_hour=split_times(float(lat),float(lon),Time_saison[k],[float('nan')]*len(Var_saison_b[k]),Var_saison_b[k],Var_saison_m[k],local_hour)
		#if (with_SUEWS=='yes' and with_obs=='yes') : 
		#	split_hour_SUEWS=split_times(float(lat),float(lon),Time_saison[k],Var_saison_OBS[k],Var_saison_SUEWS[k],Var_saison_SUEWS[k],local_hour)
		###################################### RMSE calculation
		if with_obs=='yes' : 
			RMSE_all=[RMSE(Var_saison_b[k],Var_saison_OBS[k]),RMSE(Var_saison_m[k],Var_saison_OBS[k]),RMSE(Var_saison_b3[k],Var_saison_OBS[k])]#,RMSE(Var_saison_OBS[k],Var_saison_SUEWS[k])]
			#if (with_SUEWS=='yes' and with_obs=='yes') : RMSE_all.append(RMSE(Var_saison_OBS[k],Var_saison_SUEWS[k]))
		else :  
			RMSE_all=[RMSE(Var_saison_b[k],Var_saison_m[k]),'','']

		RMSE_night=[RMSE(split_hour[i][11],split_hour[i][7]),RMSE(split_hour[i][15],split_hour[i][7]),RMSE(split_hour3[i][11],split_hour3[i][7])]
		#if (with_SUEWS=='yes' and with_obs=='yes') : RMSE_night.append(RMSE(split_hour_SUEWS[i][11],split_hour_SUEWS[i][7]))
		RMSE_transit=[RMSE(split_hour[i][8],split_hour[i][4]),RMSE(split_hour[i][12],split_hour[i][4]),RMSE(split_hour3[i][8],split_hour3[i][4])]
		#if (with_SUEWS=='yes' and with_obs=='yes') : RMSE_transit.append(RMSE(split_hour_SUEWS[i][8],split_hour_SUEWS[i][4]))
		RMSE_morning=[RMSE(split_hour[i][9],split_hour[i][5]),RMSE(split_hour[i][13],split_hour[i][5]),RMSE(split_hour3[i][9],split_hour3[i][5])]
		#if (with_SUEWS=='yes' and with_obs=='yes') : RMSE_morning.append(RMSE(split_hour_SUEWS[i][9],split_hour_SUEWS[i][5]))
		RMSE_afternoon=[RMSE(split_hour[i][10],split_hour[i][6]),RMSE(split_hour[i][14],split_hour[i][6]),RMSE(split_hour3[i][10],split_hour3[i][6])]
		#if (with_SUEWS=='yes' and with_obs=='yes') : RMSE_afternoon.append(RMSE(split_hour_SUEWS[i][10],split_hour_SUEWS[i][6]))
		ax=fig.add_subplot(141+i)
		table_vals=[RMSE_all, RMSE_transit, RMSE_morning, RMSE_afternoon,RMSE_night]
		the_table = plt.table(cellText=table_vals,colWidths = [0.20]*len(col_labels), rowLabels=row_labels_coef, colLabels=col_labels,loc='center')
		plt.xticks([])
		plt.title(season[i]+' - RMSE')
		#if(i==0) : plt.annotate(site +'\n'+year_study+'\n'+'SUEWS, OBS, MORUSES and Best ',xy=(0.01,    0.9), xycoords = 'axes fraction')
		plt.yticks([])
		ax.axis('off')
	print count_figure
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_RMSE.png',dpi=300)
	count_figure=count_figure+1



	#col_labels=['B-B2','B-OBS','B2-OBS']
	if (with_SUEWS=='yes' and with_obs=='yes') : col_labels.append('S-OBS')
	fig=plt.figure(figsize=(16,2)) #We now want to plot
	ax1 = fig.add_subplot(141)
	plt.subplots_adjust(left=0.03, bottom=0.01, right=0.97, top=None,wspace=None, hspace=None)
	for i in range(0,4):#For each season
		k=i
		#split time
		#if with_obs=='yes' : 
		#	split_hour=split_times(float(lat),float(lon),Time_saison[k],Var_saison_OBS[k],Var_saison_b[k],Var_saison_m[k],local_hour)
		#else : 
		#	split_hour=split_times(float(lat),float(lon),Time_saison[k],[float('nan')]*len(Var_saison_b[k]),Var_saison_b[k],Var_saison_m[k],local_hour)
		#if (with_SUEWS=='yes' and with_obs=='yes') : 
		#	split_hour_SUEWS=split_times(float(lat),float(lon),Time_saison[k],Var_saison_OBS[k],Var_saison_SUEWS[k],Var_saison_SUEWS[k],local_hour)
		###################################### Correlation calculation
		if with_obs=='yes' : 
			COR_all=[correlation(Var_saison_b[k],Var_saison_OBS[k],3),correlation(Var_saison_m[k],Var_saison_OBS[k],3),correlation(Var_saison_b3[k],Var_saison_OBS[k])]#,correlation(Var_saison_OBS[k],Var_saison_SUEWS[k])]
			#if (with_SUEWS=='yes' and with_obs=='yes') : COR_all.append(correlation(Var_saison_OBS[k],Var_saison_SUEWS[k]))
		else :  
			COR_all=[correlation(Var_saison_b[k],Var_saison_m[k],3),'','']

		COR_night=[correlation(split_hour[i][11],split_hour[i][7],3),correlation(split_hour[i][15],split_hour[i][7],3),correlation(split_hour3[i][11],split_hour3[i][7],3)]
		#if (with_SUEWS=='yes' and with_obs=='yes') : COR_night.append(correlation(split_hour_SUEWS[i][11],split_hour_SUEWS[i][7]))
		COR_transit=[correlation(split_hour[i][8],split_hour[i][4],3),correlation(split_hour[i][12],split_hour[i][4],3),correlation(split_hour3[i][8],split_hour3[i][4],3)]
		#if (with_SUEWS=='yes' and with_obs=='yes') : COR_transit.append(correlation(split_hour_SUEWS[i][8],split_hour_SUEWS[i][4]))
		COR_morning=[correlation(split_hour[i][9],split_hour[i][5],3),correlation(split_hour[i][13],split_hour[i][5],3),correlation(split_hour3[i][9],split_hour3[i][5],3)]
		#if (with_SUEWS=='yes' and with_obs=='yes') : COR_morning.append(correlation(split_hour_SUEWS[i][9],split_hour_SUEWS[i][5]))
		COR_afternoon=[correlation(split_hour[i][10],split_hour[i][6],3),correlation(split_hour[i][14],split_hour[i][6],3),correlation(split_hour3[i][10],split_hour3[i][6],3)]
		#if (with_SUEWS=='yes' and with_obs=='yes') : COR_afternoon.append(correlation(split_hour_SUEWS[i][10],split_hour_SUEWS[i][6]))
#		if with_obs=='yes' : 
#			COR_all=[correlation(Var_saison_b[k],Var_saison_m[k]),correlation(Var_saison_b[k],Var_saison_OBS[k]),correlation(Var_saison_m[k],Var_saison_OBS[k])]#,MAE(Var_saison_OBS[k],Var_saison_SUEWS[k])]
#			if (with_SUEWS=='yes' and with_obs=='yes') : COR_all.append(correlation(Var_saison_OBS[k],Var_saison_SUEWS[k]))
#		else :  
#			COR_all=[correlation(Var_saison_b[k],Var_saison_m[k]),'','']
#		COR_night=[correlation(split_hour[i][11],split_hour[i][15]),correlation(split_hour[i][11],split_hour[i][7]),correlation(split_hour[i][15],split_hour[i][7])]
#		if (with_SUEWS=='yes' and with_obs=='yes') : COR_night.append(correlation(split_hour_SUEWS[i][11],split_hour_SUEWS[i][7]))
#		COR_transit=[correlation(split_hour[i][8],split_hour[i][12]),correlation(split_hour[i][8],split_hour[i][4]),correlation(split_hour[i][12],split_hour[i][4])]
#		if (with_SUEWS=='yes' and with_obs=='yes') : COR_transit.append(correlation(split_hour_SUEWS[i][8],split_hour_SUEWS[i][4]))
#		COR_morning=[correlation(split_hour[i][9],split_hour[i][13]),correlation(split_hour[i][9],split_hour[i][5]),correlation(split_hour[i][13],split_hour[i][5])]
#		if (with_SUEWS=='yes' and with_obs=='yes') : COR_morning.append(correlation(split_hour_SUEWS[i][9],split_hour_SUEWS[i][5]))
#		COR_afternoon=[correlation(split_hour[i][10],split_hour[i][14]),correlation(split_hour[i][10],split_hour[i][6]),correlation(split_hour[i][14],split_hour[i][6])]
#		if (with_SUEWS=='yes' and with_obs=='yes') : COR_afternoon.append(correlation(split_hour_SUEWS[i][10],split_hour_SUEWS[i][6]))
		#print 'MAE_night ' , MAE_night
		#print 'MAE_transit ' , MAE_transit
		#print 'MAE_morning ' , MAE_morning
		#print 'MAE_afternoon ' , MAE_afternoon
		#print 'MAE_all ' , MAE_all
		ax=fig.add_subplot(141+i)
		table_vals=[COR_all, COR_transit, COR_morning, COR_afternoon,COR_night]
		the_table = plt.table(cellText=table_vals,colWidths = [0.20]*len(col_labels), rowLabels=row_labels_coef, colLabels=col_labels,loc='center')
		plt.xticks([])
		plt.title(season[i]+' - Correlation')
		#fig.suptitle(season[i])
		#ax.set_title('Correlation')
		#if(i==0) : plt.annotate(site +'\n'+year_study+'\n'+'SUEWS, OBS, MORUSES and Best ',xy=(0.01,    0.9), xycoords = 'axes fraction')
		plt.yticks([])
		ax.axis('off')
	print count_figure
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_COR.png',dpi=300)
	count_figure=count_figure+1








	col_labels=[str(model[0])+'-OBS',str(model[1])+'2-OBS',str(model[2])+'3-OBS']
	if (with_SUEWS=='yes' and with_obs=='yes') : col_labels.append('S-OBS')
	fig=plt.figure(figsize=(16,2)) #We now want to plot
	plt.subplots_adjust(left=0.05, bottom=0.01, right=0.95, top=None,wspace=None, hspace=None)
	ax1 = fig.add_subplot(141)
	for i in range(0,4):#For each season
		k=i
		################################################# MAE calculation
		if with_obs=='yes' : 
			MAE_all=[MAE(Var_saison_b[k],Var_saison_OBS[k]),MAE(Var_saison_m[k],Var_saison_OBS[k]),MAE(Var_saison_b3[k],Var_saison_OBS[k])]#,MAE(Var_saison_OBS[k],Var_saison_SUEWS[k])]
			#if (with_SUEWS=='yes' and with_obs=='yes') : MAE_all.append(MAE(Var_saison_OBS[k],Var_saison_SUEWS[k]))
		else :  
			MAE_all=[MAE(Var_saison_b[k],Var_saison_m[k]),'','']
		MAE_night=[MAE(split_hour[i][11],split_hour[i][7]),MAE(split_hour[i][15],split_hour[i][7]),MAE(split_hour3[i][11],split_hour3[i][7])]
		#if (with_SUEWS=='yes' and with_obs=='yes') : MAE_night.append(MAE(split_hour_SUEWS[i][11],split_hour_SUEWS[i][7]))
		MAE_transit=[MAE(split_hour[i][8],split_hour[i][4]),MAE(split_hour[i][12],split_hour[i][4]),MAE(split_hour3[i][8],split_hour3[i][4])]
		#if (with_SUEWS=='yes' and with_obs=='yes') : MAE_transit.append(MAE(split_hour_SUEWS[i][8],split_hour_SUEWS[i][4]))
		MAE_morning=[MAE(split_hour[i][9],split_hour[i][5]),MAE(split_hour[i][13],split_hour[i][5]),MAE(split_hour3[i][9],split_hour3[i][5])]
		#if (with_SUEWS=='yes' and with_obs=='yes') : MAE_morning.append(MAE(split_hour_SUEWS[i][9],split_hour_SUEWS[i][5]))
		MAE_afternoon=[MAE(split_hour[i][10],split_hour[i][6]),MAE(split_hour[i][14],split_hour[i][6]),MAE(split_hour3[i][10],split_hour3[i][6])]
		ax=fig.add_subplot(141+i)
		plt.scatter([1,2,3],[MAE(split_hour[i][4],split_hour[i][8]),MAE(split_hour[i][4],split_hour[i][12]),MAE(split_hour[i][4],split_hour3[i][8])], marker='o',color='g',label='T')
		plt.scatter([1,2,3],[MAE(split_hour[i][5],split_hour[i][9]),MAE(split_hour[i][5],split_hour[i][13]),MAE(split_hour[i][5],split_hour3[i][9])], marker='^',color='r',label='M')
		plt.scatter([1,2,3],[MAE(split_hour[i][6],split_hour[i][10]),MAE(split_hour[i][6],split_hour[i][14]),MAE(split_hour[i][6],split_hour3[i][10])], marker='s',color='b',label='A')
		plt.scatter([1,2,3],[MAE(split_hour[i][7],split_hour[i][11]),MAE(split_hour[i][7],split_hour[i][15]),MAE(split_hour[i][7],split_hour3[i][11])], marker='*',color='grey',label='N')
		plt.scatter([1,2,3],[MAE(Var_saison_b[k],Var_saison_b[k]),MAE(Var_saison_b[k],Var_saison_m[k]),MAE(Var_saison_b[k],Var_saison_b3[k])], marker='.',color='k',label='D')
		plt.xticks([1,2,3],legende_run,rotation='vertical')
		plt.title(season[i]+' - MAE')
	plt.legend(loc='best')
	print count_figure
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_MEA_season.png',dpi=300)
	count_figure=count_figure+1










	#col_labels_N=['B','M','OBS']
	#if (with_SUEWS=='yes') : col_labels_N.append('S')
	#fig=plt.figure(figsize=(16,2)) #We now want to plot
	#ax1 = fig.add_subplot(141)
	#for i in range(0,4):#For each season
	#	k=i
	#	################################################# MAE calculation
	#	if with_obs=='yes' : 
	#		N_all=[len(Var_saison_b[k]),len(Var_saison_m[k]),len(Var_saison_OBS[k])]#,MAE(Var_saison_OBS[k],Var_saison_SUEWS[k])]
	#		if (with_SUEWS=='yes' and with_obs=='yes') : N_all.append(len(Var_saison_SUEWS[k]))
	#	else :  
	#		N_all=[len(Var_saison_b[k]),len(Var_saison_m[k]),'']
	#		if (with_SUEWS=='yes') : N_all.append(len(Var_saison_SUEWS[k]))
	#	N_night=[len(split_hour[i][11]),len(split_hour[i][15]),'']
	#	if with_obs=='yes' :N_night[2]=len(split_hour[i][7])
	#	if with_SUEWS=='yes' :N_night.append(len(split_hour_SUEWS[i][11]))
	#	N_afternoon=[len(split_hour[i][10]),len(split_hour[i][14]),'']
	#	if with_obs=='yes' :N_afternoon[2]=len(split_hour[i][6])
	#	if with_SUEWS=='yes' :N_afternoon.append(len(split_hour_SUEWS[i][10]))
	#	N_morning=[len(split_hour[i][9]),len(split_hour[i][13]),'']
	#	if with_obs=='yes' :N_morning[2]=len(split_hour[i][5])
	#	if with_SUEWS=='yes' :N_morning.append(len(split_hour_SUEWS[i][9]))
	#	N_transit=[len(split_hour[i][8]),len(split_hour[i][12]),'']
	#	if with_obs=='yes' :N_transit[2]=len(split_hour[i][4])
	#	if with_SUEWS=='yes' :N_transit.append(len(split_hour_SUEWS[i][8]))
	#	ax=fig.add_subplot(141+i)
	#	table_vals=[N_all, N_transit, N_morning, N_afternoon,N_night]
	#	print len (table_vals), len (col_labels_N),len(row_labels_coef),len(table_vals[1])
	#	the_table = plt.table(cellText=table_vals,colWidths = [0.20]*len(col_labels_N), rowLabels=row_labels_coef, colLabels=col_labels,loc='center')
	#	plt.xticks([])
	#	plt.title(season[i]+' - N')
	#	#if(i==0) : plt.annotate(site +'\n'+year_study+'\n'+'SUEWS, OBS, MORUSES and Best ',xy=(0.01,    0.9), xycoords = 'axes fraction')
	#	plt.yticks([])
	#	ax.axis('off')
	#print count_figure
	##if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_MEA.png',dpi=300)
	##count_figure=count_figure+1


	#np.isnan(np.array(Var_saison_b[k])).sum()
	#np.isnan(np.array(split_hour[i][11])).sum()

	#col_labels_N=['B','M','OBS']
	#if (with_SUEWS=='yes' and with_obs=='yes') : col_labels_N.append('S')
	#fig=plt.figure(figsize=(16,2)) #We now want to plot
	#ax1 = fig.add_subplot(141)
	#for i in range(0,4):#For each season
	#	k=i
	#	################################################# MAE calculation
	#	if with_obs=='yes' : 
	#		N_all=[np.isnan(np.array(Var_saison_b[k])).sum(),np.isnan(np.array(Var_saison_m[k])).sum(),np.isnan(np.array(Var_saison_OBS[k])).sum()]#,MAE(Var_saison_OBS[k],Var_saison_SUEWS[k])]
	#		if (with_SUEWS=='yes' and with_obs=='yes') : N_all.append(np.isnan(np.array(Var_saison_SUEWS[k])).sum())
	#	else :  
	#		N_all=[np.isnan(np.array(Var_saison_b[k])).sum(),np.isnan(np.array(Var_saison_m[k])).sum(),'']
	#		if (with_SUEWS=='yes') : N_all.append(np.isnan(np.array(Var_saison_SUEWS[k])).sum())
	#	print np.isnan(np.array(split_hour[i][11]))
	#	N_night=[np.isnan(np.array(split_hour[i][11])).sum(),np.isnan(np.array(split_hour[i][15])).sum(),'']
	#	if with_obs=='yes' :N_night[2]=np.isnan(np.array(split_hour[i][7])).sum()
	#	if with_SUEWS=='yes' :N_night.append(np.isnan(np.array(split_hour_SUEWS[i][11])).sum())
	#	N_afternoon=[np.isnan(np.array(split_hour[i][10])).sum(),np.isnan(np.array(split_hour[i][14])).sum(),'']
	#	print [np.isnan(np.array(split_hour[i][10])).sum(),np.isnan(np.array(split_hour[i][14])).sum(),'']
	#	print len(N_afternoon)
	#	if with_obs=='yes' :N_afternoon[2]=np.isnan(np.array(split_hour[i][6])).sum()
	#	print len(N_afternoon)
	#	if with_SUEWS=='yes' :N_afternoon.append(np.isnan(np.array(split_hour_SUEWS[i][10])).sum())
	#	print len(N_afternoon)
	#	N_morning=[np.isnan(np.array(split_hour[i][9])).sum(),np.isnan(np.array(split_hour[i][13])).sum(),'']
	#	if with_obs=='yes' :N_morning[2]=np.isnan(np.array(split_hour[i][5])).sum()
	#	if with_SUEWS=='yes' :N_morning.append(np.isnan(np.array(split_hour_SUEWS[i][9])).sum())
	#	N_transit=[np.isnan(np.array(split_hour[i][11])).sum(),np.isnan(np.array(split_hour[i][15])).sum(),'']
	#	if with_obs=='yes' :N_transit[2]=np.isnan(np.array(split_hour[i][4])).sum()
	#	if with_SUEWS=='yes' :N_transit.append(np.isnan(np.array(split_hour_SUEWS[i][11])).sum())
	#	ax=fig.add_subplot(141+i)
	#	table_vals=[N_all, N_transit, N_morning, N_afternoon,N_night]
	#	print len (table_vals), len (col_labels_N),len(row_labels_coef),len(table_vals[1]),len(table_vals[0]),len(table_vals[3]),len(table_vals[1]),len(table_vals[4])
	#	the_table = plt.table(cellText=table_vals,colWidths = [0.20]*len(col_labels_N), rowLabels=row_labels_coef, colLabels=col_labels,loc='center')
	#	plt.xticks([])
	#	plt.title(season[i]+' - N')
	#	#if(i==0) : plt.annotate(site +'\n'+year_study+'\n'+'SUEWS, OBS, MORUSES and Best ',xy=(0.01,    0.9), xycoords = 'axes fraction')
	#	plt.yticks([])
	#	ax.axis('off')
	#print count_figure
	##if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_MEA.png',dpi=300)
	##count_figure=count_figure+1


#	col_labels_N=['B 0.18','B 0.09','OBS']
#	if (with_SUEWS=='yes' and with_obs=='yes') : col_labels_N.append('S')
#	fig=plt.figure(figsize=(16,2)) #We now want to plot
#	ax1 = fig.add_subplot(141)
#	for i in range(0,4):#For each season
#		k=i
#		################################################# MAE calculation
#		if with_obs=='yes' : 
#			N_all=[len(Var_saison_b[k])-np.isnan(np.array(Var_saison_b[k])).sum(),len(Var_saison_m[k])-np.isnan(np.array(Var_saison_m[k])).sum(),len(Var_saison_OBS[k])-np.isnan(np.array(Var_saison_OBS[k])).sum()]#,MAE(Var_saison_OBS[k],Var_saison_SUEWS[k])]
#			if (with_SUEWS=='yes' and with_obs=='yes') : N_all.append(len(Var_saison_SUEWS[k])-np.isnan(np.array(Var_saison_SUEWS[k])).sum())
#		else :  
#			N_all=[len(Var_saison_b[k])-np.isnan(np.array(Var_saison_b[k])).sum(),len(Var_saison_m[k])-np.isnan(np.array(Var_saison_m[k])).sum(),'']
#			if (with_SUEWS=='yes') : N_all.append(len(Var_saison_SUEWS[k])-np.isnan(np.array(Var_saison_SUEWS[k])).sum())
#		N_night=[len(split_hour[i][11])-np.isnan(np.array(split_hour[i][11])).sum(),len(split_hour[i][15])-np.isnan(np.array(split_hour[i][15])).sum(),'']
#		if with_obs=='yes' :N_night[2]=len(split_hour[i][7])-np.isnan(np.array(split_hour[i][7])).sum()
#		if with_SUEWS=='yes' :N_night.append(len(split_hour_SUEWS[i][11])-np.isnan(np.array(split_hour_SUEWS[i][11])).sum())
#		N_afternoon=[len(split_hour[i][10])-np.isnan(np.array(split_hour[i][10])).sum(),len(split_hour[i][14])-np.isnan(np.array(split_hour[i][14])).sum(),'']
#		if with_obs=='yes' :N_afternoon[2]=len(split_hour[i][6])-np.isnan(np.array(split_hour[i][6])).sum()
#		if with_SUEWS=='yes' :N_afternoon.append(len(split_hour_SUEWS[i][10])-np.isnan(np.array(split_hour[i][10])).sum())
#		N_morning=[len(split_hour[i][9])-np.isnan(np.array(split_hour[i][9])).sum(),len(split_hour[i][13])-np.isnan(np.array(split_hour[i][13])).sum(),'']
#		if with_obs=='yes' :N_morning[2]=len(split_hour[i][5])-np.isnan(np.array(split_hour[i][5])).sum()
#		if with_SUEWS=='yes' :N_morning.append(len(split_hour_SUEWS[i][9])-np.isnan(np.array(split_hour[i][9])).sum())
#		N_transit=[len(split_hour[i][8])-np.isnan(np.array(split_hour[i][8])).sum(),len(split_hour[i][12])-np.isnan(np.array(split_hour[i][12])).sum(),'']
#		if with_obs=='yes' :N_transit[2]=len(split_hour[i][4])-np.isnan(np.array(split_hour[i][4])).sum()
#		if with_SUEWS=='yes' :N_transit.append(len(split_hour_SUEWS[i][8])-np.isnan(np.array(split_hour[i][8])).sum())
#		ax=fig.add_subplot(141+i)
#		table_vals=[N_all, N_transit, N_morning, N_afternoon,N_night]
#		the_table = plt.table(cellText=table_vals,colWidths = [0.20]*len(col_labels_N), rowLabels=row_labels_coef, colLabels=col_labels_N,loc='center')
#		plt.xticks([])
#		plt.title(season[i]+' - N')
#		#if(i==0) : plt.annotate(site +'\n'+year_study+'\n'+'SUEWS, OBS, MORUSES and Best ',xy=(0.01,    0.9), xycoords = 'axes fraction')
#		plt.yticks([])
#		ax.axis('off')
#	print count_figure
#	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_N.png',dpi=300)
#	count_figure=count_figure+1


#	############################################
#	########### Distribution

#	#fig=plt.figure(figsize=(10,6))
#	couleur=['b','orange','g','r']
#	f, case = plt.subplots(1,3, sharex='col', sharey='row',figsize=(17,7))
#	for i in range(0,4):
#		print int(min_T)
#		print int(max_T)
#	#	case[0].hist(remove_nanVar_saison_OBS[i]),histtype = 'step', normed=1,label=season[i],color=couleur[i])
#	#	if with_obs=='yes' : case[0].hist(remove_nan(Var_saison_OBS)[i],histtype = 'step', normed=1,bins=range(-200,500,20),label=season[i])
#	#	case[1].hist(Var_saison_b[i],histtype = 'step', normed=1,bins=range(-200,500,20),label=season[i])
#	#	case[2].hist(Var_saison_m[i],histtype = 'step', normed=1,bins=range(-200,500,20),label=season[i])
#		if with_obs=='yes' : case[0].hist(remove_nan(Var_saison_OBS)[i],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label=season[i])
#		case[1].hist(Var_saison_b[i],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label=season[i])
#		case[2].hist(Var_saison_m[i],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label=season[i])
#		case[1].set_xlabel(legende_variable)
#		case[2].set_xlabel(legende_variable)
#		case[0].set_xlabel(legende_variable)
#	#plt.xlim(min_T-1,max_T+1)
#	case[0].annotate(site +'\n'+'OBS \n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
#	case[1].annotate(site +'\n'+'Best 0.09 '+'\n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
#	case[2].annotate(site +'\n'+'Best 0.18'+'v='+str(best_version)+'\n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
#	plt.xlabel(legende_variable)
#	plt.legend()
#	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_hist_season.png',dpi=300)
#	count_figure=count_figure+1

#	if with_SUEWS=='yes' :
#		fig=plt.figure(figsize=(4,6))
#		couleur=['b','orange','g','r']
#		for i in range(0,4):
#			plt.hist(Var_saison_SUEWS[i],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label=season[i])
#		plt.xlabel(legende_variable)
#		plt.annotate(site +'\n'+'SUEWS \n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
#		plt.legend()
#		if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_hist_season_SUEWS.png',dpi=300)
#		count_figure=count_figure+1




	print count_figure


	f, case = plt.subplots(4,8, sharex='col', sharey='row',figsize=(18,9))
	plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
	for i in range(0,4):
		for j in range(0,len(heure_3h)) :
	#		if with_obs=='yes' : case[i,j].hist(remove_nan(Var_saison_3h_OBS[i])[j],histtype = 'step', normed=1,bins=range(-200,500,20),label='OBS')
	#		case[i,j].hist(remove_nan(Var_saison_3h_b[i])[j],histtype = 'step', normed=1,bins=range(-200,500,20),label='B')
	#		case[i,j].hist(remove_nan(Var_saison_3h_m[i])[j],histtype = 'step', normed=1,bins=range(-200,500,20),label='M')
			if with_obs=='yes' : case[i,j].hist(remove_nan(Var_saison_3h_OBS[i])[j], normed=1,bins=20, range=(centile_1,centile_99), fc=(0, 0, 0, 0.35))
			if with_obs=='yes' : case[i,j].hist(remove_nan(Var_saison_3h_OBS[i])[j],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label='OBS',color='k')
			if with_SUEWS=='yes' : case[i,j].hist(remove_nan(Var_saison_3h_SUEWS[i])[j], normed=1,bins=20, range=(centile_1,centile_99), fc=(0, 1., 0, 0.35))
			if with_SUEWS=='yes' : case[i,j].hist(remove_nan(Var_saison_3h_SUEWS[i])[j],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label='SUEWS',color='g')
			if(third=='yes') :
				case[i,j].hist(remove_nan(Var_saison_3h_b3[i])[j], normed=1,bins=20, range=(centile_1,centile_99), fc=(0, 1., 0, 0.35))
				case[i,j].hist(remove_nan(Var_saison_3h_b3[i])[j],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label=str(model[0])+'1',color='g')
			case[i,j].hist(remove_nan(Var_saison_3h_b[i])[j], normed=1,bins=20, range=(centile_1,centile_99), fc=(1, 0, 0, 0.35))
			case[i,j].hist(remove_nan(Var_saison_3h_b[i])[j],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label=str(model[0])+'1',color='r')
			case[i,j].hist(remove_nan(Var_saison_3h_m[i])[j], normed=1,bins=20, range=(centile_1,centile_99), fc=(0, 0, 1, 0.35))
			case[i,j].hist(remove_nan(Var_saison_3h_m[i])[j],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label=str(model[1])+'2',color='b')
			case[i,0].set_ylabel(season[i])
			case[0,j].set_title(heure_3h[j])
			case[3,j].set_xlabel(legende_variable)
	case[0,(len(heure_3h)-1)].legend()
	f.suptitle(site+' '+year_study+' SUEwS OBS '+' '+str(model[1])+' v='+str(best2_version)+str(model[0])+' v='+str(best_version),fontsize=14)
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_hist_hour_season_SUEWS.png',dpi=300)
	count_figure=count_figure+1

	print count_figure


	print 'done', legende_variable


print Var_best2.mean()
print Var_best.mean()

print 'done'
plt.show()
