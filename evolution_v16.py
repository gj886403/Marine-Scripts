#!/usr/bin/python
# -*- coding: utf8 -*-

from fonction import *
from jules_download import *
from Split_times_Marine import *

from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

save_plot='yes' # 'yes' or 'no' if we want to save the plot, or not

#Choose which run you want to plot
#version_plot='' #OBS and AnthroOff
#version_plot='AnthroOn_' #OBS and AnthroOn

#version_plot='SUEWS_AnthroOn_' #SUEWS and AnthroOn
#version_plot='SUEWS_AnthroOff_' #SUEWS and AnthroOff

#version_plot='WFDEI_AnthroOn_' #WFDEI and AnthroOn
version_plot='WFDEI_AnthroOff_' #WFDEI and AnthroOff




#Variables
#var=['SW_up','QH','Q_star','K_star','K_down','L_up','L_down']

#var=['SW_up']
#var=['QH']
#var=['Q_star']
#var=['K_star']
#var=['K_down']
#var=['L_up']
var=['L_down']
#var=['Emissivity']
#var=['Tsurf']
#var=['Albedo']
#var=['Tsoil']
#level=0 # associeted with Tsoil


for var_i in var :
	if (var_i=='QH') : # Sensible heat
		legende_variable='$Q_{H}$  $W$ $m^{-2}$' # Will be plot as a label on plots
		name_variable_JULES='ftl_gb' #name of the variable in JULES
		name_variable_OBS='qh' #name of the variable in observations
		name_file_plot='QH' #name of the plot when you will save it
		#name_file_plot_A='AnthroOn_QH'
		name_variable_SUEWS='QH' #name of the variable in SUEWS

	if (var_i=='SW_up') : # K up outgoing short wave radiation
		name_file_plot='SW_up'
		#name_file_plot='AnthroOn_SW_up'
		legende_variable='$K_{\uparrow}$ $W$ $m^{-2}$'
		name_variable_JULES='sw_net'# in JULES, we need to calculate Kup from SW_net and SW_down
		name_variable_JULES2='sw_down'
		name_variable_OBS='kup'
		name_variable_SUEWS='kup'

	if (var_i=='Q_star') : # net all waves radiation
		legende_variable='Q* $W$ $m^{-2}$'
		name_variable_JULES='rad_net'
		name_variable_OBS='kdown' # in obs, we need to calculate Q* from others variables
		name_variable_OBS2='kup'
		name_variable_OBS3='ldown'
		name_variable_OBS4='lup'
		name_variable_SUEWS='kdown'
		name_variable_SUEWS2='kup'
		name_variable_SUEWS3='ldown'
		name_variable_SUEWS4='lup'
		name_file_plot='Q_star'
 
	if (var_i=='K_star') : # net K short wave radiation
		legende_variable='$K*$  $W$ $m^{-2}$'
		name_variable_JULES='sw_net'
		name_variable_OBS='kdown' # in SUEWS, we need to calculate K* from others variables
		name_variable_OBS2='kup'
		name_variable_SUEWS='kdown' # in SUEWS, we need to calculate K* from others variables
		name_variable_SUEWS2='kup'
		name_file_plot='K_star'

	if (var_i=='K_down') : # K down incoming short wave radiation
		legende_variable='$K_{\downarrow}$  $W$ $m^{-2}$'
		name_variable_JULES='sw_down'
		name_variable_OBS='kdown'
		name_file_plot='K_down'
		name_variable_SUEWS='kdown'

	if (var_i=='L_up') : # L up outgoing longwave radiation
		legende_variable='$L_{\uparrow}$  $W$ $m^{-2}$'
		name_variable_JULES='lw_up'
		name_variable_OBS='lup'
		name_file_plot='L_up'
		name_variable_SUEWS='lup'

	if (var_i=='L_down') : # Ldown incoming longwave radiation
		legende_variable='$L_{\downarrow}$  $W$ $m^{-2}$'
		name_variable_JULES='lw_down'
		name_variable_OBS='ldown'
		name_file_plot='L_down'
		name_variable_SUEWS='ldown'

	if (var_i=='Albedo') :
		legende_variable='$Albedo$  $(-)$'
		name_variable_JULES='albedo_land'
		name_file_plot='Albedo'
		with_obs='no' #There is not observation for the albedo
		with_SUEWS='no' #There is no SUEWS variable for the albedo

	if (var_i=='Emissivity') :
		legende_variable='$Emissivity$  $(-)$'
		name_variable_JULES='emis_gb'
		name_file_plot='Emissivity'
		with_obs='no'
		with_SUEWS='no'

	if (var_i=='Tsurf') :
		legende_variable='$Tsurf$  $(K)$'
		name_variable_JULES='tstar_gb'
		name_file_plot='Tsurf'
		with_obs='no'
		with_SUEWS='no'

	if (var_i=='Tsoil') :
		legende_variable='$Tsoil$  $(K)$'
		name_variable_JULES='t_soil'
		name_file_plot='Tsoil'+str(level)
		with_obs='no'
		with_SUEWS='no'



	##################################################################
	###### Choose the site that you want
	###### Comment and uncomment the lines that you want
	###### It's also here that you can change some information :
	###### time of study, SUEWS folder....

	##LONDON
   name_file_suews = 'suews_2011_2013.xlsx'
	site='London KC'
	moruses_folder='C:/Users/qw919026/Desktop/JULES/JULES runs/MORUSES/u-bb155/' # Folder with the input of JULES runned with MORUSES
	best_folder='C:/Users/qw919026/Desktop/JULES/JULES runs/Best/u-bc064/' # Folder with the input of JULES runned with BEST
	obs_folder='C:/Users/qw919026/Desktop/JULES/JULES runs/KSSW_OBS/' # Folder with obs
	suews_folder='C:/Users/qw919026/Desktop/JULES/JULES runs/SUEWS_output_KSSW/' # Folder with suews
	#name_file_suews=['Kc1_2011_60.txt','Kc1_2012_60.txt','Kc1_2013_60.txt'] #Name of the file in SUEWS's folder
   
	local_time='Europe/London' #For london, the local time does not really matter : LONDON is +00
	Start= datetime.datetime(2011, 01, 01, 00, 00, 00) #First time step in JULES
	Start_SUEWS= datetime.datetime(2011, 01, 01, 00, 00, 00) #First time step in SUEWS
	year_study='2011-2013' #Date of study : used in legend
	year_study_short='11-13' # Same, shorter
	local_hour=0 #LONDON is +00
	if (var_i!='Emissivity' and var_i!='Albedo' and var_i!='Tsurf' and var_i!='Tsoil') : with_obs='yes' #Emissivity, albedo, Tsurf and soil don't have observations
	if (var_i!='Emissivity' and var_i!='Albedo' and var_i!='Tsurf' and var_i!='Tsoil') : with_SUEWS='yes' #Emissivity, albedo, Tsurf and soil don't have observations
	#with_SUEWS='no' # In this study, we dont want to plot SUEWS, but you want SUEWS for SEB variables, just comment this line

	# Depending on the version of JULES that you want, and that you choose at the beginning  of the script, python will read different files :
	# You dont have to change anything, it's automatic, from the 'version_plot' what you choose
	# if you run a new version of the JULES, you can just add a line or change moruses_version or best_version
	if(version_plot=='SUEWS_AnthroOn_'):
		save_directory='C:/Users/qw919026/Desktop/Marine_scripts/plots/London/SUEWS_forcing_data/'# Anthropogenic Flux OFF
		moruses_version=93166# Anthropogenic Flux ON
		best_version=93432# Anthropogenic Flux ON
	elif(version_plot=='SUEWS_AnthroOff_'):
		save_directory='C:/Users/qw919026/Desktop/Marine_scripts/plots/London/SUEWS_forcing_data/'# Anthropogenic Flux ON
		moruses_version=93157# Anthropogenic Flux OFF
		best_version=93444# Anthropogenic Flux OFF
	elif(version_plot=='WFDEI_AnthroOn_'):
		save_directory='C:/Users/qw919026/Desktop/Marine_scripts/plots/London/WFDEI_forcing_data/'# Anthropogenic Flux ON
		moruses_version=93110# Anthropogenic Flux ON
		best_version=93470# Anthropogenic Flux ON
	elif(version_plot=='WFDEI_AnthroOff_'):
		save_directory='C:/Users/qw919026/Desktop/Marine_scripts/plots/London/WFDEI_forcing_data/'# Anthropogenic Flux ON
		moruses_version=93143# Anthropogenic Flux OFF
		best_version=93457# Anthropogenic Flux OFF




#	###Shanghai
#	site='Shanghai'
#	moruses_folder='/storage/shared/research/met/micromet/JULES/u-aw196_MORUSES_Shanghai_XJH/'
#	best_folder='/storage/shared/research/met/micromet/JULES/u-aw195_1-tile_Shanghai_XJH/'
#	local_time='Asia/Shanghai' # the local time != UTC time
#	Start= datetime.datetime(2012, 01, 01,00,00,00) 
#	year_study='2012-2013'
#	year_study_short='12-13'
#	with_obs='no'
#	local_hour=8 # +08:00
#	with_SUEWS='no'

#	# No observation is available for Shanghai, only runs with WFDEI are available
#	# see LONDON for more explaination
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
#	local_time='Asia/Shanghai'  # the local time != UTC time
#	Start= datetime.datetime(2014, 01, 01,00,00,00)
#	year_study='2014-2015'
#	year_study_short='14-15'
#	with_obs='no'
#	local_hour=8 # +08:00
#	with_SUEWS='no'

##	# No observation is available for Beijing, only run with WFDEI are available
##	# see LONDON for more explaination
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

	Var_moruses=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES,Start)[0] # Download of MORUSES variable
	Var_best=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[0] # Download of BEST variable
	#print type(Var_moruses)
	#print Var_moruses.shape

	if(name_file_plot=='AnthroOn_SW_up' or name_file_plot=='SW_up'): # Kup is calculated from other variables in JULES
		Var_moruses_1=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_best_1=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[0]
		Var_moruses_2=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_best_2=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES2,Start)[0]
		Var_moruses=Var_moruses_2-Var_moruses_1
		Var_best=Var_best_2-Var_best_1
	elif(var_i=='Tsoil') : # a level need to be choose from Tsoil
		Var_moruses=Var_moruses[:,level]
		Var_best=Var_best[:,level]

	#print type(Var_moruses)
	#print Var_moruses.shape

	Time_moruses=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc',name_variable_JULES,Start)[1]# Download of MORUSES time : UTC
	if(local_time!='Europe/London') : Time_moruses=convert_UTC_to_local(Time_moruses,local_time) # If it s London, we dont change anything, if its not, we need to get the local time
	Time_best=jules_download(best_folder+str(best_version)+'/jules.all.nc',name_variable_JULES,Start)[1]# Download of BEST time : UTC || its supposed to be the same as MORUSES
	if(local_time!='Europe/London') : Time_best=convert_UTC_to_local(Time_best,local_time)

	lon=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc','longitude',Start)[0] # Get the longitude of the site
	lat=jules_download(moruses_folder+str(moruses_version)+'/jules.all.nc','latitude',Start)[0] # Get the latitude of the site

	if  (Time_moruses!=Time_best) : print 'MORUSES and Best are not the same size'
	print 'lon',lon,'lat',lat



	##########################  OBS
	if with_obs=='yes' :
		if(name_file_plot=='Q_star' or name_file_plot=='AnthroOn_Q_star'): # Q* is calculated from other variables in obs
			Var_OBS1=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS)),-999.,float('nan'))
			Var_OBS2=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS2)),-999.,float('nan'))
			Var_OBS3=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS3)),-999.,float('nan'))
			Var_OBS4=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS4)),-999.,float('nan'))
			Var_OBS=Var_OBS1-Var_OBS2+Var_OBS3-Var_OBS4
		elif(name_file_plot=='K_star' or name_file_plot=='AnthroOn_K_star'): # K* is calculated from other variables in obs
			Var_OBS1=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS)),-999.,float('nan'))
			Var_OBS2=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS2)),-999.,float('nan'))
			Var_OBS=Var_OBS1-Var_OBS2
		else : Var_OBS=change_missing_value(np.array(extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), name_variable_OBS)),-999.,float('nan')) #Download other variables
		#Var_OBS=quite_modif(Var_OBS,-500,900,float('nan'))
		Time_OBS=extract_variable(extract_txt(obs_folder+'Kc1_Obs.csv',nomber_header=0), 'DateTime',date=True) # Time in OBS
		if(local_time!='Europe/London') : Time_OBS=convert_UTC_to_local(Time_OBS,local_time) # If it s London, we dont change anything, if its not, we need to get the local time
		Var_missing_OBS=missing_measurement(Time_moruses,Var_OBS,Time_OBS,value_nan=-999.)[1]
		missing_OBS=missing_measurement(Time_moruses,Var_OBS,Time_OBS,value_nan=-999.)[0]
      

	'''##########################  SUEWS
	if with_SUEWS=='yes' :
		if(name_file_plot=='Q_star' or name_file_plot=='AnthroOn_Q_star'):
			Var_SUEWS1=get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS)
			Var_SUEWS2=get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS2)
			Var_SUEWS3=get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS3)
			Var_SUEWS4=get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS4)
			Var_SUEWS=np.array(Var_SUEWS1)-np.array(Var_SUEWS2)+np.array(Var_SUEWS3)-np.array(Var_SUEWS4)
		elif(name_file_plot=='K_star' or name_file_plot=='AnthroOn_K_star'):
			Var_SUEWS1=get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS)
			Var_SUEWS2=get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS2)
			Var_SUEWS=np.array(Var_SUEWS1)-np.array(Var_SUEWS2)
		else : Var_SUEWS=np.array(get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS))
		Time_SUEWS=get_time_suews(suews_folder,name_file_suews,Start_SUEWS)
		if(local_time!='Europe/London') : Time_SUEWS=convert_UTC_to_local(Time_SUEWS,local_time)
		Var_missing_SUEWS=missing_measurement(Time_moruses,Var_SUEWS,Time_SUEWS,value_nan=-999.)[1]'''
        
   ########################### SUEWS as one file
   if with_SUEWS=='yes' :
         if(name_file_plot=='Q_star' or name_file_plot=='AnthroOn_Q_star'):
               Var_SUEWS1=get_variable_suews_2(suews_folder,name_file_suews,name_variable_SUEWS)
               Var_SUEWS2=get_variable_suews_2(suews_folder,name_file_suews,name_variable_SUEWS2)
               Var_SUEWS3=get_variable_suews_2(suews_folder,name_file_suews,name_variable_SUEWS3)
               Var_SUEWS4=get_variable_suews_2(suews_folder,name_file_suews,name_variable_SUEWS4)
               Var_SUEWS=np.array(Var_SUEWS1)-np.array(Var_SUEWS2)+np.array(Var_SUEWS3)-np.array(Var_SUEWS4)
         elif(name_file_plot=='K_star' or name_file_plot=='AnthroOn_K_star'):
               Var_SUEWS1=get_variable_suews_2(suews_folder,name_file_suews,name_variable_SUEWS)
               Var_SUEWS2=get_variable_suews_2(suews_folder,name_file_suews,name_variable_SUEWS2)
               Var_SUEWS=np.array(Var_SUEWS1)-np.array(Var_SUEWS2)
         else: Var_SUEWS=np.array(get_variable_suews_2(suews_folder,name_file_suews,name_variable_SUEWS))
         rng = pandas.date_range(start='01/01/2011 01:00',end='01/01/2014 00:00', freq='H')
         Time_SUEWS = rng.to_pydatetime().tolist()
         Var_missing_SUEWS=missing_measurement(Time_moruses,Var_SUEWS,Time_SUEWS,value_nan=-999.)[1]

	##########################  Divide
	# To plot the daily cycle, data need to be split into Season/ Month and 3H/H

	# split each season : you will get a list with 4 lists : [[DJF],[MAM],[JJA],[SON]], each list is the data of 1 season 
	if with_obs=='yes' : Var_saison_OBS=divide_periode_day('season',Var_missing_OBS,Time_moruses)
	if with_SUEWS=='yes' : Var_saison_SUEWS=divide_periode_day('season',Var_missing_SUEWS,Time_moruses)
	Var_saison_m=divide_periode_day('season',Var_moruses,Time_moruses)
	Var_saison_b=divide_periode_day('season',Var_best,Time_moruses)
	Time_saison=divide_periode_day('season',Time_moruses,Time_moruses)

	# split each season and each 3h : [[DJF],[MAM],[JJA],[SON]], each list is the 8 list of 1 season 
	# [DJF] = [[0h],[3h], ... [21h]] each SeasonList contain 8 list for each 3h periode
	if with_obs=='yes' : Var_saison_3h_OBS=divide_periode_day('season',Var_missing_OBS,Time_moruses,which_day=3)
	if with_SUEWS=='yes' : Var_saison_3h_SUEWS=divide_periode_day('season',Var_missing_SUEWS,Time_moruses,which_day=3)
	Var_saison_3h_b=divide_periode_day('season',Var_best,Time_moruses,which_day=3)
	Var_saison_3h_m=divide_periode_day('season',Var_moruses,Time_moruses,which_day=3)
	Time_saison_3h=divide_periode_day('season',Time_moruses,Time_moruses,which_day=3)

	# split each season and each h : [[DJF],[MAM],[JJA],[SON]], each list is the 24 list of 1 season 
	# [DJF] = [[0h],[1h], ... [23h]] each SeasonList contain 24 list for each h periode
	if with_obs=='yes' : Var_saison_h_OBS=divide_periode_day('season',Var_missing_OBS,Time_moruses,which_day=1)
	if with_SUEWS=='yes' : Var_saison_h_SUEWS=divide_periode_day('season',Var_missing_SUEWS,Time_moruses,which_day=1)
	Var_saison_h_b=divide_periode_day('season',Var_best,Time_moruses,which_day=1)
	Var_saison_h_m=divide_periode_day('season',Var_moruses,Time_moruses,which_day=1)
	#Time_saison_h=divide_periode_day('season',Time_JULES,Time_JULES,which_day=1)

	# split each month and each h : [[J],[F],[M],...,[N],[D]], each list is the 24 list of 1 month
	# [J] = [[0h],[1h], ... [23h]] each MonthList contain 24 list for each h periode
	if with_obs=='yes' : Var_h_OBS=divide_periode_day('month',Var_missing_OBS,Time_moruses,which_day=1)
	if with_SUEWS=='yes' : Var_h_SUEWS=divide_periode_day('month',Var_missing_SUEWS,Time_moruses,which_day=1)


	#####################Usefull information
	vect_all=[Var_best,Var_moruses] # this list wil contain everydata
	if with_obs=='yes' : vect_all.append(Var_missing_OBS)
	if with_SUEWS=='yes' : vect_all.append(Var_missing_SUEWS)
	centile_99=float(np.nanpercentile(np.array(vect_all),99)) # get the 99th centile of the merged dataset, with all data : best, moruses, obs and suews
	centile_1=float(np.nanpercentile(np.array(vect_all),1)) # get the 1st centile of the merged dataset, with all data : best, moruses, obs and suews

	max_T=max([Var_best.max(),Var_moruses.max()])
	min_T=min([Var_best.min(),Var_moruses.min()])
	if with_obs=='yes' : 
		max_T=max([max_T,max(Var_missing_OBS)])
		min_T=min([min_T,min(Var_missing_OBS)])
	if with_SUEWS=='yes' : 
		max_T=max([max_T,max(Var_missing_SUEWS)])
		min_T=min([min_T,min(Var_missing_SUEWS)])

	position_title=max_T-(max_T-min_T)*0.10


	heure_3h=['0h','3h','6h','9h','12h','15h','18h','21h']
	mois=['J','F','M','A','M','J','J','A','S','O','N','D']
	season=['Winter DJF','Spring MAM','Summer JJA','Autumn SON']
	heure=['']*24
	for i in range(0,len(heure)):
		if (i%3==0) : heure[i]=str(i)
	#for i in range(0,24): heure.extend([str(i)])
	row_labels_coef=['24h','T','M','A','N']
	count_figure=1


	#####################

	#########################################################
	########### Evolution over the Period
	
	###############################################################################################
	########################################### Plot missing observation :
	# red : missing, blue : available
	count_figure=1
	color_value=(1.,.0,.0)#red
	color_missing=(0.,0.,1.)#blue
	colors=[color_value,color_missing]
	n_bin=2
	cm = LinearSegmentedColormap.from_list('color_value_missing', colors, N=2)

	if with_obs=='yes' :
		plt.figure(figsize=(14,3))
		plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
		plt.pcolor(Time_moruses,[1,2,3],np.array([missing_OBS,missing_OBS]),cmap=cm)
		plt.yticks([1,2,3], ['Kc']+['',' '])
		plt.title('Kc OBS 2011-2013')
		cbar=plt.colorbar(ticks=[0, 1])
		cbar.ax.set_yticklabels([ 'missing', 'available'])
		if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_missing_obs.png',dpi=200)
		count_figure=count_figure+1

	###############################################################################################
	########################################### Plot time evolution, with daily mean

	fig=plt.figure(figsize=(17,11)) #We now want to plot
	ax1 = fig.add_subplot(311)
	plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
	epaisseur_percentile=0.8
	transparance=0.1

	fig.add_subplot(311)
	if with_obs=='yes' :
		plt.plot(Time_moruses,Var_missing_OBS,color='k',label='Hourly',linewidth=0.5,alpha=0.7) # Hourly evolution
		plt.scatter(daily_mean(Var_missing_OBS,Time_moruses,val_min=15)[1],daily_mean(Var_missing_OBS,Time_moruses,val_min=15)[0],color='r',label='Daily mean',marker='+') # Daily mean
		plt.annotate(site +'\n'+'OBS '+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction') # legend
		plt.ylabel(legende_variable)
		if(name_file_plot!='Albedo' or name_file_plot=='Emissivity') : plt.ylim(min_T,max_T)
		plt.xticks([])

	fig.add_subplot(312)
	plt.plot(Time_moruses,Var_moruses,color='k',label='Hourly',linewidth=0.5,alpha=0.7)
	plt.scatter(daily_mean(Var_moruses,Time_moruses,val_min=15)[1],daily_mean(Var_moruses,Time_moruses,val_min=15)[0],color='r',label='Daily mean',marker='+')
	#plt.annotate(site +'\n'+'MORUSES '+'v='+str(moruses_version)+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction')
	plt.annotate(site +'\n'+'MORUSES '+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction')
	plt.ylabel(legende_variable)
	if(name_file_plot!='Albedo'or name_file_plot=='Emissivity') : plt.ylim(min_T,max_T)
	plt.xticks([])

	fig.add_subplot(313)
	plt.plot(Time_moruses,Var_best,color='k',label='Hourly',linewidth=0.5,alpha=0.7)
	plt.scatter(daily_mean(Var_best,Time_moruses,val_min=15)[1],daily_mean(Var_best,Time_moruses,val_min=15)[0],color='r',label='Daily mean',marker='+')
	#plt.annotate(site +'\n'+'Best '+'v='+str(best_version)+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction')
	plt.annotate(site +'\n'+'Best '+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction')
	plt.ylabel(legende_variable)
	plt.xlabel('Time (day)')
	if(name_file_plot!='Albedo' or name_file_plot!='Emissivity') : plt.ylim(min_T,max_T)
	plt.legend(loc='best')


	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_variations.png',dpi=300)
	count_figure=count_figure+1

	if with_SUEWS=='yes' :
		fig=plt.figure(figsize=(17,3)) #We now want to plot
		plt.plot(Time_moruses,Var_missing_SUEWS,color='k',label='Hourly',linewidth=0.5,alpha=0.7)
		plt.scatter(daily_mean(Var_missing_SUEWS,Time_moruses,val_min=15)[1],daily_mean(Var_missing_SUEWS,Time_moruses,val_min=15)[0],color='r',label='Daily mean',marker='+')
		plt.annotate(site +'\n'+'SUEWS '+'\n'+year_study,xy=(0.005,    0.8), xycoords = 'axes fraction')
		plt.ylabel(legende_variable)
		if(name_file_plot!='Albedo' or name_file_plot=='Emissivity') : plt.ylim(min_T,max_T)
		plt.xticks([])
		if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_variations_SUEWS.png',dpi=300)
		count_figure=count_figure+1

	###############################################################################################
	########################################### Plot daily mean of each dataset


	plt.figure(figsize=(12,6))
	plt.subplots_adjust(left=0.06, bottom=None, right=0.94, top=None,wspace=0.05, hspace=0.05)	
	if with_obs=='yes' : plt.scatter(daily_mean(Var_missing_OBS,Time_moruses,val_min=15)[1],daily_mean(Var_missing_OBS,Time_moruses,val_min=15)[0],color='k',label='OBS',marker='+')
	if with_SUEWS=='yes' : plt.scatter(daily_mean(Var_missing_SUEWS,Time_moruses,val_min=15)[1],daily_mean(Var_missing_SUEWS,Time_moruses,val_min=15)[0],color='g',label='SUEWS',marker='+')
	plt.scatter(daily_mean(Var_best,Time_moruses,val_min=15)[1],daily_mean(Var_best,Time_moruses,val_min=15)[0],color='r',label='Best',marker='+')
	plt.scatter(daily_mean(Var_moruses,Time_moruses,val_min=15)[1],daily_mean(Var_moruses,Time_moruses,val_min=15)[0],color='b',label='MORUSES',marker='+')
	plt.title('Downwelling shortwave radiation, daily mean - 2011-2013 over London (KC)')
	plt.legend(loc='best')
	plt.ylabel(legende_variable)
	plt.xlabel('Time (day)')
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_daily_mean.png',dpi=300)
	count_figure=count_figure+1

	if (save_plot=='yes') : print 'ok'
	print save_directory+name_file_plot+str(count_figure)+'.png'






	###############################################################################################
	########################################### Boxplot

	#OBS
	if with_obs=='yes' :
		f, case = plt.subplots(1,4, sharex='col', sharey='row',figsize=(18,9))
		plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
		for i in range(0,4):#for each month
			plot_evolution_boxplot(case[i],Var_saison_h_OBS[i],heure,season[i],min_T,max_T)
			case[i].set_xlabel('Time (h)')
			if (i==0 or i==6) :case[i].set_ylabel(legende_variable)
		case[0].annotate(site +'\n'+'OBS '+'\n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
		if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_OBS.png',dpi=300)
		count_figure=count_figure+1

	#SUEWS
	if with_SUEWS=='yes' :
		f, case = plt.subplots(1,4, sharex='col', sharey='row',figsize=(18,9))
		plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
		for i in range(0,4):#for each month
			plot_evolution_boxplot(case[i],Var_saison_h_SUEWS[i],heure,season[i],min_T,max_T)
			case[i].set_xlabel('Time (h)')
			if (i==0 or i==6) :case[i].set_ylabel(legende_variable)
		case[0].annotate(site +'\n'+'SUEWS '+'\n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
		if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_SUEWS.png',dpi=300)
		count_figure=count_figure+1



	#best
	f, case = plt.subplots(1,4, sharex='col', sharey='row',figsize=(18,9))
	plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
	for i in range(0,4):#for each month
		min_max='yes'
		if(name_file_plot=='Albedo' or name_file_plot=='Emissivity') : min_max='no'
		plot_evolution_boxplot(case[i],Var_saison_h_b[i],heure,season[i],min_T,max_T,do_min_max=min_max)
		case[i].set_xlabel('Time (h)')
		if (i==0 or i==6) :case[i].set_ylabel(legende_variable)
	case[0].annotate(site +'\n'+'Best '+'v='+str(best_version)+'\n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_Best.png',dpi=300)
	count_figure=count_figure+1


	#moruses
	f, case = plt.subplots(1,4, sharex='col', sharey='row',figsize=(18,9))
	plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
	for i in range(0,4):#for each month
		min_max='yes'
		if(name_file_plot=='Albedo' or name_file_plot=='Emissivity') : min_max='no'
		plot_evolution_boxplot(case[i],Var_saison_h_m[i],heure,season[i],min_T,max_T,do_min_max=min_max)
		case[i].set_xlabel('Time (h)')
		if (i==0 or i==6) :case[i].set_ylabel(legende_variable)
	case[0].annotate(site +'\n'+'MORUSES '+'v='+str(moruses_version)+'\n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_MORUSES.png',dpi=300)
	count_figure=count_figure+1



	f, case = plt.subplots(2,4, sharex='col', sharey='row',figsize=(18,9))
	plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.04, hspace=0.04)
	for i in range(0,4):#for each month
		min_max='yes'
		case[0,i].ticklabel_format(useOffset=False)
		if(name_file_plot=='Albedo' or name_file_plot=='Emissivity') : min_max='no'
		plot_evolution_boxplot(case[0,i],Var_saison_h_b[i],heure,season[i],min_T,max_T,do_min_max=min_max)
		case[0,i].set_xlabel('Time (h)')
		if (i==0 or i==6) :case[0,i].set_ylabel(legende_variable)
		print type(case[0,i])
		#case[0,i].get_xaxis().get_major_formatter().set_useOffset(False)
	case[0,0].annotate(site +'\n'+'Best '+'v='+str(best_version)+'\n'+year_study,xy=(0.01,    0.8), xycoords = 'axes fraction')
	for i in range(0,4):#for each month
		min_max='yes'
		if(name_file_plot=='Albedo' or name_file_plot=='Emissivity') : min_max='no'
		plot_evolution_boxplot(case[1,i],Var_saison_h_m[i],heure,'',min_T,max_T,do_min_max=min_max)
		case[1,i].set_xlabel('Time (h)')
		if (i==0 or i==6) :case[1,i].set_ylabel(legende_variable)
	case[1,0].annotate(site +'\n'+'MORUSES '+'v='+str(moruses_version)+'\n'+year_study,xy=(0.01,    0.8), xycoords = 'axes fraction')
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_MORUSES_Best.png',dpi=300)
	count_figure=count_figure+1

	f, case = plt.subplots(1,4, sharex='col', sharey='row',figsize=(18,4.5))
	plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.04, hspace=0.04)
	for i in range(0,4):#for each month
		min_max='yes'
		if(name_file_plot=='Albedo' or name_file_plot=='Emissivity') : min_max='no'
		plot_evolution_boxplot(case[i],Var_saison_h_m[i],heure,'',min_T,max_T,do_min_max=min_max)
		case[i].set_xlabel('Time (h)',fontsize=15)
		if (i==0 or i==6) :case[i].set_ylabel(legende_variable,fontsize=15)
	case[0].annotate(site +'\n'+'MORUSES '+'v='+str(moruses_version)+'\n'+year_study,xy=(0.01,    0.8), xycoords = 'axes fraction')
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_MORUSES.png',dpi=300)
	count_figure=count_figure+1

	if with_obs=='yes' :
		f, case = plt.subplots(2,6, sharex='col', sharey='row',figsize=(18,9))
		plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
		for i in range(0,12):#for each month
			plot_evolution_boxplot(case[i/6,i%6],Var_h_OBS[i],heure,mois[i],min_T,max_T)
			if (i>5) : case[i/6,i%6].set_xlabel('Time (h)')
			if (i==0 or i==6) :case[i/6,i%6].set_ylabel(legende_variable)
		case[0,0].annotate(site +'\n'+'OBS '+'\n'+year_study,xy=(0.01,    0.8), xycoords = 'axes fraction')
		f.suptitle('OBS - KC - 2011-2013')
		if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_OBS_month.png',dpi=300)
		count_figure=count_figure+1



	###############################################################################################
	########################################### Boxplot Line


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
		plot_line_bloxplot(Var_saison_h_b[i],heure,case_plot=plt,str_color='r',str_label='B')
		plot_line_bloxplot(Var_saison_h_m[i],heure,case_plot=plt,str_color='b',str_label='M')
		if with_obs=='yes' : plot_line_bloxplot(Var_saison_h_OBS[i],heure,case_plot=plt,str_color='k',str_label='OBS ')
		plt.xticks(range(0,len(heure)+1),heure+['Mean'],rotation='vertical')
		plt.title(season[i], fontsize=15)
		#print (name_file_plot!='Albedo' and name_file_plot!='Emissivity'), name_file_plot
		if(name_file_plot!='Albedo' and name_file_plot!='Emissivity') : plt.ylim(min_T,max_T)
		#plt.ylim(min_T-1,max_T+1)
		plt.xlabel('Time (h)', fontsize=15)
		if(i==0) : plt.annotate(site +'\n'+year_study+'\n'+'OBS, MORUSES and Best ',xy=(0.01,    0.89), xycoords = 'axes fraction')
		if(i!=0) : plt.yticks([])
		else : 	plt.ylabel(legende_variable, fontsize=15)
	plt.legend(loc='best',fontsize=12)
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_line.png',dpi=300)
	count_figure=count_figure+1


	#plt.show()



	if with_SUEWS=='yes' :
		col_labels=['B-M','B-OBS','M-OBS','S-OBS']
		fig=plt.figure(figsize=(16,6)) #We now want to plot
		ax1 = fig.add_subplot(141)
		plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
		epaisseur_percentile=0.8
		transparance=0.1
		toto=[0,2,4,8]
		for i in range(0,4):#For each season
			k=i
			ax=fig.add_subplot(141+i)
			plot_line_bloxplot(Var_saison_h_b[i],heure,case_plot=plt,str_color='r',str_label='B ')
			plot_line_bloxplot(Var_saison_h_m[i],heure,case_plot=plt,str_color='b',str_label='M ')
			if with_obs=='yes' : plot_line_bloxplot(Var_saison_h_OBS[i],heure,case_plot=plt,str_color='k',str_label='OBS ')
			if with_SUEWS=='yes' : plot_line_bloxplot(Var_saison_h_SUEWS[i],heure,case_plot=plt,str_color='g',str_label='SUEWS ')
			plt.xticks(range(0,len(heure)+1),heure+['Mean'],rotation='vertical')
			plt.title(season[i],size=10)
			print (name_file_plot!='Albedo' and name_file_plot!='Emissivity'), name_file_plot
			if(name_file_plot!='Albedo' and name_file_plot!='Emissivity') : plt.ylim(min_T,max_T)
			plt.xlabel('Time (h)')
			if(i==0) : plt.annotate(site +'\n'+year_study+'\n'+'SUEWS, OBS, MORUSES and Best ',xy=(0.01,    0.9), xycoords = 'axes fraction')
			if(i!=0) : plt.yticks([])
			else : 	plt.ylabel(legende_variable, size=10)
		plt.legend(loc='best')
		print count_figure
		if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_boxplot_line_SUEWS.png',dpi=300)
		count_figure=count_figure+1

	#plt.show()

	###############################################################################################
	########################################### Split 

	#Split the daily into 4 periods : Morning, Afternoon, Transition, Night.
	split_hour=[]
	split_hour_SUEWS=[]
	for i in range(0,4):
		k=i
		if with_obs=='yes' : 
			split_hour.append(split_times(float(lat),float(lon),Time_saison[k],Var_saison_OBS[k],Var_saison_b[k],Var_saison_m[k],local_hour))
		else : 
			split_hour.append(split_times(float(lat),float(lon),Time_saison[k],[float('nan')]*len(Var_saison_b[k]),Var_saison_b[k],Var_saison_m[k],local_hour))
		if (with_SUEWS=='yes' and with_obs=='yes') : 
			split_hour_SUEWS.append(split_times(float(lat),float(lon),Time_saison[k],Var_saison_OBS[k],Var_saison_SUEWS[k],Var_saison_SUEWS[k],local_hour))

	###############################################################################################
	########################################### Plot MAE


	col_labels=['B-M','B-OBS','M-OBS']
	if (with_SUEWS=='yes' and with_obs=='yes') : col_labels.append('S-OBS')
	fig=plt.figure(figsize=(16,2)) #We now want to plot
	ax1 = fig.add_subplot(141)
	plt.subplots_adjust(left=0.03, bottom=0.01, right=0.97, top=None,wspace=None, hspace=None)
	for i in range(0,4):#For each season
		k=i
		################################################# MAE calculation
		#For the entire day
		if with_obs=='yes' :
			MAE_all=[MAE(Var_saison_b[k],Var_saison_m[k]),MAE(Var_saison_b[k],Var_saison_OBS[k]),MAE(Var_saison_m[k],Var_saison_OBS[k])]#,MAE(Var_saison_OBS[k],Var_saison_SUEWS[k])]
			if (with_SUEWS=='yes' and with_obs=='yes') : MAE_all.append(MAE(Var_saison_OBS[k],Var_saison_SUEWS[k]))
		else :  
			MAE_all=[MAE(Var_saison_b[k],Var_saison_m[k]),'','']
		#Night
		MAE_night=[MAE(split_hour[i][11],split_hour[i][15]),MAE(split_hour[i][11],split_hour[i][7]),MAE(split_hour[i][15],split_hour[i][7])]
		if (with_SUEWS=='yes' and with_obs=='yes') : MAE_night.append(MAE(split_hour_SUEWS[i][11],split_hour_SUEWS[i][7]))
		#Transition
		MAE_transit=[MAE(split_hour[i][8],split_hour[i][12]),MAE(split_hour[i][8],split_hour[i][4]),MAE(split_hour[i][12],split_hour[i][4])]
		if (with_SUEWS=='yes' and with_obs=='yes') : MAE_transit.append(MAE(split_hour_SUEWS[i][8],split_hour_SUEWS[i][4]))
		#Morning
		MAE_morning=[MAE(split_hour[i][9],split_hour[i][13]),MAE(split_hour[i][9],split_hour[i][5]),MAE(split_hour[i][13],split_hour[i][5])]
		if (with_SUEWS=='yes' and with_obs=='yes') : MAE_morning.append(MAE(split_hour_SUEWS[i][9],split_hour_SUEWS[i][5]))
		#Afternoon
		MAE_afternoon=[MAE(split_hour[i][10],split_hour[i][14]),MAE(split_hour[i][10],split_hour[i][6]),MAE(split_hour[i][14],split_hour[i][6])]
		if (with_SUEWS=='yes' and with_obs=='yes') : MAE_afternoon.append(MAE(split_hour_SUEWS[i][10],split_hour_SUEWS[i][6]))
		ax=fig.add_subplot(141+i)
		# Table is ploted :
		table_vals=[MAE_all, MAE_transit, MAE_morning, MAE_afternoon,MAE_night]
		the_table = plt.table(cellText=table_vals,colWidths = [0.20]*len(col_labels), rowLabels=row_labels_coef, colLabels=col_labels,loc='center',fontsize=15)
		plt.xticks([])
		plt.annotate(season[i]+' - MAE',xy=(0.2,    0.85), xycoords = 'axes fraction',fontsize=15)
		#plt.text(0, 0.5, "Direction", ha="center", va="center", rotation=45,size=15,bbox=bbox_props)
		#plt.title(season[i]+' - MAE')
		plt.yticks([])
		ax.axis('off')
	print count_figure
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_MAE.png',dpi=300,bbox_inches='tight')
	count_figure=count_figure+1

	###############################################################################################
	########################################### Plot RMSE

	col_labels=['B-M','B-OBS','M-OBS']
	if (with_SUEWS=='yes' and with_obs=='yes') : col_labels.append('S-OBS')
	fig=plt.figure(figsize=(16,2)) #We now want to plot
	ax1 = fig.add_subplot(141)
	plt.subplots_adjust(left=0.03, bottom=0.01, right=0.97, top=None,wspace=None, hspace=None)
	for i in range(0,4):#For each season
		k=i
		###################################### RMSE calculation
		if with_obs=='yes' : 
			RMSE_all=[RMSE(Var_saison_b[k],Var_saison_m[k]),RMSE(Var_saison_b[k],Var_saison_OBS[k]),RMSE(Var_saison_m[k],Var_saison_OBS[k])]
			if (with_SUEWS=='yes' and with_obs=='yes') : RMSE_all.append(RMSE(Var_saison_OBS[k],Var_saison_SUEWS[k]))
		else :  
			RMSE_all=[RMSE(Var_saison_b[k],Var_saison_m[k]),'','']
		RMSE_night=[RMSE(split_hour[i][11],split_hour[i][15]),RMSE(split_hour[i][11],split_hour[i][7]),RMSE(split_hour[i][15],split_hour[i][7])]
		if (with_SUEWS=='yes' and with_obs=='yes') : RMSE_night.append(RMSE(split_hour_SUEWS[i][11],split_hour_SUEWS[i][7]))
		RMSE_transit=[RMSE(split_hour[i][8],split_hour[i][12]),RMSE(split_hour[i][8],split_hour[i][4]),RMSE(split_hour[i][12],split_hour[i][4])]
		if (with_SUEWS=='yes' and with_obs=='yes') : RMSE_transit.append(RMSE(split_hour_SUEWS[i][8],split_hour_SUEWS[i][4]))
		RMSE_morning=[RMSE(split_hour[i][9],split_hour[i][13]),RMSE(split_hour[i][9],split_hour[i][5]),RMSE(split_hour[i][13],split_hour[i][5])]
		if (with_SUEWS=='yes' and with_obs=='yes') : RMSE_morning.append(RMSE(split_hour_SUEWS[i][9],split_hour_SUEWS[i][5]))
		RMSE_afternoon=[RMSE(split_hour[i][10],split_hour[i][14]),RMSE(split_hour[i][10],split_hour[i][6]),RMSE(split_hour[i][14],split_hour[i][6])]
		if (with_SUEWS=='yes' and with_obs=='yes') : RMSE_afternoon.append(RMSE(split_hour_SUEWS[i][10],split_hour_SUEWS[i][6]))
		ax=fig.add_subplot(141+i)
		table_vals=[RMSE_all, RMSE_transit, RMSE_morning, RMSE_afternoon,RMSE_night]
		the_table = plt.table(cellText=table_vals,colWidths = [0.20]*len(col_labels), rowLabels=row_labels_coef, colLabels=col_labels,loc='center')
		plt.xticks([])
		plt.title(season[i]+' - RMSE')
		plt.yticks([])
		ax.axis('off')
	print count_figure
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_RMSE.png',dpi=300)
	count_figure=count_figure+1


	###############################################################################################
	########################################### Plot Correlation

	col_labels=['B-M','B-OBS','M-OBS']
	if (with_SUEWS=='yes' and with_obs=='yes') : col_labels.append('S-OBS')
	fig=plt.figure(figsize=(16,2)) #We now want to plot
	ax1 = fig.add_subplot(141)
	plt.subplots_adjust(left=0.03, bottom=0.01, right=0.97, top=None,wspace=None, hspace=None)
	for i in range(0,4):#For each season
		k=i
		###################################### Correlation calculation
		if with_obs=='yes' : 
			COR_all=[correlation(Var_saison_b[k],Var_saison_m[k]),correlation(Var_saison_b[k],Var_saison_OBS[k]),correlation(Var_saison_m[k],Var_saison_OBS[k])]
			if (with_SUEWS=='yes' and with_obs=='yes') : COR_all.append(correlation(Var_saison_OBS[k],Var_saison_SUEWS[k]))
		else :  
			COR_all=[correlation(Var_saison_b[k],Var_saison_m[k]),'','']
		COR_night=[correlation(split_hour[i][11],split_hour[i][15]),correlation(split_hour[i][11],split_hour[i][7]),correlation(split_hour[i][15],split_hour[i][7])]
		if (with_SUEWS=='yes' and with_obs=='yes') : COR_night.append(correlation(split_hour_SUEWS[i][11],split_hour_SUEWS[i][7]))
		COR_transit=[correlation(split_hour[i][8],split_hour[i][12]),correlation(split_hour[i][8],split_hour[i][4]),correlation(split_hour[i][12],split_hour[i][4])]
		if (with_SUEWS=='yes' and with_obs=='yes') : COR_transit.append(correlation(split_hour_SUEWS[i][8],split_hour_SUEWS[i][4]))
		COR_morning=[correlation(split_hour[i][9],split_hour[i][13]),correlation(split_hour[i][9],split_hour[i][5]),correlation(split_hour[i][13],split_hour[i][5])]
		if (with_SUEWS=='yes' and with_obs=='yes') : COR_morning.append(correlation(split_hour_SUEWS[i][9],split_hour_SUEWS[i][5]))
		COR_afternoon=[correlation(split_hour[i][10],split_hour[i][14]),correlation(split_hour[i][10],split_hour[i][6]),correlation(split_hour[i][14],split_hour[i][6])]
		if (with_SUEWS=='yes' and with_obs=='yes') : COR_afternoon.append(correlation(split_hour_SUEWS[i][10],split_hour_SUEWS[i][6]))
		ax=fig.add_subplot(141+i)
		table_vals=[COR_all, COR_transit, COR_morning, COR_afternoon,COR_night]
		the_table = plt.table(cellText=table_vals,colWidths = [0.20]*len(col_labels), rowLabels=row_labels_coef, colLabels=col_labels,loc='center')
		plt.xticks([])
		plt.title(season[i]+' - Correlation')
		plt.yticks([])
		ax.axis('off')
	print count_figure
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_COR.png',dpi=300)
	count_figure=count_figure+1


	###############################################################################################
	########################################### Plot N



	col_labels_N=['B','M','OBS']
	if (with_SUEWS=='yes' and with_obs=='yes') : col_labels_N.append('S')
	fig=plt.figure(figsize=(16,2)) #We now want to plot
	ax1 = fig.add_subplot(141)
	plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=None, hspace=None)
	for i in range(0,4):#For each season
		k=i
		################################################# MAE calculation
		if with_obs=='yes' : 
			N_all=[len(Var_saison_b[k])-np.isnan(np.array(Var_saison_b[k])).sum(),len(Var_saison_m[k])-np.isnan(np.array(Var_saison_m[k])).sum(),len(Var_saison_OBS[k])-np.isnan(np.array(Var_saison_OBS[k])).sum()]
			if (with_SUEWS=='yes' and with_obs=='yes') : N_all.append(len(Var_saison_SUEWS[k])-np.isnan(np.array(Var_saison_SUEWS[k])).sum())
		else :  
			N_all=[len(Var_saison_b[k])-np.isnan(np.array(Var_saison_b[k])).sum(),len(Var_saison_m[k])-np.isnan(np.array(Var_saison_m[k])).sum(),'']
			if (with_SUEWS=='yes') : N_all.append(len(Var_saison_SUEWS[k])-np.isnan(np.array(Var_saison_SUEWS[k])).sum())
		N_night=[len(split_hour[i][11])-np.isnan(np.array(split_hour[i][11])).sum(),len(split_hour[i][15])-np.isnan(np.array(split_hour[i][15])).sum(),'']
		if with_obs=='yes' :N_night[2]=len(split_hour[i][7])-np.isnan(np.array(split_hour[i][7])).sum()
		if with_SUEWS=='yes' :N_night.append(len(split_hour_SUEWS[i][11])-np.isnan(np.array(split_hour_SUEWS[i][11])).sum())
		N_afternoon=[len(split_hour[i][10])-np.isnan(np.array(split_hour[i][10])).sum(),len(split_hour[i][14])-np.isnan(np.array(split_hour[i][14])).sum(),'']
		if with_obs=='yes' :N_afternoon[2]=len(split_hour[i][6])-np.isnan(np.array(split_hour[i][6])).sum()
		if with_SUEWS=='yes' :N_afternoon.append(len(split_hour_SUEWS[i][10])-np.isnan(np.array(split_hour[i][10])).sum())
		N_morning=[len(split_hour[i][9])-np.isnan(np.array(split_hour[i][9])).sum(),len(split_hour[i][13])-np.isnan(np.array(split_hour[i][13])).sum(),'']
		if with_obs=='yes' :N_morning[2]=len(split_hour[i][5])-np.isnan(np.array(split_hour[i][5])).sum()
		if with_SUEWS=='yes' :N_morning.append(len(split_hour_SUEWS[i][9])-np.isnan(np.array(split_hour[i][9])).sum())
		N_transit=[len(split_hour[i][8])-np.isnan(np.array(split_hour[i][8])).sum(),len(split_hour[i][12])-np.isnan(np.array(split_hour[i][12])).sum(),'']
		if with_obs=='yes' :N_transit[2]=len(split_hour[i][4])-np.isnan(np.array(split_hour[i][4])).sum()
		if with_SUEWS=='yes' :N_transit.append(len(split_hour_SUEWS[i][8])-np.isnan(np.array(split_hour[i][8])).sum())
		ax=fig.add_subplot(141+i)
		table_vals=[N_all, N_transit, N_morning, N_afternoon,N_night]
		the_table = plt.table(cellText=table_vals,colWidths = [0.20]*len(col_labels_N), rowLabels=row_labels_coef, colLabels=col_labels_N,loc='center')
		plt.xticks([])
		plt.title(season[i]+' - N')
		plt.yticks([])
		ax.axis('off')
	print count_figure
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_N.png',dpi=300)
	count_figure=count_figure+1


	############################################
	########### Distribution

	#fig=plt.figure(figsize=(10,6))
	couleur=['b','orange','g','r']
	f, case = plt.subplots(1,3, sharex='col', sharey='row',figsize=(17,7))
	plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
	for i in range(0,4):
		if with_obs=='yes' : case[0].hist(remove_nan(Var_saison_OBS)[i],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label=season[i])
		case[1].hist(Var_saison_b[i],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label=season[i])
		case[2].hist(Var_saison_m[i],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label=season[i])
		case[1].set_xlabel(legende_variable)
		case[2].set_xlabel(legende_variable)
		case[0].set_xlabel(legende_variable)
	#plt.xlim(min_T-1,max_T+1)
	case[0].annotate(site +'\n'+'OBS \n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
	case[1].annotate(site +'\n'+'MORUSES '+'v='+str(moruses_version)+'\n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
	case[2].annotate(site +'\n'+'Best '+'v='+str(best_version)+'\n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
	plt.xlabel(legende_variable)
	plt.legend()
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_hist_season.png',dpi=300)
	count_figure=count_figure+1

	if with_SUEWS=='yes' :
		fig=plt.figure(figsize=(4,6))
		couleur=['b','orange','g','r']
		for i in range(0,4):
			plt.hist(Var_saison_SUEWS[i],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label=season[i])
		plt.xlabel(legende_variable)
		plt.annotate(site +'\n'+'SUEWS \n'+year_study,xy=(0.01,    0.9), xycoords = 'axes fraction')
		plt.legend()
		if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_hist_season_SUEWS.png',dpi=300)
		count_figure=count_figure+1



	f, case = plt.subplots(4,8, sharex='col', sharey='row',figsize=(18,9))
	plt.subplots_adjust(left=0.05, bottom=None, right=0.95, top=None,wspace=0.05, hspace=0.05)
	for i in range(0,4):
		for j in range(0,len(heure_3h)) :
			if with_obs=='yes' : case[i,j].hist(remove_nan(Var_saison_3h_OBS[i])[j], normed=1,bins=20, range=(centile_1,centile_99), fc=(0, 0, 0, 0.35))
			if with_obs=='yes' : case[i,j].hist(remove_nan(Var_saison_3h_OBS[i])[j],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label='OBS',color='k')
			if with_SUEWS=='yes' : case[i,j].hist(remove_nan(Var_saison_3h_SUEWS[i])[j], normed=1,bins=20, range=(centile_1,centile_99), fc=(0, 1., 0, 0.35))
			if with_SUEWS=='yes' : case[i,j].hist(remove_nan(Var_saison_3h_SUEWS[i])[j],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label='SUEWS',color='g')
			case[i,j].hist(remove_nan(Var_saison_3h_b[i])[j], normed=1,bins=20, range=(centile_1,centile_99), fc=(1, 0, 0, 0.35))
			case[i,j].hist(remove_nan(Var_saison_3h_b[i])[j],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label='B',color='r')
			case[i,j].hist(remove_nan(Var_saison_3h_m[i])[j], normed=1,bins=20, range=(centile_1,centile_99), fc=(0, 0, 1, 0.35))
			case[i,j].hist(remove_nan(Var_saison_3h_m[i])[j],histtype = 'step', normed=1,bins=20, range=(centile_1,centile_99),label='M',color='b')
			case[i,0].set_ylabel(season[i])
			case[0,j].set_title(heure_3h[j])
			case[3,j].set_xlabel(legende_variable)
	case[0,(len(heure_3h)-1)].legend()
	f.suptitle(site+' '+year_study+' SUEwS OBS '+' '+'M '+' v='+str(moruses_version)+' B '+' v='+str(best_version),fontsize=14)
	if (save_plot=='yes') :plt.savefig(save_directory+version_plot+name_file_plot+'_hist_hour_season_SUEWS.png',dpi=300)
	count_figure=count_figure+1

	print count_figure


	print 'done', legende_variable

	#plt.show()

print Var_moruses.mean()
print Var_best.mean()

print 'done'
plt.show()
