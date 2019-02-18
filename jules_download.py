#!/usr/bin/python
# -*- coding: utf8 -*-

######################################################
#		Download JULES variable
######################################################

######################################################
# The aims of this file is to download a variable from JULES Files
#
# Variables in JULES :
# time_bounds and time in second
# latitude and longiture (float)
# Gridbox variables : 
# 	fqw_gb (moisture flux from the surface), ftl_gb (surface sensible heat flux), t_start_gb (Surface Temeprature), surf_ht_flux (downward heat flux at the surface over sea-ice fraction), snow_mass
# 	latent_heat
# Layer variables, 4 levels :
#	smcl (humidity), t_soil (soil temperature) 
# Other variable
######################################################

from fonction import *

def jules_download(name_file,name_variable,datetime_start) :
	f = Dataset(name_file, 'r')
	Var_JULES= np.squeeze(f.variables[name_variable][:])
	Time = np.squeeze(f.variables['time'][:])
	Date_list = [datetime_start + datetime.timedelta(seconds=x) for x in Time.tolist()]
	print 'Reading JULES Files ok'
	return [Var_JULES,Date_list]


