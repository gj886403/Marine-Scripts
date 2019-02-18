#!/usr/bin/python
# -*- coding: utf8 -*-

from fonction import *
from jules_download import *
from Split_times_Marine import *



save_plot='no'
#version_plot='' #OBS and AnthroOff
version_plot='AnthroOn_' #OBS and AnthroOn
#version_plot='WFDEI_AnthroOff_' #WFDEI and AnthroOff
#version_plot='WFDEI_AnthroOn_' #WFDEI and AnthroOn

#var=['SW_up','QH','Q_star','K_star','K_down','L_up','L_down']
var=['L_up']



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



	#legende_variable='Albedo '
	#name_variable_JULES='albedo_land'
	#name_file_plot='Albedo'
	#with_obs='no'
	#with_SUEWS='no'

	#legende_variable='Emissivity '
	#name_variable_JULES='emis_gb'
	#name_file_plot='Emisivity'
	#with_obs='no'
	#with_SUEWS='no'

	##LONDON
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
		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/OTHER'# Anthropogenic Flux OFF
		moruses_version_OBS=74899# Anthropogenic Flux OFF
		#best_version_OBS=74898# Anthropogenic Flux OFF
		moruses_version_WFDEI=74885# Anthropogenic Flux ON
		#best_version_WFDEI=74884# Anthropogenic Flux ON
	elif(version_plot=='AnthroOn_'):
		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/OTHER'# Anthropogenic Flux ON
		moruses_version_OBS=74930# Anthropogenic Flux ON
		best_version_OBS=74929# Anthropogenic Flux ON
		#moruses_version_WFDEI=74281# Anthropogenic Flux ON
		#best_version_WFDEI=74280# Anthropogenic Flux ON
		moruses_version_OBS_new=76277# Anthropogenic Flux ON
		best_version_OBS_new=76268# Anthropogenic Flux ON
		#moruses_version_OBS_new=76091# Anthropogenic Flux ON
#	elif(version_plot=='WFDEI_AnthroOff_'):
#		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOff/KC/'# Anthropogenic Flux ON
#		moruses_version=74885# Anthropogenic Flux ON
#		best_version=74884# Anthropogenic Flux ON
#	elif(version_plot=='WFDEI_AnthroOn_'):
#		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOn/KC/'# Anthropogenic Flux ON
#		moruses_version=74281# Anthropogenic Flux ON
#		best_version=74280# Anthropogenic Flux ON

#f=Dataset(moruses_folder+str(moruses_version_OBS)+'/jules.all.nc','r')
#for v in f.variables : print '*****', v, f.variables[v]

#print '------------------------------------------------'

#f=Dataset(moruses_folder+str(moruses_version_OBS_new)+'/jules.all.nc','r')
#for v in f.variables : print '*****', v, f.variables[v]

#print '------------------------------------------------'

print moruses_folder+str(moruses_version_OBS)+'/jules.all.nc'
print best_folder+str(best_version_OBS)+'/jules.all.nc'
print name_variable_JULES
Var_moruses_OBS=jules_download(moruses_folder+str(moruses_version_OBS)+'/jules.all.nc',name_variable_JULES,Start)[0]
Var_best_OBS=jules_download(best_folder+str(best_version_OBS)+'/jules.all.nc',name_variable_JULES,Start)[0]

print moruses_folder+str(moruses_version_OBS_new)+'/jules.all.nc'
print best_folder+str(best_version_OBS_new)+'/jules.all.nc'
print name_variable_JULES
Var_moruses_OBS_new=jules_download(moruses_folder+str(moruses_version_OBS_new)+'/jules.all.nc',name_variable_JULES,Start)[0]
Var_best_OBS_new=jules_download(best_folder+str(best_version_OBS_new)+'/jules.all.nc',name_variable_JULES,Start)[0]
Time_moruses=jules_download(moruses_folder+str(moruses_version_OBS)+'/jules.all.nc',name_variable_JULES,Start)[1]
Time_moruses_new=jules_download(moruses_folder+str(moruses_version_OBS_new)+'/jules.all.nc',name_variable_JULES,Start)[1]

print len(Time_moruses_new)
print len(Time_moruses)

print max(Time_moruses_new)
print max(Time_moruses)

print min(Time_moruses_new)
print min(Time_moruses)

print len(Var_moruses_OBS_new)
print len(Var_moruses_OBS)

print max(Var_moruses_OBS_new)
print max(Var_moruses_OBS)

print min(Var_moruses_OBS_new)
print min(Var_moruses_OBS)



plt.figure()
plt.plot(Time_moruses_new,Var_moruses_OBS_new,color='r')
plt.plot(Time_moruses,Var_moruses_OBS,color='b')

plt.figure()
plt.plot(Time_moruses_new,Var_moruses_OBS_new-Var_moruses_OBS,color='r')

plt.figure()
plt.plot(Time_moruses_new,Var_best_OBS_new,color='r')
plt.plot(Time_moruses,Var_best_OBS,color='b')

plt.figure()
plt.plot(Time_moruses_new,Var_best_OBS_new-Var_best_OBS,color='r')

fig=plt.figure(figsize=(16,8)) #We now want to plot
ax1 = fig.add_subplot(121)

#plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0.05, hspace=0.05)

fig.add_subplot(121)
plt.plot(Time_moruses_new,Var_best_OBS_new-Var_best_OBS,color='r')
plt.ylabel('QH $W.m^{-2}$')
plt.title('Best New-Old')

fig.add_subplot(122)
plt.plot(Time_moruses_new,Var_moruses_OBS_new-Var_moruses_OBS,color='r')
plt.ylabel('QH $W.m^{-2}$')
plt.title('MORUSES New-Old')
print save_directory+'/comparaison_JULES.png'
plt.savefig(save_directory+'/comparaison_JULES.png',dpi=300)

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
#		moruses_version=72432# Anthropogenic Flux ON
#		best_version=72433# Anthropogenic Flux ON
#	elif(version_plot=='WFDEI_AnthroOn_'):
#		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOn/Shanghai/'# Anthropogenic Flux ON
#		moruses_version=72481# Anthropogenic Flux ON
#		best_version=72480# Anthropogenic Flux ON


##	#Beijing
##	site='Beijing'
##	moruses_folder='/storage/shared/research/met/micromet/JULES/u-aw219_MORUSES_Beijing_IAP/'
##	best_folder='/storage/shared/research/met/micromet/JULES/u-aw217_1-tile_Beijing_IAP/'
##	#obs_folder=
##	#suews_folder=
##	#name_file_suews=
##	local_time='Asia/Shanghai'
##	Start= datetime.datetime(2014, 01, 01,00,00,00)
##	#Start_SUEWS= 
##	year_study='2014-2015'
##	year_study_short='14-15'
##	with_obs='no'
##	local_hour=8
##	with_SUEWS='no'

##	#if(version_plot==''):
##		#save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/AnthroOff/Beijing/'# Anthropogenic Flux OFF
##		#moruses_version=74899# Anthropogenic Flux OFF
##		#best_version=74898# Anthropogenic Flux OFF
##	#elif(version_plot=='AnthroOn_'):
##		#save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/AnthroOn/Beijing/'# Anthropogenic Flux ON
##		#moruses_version=74930# Anthropogenic Flux ON
##		#best_version=74929# Anthropogenic Flux ON
##	if(version_plot=='WFDEI_AnthroOff_'):
##		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOff/Beijing/'# Anthropogenic Flux ON
##		moruses_version=72487# Anthropogenic Flux ON
##		best_version=72486# Anthropogenic Flux ON
##	elif(version_plot=='WFDEI_AnthroOn_'):
##		save_directory='/storage/shared/research/met/micromet/JULES/Marine/FIGURE/WFDEI_AnthroOn/Beijing/'# Anthropogenic Flux ON
##		moruses_version=72662# Anthropogenic Flux ON
##		best_version=72661# Anthropogenic Flux ON


#	#### Here are the files that we want to study : (NetCDF files)


#	########################## JULES

#	#name_variable_JULES='ftl_gb'


#	Var_moruses_OBS=jules_download(moruses_folder+str(moruses_version_OBS)+'/jules.all.nc',name_variable_JULES,Start)[0]
#	Var_best_OBS=jules_download(best_folder+str(best_version_OBS)+'/jules.all.nc',name_variable_JULES,Start)[0]
#	Var_moruses_WFDEI=jules_download(moruses_folder+str(moruses_version_WFDEI)+'/jules.all.nc',name_variable_JULES,Start)[0]
#	Var_best_WFDEI=jules_download(best_folder+str(best_version_WFDEI)+'/jules.all.nc',name_variable_JULES,Start)[0]

#	if(name_file_plot=='AnthroOn_SW_up' or name_file_plot=='SW_up'):
#		Var_moruses_1_OBS=jules_download(moruses_folder+str(moruses_version_OBS)+'/jules.all.nc',name_variable_JULES,Start)[0]
#		Var_best_1_OBS=jules_download(best_folder+str(best_version_OBS)+'/jules.all.nc',name_variable_JULES,Start)[0]
#		Var_moruses_2_OBS=jules_download(moruses_folder+str(moruses_version_OBS)+'/jules.all.nc',name_variable_JULES2,Start)[0]
#		Var_best_2_OBS=jules_download(best_folder+str(best_version_OBS)+'/jules.all.nc',name_variable_JULES2,Start)[0]
#		Var_moruses_OBS=Var_moruses_2_OBS-Var_moruses_1_OBS
#		Var_best_OBS=Var_best_2_OBS-Var_best_1_OBS
#		Var_moruses_1_WFDEI=jules_download(moruses_folder+str(moruses_version_WFDEI)+'/jules.all.nc',name_variable_JULES,Start)[0]
#		Var_best_1_WFDEI=jules_download(best_folder+str(best_version_WFDEI)+'/jules.all.nc',name_variable_JULES,Start)[0]
#		Var_moruses_2_WFDEI=jules_download(moruses_folder+str(moruses_version_WFDEI)+'/jules.all.nc',name_variable_JULES2,Start)[0]
#		Var_best_2_WFDEI=jules_download(best_folder+str(best_version_WFDEI)+'/jules.all.nc',name_variable_JULES2,Start)[0]
#		Var_moruses_WFDEI=Var_moruses_2_WFDEI-Var_moruses_1_WFDEI
#		Var_best_WFDEI=Var_best_2_WFDEI-Var_best_1_WFDEI

#	Time_moruses=jules_download(moruses_folder+str(moruses_version_OBS)+'/jules.all.nc',name_variable_JULES,Start)[1]
#	if(local_time!='Europe/London') : Time_moruses=convert_UTC_to_local(Time_moruses,local_time)
#	Time_best=jules_download(best_folder+str(best_version_OBS)+'/jules.all.nc',name_variable_JULES,Start)[1]
#	if(local_time!='Europe/London') : Time_best=convert_UTC_to_local(Time_best,local_time)

#	lon=jules_download(moruses_folder+str(moruses_version_OBS)+'/jules.all.nc','longitude',Start)[0]
#	lat=jules_download(moruses_folder+str(moruses_version_OBS)+'/jules.all.nc','latitude',Start)[0]

#	if  (Time_moruses!=Time_best) : print 'MORUSES and Best are not the same size'
#	print 'lon',lon,'lat',lat



#	Var_saison_m_OBS=divide_periode_day('season',Var_moruses_OBS,Time_moruses)
#	Var_saison_b_OBS=divide_periode_day('season',Var_best_OBS,Time_moruses)

#	Var_saison_m_WFDEI=divide_periode_day('season',Var_moruses_WFDEI,Time_moruses)
#	Var_saison_b_WFDEI=divide_periode_day('season',Var_best_WFDEI,Time_moruses)

#	Time_saison=divide_periode_day('season',Time_moruses,Time_moruses)


#	#Var_saison_3h_b=divide_periode_day('season',Var_best,Time_moruses,which_day=3)
#	#Var_saison_3h_m=divide_periode_day('season',Var_moruses,Time_moruses,which_day=3)
#	#Time_saison_3h=divide_periode_day('season',Time_moruses,Time_moruses,which_day=3)

#	#if with_obs=='yes' : Var_saison_h_OBS=divide_periode_day('season',Var_missing_OBS,Time_moruses,which_day=1)
#	#if with_SUEWS=='yes' : Var_saison_h_SUEWS=divide_periode_day('season',Var_missing_SUEWS,Time_moruses,which_day=1)
#	#Var_saison_h_b=divide_periode_day('season',Var_best,Time_moruses,which_day=1)
#	#Var_saison_h_m=divide_periode_day('season',Var_moruses,Time_moruses,which_day=1)
#	#Time_saison_h=divide_periode_day('season',Time_JULES,Time_JULES,which_day=1)



#season=['Winter DJF','Spring MAM','Summer JJA','Autumn SON']


#plt.figure()
#plt.scatter(Var_moruses_OBS,Var_moruses_WFDEI,marker='+')

#plt.figure()
#plt.scatter(Var_best_OBS,Var_best_WFDEI,marker='+')

#plt.figure()
#plt.scatter(Var_saison_m_OBS[0],Var_saison_b_WFDEI[0],marker='+')
#plt.title(season[0])
#print max(Var_saison_m_OBS[0])
#print [max(Var_saison_m_OBS[0]),max(Var_saison_m_OBS[0])]
#print max([max(Var_saison_m_OBS[0]),max(Var_saison_m_OBS[0])])
#plt.plot([0,max([max(Var_saison_m_OBS[0]),max(Var_saison_m_OBS[0])])],[0,max([max(Var_saison_m_OBS[0]),max(Var_saison_m_OBS[0])])],color='r')

#plt.figure()
#plt.scatter(Var_saison_m_OBS[1],Var_saison_b_WFDEI[1],marker='+')
#plt.title(season[1])
#plt.plot([0,max([max(Var_saison_m_OBS[1]),max(Var_saison_m_OBS[1])])],[0,max([max(Var_saison_m_OBS[1]),max(Var_saison_m_OBS[1])])],color='r')

#plt.figure()
#plt.scatter(Var_saison_m_OBS[2],Var_saison_b_WFDEI[2],marker='+')
#plt.title(season[2])
#plt.plot([0,max([max(Var_saison_m_OBS[2]),max(Var_saison_m_OBS[2])])],[0,max([max(Var_saison_m_OBS[2]),max(Var_saison_m_OBS[2])])],color='r')

#plt.figure()
#plt.scatter(Var_saison_m_OBS[3],Var_saison_b_WFDEI[3],marker='+')
#plt.title(season[3])
#plt.plot([0,max([max(Var_saison_m_OBS[3]),max(Var_saison_m_OBS[3])])],[0,max([max(Var_saison_m_OBS[3]),max(Var_saison_m_OBS[3])])],color='r')




#plt.figure()
#plt.scatter(Var_saison_m_OBS[0],Var_saison_b_WFDEI[0],marker='+')

#plt.scatter(Var_saison_m_OBS[1],Var_saison_b_WFDEI[1],marker='+')

#plt.scatter(Var_saison_m_OBS[2],Var_saison_b_WFDEI[2],marker='+')

#plt.scatter(Var_saison_m_OBS[3],Var_saison_b_WFDEI[3],marker='+')




#plt.figure()
plt.show()

