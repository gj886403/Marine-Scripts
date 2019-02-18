#!/bin/env python2.7


import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

import sys,os


def optional_argparse(arg,default):
    if arg in sys.argv:
        temp_loc=sys.argv.index(arg)
        temp_arg=sys.argv.pop(temp_loc)
        value=sys.argv.pop(temp_loc)
    else:
        value=default
    return value

def get_nc_timeobj(invar):
    time_obj = nc.num2date(invar[:],units=invar.units,calendar=invar.calendar)
    return time_obj

# Input directories and filename options
data_dir= optional_argparse('-data_dir', '../../JULES_Tutorial/output')
if data_dir[-1]!='/': data_dir+='/'
run_ids  = optional_argparse('-run_ids', 'experiment1,experiment2').split(',')
profile_id  = optional_argparse('-profile_id', 'timestep')

# Set plot directory, and create if necessary
plot_dir= optional_argparse('-plot_dir', '../../JULES_Tutorial/plots')
if  not os.path.isdir(plot_dir): os.system('mkdir -p '+plot_dir)

# Set plot_tag, default is the [run_id]_[profile_id]
plot_tag = optional_argparse('-plot_tag',profile_id)

# Choose variables to plot
plot_vars = optional_argparse('-plots_vars','fqw_gb,ftl_gb,t_soil,smc_tot').split(',')
nplotvars = len(plot_vars)
print(nplotvars,plot_vars)

#z_method = optional_argparse('-z_method','surface')
#z_method = optional_argparse('-z_method','median')
z_method = optional_argparse('-z_method','mean')

data={}

for run_id in run_ids:
    data[run_id] = {}
    # construct file name
    infile = data_dir+run_id+'.'+profile_id+'.nc'

    # Read in data from file:
    print(infile)
    inf=nc.Dataset(infile,'r')

    #first get the time data:
    time_obj = get_nc_timeobj(inf.variables['time']).squeeze()
    #print(time_obj)

    # Loop over input variables and store data in a dictionary:
    for var in plot_vars:
        indata = inf.variables[var][:].squeeze()
        while len(indata.shape)>1:
            if z_method=='mean':
                indata = indata.mean(axis=-1)
            elif z_method=='median':
                indata = indata.median(axis=-1)
            elif z_method=='surface':
                indata = indata[:,0]
            elif 'z_layer' in z_method:
                z_layer=int(z_method[-1:])
                indata = indata[:,z_layer]
            else:
                print('Unrecognised Z method')

        data[run_id][var] = indata

    inf.close()


# Create figure to plot time-series:
fig,axes = plt.subplots(ncols=1,nrows=nplotvars, figsize=(12,4*nplotvars) )
fig.subplots_adjust(hspace=0.3, bottom=0.07)

for run_id in run_ids:
    for ivar in range(nplotvars):
        var = plot_vars[ivar]
        ax = axes[ivar]

        ax.plot(time_obj,data[run_id][var],label=run_id)
        ax.set_title(var)

fig.savefig(plot_dir,bbox_inches='tight')
handles,labels=ax.get_legend_handles_labels()
fig.legend(handles,labels,ncol=nplotvars, loc=8)
plt.show()
