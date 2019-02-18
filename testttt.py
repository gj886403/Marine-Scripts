# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:39:56 2018

@author: qw919026
"""
from fonction import *

def change_missing_value(dataset,old_missing,new_missing_value):
	# /!\ Be carfull ! old_missing must be different than float('nan') it must be a int
	old_missing_compare=old_missing
	if(type(new_missing_value)==float) : old_missing_compare=int(old_missing)
	for i in range(0,len(dataset)):
		missing_compare=dataset[i]
		if(type(missing_compare)==float) : missing_compare=int(dataset[i])
		if (missing_compare==old_missing_compare) : dataset[i]=new_missing_value
	return(dataset)

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
        
        
        
var=['SW_up']
var= ['QH']
name_file_plot='SW_up'
name_variable_SUEWS='kup'

suews_folder='C:/Users/qw919026/Desktop/JULES/JULES runs/SUEWS_output_KSSW/' # Folder with suews
file_name = 'suews_2011_2013.xlsx'
name_file_suews=['Kc1_2011_60.txt','Kc1_2012_60.txt','Kc1_2013_60.txt'] #Name of the file in SUEWS's folder
local_time='Europe/London' #For london, the local time does not really matter : LONDON is +00
Start_SUEWS= datetime.datetime(2011, 01, 01, 00, 00, 00) #First time step in SUEWS


Var_SUEWS=np.array(get_variable_suews(suews_folder,name_file_suews,name_variable_SUEWS))
Time_SUEWS=get_time_suews(suews_folder,name_file_suews,Start_SUEWS)
#Var_missing_SUEWS=missing_measurement(Time_moruses,Var_SUEWS,Time_SUEWS,value_nan=-999.)[1]


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
		Var_missing_SUEWS=missing_measurement(Time_moruses,Var_SUEWS,Time_SUEWS,value_nan=-999.)[1]



Var_SUEWS = suews_2011_2013[var]
Time_SUEWS = suews_2011_2013['DateTime']

suews_2011_2013 = pandas.read_excel(suews_folder + file_name)
suews_2011_2013_filled = pandas.DataFrame.fillna(suews_2011_2013, value=-999)

def get_variable_suews_2(folder,file_name,variable):
	#read in the data
    data = pandas.read_excel(folder + file_name)
    #conver all fill values to NaN
    data_filled = pandas.DataFrame.fillna(data, value=-999)
    #extract variable
    Var = data_filled[variable]
    return Var



def get_time_suews_2(folder,file_name):
    #read in the data
    data = pandas.read_excel(folder + file_name)
    #conver all fill values to NaN
    data_filled = pandas.DataFrame.fillna(data, value=-999)
    #extract variable
    Time_SUEWS = data_filled['DateTime']
    #convert form datetime64[ns] to datetime.datetime obj
    Time_SUEWS = Time_SUEWS.to_pydatetime()
    return Time_SUEWS
      
	
Var_SUEWS = get_variable_suews_2(suews_folder, file_name, name_variable_SUEWS)        
Time_SUEWS = get_time_suews_2(suews_folder, file_name)

rng = pandas.date_range(start='01/01/2011 01:00',end='01/01/2014 00:00', freq='H')

new = rng.to_pydatetime().tolist()

#Time_SUEWS_list = Time_SUEWS.tolist()

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
		else : Var_SUEWS=np.array(get_variable_suews_2(suews_folder,name_file_suews,name_variable_SUEWS))
		Time_SUEWS=get_time_suews_2(suews_folder,name_file_suews)
		if(local_time!='Europe/London') : Time_SUEWS=convert_UTC_to_local(Time_SUEWS,local_time)
		Var_missing_SUEWS=missing_measurement(Time_moruses,Var_SUEWS,Time_SUEWS,value_nan=-999.)[1]







