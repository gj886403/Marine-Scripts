#!/usr/bin/python
# -*- coding: utf8 -*-

from fonction import *
from jules_download import *
from Split_times_Marine import *

from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

save_plot='yes'
version_plot='' #OBS and AnthroOff

var=['SW_up','QH','Q_star','K_star','K_down','L_up','L_down']
var=['SW_up','QH','Q_star','L_up']
#var=['QH']
#var=['Emissivity']
#var=['Tsurf']

#var=['Tsoil']
#level=0

#legende_run=['C=2.8E5','C=2.E5','C=1.E5']
#legende_run=['C=2.8E5','C=2.E5','C=3.5E5']
legende_run=[r'$ \alpha = 0.18 $ ',r'$ \alpha = 0.09 $ ',r'$ \alpha = 0.11 $ ']
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

	best_folder='/storage/shared/research/met/micromet/JULES/u-av588_1-tile_London_KSSW/76913/'
	best3_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/7_best_albedo11_C28_anthroON/'
	best2_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/3_best_albedo09_C28_anthroON/'

#	best_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/7_best_albedo11_C28_anthroON/'
	best6_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/9_best_albedo11_C1_anthropoON/'
	best5_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/10_best_albedo11_C35_anthropoON/'
	best4_folder='/storage/shared/research/met/micromet/JULES/Marine/JULES_run/8_best_albedo11_c2_anthroON/'
	best0_folder='/storage/shared/research/met/micromet/JULES/u-av588_1-tile_London_KSSW/76922/'

	moruses0_folder='/storage/shared/research/met/micromet/JULES/u-av612_MORUSES_London_KSSW/76930/'
	moruses1_folder='/storage/shared/research/met/micromet/JULES/u-av612_MORUSES_London_KSSW/76956/'

	obs_folder='/storage/shared/research/met/micromet/JULES/SUEWSEvaluationData/Kc/Obs/'
	local_time='Europe/London'
	Start= datetime.datetime(2011, 01, 01,00,00,00)
	year_study='2011-2013'
	year_study_short='11-13'
	#with_obs='yes'
	local_hour=0
	if (var_i!='Emissivity' and var_i!='Albedo' and var_i!='Tsurf' and var_i!='Tsoil') : with_obs='yes'
	with_SUEWS='no'


	
	save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/Compare_Best/'# Anthropogenic Flux OFF
	#best2_version=76930# Anthropogenic Flux OFF
	#best_version=76922# Anthropogenic Flux OFF




	########################## JULES

	Var_best2=jules_download(best2_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
	#print best_folder+str(best_version)+'/jules.all.nc'
	#Var_best=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_best=jules_download(best_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_best3=jules_download(best3_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_best4=jules_download(best4_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_best5=jules_download(best5_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_best6=jules_download(best6_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_best0=jules_download(best0_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_moruses0=jules_download(moruses0_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
	Var_moruses1=jules_download(moruses1_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
	print type(Var_best2)
	print Var_best2.shape
	print Var_best.shape

	if(name_file_plot=='AnthroOn_SW_up' or name_file_plot=='SW_up'):
		Var_best3_1=jules_download(best3_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_best4_1=jules_download(best4_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_best5_1=jules_download(best5_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_best6_1=jules_download(best6_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_best0_1=jules_download(best0_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_best2_1=jules_download(best2_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_moruses0_1=jules_download(moruses0_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_moruses1_1=jules_download(moruses1_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
		#Var_best_1=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_best_1=jules_download(best_folder+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_best2_2=jules_download(best2_folder+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_best3_2=jules_download(best3_folder+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_best4_2=jules_download(best4_folder+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_best5_2=jules_download(best5_folder+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_best6_2=jules_download(best6_folder+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_best0_2=jules_download(best0_folder+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_moruses0_2=jules_download(moruses0_folder+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_moruses1_2=jules_download(moruses1_folder+'/jules.all.nc',name_variable_JULES2,Start)[0]
		#Var_best_2=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_best_2=jules_download(best_folder+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_best2=Var_best2_2-Var_best2_1
		Var_best3=Var_best3_2-Var_best3_1
		Var_best4=Var_best4_2-Var_best4_1
		Var_best5=Var_best5_2-Var_best5_1
		Var_best6=Var_best6_2-Var_best6_1
		Var_best0=Var_best0_2-Var_best0_1
		Var_moruses0=Var_moruses0_2-Var_moruses0_1
		Var_moruses1=Var_moruses1_2-Var_moruses1_1
		Var_best=Var_best_2-Var_best_1
	elif(var_i=='Tsoil') :
		Var_best2=Var_best2[:,level]
		Var_best3=Var_best3[:,level]
		Var_best4=Var_best4[:,level]
		Var_best5=Var_best5[:,level]
		Var_best6=Var_best6[:,level]
		Var_best0=Var_best0[:,level]
		Var_moruses0=Var_moruses0[:,level]
		Var_moruses1=Var_moruses1[:,level]
		Var_best=Var_best[:,level]

	#print type(Var_best2)
	#print Var_best2.shape

	Time_best2=jules_download(best2_folder+'/jules.all.nc',name_variable_JULES,Start)[1]
	Time_best3=jules_download(best3_folder+'/jules.all.nc',name_variable_JULES,Start)[1]
	Time_best4=jules_download(best4_folder+'/jules.all.nc',name_variable_JULES,Start)[1]
	Time_best5=jules_download(best5_folder+'/jules.all.nc',name_variable_JULES,Start)[1]
	Time_best6=jules_download(best6_folder+'/jules.all.nc',name_variable_JULES,Start)[1]
	Time_best0=jules_download(best0_folder+'/jules.all.nc',name_variable_JULES,Start)[1]
	Time_moruses0=jules_download(moruses0_folder+'/jules.all.nc',name_variable_JULES,Start)[1]
	Time_moruses1=jules_download(moruses0_folder+'/jules.all.nc',name_variable_JULES,Start)[1]
	if(local_time!='Europe/London') : 
		Time_best2=convert_UTC_to_local(Time_best2,local_time)
		Time_best3=convert_UTC_to_local(Time_best3,local_time)
	Time_best=jules_download(best_folder+'/jules.all.nc',name_variable_JULES,Start)[1]
	if(local_time!='Europe/London') : Time_best=convert_UTC_to_local(Time_best,local_time)

	lon=jules_download(best2_folder+'/jules.all.nc','longitude',Start)[0]
	lat=jules_download(best2_folder+'/jules.all.nc','latitude',Start)[0]

	if  (Time_best2!=Time_best) : print 'Best2 and Best are not the same size'
	print 'lon',lon,'lat',lat



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


	if with_obs=='yes' : Var_saison_OBS=divide_periode_day('season',Var_missing_OBS,Time_best2)
	Var_saison_m=divide_periode_day('season',Var_best2,Time_best2)
	Var_saison_b=divide_periode_day('season',Var_best,Time_best2)
	Var_saison_b3=divide_periode_day('season',Var_best3,Time_best2)
	Var_saison_b4=divide_periode_day('season',Var_best4,Time_best2)
	Var_saison_b5=divide_periode_day('season',Var_best5,Time_best2)
	Var_saison_b6=divide_periode_day('season',Var_best6,Time_best2)
	Var_saison_b0=divide_periode_day('season',Var_best0,Time_best2)
	Var_saison_m0=divide_periode_day('season',Var_moruses0,Time_best2)
	Var_saison_m1=divide_periode_day('season',Var_moruses1,Time_best2)
	Time_saison=divide_periode_day('season',Time_best2,Time_best2)

	if with_obs=='yes' : Var_saison_3h_OBS=divide_periode_day('season',Var_missing_OBS,Time_best2,which_day=3)
	Var_saison_3h_b=divide_periode_day('season',Var_best,Time_best2,which_day=3)
	Var_saison_3h_b3=divide_periode_day('season',Var_best3,Time_best2,which_day=3)
	Var_saison_3h_b4=divide_periode_day('season',Var_best4,Time_best2,which_day=3)
	Var_saison_3h_b5=divide_periode_day('season',Var_best5,Time_best2,which_day=3)
	Var_saison_3h_b6=divide_periode_day('season',Var_best6,Time_best2,which_day=3)
	Var_saison_3h_b0=divide_periode_day('season',Var_best0,Time_best2,which_day=3)
	Var_saison_3h_m0=divide_periode_day('season',Var_moruses0,Time_best2,which_day=3)
	Var_saison_3h_m1=divide_periode_day('season',Var_moruses1,Time_best2,which_day=3)
	Var_saison_3h_m=divide_periode_day('season',Var_best2,Time_best2,which_day=3)
	Time_saison_3h=divide_periode_day('season',Time_best2,Time_best2,which_day=3)

	if with_obs=='yes' : Var_saison_h_OBS=divide_periode_day('season',Var_missing_OBS,Time_best2,which_day=1)
	Var_saison_h_b=divide_periode_day('season',Var_best,Time_best2,which_day=1)
	Var_saison_h_b3=divide_periode_day('season',Var_best3,Time_best2,which_day=1)
	Var_saison_h_b4=divide_periode_day('season',Var_best4,Time_best2,which_day=1)
	Var_saison_h_b5=divide_periode_day('season',Var_best5,Time_best2,which_day=1)
	Var_saison_h_b6=divide_periode_day('season',Var_best6,Time_best2,which_day=1)
	Var_saison_h_b0=divide_periode_day('season',Var_best0,Time_best2,which_day=1)
	Var_saison_h_m0=divide_periode_day('season',Var_moruses0,Time_best2,which_day=1)
	Var_saison_h_m1=divide_periode_day('season',Var_moruses1,Time_best2,which_day=1)
	Var_saison_h_m=divide_periode_day('season',Var_best2,Time_best2,which_day=1)
	#Time_saison_h=divide_periode_day('season',Time_JULES,Time_JULES,which_day=1)

	if with_obs=='yes' : Var_h_OBS=divide_periode_day('month',Var_missing_OBS,Time_best2,which_day=1)

	if with_obs=='yes' : Var_all_h_OBS=divide_periode_day('all',Var_missing_OBS,Time_best2,which_day=1)
	Var_all_h_b=divide_periode_day('all',Var_best,Time_best2,which_day=1)
	Var_all_h_b3=divide_periode_day('all',Var_best3,Time_best2,which_day=1)
	Var_all_h_b4=divide_periode_day('all',Var_best4,Time_best2,which_day=1)
	Var_all_h_b5=divide_periode_day('all',Var_best5,Time_best2,which_day=1)
	Var_all_h_b6=divide_periode_day('all',Var_best6,Time_best2,which_day=1)
	Var_all_h_b0=divide_periode_day('all',Var_best0,Time_best2,which_day=1)
	Var_all_h_m0=divide_periode_day('all',Var_moruses0,Time_best2,which_day=1)
	Var_all_h_m1=divide_periode_day('all',Var_moruses1,Time_best2,which_day=1)
	Var_all_h_m=divide_periode_day('all',Var_best2,Time_best2,which_day=1)




	split_hour_all=split_times(float(lat),float(lon),Time_best2,Var_missing_OBS,Var_best,Var_best2,local_hour)
	if(third=='yes') :split_hour3_all=split_times(float(lat),float(lon),Time_best2,Var_best3,Var_best4,Var_best5,local_hour)
	if(third=='yes') :split_hour4_all=split_times(float(lat),float(lon),Time_best2,Var_best6,Var_best0,Var_moruses0,local_hour)
	if(third=='yes') :split_hour5_all=split_times(float(lat),float(lon),Time_best2,Var_moruses1,Var_moruses1,Var_moruses1,local_hour)

	plt.figure()
	plt.plot([0,1,2,3,4,5,6],[MAE(split_hour_all[4],split_hour4_all[8]),MAE(split_hour_all[4],split_hour_all[8]),MAE(split_hour_all[4],split_hour_all[12]),MAE(split_hour_all[4],split_hour3_all[4]),MAE(split_hour_all[4],split_hour3_all[8]),MAE(split_hour_all[4],split_hour3_all[12]),MAE(split_hour_all[4],split_hour4_all[4])], marker='o',color='g',label='T', linestyle=':')

	plt.scatter([-2,-1],[MAE(split_hour_all[4],split_hour4_all[12]),MAE(split_hour_all[4],split_hour5_all[4])], marker='o',facecolors='none', edgecolors='g')



	plt.plot([0,1,2,3,4,5,6],[MAE(split_hour_all[5],split_hour4_all[9]),MAE(split_hour_all[5],split_hour_all[9]),MAE(split_hour_all[5],split_hour_all[13]),MAE(split_hour_all[5],split_hour3_all[5]),MAE(split_hour_all[5],split_hour3_all[9]),MAE(split_hour_all[5],split_hour3_all[13]),MAE(split_hour_all[5],split_hour4_all[5])], marker='^',color='r',label='M', linestyle=':')
	plt.scatter([-2,-1],[MAE(split_hour_all[5],split_hour4_all[13]),MAE(split_hour_all[5],split_hour5_all[5])], marker='^', facecolors='none', edgecolors='r')

	plt.plot([0,1,2,3,4,5,6],[MAE(split_hour_all[6],split_hour4_all[10]),MAE(split_hour_all[6],split_hour_all[10]),MAE(split_hour_all[6],split_hour_all[14]),MAE(split_hour_all[6],split_hour3_all[6]),MAE(split_hour_all[6],split_hour3_all[10]),MAE(split_hour_all[6],split_hour3_all[14]),MAE(split_hour_all[6],split_hour4_all[6])], marker='s',color='b',label='A', linestyle=':')
	plt.scatter([-2,-1],[MAE(split_hour_all[6],split_hour4_all[14]),MAE(split_hour_all[6],split_hour5_all[6])], marker='s', facecolors='none', edgecolors='b')

	plt.plot([0,1,2,3,4,5,6],[MAE(split_hour_all[7],split_hour4_all[11]),MAE(split_hour_all[7],split_hour_all[11]),MAE(split_hour_all[7],split_hour_all[15]),MAE(split_hour_all[7],split_hour3_all[7]),MAE(split_hour_all[7],split_hour3_all[11]),MAE(split_hour_all[7],split_hour3_all[15]),MAE(split_hour_all[7],split_hour4_all[7])], marker='*',color='grey',label='N', linestyle=':')
	plt.scatter([-2,-1],[MAE(split_hour_all[7],split_hour4_all[15]),MAE(split_hour_all[7],split_hour5_all[7])], marker='*', facecolors='none', edgecolors='grey')

	plt.plot([0,1,2,3,4,5,6],[MAE(Var_missing_OBS,Var_best0),MAE(Var_missing_OBS,Var_best),MAE(Var_missing_OBS,Var_best2),MAE(Var_missing_OBS,Var_best3),MAE(Var_missing_OBS,Var_best4),MAE(Var_missing_OBS,Var_best5),MAE(Var_missing_OBS,Var_best6)],marker='.',color='k',label='24h', linestyle=':')

	plt.scatter([-2,-1],[MAE(Var_missing_OBS,Var_moruses0),MAE(Var_missing_OBS,Var_moruses1)],facecolors='none', edgecolors='k')

	plt.grid(True)
	plt.legend(loc='best')
	plt.xticks([-2,-1,0,1,2,3,4,5,6],['M0','M1','B0','B1','B2','B3','B4','B5','B6'])
	plt.suptitle(legende_variable)
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_MAE_year.png',dpi=300)
	#plt.show()








	#####################Usefull information
	vect_all=[Var_best,Var_best2,Var_best3]
	if with_obs=='yes' : vect_all.append(Var_missing_OBS)
	centile_99=float(np.nanpercentile(np.array(vect_all),99))
	centile_1=float(np.nanpercentile(np.array(vect_all),1))

	max_T=max([Var_best.max(),Var_best2.max(),Var_best3.max()])
	min_T=min([Var_best.min(),Var_best2.min(),Var_best3.min()])
	if with_obs=='yes' : 
		max_T=max([max_T,max(Var_missing_OBS)])
		min_T=min([min_T,min(Var_missing_OBS)])

	position_title=max_T-(max_T-min_T)*0.10

	#plt.figure()
	#plt.show()

	heure_3h=['0h','3h','6h','9h','12h','15h','18h','21h']
	mois=['J','F','M','A','M','J','J','A','S','O','N','D']
	season=['Winter DJF','Spring MAM','Summer JJA','Autumn SON']
	heure=['']*24
	for i in range(0,len(heure)):
		if (i%3==0) : heure[i]=str(i)
	row_labels_coef=['24h','T','M','A','N']
	count_figure=1



	#plt.figure()
	#plt.show()

####################################################################################################################################

	split_hour=[]
	split_hour3=[]
	split_hour4=[]
	split_hour5=[]
	split_hour_SUEWS=[]
	for i in range(0,4):#For each season
		k=i
		#split time
		if with_obs=='yes' : 
			split_hour.append(split_times(float(lat),float(lon),Time_saison[k],Var_saison_OBS[k],Var_saison_b[k],Var_saison_m[k],local_hour))
			split_hour3.append(split_times(float(lat),float(lon),Time_saison[k],Var_saison_b3[k],Var_saison_b4[k],Var_saison_b5[k],local_hour))
			split_hour4.append(split_times(float(lat),float(lon),Time_saison[k],Var_saison_b6[k],Var_saison_b0[k],Var_saison_m0[k],local_hour))
			split_hour5.append(split_times(float(lat),float(lon),Time_saison[k],Var_saison_m1[k],Var_saison_m1[k],Var_saison_m1[k],local_hour))
		else : 
			split_hour.append(split_times(float(lat),float(lon),Time_saison[k],[float('nan')]*len(Var_saison_b[k]),Var_saison_b[k],Var_saison_m[k],local_hour))
#		if (with_SUEWS=='yes' and with_obs=='yes') : 
#			split_hour_SUEWS.append(split_times(float(lat),float(lon),Time_saison[k],Var_saison_OBS[k],Var_saison_SUEWS[k],Var_saison_SUEWS[k],local_hour))






	col_labels=[str(model[0])+'-OBS',str(model[1])+'2-OBS',str(model[2])+'3-OBS']
	if (with_SUEWS=='yes' and with_obs=='yes') : col_labels.append('S-OBS')
	fig=plt.figure(figsize=(16,2)) #We now want to plot
	plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=None, hspace=None)
	ax1 = fig.add_subplot(141)
	for i in range(0,4):#For each season
		k=i
		################################################# MAE calculation
		if with_obs=='yes' : 
			MAE_all=[MAE(Var_saison_b0[k],Var_saison_OBS[k]),MAE(Var_saison_b[k],Var_saison_OBS[k]),MAE(Var_saison_m[k],Var_saison_OBS[k]),MAE(Var_saison_b3[k],Var_saison_OBS[k]),MAE(Var_saison_b4[k],Var_saison_OBS[k]),MAE(Var_saison_b5[k],Var_saison_OBS[k]),MAE(Var_saison_b6[k],Var_saison_OBS[k])]#,MAE(Var_saison_OBS[k],Var_saison_SUEWS[k])]
			MAE_all_m=[MAE(Var_saison_m0[k],Var_saison_OBS[k]),MAE(Var_saison_m1[k],Var_saison_OBS[k])]
			#if (with_SUEWS=='yes' and with_obs=='yes') : MAE_all.append(MAE(Var_saison_OBS[k],Var_saison_SUEWS[k]))
		else :  
			MAE_all=[MAE(Var_saison_b[k],Var_saison_m[k]),'','']
		MAE_transit=[MAE(split_hour4[i][8],split_hour[i][4]),MAE(split_hour[i][8],split_hour[i][4]),MAE(split_hour[i][12],split_hour[i][4]),MAE(split_hour3[i][4],split_hour[i][4]),MAE(split_hour3[i][8],split_hour[i][4]),MAE(split_hour3[i][12],split_hour[i][4]),MAE(split_hour4[i][4],split_hour[i][4])]
		MAE_transit_m=[MAE(split_hour4[i][12],split_hour[i][4]),MAE(split_hour5[i][4],split_hour[i][4])]
		MAE_morning=[MAE(split_hour4[i][9],split_hour[i][5]),MAE(split_hour[i][9],split_hour[i][5]),MAE(split_hour[i][13],split_hour[i][5]),MAE(split_hour3[i][5],split_hour[i][5]),MAE(split_hour3[i][9],split_hour[i][5]),MAE(split_hour3[i][13],split_hour[i][5]),MAE(split_hour4[i][5],split_hour[i][5])]
		MAE_morning_m=[MAE(split_hour4[i][13],split_hour[i][5]),MAE(split_hour5[i][5],split_hour[i][5])]
		MAE_afternoon=[MAE(split_hour4[i][10],split_hour[i][6]),MAE(split_hour[i][10],split_hour[i][6]),MAE(split_hour[i][14],split_hour[i][6]),MAE(split_hour3[i][6],split_hour[i][6]),MAE(split_hour3[i][10],split_hour[i][6]),MAE(split_hour3[i][14],split_hour[i][6]),MAE(split_hour4[i][6],split_hour[i][6])]
		MAE_afternoon_m=[MAE(split_hour4[i][14],split_hour[i][6]),MAE(split_hour5[i][14],split_hour[i][6])]
		MAE_night=[MAE(split_hour4[i][11],split_hour[i][7]),MAE(split_hour[i][11],split_hour[i][7]),MAE(split_hour[i][15],split_hour[i][7]),MAE(split_hour3[i][7],split_hour[i][7]),MAE(split_hour3[i][11],split_hour[i][7]),MAE(split_hour3[i][15],split_hour[i][7]),MAE(split_hour4[i][7],split_hour[i][7])]
		MAE_night_m=[MAE(split_hour4[i][15],split_hour[i][7]),MAE(split_hour5[i][15],split_hour[i][7])]
		ax=fig.add_subplot(141+i)
		plt.scatter([0,1,2,3,4,5,6],MAE_transit, marker='o',color='g',label='T')
		plt.scatter([-2,-1],MAE_transit_m, marker='o',label='T', facecolors='none', edgecolors='g')


		plt.scatter([0,1,2,3,4,5,6],MAE_morning, marker='^',color='r',label='M')
		plt.scatter([-2,-1],MAE_morning_m, marker='^',label='T', facecolors='none', edgecolors='r')
		plt.scatter([0,1,2,3,4,5,6],MAE_afternoon, marker='s',color='b',label='A')
		plt.scatter([-2,-1],MAE_afternoon_m, marker='s',label='T',facecolors='none', edgecolors='b')
		plt.scatter([0,1,2,3,4,5,6],MAE_night, marker='*',color='grey',label='N')
		plt.scatter([-2,-1],MAE_night_m, marker='*',label='T', facecolors='none', edgecolors='grey')
		plt.scatter([0,1,2,3,4,5,6],MAE_all, marker='.',color='k',label='D')
		plt.scatter([-2,-1],MAE_transit_m, marker='.',label='T',facecolors='none', edgecolors='k')
		plt.xticks([-2,-1,0,1,2,3,4,5,6],['M0','M1','B0','B1','B2','B3','B4','B5','B6'])
		plt.title(season[i]+' - MAE')
		plt.grid(True)
	plt.suptitle(legende_variable)
	#plt.legend(loc='best')
	print count_figure
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_MEA_season.png',dpi=300)
	count_figure=count_figure+1



#plt.scatter(toto,titi,facecolors='none', edgecolors='r')





plt.show()
