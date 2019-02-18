#!/usr/bin/python
# -*- coding: utf8 -*-

from fonction import *

save_directory='/home/sufs1/ru5/sw/fq208733/WORKDIR/FIGURE/Other/'
save_plot='no'


toto=np.random.rand(1,100).tolist()
toto=np.array(range(0,100))
print 'len',len(toto)
print toto

#def plot_evolution_boxplot(case_plot,list_parameter,x_graduation,str_title,min_param,max_param):
	#case_plt : case[,] from f, case = plt.subplots()
	#list_parameter : which dataset we want to plot
	#x_graduation
#	case_plot.plot(range(0,len(x_graduation)),get_percentile(list_parameter,95),color='w',marker='+',markeredgecolor='k')
#	case_plot.plot(range(0,len(x_graduation)),get_percentile(list_parameter,5),color='w',marker='+',markeredgecolor='k')
#	case_plot.plot(range(0,len(x_graduation)),get_mean(list_parameter),color='w',marker='x',markeredgecolor='r')
#	medianprops = dict(linestyle='-', linewidth=1, color='blue',)
#	case_plot.boxplot(list_parameter,positions=range(0,len(x_graduation)),labels=x_graduation, showmeans=False,whis=[1, 99], sym='.',medianprops=medianprops)
#	case_plot.set_title(str_title)#,y=0.98)
#	case_plot.set_xticks(range(0,len(x_graduation)),x_graduation)
#	case_plot.set_ylim(min_param-1,max_param+1)

print range(0,len([1]))
print get_percentile(toto,95)
print np.nanpercentile(toto,95)

#plt.figure()
#f, case = plt.subplots(1,1, sharex='col', sharey='row',figsize=(5,7))
#plot_evolution_boxplot(case,toto,[1],'',0-0.1,1.1)
#case.plot(range(0,len([1])),get_percentile(toto,95),color='w',marker='+',markeredgecolor='k')
#case.boxplot(remove_nan(dataset_boxplot),positions=range(0,len(x_graduation)),labels=x_graduation, showmeans=False,whis=[1, 99], sym='.',medianprops=medianprops)

print range(0,len([1]))
print get_percentile(toto,95)

plt.show()

def plot_evolution_boxplot(case_plot,list_parameter,x_graduation,str_title,min_param,max_param,):
	#case_plt : case[,] from f, case = plt.subplots()
	#list_parameter : which dataset we want to plot
	#x_graduation
	#case_plot.plot(range(0,len(x_graduation)),get_percentile(list_parameter,95),color='w',marker='+',markeredgecolor='k')
	#case_plot.plot(range(0,len(x_graduation)),get_percentile(list_parameter,5),color='w',marker='+',markeredgecolor='k')
	#case_plot.plot(range(0,len(x_graduation)),get_mean(list_parameter),color='w',marker='x',markeredgecolor='r')
	medianprops = dict(linestyle='-', linewidth=1, color='blue')
	dataset_boxplot=list_parameter
	if(type(list_parameter)!=list) :dataset_boxplot= list_parameter.tolist()
	#print dataset_boxplot[~np.isnan(dataset_boxplot)]
	if(len(list_parameter)!=1) : case_plot.boxplot(remove_nan(dataset_boxplot),positions=range(0,len(x_graduation)),labels=x_graduation, showmeans=False,whis=[1, 99], sym='.',medianprops=medianprops)
	else :case_plot.boxplot(list_parameter,positions=range(0,len(x_graduation)),labels=x_graduation, showmeans=False,whis=[1, 99], sym='.',medianprops=medianprops)
	case_plot.set_title(str_title)#,y=0.98)
	case_plot.set_xticks(range(0,len(x_graduation)),x_graduation)
	case_plot.set_ylim(min_param-1,max_param+1)

#plt.figure()
#f, case = plt.subplots(1,1, sharex='col', sharey='row',figsize=(5,7))
#plot_evolution_boxplot(case,toto,[1],'',0-0.1,1.1)
#case.plot(range(0,len([1])),get_percentile(toto,95),color='w',marker='+',markeredgecolor='k')
#case.boxplot(remove_nan(dataset_boxplot),positions=range(0,len(x_graduation)),labels=x_graduation, showmeans=False,whis=[1, 99], sym='.',medianprops=medianprops)


plt.figure(figsize=(4,6))
medianprops = dict(linestyle='-', linewidth=1, color='blue')
plt.boxplot(range(0,100),whis=[1, 99], showmeans=False,sym='.',medianprops=medianprops)
plt.plot(1,np.percentile(toto,95),color='w',marker='+',markeredgecolor='k')
plt.plot(1,np.percentile(toto,5),color='w',marker='+',markeredgecolor='k')
plt.plot(1,np.mean(toto),color='w',marker='x',markeredgecolor='r',label='mean')
plt.plot(1,np.percentile(toto,50),color='w',marker='_',markeredgecolor='b',label='median')
plt.plot(1,99,color='w',marker='.',markeredgecolor='k',label='outlier')
plt.legend(loc='upper left')
plt.text(1.03,97,'  99th centile', fontsize='smaller')
plt.text(1.015,92,' 95th centile', fontsize='smaller')

plt.text(1.1,73,'  75th centile', fontsize='smaller')
plt.text(1.1,25,'  25th centile', fontsize='smaller')

plt.text(1.03,-1,'  1th centile', fontsize='smaller')
plt.text(1.015,4,' 5th centile', fontsize='smaller')
plt.yticks([])
if (save_plot=='yes') :plt.savefig(save_directory+'Boxplot.png')



plt.figure(figsize=(4,6))
str_color='r'
epaisseur_percentile=0.8
transparance=0.1
plt.plot([2,3],[np.percentile(toto,99),np.percentile(toto,99)],color=str_color,linestyle=':',linewidth=epaisseur_percentile,alpha=0.7)
plt.text(2.5,99,' 99th centile', fontsize='smaller')
plt.plot([2,3],[np.percentile(toto,95)]*2,color=str_color,linestyle='--',linewidth=epaisseur_percentile,alpha=0.7)
plt.text(2.5,95,' 95th centile', fontsize='smaller')
plt.plot([2,3],[np.percentile(toto,50)]*2,color=str_color,label='median',linewidth=1.5)
plt.text(2.5,50,' median', fontsize='smaller')
plt.plot([2,3],[np.percentile(toto,5)]*2,color=str_color,linestyle='--',linewidth=epaisseur_percentile,alpha=0.7)
plt.text(2.5,5,' 5th centile', fontsize='smaller')
plt.plot([2,3],[np.percentile(toto,1)]*2,color=str_color,linestyle=':',linewidth=epaisseur_percentile,alpha=0.7)
plt.text(2.5,1,' 1st centile', fontsize='smaller')
plt.fill_between([2,3], [np.percentile(toto,25)]*2,[np.percentile(toto,75)]*2,color=str_color,alpha=transparance)
plt.text(2.5,75,' 75th centile', fontsize='smaller')
plt.text(2.5,25,' 25th centile', fontsize='smaller')
plt.yticks([])
plt.xticks([])
if (save_plot=='yes') :plt.savefig(save_directory+'Boxplot_line.png')


	#case_plot.plot(range(0,len(x_graduation)),get_percentile(list_parameter,5),color='w',marker='+',markeredgecolor='k')
	#case_plot.plot(range(0,len(x_graduation)),get_mean(list_parameter),color='w',marker='x',markeredgecolor='r')

#f, case = plt.subplots(1,1, sharex='col', sharey='row',figsize=(5,7))
#plot_evolution_boxplot(case,toto,[1],'',0-0.1,1.1)
#case.plot(range(0,len([1])),get_percentile(toto,95),color='w',marker='+',markeredgecolor='k')
#case.boxplot(remove_nan(dataset_boxplot),positions=range(0,len(x_graduation)),labels=x_graduation, showmeans=False,whis=[1, 99], sym='.',medianprops=medianprops)


plt.show()

