#!/usr/bin/python
# -*- coding: utf8 -*-

import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime	
import pandas
from datetime import datetime as dt
from datetime import timedelta
import math
from matplotlib.colors import LinearSegmentedColormap
from dateutil import tz 
import copy
import scipy.stats as stat
import random
from scipy import stats 
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

def daily_mean(variable_1D,list_of_date,val_min=23,missing='No value') :
 #This function calculate the daily mean from variable_1D
 #
 # Imput :
 #	variable_1D list or array with the data. MO missing data, they have to excluded !
 #	list_of_date list of the date corresponding to variable_1D. They have to ne the same size
 #	val_min:nombre de minimum of value that be have to have for 1 day : if it's above this value, we can considere that we have enought value for this day so that it would be representative : we can then calculate the mean. 23 is choosen because we usually have data every 1/2hour and so we say that we need half of every data over one day so that it would be representatitve ((24*2)/2-1)
 #	missing : if a missing value do not appear in variable_1D, let missing='No value'
 #		if a missing value is written as 'nan' in variable_1D, then missing must be 'nan'
 #	result : list with [moyenne,date_moyenne]
 #	moyenne : list of daily mean
 #	date_moyenne : list of date when we where able to calculate the daily mean
 #
 #Initialisation
 compte=0# count the nomber of values that we have for one day. it has to be >val_min
 day_memory=0 #memorization of the day of the data in the loop
 moyenne_1_day=0 # memorization of datas for the day being studying by the loop
 moyenne=[] #result[0]
 date_moyenne=[] #result[1]
 compte_array=[]
# compte=compte+1 
 for i in range(0,len(list_of_date)) :# we study the all list
  #if(missing=='No value') :  compte=compte+1 # me are studying a new data, so we ad 1 to the count
  #if(missing=='nan' and math.isnan(variable_1D[i]) : compte=compte+1
  if (not(math.isnan(variable_1D[i]))) : compte=compte+1
  #print list_of_date[i], compte, day_memory==list_of_date[i].day, variable_1D[i]
  if (day_memory==list_of_date[i].day) : #if the day of the data is the same as the memorized one (meaning the one studyed just above), then we sum it, so that we could have the mean once me chance day betweens 2 datas
    moyenne_1_day=float(np.nansum(np.array([moyenne_1_day,variable_1D[i]])))
    #print 'same day'
    #print 'if1'
  else: #if it's not the same day, it means that we changed day, so we can calculte the mean of the previous day.
    #print 'differente day'
    day_memory=list_of_date[i].day #We memorize the new day so thay we could use it after
    compte_array.append(compte)
    #print 'else1'
    if (compte>val_min) : # we check that we have enought values
      moyenne.append(moyenne_1_day/(compte)) # and so we memorize the daily mean of the previous day
      date_moyenne.append(datetime.datetime(list_of_date[i].year,list_of_date[i].month,list_of_date[i].day)) #and also the day of the previous day
      #print 'if2'
    else :
      moyenne.append(float('nan'))
      date_moyenne.append(datetime.datetime(list_of_date[i].year,list_of_date[i].month,list_of_date[i].day))
    #
    compte=0 #we changed day, so we re-initiate the counter
    moyenne_1_day=variable_1D[i]#We now need to memorize the value that that we could start again with a new day
 #print moyenne
 #print date_moyenne[:10]
 return [moyenne,date_moyenne,compte_array]




def plot_variation_over_time(variable_1D,time,label_y,mini='NaN',maxi='NaN',label_variable=' ',fig_number=None,subplot_number=111) :
 fig = plt.figure(fig_number,figsize=(8,6))
 ax1 = fig.add_subplot(subplot_number)
 p = plt.plot(time,variable_1D, '-k',label=label_variable)
 if (mini!='NaN' or maxi!='NaN'):
   if (mini=='NaN') : mini=variable_1D.min()
   if (maxi=='NaN') : maxi=variable_1D.max()
   axes = plt.gca()
   axes.set_ylim([mini,maxi])
 plt.xlabel('Date')
 plt.ylabel(label_y)
  #plt.title(title_plot)






def add_pwd(way_pwd,file_name):
	#Function creating a list of full pathname to the files in file_name 
	# way_pwd amd file_name can be str or list (if file_name is str then way_pwd must be str)
	# if file_name is str and the result will be str. If it's a list, the result will be a list
	# if file_name is a list and way_pwd is str, then we assume that the path is the same for all files
	# if both are list, he len must be the same
	#	way_pwd : path to the file_name. Can be str is it's the same path for all file or list if it's differente
	#	file_name : name of the file that be want to use. Can be str or list of str depending on how many file we want to extract
	#	result : Can be str or list of str depending on how many file we want to extract
	if(type(file_name)==str and type(way_pwd)==str) : return way_pwd+file_name
	result=['']*len(file_name)
	if(type(file_name)==list and type(way_pwd)==str):
		for i in range(0,len(file_name)) : result[i]=way_pwd+file_name[i]
		return result
	if(type(file_name)==list and type(way_pwd)==list):
		for i in range(0,len(file_name)) : result[i]=way_pwd[i]+file_name[i]



def extract_txt(name_of_file,separateur=',',nomber_header=2):
	#This function extracts dataframe from a file.
	#See add_pwd fir explaination
	#	name_of_file : name of the file that be want to use. Can be str or list of str depending on how many file we want to extract
	#	result : Can be data.frame or list of data.frame depending on how many file we want to extract
	if (type(name_of_file)==str) :
		print 'Reading of the file ...'
		return pandas.read_table(name_of_file, sep = separateur, header=nomber_header, index_col =False)
	elif (type(name_of_file)==list):
		print 'Reading of many files ...'
		list_data=[]
		for i in range(0,len(name_of_file)):
			list_data.append(pandas.read_table(name_of_file[i], sep=separateur, header=nomber_header, index_col =False))
		print 'Reading ok'		
		return list_data

def list_str_to_datetime(list_str) :
  # Convert a list of date in str in list of datetime
  result=[dt.strptime(x,'%d/%m/%Y  %H:%M') for x in list_str]
  return(result)


def extract_variable(list_panda_array,variable,date=False):
	#This function extracts a list (of a list of lists) with just the variable 'variable' that we want to study
	#
	#Imput:	list_panda_array can we a list of data.frame with multiple variables, or only one data.frame
	#	variable : str with the name of the variable that we would like to extract.
	#	date (True or False) : is True if the variable that we want to extract is a date, and if we want it as a datetime
	#
	#Output: a list with:
    #	1. multiple lists for each array that we had with list_panda_array
	 # 2. just one list if list_panda_array is only a dataframe
	if (type(list_panda_array)==list) :
		result=[]
		if (date==True) :
			for i in range(0,len(list_panda_array)) : result.append(list_str_to_datetime(list_panda_array[i][variable].tolist()))
		else :
			for i in range(0,len(list_panda_array)) : result.append(list_panda_array[i][variable].tolist())
		return result
	else : 
		if (date==True) : return list_str_to_datetime(list_panda_array[variable].tolist())
		else : return list_panda_array[variable].tolist()



def missing_measurement(list_date_all,data_measurement,list_date_measurement,toto='non',value_nan=9999.9): 
	# With this fonction, we create differente list dealing with missing data.
	#
	#IMPUT : list_date_all : every date/time where we would have wanted to get a data, but for reason, we may not have it.
	#	data_measurement : list with data. This list can containe some gaps between different times (if the sensor is broken for example)
	#			it can also contain 9999.9 which is a mistake. We want to lead with that.
	#	list_date_measurement : list with date, see data_measurement for more explainations
	#	value_nan : value given in data_measurement to indicate a missing value	
	#	
	#OUTPUT : [0] missing_data : the lenght of this list is the same than for list_date_measurement
	#			we will have one information for each date of list_date_measurement
	#			if we have a measurement, we return a 1, if we don't it a 0.
	#	[1] measurement_periode : same as missing_data, but instead of a 1 if we have a measurement, we get the measurement
	#				instead of a 0 if we don't have measurement, we return None
	#	[2] date_available : we delete the 9999.9 from list_date_all
	#	[2] measurement_available : we delete the 9999.9 from data_measurement
	#missing_data=[None]*len(list_date_all)
	missing_data=np.zeros(len(list_date_all)).tolist()
	measurement_periode=[float('nan')]*len(list_date_all)
	measure_available=[]
	date_available=[]
	j=0
	k=0
	start_j=0
	#if the period of study is not include in the periode of measurement, then  we just return empty data.
	if (list_date_all[0]>list_date_measurement[-1] or list_date_all[-1]<list_date_measurement[0]) :
		print 'out'
		return([missing_data,measurement_periode,date_available,measure_available])
	else:
		print 'in'
	#if it's include, then we need to analyse it.	
	if(list_date_all[0]>list_date_measurement[0]) : # here we want to get the index until the list_date_all is in list_date_measurement
		start_j=list_date_measurement.index(np.array(list_date_measurement)[np.array(list_date_measurement)>=list_date_all[0]].tolist()[0])
		print start_j
	#end_j=len(list_date_measurement)
	end_j=list_date_measurement.index(np.array(list_date_measurement)[np.array(list_date_measurement)<=list_date_all[-1]].tolist()[-1])
	print 'end_j',end_j
	for i in range(0,len(list_date_all)) :
		j=0
		if (list_date_all[i]>list_date_measurement[end_j]):
			print list_date_all[i], list_date_measurement[end_j], 'we have finished to read list_date_measurement'
			return([missing_data,measurement_periode,date_available,measure_available])
		if(list_date_all[i]>list_date_measurement[start_j]):
			while(list_date_all[i]>list_date_measurement[start_j+j]): j=j+1 
		if(list_date_all[i]==list_date_measurement[start_j+j]) :
			#if(data_measurement[start_j+j]!=value_nan) :
			#if(data_measurement[start_j+j]<=value_nan-1) :
			if(abs(data_measurement[start_j+j])<=(abs(value_nan)-1) or not(math.isnan(data_measurement[start_j+j]))):
				date_available.extend([list_date_measurement[start_j+j]])
				measure_available.extend([data_measurement[start_j+j]])
				missing_data[i]=1
				measurement_periode[i]=data_measurement[start_j+j]
				if(toto=='yes') : print 'ok', list_date_all[i],list_date_measurement[start_j+j]
			else :
				if(toto=='yes') : print 'not ok 9999.', list_date_all[i],list_date_measurement[start_j+j]
			start_j=start_j+j
	return [missing_data,measurement_periode,date_available,measure_available]



def quite_modif(list_data,value_inf,value_sup,value_missing=9999.):
	#This fonction change absurd value to 9999.9
	#IMPUT : list_data : list with data which we want ot analyse
	# 	value_inf : if a value is inferior to this value, we considere it is wrong : we put 9999.9 instead
	# 	value_sup : if a value is superior to this value, we considere it is wrong : we put 9999.9 instead
	#OUTPUT : list_return : same list as list_data, but if some value are absurd, we have 9999.9 instead
	list_return=list_data
	for i in (range(0,len(list_data))) :
		if(list_data[i]<value_inf or list_data[i]>value_sup) : list_return[i]=value_missing
	return(list_return)

def change_missing_value(dataset,old_missing,new_missing_value):
	# /!\ Be carfull ! old_missing must be different than float('nan') it must be a int
	old_missing_compare=old_missing
	if(type(new_missing_value)==float) : old_missing_compare=int(old_missing)
	for i in range(0,len(dataset)):
		missing_compare=dataset[i]
		if(type(missing_compare)==float) : missing_compare=int(dataset[i])
		if (missing_compare==old_missing_compare) : dataset[i]=new_missing_value
	return(dataset)


def get_percentile (list_2D,number) :
	#list_2D is a list consitueted with list
	#The idea with this list is that me want the median of each list in the list
	# At the end we will have a list result_list (len(result_list)==len(list_2D)) but with value (median of each list) instead of list
	result_list=[]
	for j in range(0,len(list_2D)):result_list.append(np.nanpercentile(np.array(list_2D[j]),number))
	return result_list

def get_mean (list_2D) :
	#list_2D is a list consitueted with list
	#The idea with this list is that me want the mediane of each list in the list
	# At the end we will have a list result_list (len(result_list)==len(list_2D)) but with value (median of each list) instead of list
	result_list=[]
	for i in range(0,len(list_2D)):result_list.append(np.nanmean(np.array(list_2D[i])))
	return result_list

def remove_nan(list_of_list) :
	result=[]
	for i in range(0,len(list_of_list)):
		result.append((np.array(list_of_list[i])[np.logical_not(np.isnan(np.array(list_of_list[i])))]).tolist())
	return result

def plot_evolution_boxplot(case_plot,list_parameter,x_graduation,str_title,min_param,max_param,do_min_max='yes'):
	#case_plt : case[,] from f, case = plt.subplots()
	#list_parameter : which dataset we want to plot
	#x_graduation
	case_plot.plot(range(0,len(x_graduation)),get_percentile(list_parameter,95),color='w',marker='+',markeredgecolor='k')
	case_plot.plot(range(0,len(x_graduation)),get_percentile(list_parameter,5),color='w',marker='+',markeredgecolor='k')
	case_plot.plot(range(0,len(x_graduation)),get_mean(list_parameter),color='w',marker='x',markeredgecolor='r')
	medianprops = dict(linestyle='-', linewidth=1, color='blue')
	dataset_boxplot=list_parameter
	if(type(list_parameter)!=list) :dataset_boxplot= list_parameter.tolist()
	case_plot.boxplot(remove_nan(dataset_boxplot),positions=range(0,len(x_graduation)),labels=x_graduation, showmeans=False,whis=[1, 99], sym='.',medianprops=medianprops)
	case_plot.set_title(str_title)#,y=0.98)
	case_plot.set_xticks(range(0,len(x_graduation)),x_graduation)
	if (do_min_max=='yes'):case_plot.set_ylim(min_param,max_param)

def plot_line_bloxplot(list_parameter,x_graduation,case_plot=plt,str_color='k',str_label='',transparance=0.1) :
	epaisseur_percentile=0.8
	case_plot.plot(range(0,len(x_graduation)),get_percentile(list_parameter,50),color=str_color,label=str_label,linewidth=1.5)
	case_plot.plot(range(0,len(x_graduation)),get_percentile(list_parameter,95),color=str_color,linestyle='--',linewidth=epaisseur_percentile,alpha=0.7)
	case_plot.plot(range(0,len(x_graduation)),get_percentile(list_parameter,5),color=str_color,linestyle='--',linewidth=epaisseur_percentile,alpha=0.7)
	case_plot.plot(range(0,len(x_graduation)),get_percentile(list_parameter,99),color=str_color,linestyle=':',linewidth=epaisseur_percentile,alpha=0.7)
	case_plot.plot(range(0,len(x_graduation)),get_percentile(list_parameter,1),color=str_color,linestyle=':',linewidth=epaisseur_percentile,alpha=0.7)
	case_plot.fill_between(range(0,len(x_graduation)), get_percentile(list_parameter,25), get_percentile(list_parameter,75),color=str_color,alpha=transparance)
	case_plot.scatter(len(x_graduation),np.mean(np.array(get_mean(list_parameter))),color=str_color,marker='+')


def get_median (list_2D) :
	#list_2D is a list consitueted with list
	#The idea with this list is that me want the mediane of each list in the list
	# At the end we will have a list result_list (len(result_list)==len(list_2D)) but with value (median of each list) instead of list
	result_list=[]
	for i in range(0,len(list_2D)):result_list.append(statistics.median(list_2D[i]))
	return result_list


def MAE(list_1,list_2):
	#Calculation of MAE from 2 list
	if(type(list_1)==list) : list_1=np.array(list_1)
	if(type(list_2)==list) : list_2=np.array(list_2)
	if (list_2.shape != list_1.shape ) :
		print 'list_1 and list_2 have to be the same size !'
		return []
	else : 
		return np.around(np.nanmean(abs(np.array(list_1)-np.array(list_2))),2)

def RMSE(list_1,list_2):
	#Calculation of MAE from 2 list
	if(type(list_1)==list) : list_1=np.array(list_1)
	if(type(list_2)==list) : list_2=np.array(list_2)
	if (list_2.shape != list_1.shape ) :
		print 'list_1 and list_2 have to be the same size !'
		return []
	else : 
		return np.around(math.sqrt(np.nanmean((np.array(list_1)-np.array(list_2))*(np.array(list_1)-np.array(list_2)))),2)

def correlation(list_1,list_2,num_round=2):
	#Calculation of MAE from 2 list
	if(type(list_1)==list) : list_1=np.array(list_1)
	if(type(list_2)==list) : list_2=np.array(list_2)
	if (list_2.shape != list_1.shape ) :
		print 'list_1 and list_2 have to be the same size !'
		return []
	else : 
		df=pandas.DataFrame({'list1':list_1,'list2':list_2})
		return np.around(df.corr()['list2']['list1'],num_round)


def print_list(liste):
	# If we want to print each element of a list
	for i in range(0,len(liste)): print i, liste[i]

def nan_list(dataset):
	#This fonction return True is we have at least one 'nan'. And False if there is no missing value
	# Input : dataset must be a list
	# Output : Boolean
	i=0
	stop='no'
	for i in range(0,len(dataset)):
		print dataset[i]
		if (dataset[i] != dataset[i]) : return True
	return False



def divide_periode_day(which_periode,dataset,dataset_time,which_day=0):
	#This function devide dataset into each season or month
	#Input : which_periode ('season' or 'month') : periode that we want to split. Possible values : 'season' or 'month'
	#	 which_day (integer between 1 and 24, multiple of 24) : periode for which we want to split one day (ex: 1 to split each hour)
	#		if we don't want to split days, we give 0	
	#	 dataset: dataset that we want to 
	#	 dataset_time : time corresponding to dataset. It must be the same size as dataset
	result_periode=[]
	size_divide=1
	if(which_periode=='season') : size_divide=4
	if(which_periode=='month') : size_divide=12
	if(which_periode=='year') : size_divide=dataset_time[0].year-dataset_time[-1].year+1
	#
	#Initialisation
	for i in range(0,size_divide) :result_periode.append([])
	if (which_day !=0) :# if we also want to split between each day
		for i in range(0,size_divide) :
			for j in range(0,24/which_day) : result_periode[i].append([])
			print 'initialisation divide day ok'
	#			
	#Classification
	if (which_periode=='season' and which_day==0) : 
		for i in range(0,len(dataset_time)) : result_periode[((dataset_time[i].month)/3)%4].append(dataset[i])
		print 'ok1'
	if (which_periode=='month' and which_day==0) : 
		for i in range(0,len(dataset_time)) : result_periode[((dataset_time[i].month)-1)].append(dataset[i])
		print 'ok2'
	if (which_periode=='season' and which_day!=0) :
		for i in range (0,len(dataset_time)) : result_periode[((dataset_time[i].month)/3)%4][(dataset_time[i].hour)/which_day].append(dataset[i])
		print 'ok3'
	if (which_periode=='month' and which_day!=0) :
		for i in range (0,len(dataset_time)) : result_periode[((dataset_time[i].month)-1)][(dataset_time[i].hour)/which_day].append(dataset[i])
		print 'ok4'
	if (which_periode=='year' and which_day!=0) :
		for i in range (0,len(dataset_time)) : result_periode[((dataset_time[i].year)-dataset_time[0].year)][(dataset_time[i].hour)/which_day].append(dataset[i])
	if (which_periode=='all' and which_day!=0) :
		for i in range (0,len(dataset_time)) : result_periode[0][(dataset_time[i].hour)/which_day].append(dataset[i])
	return result_periode




def divide_periode_day_climate(which_periode,dataset,dataset_time,which_day=0):
	#This function devide dataset into each season or month
	#Input : which_periode ('season' or 'month') : periode that we want to split. Possible values : 'season' or 'month'
	#	 which_day (integer between 1 and 24, multiple of 24) : periode for which we want to split one day (ex: 1 to split each hour)
	#		if we don't want to split days, we give 0	
	#	 dataset: dataset that we want to 
	#	 dataset_time : time corresponding to dataset. It must be the same size as dataset
	result_periode=[]
	size_divide=1
	if(which_periode=='season') : size_divide=4
	if(which_periode=='month') : size_divide=12
	if(which_periode=='year') : size_divide=dataset_time[0].year-dataset_time[-1].year+1
	#
	#Initialisation
	for i in range(0,size_divide) :result_periode.append([])
	if (which_day !=0) :# if we also want to split between each day
		for i in range(0,size_divide) :
			for j in range(0,24/which_day) : result_periode[i].append([])
			print 'initialisation divide day ok'
	day_frac=[]
	for i in range(0,24):
		day_frac.append(round(float(i)/24,4))
	#Classification
	if (which_periode=='season' and which_day==0) : 
		for i in range(0,len(dataset_time)) : result_periode[int(dataset_time[i])/90%4].append(dataset[i])
		print 'ok1'
	if (which_periode=='month' and which_day==0) : 
		for i in range(0,len(dataset_time)) : result_periode[int(dataset_time[i])/30%12].append(dataset[i])
		print 'ok2'
	if (which_periode=='season' and which_day!=0) :
		for i in range (0,len(dataset_time)) : result_periode[int(dataset_time[i])/90%4][day_frac.index(round(dataset_time[i]-int(dataset_time[i]),4))].append(dataset[i])
		print 'ok3'
	if (which_periode=='month' and which_day!=0) :
		for i in range (0,len(dataset_time)) : result_periode[int(dataset_time[i])/30%12][day_frac.index(round(dataset_time[i]-int(dataset_time[i]),4))].append(dataset[i])
		print 'ok4'
	#if (which_periode=='year' and which_day!=0) :
		for i in range (0,len(dataset_time)) : result_periode[((dataset_time[i].year)-dataset_time[0].year)][(dataset_time[i].hour)/which_day].append(dataset[i])
	#if (which_periode=='all' and which_day!=0) :
		for i in range (0,len(dataset_time)) : result_periode[0][(dataset_time[i].hour)/which_day].append(dataset[i])
	return result_periode







def convert_UTC_to_local(list_date,zone):
	result=list_date[:]
	zone_UTC = tz.gettz('UTC')
	zone_local = tz.gettz(zone)
	utc=0
	for i in range(0,len(list_date)):
		utc=list_date[i]
		utc = utc.replace(tzinfo=zone_UTC)
		result[i]=utc.astimezone(zone_local)
	return(result)





def get_variable_suews(folder,list_file,variable):
	#Extract variable from SUEWS file
	if(type(list_file)==str):
		return(change_missing_value(np.array(extract_variable(extract_txt(folder+name_file_suews[i],nomber_header=0,separateur="\s+"), name_variable_SUEWS)),-999,float('nan')))
	else:
		result=[]
		for i in range(0,len(list_file)):
			result.extend(change_missing_value(np.array(extract_variable(extract_txt(folder+list_file[i],nomber_header=0,separateur="\s+"), variable)),-999,float('nan')))
		return(result)




def get_time_suews(folder,list_file,Start_time,name_year='%iy'):
	#Extract time from SUEWS file
	if(type(list_file)==str):
		y=change_missing_value(np.array(extract_variable(extract_txt(folder+list_file,nomber_header=0,separateur="\s+"), name_year)),-999,float('nan'))
		d=change_missing_value(np.array(extract_variable(extract_txt(folder+list_file,nomber_header=0,separateur="\s+"), 'id')),-999,float('nan'))
		t=change_missing_value(np.array(extract_variable(extract_txt(folder+list_file,nomber_header=0,separateur="\s+"), 'it')),-999,float('nan'))
		m=change_missing_value(np.array(extract_variable(extract_txt(folder+list_file,nomber_header=0,separateur="\s+"), 'imin')),-999,float('nan'))
		result=[]
		for j in range (0,len(y)):
			result.append(Start_time.replace(year=y[j], hour=t[j], minute=m[j]))
			#result[-1]=result[-1]+datetime.timedelta(days=d[j]-1)
		return(result)
	else:
		result=[]
		for i in range(0,len(list_file)):
			y=change_missing_value(np.array(extract_variable(extract_txt(folder+list_file[i],nomber_header=0,separateur="\s+"), name_year)),-999,float('nan'))
			d=change_missing_value(np.array(extract_variable(extract_txt(folder+list_file[i],nomber_header=0,separateur="\s+"), 'id')),-999,float('nan'))
			t=change_missing_value(np.array(extract_variable(extract_txt(folder+list_file[i],nomber_header=0,separateur="\s+"), 'it')),-999,float('nan'))
			m=change_missing_value(np.array(extract_variable(extract_txt(folder+list_file[i],nomber_header=0,separateur="\s+"), 'imin')),-999,float('nan'))
			for j in range (0,len(y)):
				result.append(Start_time.replace(year=y[j], hour=t[j], minute=m[j]))
				#result[-1]=result[-1]+datetime.timedelta(days=d[j]-1)
		return(result)
        
        
def get_variable_suews_2(folder,file_name,variable):
	#read in the data
    data = pandas.read_excel(folder + file_name)
    #conver all fill values to NaN
    data_filled = pandas.DataFrame.fillna(data, value=-999)
    #extract variable
    Var = data_filled[variable]
    return Var
      
             

def select_time(dataset, time, time_min, time_max):
	return_dataset=[]
	return_time=[]
	for i in range(0,len(dataset)):
		if(time[i]<time_max and time[i]>=time_min) :
			return_dataset.append(dataset[i])
			return_time.append(time[i])	
	return([return_dataset,return_time])




def month_mean(variable_1D,list_of_date,val_min=23,missing='No value') :
 #This function calculate the daily mean from variable_1D
 #
 # Imput :
 #	variable_1D list or array with the data. MO missing data, they have to excluded !
 #	list_of_date list of the date corresponding to variable_1D. They have to ne the same size
 #	val_min:nombre de minimum of value that be have to have for 1 day : if it's above this value, we can considere that we have enought value for this day so that it would be representative : we can then calculate the mean. 23 is choosen because we usually have data every 1/2hour and so we say that we need half of every data over one day so that it would be representatitve ((24*2)/2-1)
 #	missing : if a missing value do not appear in variable_1D, let missing='No value'
 #		if a missing value is written as 'nan' in variable_1D, then missing must be 'nan'
 #	result : list with [moyenne,date_moyenne]
 #	moyenne : list of daily mean
 #	date_moyenne : list of date when we where able to calculate the daily mean
 #
 #Initialisation
 compte=0# count the number of values that we have for one day. it has to be >val_min
 day_memory=list_of_date[0].month #memorization of the day of the data in the loop
 year_memory=list_of_date[0].year #memorization of the day of the data in the loop
 moyenne_1_day=0 # memorization of datas for the day being studying by the loop
 moyenne=[] #result[0]
 date_moyenne=[] #result[1]
 compte_array=[]
 # compte=compte+1 
 for i in range(0,len(list_of_date)) :# we study the all list
  if (not(math.isnan(variable_1D[i]))) : compte=compte+1
  if (day_memory==list_of_date[i].month and year_memory==list_of_date[i].year) : 
    moyenne_1_day=float(np.nansum(np.array([moyenne_1_day,variable_1D[i]])))
    #print 'same day'
    #print 'if1'
  else: #if it's not the same day, it means that we changed day, so we can calculte the mean of the previous day.
    #print 'differente day'
    day_memory=list_of_date[i].month #We memorize the new month so thay we could use it after
    year_memory=list_of_date[i].year #We memorize the new year so thay we could use it after
    compte_array.append(compte)
    #print 'else1'
    if (compte>val_min) : # we check that we have enought values
      moyenne.append(moyenne_1_day/(compte)) # and so we memorize de daily mean of the previous day
      date_moyenne.append(datetime.datetime(list_of_date[i-1].year,list_of_date[i-1].month,15)) #and also the day of the previous day
      #print 'if2'
    else :
      moyenne.append(float('nan'))
      date_moyenne.append(datetime.datetime(list_of_date[i-1].year,list_of_date[i-1].month-1,15))
    #
    compte=0 #we changed day, so we re-initiate the counter
    moyenne_1_day=variable_1D[i]#We now need to memorize the value that that we could start again with a new day
  if(i==len(list_of_date)-1 and compte>val_min):
     moyenne.append(moyenne_1_day/(compte)) # and so we memorize de daily mean of the previous day
     print list_of_date[i].month
     date_moyenne.append(datetime.datetime(list_of_date[i].year,list_of_date[i].month,15)) #and also the day of the previous day
 #print moyenne
 #print date_moyenne[:10]
 return [moyenne,date_moyenne,compte_array]


def convert_time_obs_datetime(date,heure=None):
	datetime_return=[]
	if (heure==None):
		for i in range(0,len(date)):
			datetime_return.append(datetime.datetime(date[i]/10000, date[i]/100%(date[i]/10000), date[i]%(date[i]/100), 00, 00))
	else :
		for i in range(0,len(date)):
			datetime_return.append(datetime.datetime(date[i]/10000, date[i]/100%(date[i]/10000), date[i]%(date[i]/100), heure[i]/100,heure[i]%100))
		
	return (datetime_return)


