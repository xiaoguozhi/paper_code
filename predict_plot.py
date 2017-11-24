import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
from sklearn.neighbors import KernelDensity
from scipy.stats import norm
from scipy import stats
import os

os.chdir("D:/Rdata/Third_paper/third_paper_data/")

pre_dat=pd.read_excel('nanjing_pre.xlsx',index_col=[0])

pre_dat_1=pre_dat[356:365]
#pre_dat_1=pre_dat
#pre_dat_1.plot(kind='line',ylim=(10000,30000),)


fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(111)
#plt.figure(figsize=(10,5))
ax1.plot(pre_dat_1['E_demand'],label='True value',linewidth=3)
ax1.plot(pre_dat_1['DL'],label='Deep learning',linewidth=2,linestyle='dashed',marker='o')
ax1.plot(pre_dat_1['GBM'],label='Gradient boosting',linewidth=2,linestyle='dashed',marker='d')
ax1.plot(pre_dat_1['RF'],label='Random forest',linewidth=2,linestyle='dashed',marker='p')
ax1.set_ylim(10000,30000)
plt.xlabel('Date(day)')
plt.ylabel('Electricity consumption(KWh)')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=1))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
#plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
ax1.legend(loc='upper left')




############################################################
#####plot for  predict
fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(111)
#plt.figure(figsize=(10,5))
ax1.plot(pre_dat_1['E_demand'],label='True value',linewidth=3)
ax1.plot(pre_dat_1['DL'],label='Deep learning',linewidth=2,linestyle='dashed')
ax1.plot(pre_dat_1['GBM'],label='Gradient boosting',linewidth=2,linestyle='dashed')
ax1.plot(pre_dat_1['RF'],label='Random forest',linewidth=2,linestyle='dashed')
ax1.axvline(pre_dat_1.index[335],color='r',linewidth=3)
ax1.set_ylim(5000,40000)
plt.xlabel('Date(day)')
plt.ylabel('Electricity consumption(KWh)')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=16))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
ax1.legend(loc='upper left')



################################################################
#######plot for real value for Lianyungang

real_dat=pd.read_excel('lianyungang_total.xlsx',index_col=[0])

fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(111)
#plt.figure(figsize=(10,5))
ax1.plot(real_dat['value'],label='True value',linewidth=3)
ax1.set_ylim(5000,40000)
plt.xlabel('Date(day)')
plt.ylabel('Electricity consumption(KWh)')
plt.title('Electricity consumption in Lianyungang in 2014')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=16))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
ax1.legend(loc='upper left')


################################################################
#######plot for real value for Suzhou

real_dat=pd.read_excel('suzhou_total.xlsx',index_col=[0])

fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(111)
#plt.figure(figsize=(10,5))
ax1.plot(real_dat['value'],label='True value',linewidth=3)
ax1.set_ylim(5000,40000)
plt.xlabel('Date(day)')
plt.ylabel('Electricity consumption(KWh)')
plt.title('Electricity consumption in Suzhou in 2014')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=16))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
ax1.legend(loc='upper left')

################################################################
#######plot for real value for Nanjing

real_dat=pd.read_excel('nanjing_total.xlsx',index_col=[0])

fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(111)
#plt.figure(figsize=(10,5))
ax1.plot(real_dat['value'],label='True value',linewidth=3)
ax1.set_ylim(5000,40000)
plt.xlabel('Date(day)')
plt.ylabel('Electricity consumption(KWh)')
plt.title('Electricity consumption in Nanjing in 2014')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=16))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
ax1.legend(loc='upper left')




###########################################################################
#############wendu and power demand in Nanjing

total_dat=pd.read_excel('nanjing_total_feature.xlsx',index_col=[0])
total_dat['average_person']=total_dat['E_demand']/3000

total_dat1=total_dat['20140601':'20140831']

fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(111)

ax1.plot(total_dat1['average_person'],label='Electricity consumption',linewidth=3)
ax1.plot(total_dat1['wdh_var1(t)'],label='Temperature',linewidth=3,color='m')
ax1.axvline(x=total_dat1.index[64],color='black',linewidth=1,linestyle='dashed',label='Local high temperature')
ax1.axvline(x=total_dat1.index[39],color='black',linewidth=1,linestyle='dashed')
ax1.axvline(x=total_dat1.index[50],color='black',linewidth=1,linestyle='dashed')
ax1.axvline(x=total_dat1.index[59],color='black',linewidth=1,linestyle='dashed')

ax1.set_ylim(0,60)
plt.xlabel('Date(day)')
plt.ylabel('Electricity consumption(KWh) and temperature')
plt.title('Electricity consumption and temperature in Nanjing')
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=4))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
ax1.legend(loc='upper left')


###########################################################################
#############wendu and power demand in Suzhou

total_dat=pd.read_excel('suzhou_total_feature.xlsx',index_col=[0])
total_dat['average_person']=total_dat['E_demand']/3000

total_dat1=total_dat['20140601':'20140831']

fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(111)

ax1.plot(total_dat1['average_person'],label='Electricity consumption',linewidth=3)
ax1.plot(total_dat1['wdh_var1(t)'],label='Temperature',linewidth=3,color='m')
ax1.axvline(x=total_dat1.index[64],color='black',linewidth=1,linestyle='dashed',label='Local high temperature')
ax1.axvline(x=total_dat1.index[39],color='black',linewidth=1,linestyle='dashed')
ax1.axvline(x=total_dat1.index[49],color='black',linewidth=1,linestyle='dashed')
ax1.axvline(x=total_dat1.index[59],color='black',linewidth=1,linestyle='dashed')
ax1.axvline(x=total_dat1.index[84],color='black',linewidth=1,linestyle='dashed')


ax1.set_ylim(0,60)
plt.xlabel('Date(day)')
plt.ylabel('Electricity consumption(KWh) and temperature')
plt.title('Electricity consumption and temperature in Suzhou')
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=4))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
ax1.legend(loc='upper left')



###########################################################################
#############wendu and power demand in Lianyungang

total_dat=pd.read_excel('lianyungang_total_feature.xlsx',index_col=[0])
total_dat['average_person']=total_dat['E_demand']/3000

total_dat1=total_dat['20140601':'20140831']

fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(111)

ax1.plot(total_dat1['average_person'],label='Electricity consumption',linewidth=3)
ax1.plot(total_dat1['wdh_var1(t)'],label='Temperature',linewidth=3,color='m')
ax1.axvline(x=total_dat1.index[64],color='black',linewidth=1,linestyle='dashed',label='Local high temperature')
ax1.axvline(x=total_dat1.index[29],color='black',linewidth=1,linestyle='dashed')
ax1.axvline(x=total_dat1.index[50],color='black',linewidth=1,linestyle='dashed')
ax1.axvline(x=total_dat1.index[82],color='black',linewidth=1,linestyle='dashed')


ax1.set_ylim(0,60)
plt.xlabel('Date(day)')
plt.ylabel('Electricity consumption(KWh) and temperature')
plt.title('Electricity consumption and temperature in Lianyungang')
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=4))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
ax1.legend(loc='upper left')













##################################################################
####南京 

dat_density=pd.read_csv('nanjing_quantile_m.csv',index_col=[0])

dat_density=dat_density.T

density1 = stats.kde.gaussian_kde(dat_density.iloc[:,0].values)
density2 = stats.kde.gaussian_kde(dat_density.iloc[:,1].values)
density3 = stats.kde.gaussian_kde(dat_density.iloc[:,2].values)
density4 = stats.kde.gaussian_kde(dat_density.iloc[:,3].values)
density5 = stats.kde.gaussian_kde(dat_density.iloc[:,4].values)
density6 = stats.kde.gaussian_kde(dat_density.iloc[:,5].values)
density7 = stats.kde.gaussian_kde(dat_density.iloc[:,6].values)
density8 = stats.kde.gaussian_kde(dat_density.iloc[:,7].values)
density9 = stats.kde.gaussian_kde(dat_density.iloc[:,8].values)

fig, ax = plt.subplots(nrows=3, ncols=3)
fig.set_size_inches(20,15)

x=np.linspace(10000, 30000, 99)

ax[0,0].plot(x, density1(x),linewidth=3,label='Gaussian kernel')
ax[0,0].axvline(x=18404,color='r',linewidth=3)
ax[0,0].set_title('2014-12-22')

ax[0,1].plot(x, density2(x),linewidth=3,label='Gaussian kernel')
ax[0,1].axvline(x=18188,color='r',linewidth=3)
ax[0,1].set_title('2014-12-23')

ax[0,2].plot(x, density3(x),linewidth=3,label='Gaussian kernel')
ax[0,2].axvline(x=17003,color='r',linewidth=3)
ax[0,2].set_title('2014-12-24')

ax[1,0].plot(x, density4(x),linewidth=3,label='Gaussian kernel')
ax[1,0].axvline(x=17997,color='r',linewidth=3)
ax[1,0].set_title('2014-12-25')

ax[1,1].plot(x, density5(x),linewidth=3,label='Gaussian kernel')
ax[1,1].axvline(x=17714,color='r',linewidth=3)
ax[1,1].set_title('2014-12-26')

ax[1,2].plot(x, density6(x),linewidth=3,label='Gaussian kernel')
ax[1,2].axvline(x=18576,color='r',linewidth=3)
ax[1,2].set_title('2014-12-27')

ax[2,0].plot(x, density7(x),linewidth=3,label='Gaussian kernel')
ax[2,0].axvline(x=18963,color='r',linewidth=3)
ax[2,0].set_title('2014-12-28')

ax[2,1].plot(x, density8(x),linewidth=3,label='Gaussian kernel')
ax[2,1].axvline(x=16182,color='r',linewidth=3)
ax[2,1].set_title('2014-12-29')

ax[2,2].plot(x, density9(x),linewidth=3,label='Gaussian kernel')
ax[2,2].axvline(x=15920,color='r',linewidth=3)
ax[2,2].set_title('2014-12-30')

ax[0,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[0,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[0,2].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[1,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[1,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[1,2].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[2,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[2,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[2,2].ticklabel_format(style='sci', axis='y', scilimits=(0,0))

ax[0,0].set_xlabel('Electricity consumption(KWh)')
ax[0,0].set_ylabel('Probability density')
ax[0,0].legend(loc='upper right')

ax[0,1].set_xlabel('Electricity consumption(KWh)')
ax[0,1].set_ylabel('Probability density')
ax[0,1].legend(loc='upper right')

ax[0,2].set_xlabel('Electricity consumption(KWh)')
ax[0,2].set_ylabel('Probability density')
ax[0,2].legend(loc='upper right')

ax[1,0].set_xlabel('Electricity consumption(KWh)')
ax[1,0].set_ylabel('Probability density')
ax[1,0].legend(loc='upper right')

ax[1,1].set_xlabel('Electricity consumption(KWh)')
ax[1,1].set_ylabel('Probability density')
ax[1,1].legend(loc='upper right')

ax[1,2].set_xlabel('Electricity consumption(KWh)')
ax[1,2].set_ylabel('Probability density')
ax[1,2].legend(loc='upper right')

ax[2,0].set_xlabel('Electricity consumption(KWh)')
ax[2,0].set_ylabel('Probability density')
ax[2,0].legend(loc='upper right')

ax[2,1].set_xlabel('Electricity consumption(KWh)')
ax[2,1].set_ylabel('Probability density')
ax[2,1].legend(loc='upper right')

ax[2,2].set_xlabel('Electricity consumption(KWh)')
ax[2,2].set_ylabel('Probability density')
ax[2,2].legend(loc='upper right')

################################################################################
##############苏州##########################
dat_density=pd.read_csv('suzhou_quantile_m.csv',index_col=[0])

dat_density=dat_density.T

density1 = stats.kde.gaussian_kde(dat_density.iloc[:,0].values)
density2 = stats.kde.gaussian_kde(dat_density.iloc[:,1].values)
density3 = stats.kde.gaussian_kde(dat_density.iloc[:,2].values)
density4 = stats.kde.gaussian_kde(dat_density.iloc[:,3].values)
density5 = stats.kde.gaussian_kde(dat_density.iloc[:,4].values)
density6 = stats.kde.gaussian_kde(dat_density.iloc[:,5].values)
density7 = stats.kde.gaussian_kde(dat_density.iloc[:,6].values)
density8 = stats.kde.gaussian_kde(dat_density.iloc[:,7].values)
density9 = stats.kde.gaussian_kde(dat_density.iloc[:,8].values)

fig, ax = plt.subplots(nrows=3, ncols=3)
fig.set_size_inches(20,15)

x=np.linspace(10000, 30000, 99)

ax[0,0].plot(x, density1(x),linewidth=3,label='Gaussian kernel')
ax[0,0].axvline(x=20071,color='r',linewidth=3)
ax[0,0].set_title('2014-12-22')

ax[0,1].plot(x, density2(x),linewidth=3,label='Gaussian kernel')
ax[0,1].axvline(x=19069,color='r',linewidth=3)
ax[0,1].set_title('2014-12-23')

ax[0,2].plot(x, density3(x),linewidth=3,label='Gaussian kernel')
ax[0,2].axvline(x=18218,color='r',linewidth=3)
ax[0,2].set_title('2014-12-24')

ax[1,0].plot(x, density4(x),linewidth=3,label='Gaussian kernel')
ax[1,0].axvline(x=18874,color='r',linewidth=3)
ax[1,0].set_title('2014-12-25')

ax[1,1].plot(x, density5(x),linewidth=3,label='Gaussian kernel')
ax[1,1].axvline(x=18487,color='r',linewidth=3)
ax[1,1].set_title('2014-12-26')

ax[1,2].plot(x, density6(x),linewidth=3,label='Gaussian kernel')
ax[1,2].axvline(x=19158,color='r',linewidth=3)
ax[1,2].set_title('2014-12-27')

ax[2,0].plot(x, density7(x),linewidth=3,label='Gaussian kernel')
ax[2,0].axvline(x=20061,color='r',linewidth=3)
ax[2,0].set_title('2014-12-28')

ax[2,1].plot(x, density8(x),linewidth=3,label='Gaussian kernel')
ax[2,1].axvline(x=17648,color='r',linewidth=3)
ax[2,1].set_title('2014-12-29')

ax[2,2].plot(x, density9(x),linewidth=3,label='Gaussian kernel')
ax[2,2].axvline(x=17474,color='r',linewidth=3)
ax[2,2].set_title('2014-12-30')

ax[0,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[0,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[0,2].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[1,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[1,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[1,2].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[2,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[2,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[2,2].ticklabel_format(style='sci', axis='y', scilimits=(0,0))

ax[0,0].set_xlabel('Electricity consumption(KWh)')
ax[0,0].set_ylabel('Probability density')
ax[0,0].legend(loc='upper right')

ax[0,1].set_xlabel('Electricity consumption(KWh)')
ax[0,1].set_ylabel('Probability density')
ax[0,1].legend(loc='upper right')

ax[0,2].set_xlabel('Electricity consumption(KWh)')
ax[0,2].set_ylabel('Probability density')
ax[0,2].legend(loc='upper right')

ax[1,0].set_xlabel('Electricity consumption(KWh)')
ax[1,0].set_ylabel('Probability density')
ax[1,0].legend(loc='upper right')

ax[1,1].set_xlabel('Electricity consumption(KWh)')
ax[1,1].set_ylabel('Probability density')
ax[1,1].legend(loc='upper right')

ax[1,2].set_xlabel('Electricity consumption(KWh)')
ax[1,2].set_ylabel('Probability density')
ax[1,2].legend(loc='upper right')

ax[2,0].set_xlabel('Electricity consumption(KWh)')
ax[2,0].set_ylabel('Probability density')
ax[2,0].legend(loc='upper right')

ax[2,1].set_xlabel('Electricity consumption(KWh)')
ax[2,1].set_ylabel('Probability density')
ax[2,1].legend(loc='upper right')

ax[2,2].set_xlabel('Electricity consumption(KWh)')
ax[2,2].set_ylabel('Probability density')
ax[2,2].legend(loc='upper right')



################################################################################
##############连云港##########################
dat_density=pd.read_csv('lianyungang_quantile_m.csv',index_col=[0])

dat_density=dat_density.T

density1 = stats.kde.gaussian_kde(dat_density.iloc[:,0].values)
density2 = stats.kde.gaussian_kde(dat_density.iloc[:,1].values)
density3 = stats.kde.gaussian_kde(dat_density.iloc[:,2].values)
density4 = stats.kde.gaussian_kde(dat_density.iloc[:,3].values)
density5 = stats.kde.gaussian_kde(dat_density.iloc[:,4].values)
density6 = stats.kde.gaussian_kde(dat_density.iloc[:,5].values)
density7 = stats.kde.gaussian_kde(dat_density.iloc[:,6].values)
density8 = stats.kde.gaussian_kde(dat_density.iloc[:,7].values)
density9 = stats.kde.gaussian_kde(dat_density.iloc[:,8].values)

fig, ax = plt.subplots(nrows=3, ncols=3)
fig.set_size_inches(20,15)

x=np.linspace(10000, 30000, 99)

ax[0,0].plot(x, density1(x),linewidth=3,label='Gaussian kernel')
ax[0,0].axvline(x=15172,color='r',linewidth=3)
ax[0,0].set_title('2014-12-22')

ax[0,1].plot(x, density2(x),linewidth=3,label='Gaussian kernel')
ax[0,1].axvline(x=14331,color='r',linewidth=3)
ax[0,1].set_title('2014-12-23')

ax[0,2].plot(x, density3(x),linewidth=3,label='Gaussian kernel')
ax[0,2].axvline(x=13838,color='r',linewidth=3)
ax[0,2].set_title('2014-12-24')

ax[1,0].plot(x, density4(x),linewidth=3,label='Gaussian kernel')
ax[1,0].axvline(x=14283,color='r',linewidth=3)
ax[1,0].set_title('2014-12-25')

ax[1,1].plot(x, density5(x),linewidth=3,label='Gaussian kernel')
ax[1,1].axvline(x=14585,color='r',linewidth=3)
ax[1,1].set_title('2014-12-26')

ax[1,2].plot(x, density6(x),linewidth=3,label='Gaussian kernel')
ax[1,2].axvline(x=14723,color='r',linewidth=3)
ax[1,2].set_title('2014-12-27')

ax[2,0].plot(x, density7(x),linewidth=3,label='Gaussian kernel')
ax[2,0].axvline(x=14979,color='r',linewidth=3)
ax[2,0].set_title('2014-12-28')

ax[2,1].plot(x, density8(x),linewidth=3,label='Gaussian kernel')
ax[2,1].axvline(x=13440,color='r',linewidth=3)
ax[2,1].set_title('2014-12-29')

ax[2,2].plot(x, density9(x),linewidth=3,label='Gaussian kernel')
ax[2,2].axvline(x=13224,color='r',linewidth=3)
ax[2,2].set_title('2014-12-30')

ax[0,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[0,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[0,2].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[1,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[1,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[1,2].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[2,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[2,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[2,2].ticklabel_format(style='sci', axis='y', scilimits=(0,0))

ax[0,0].set_xlabel('Electricity consumption(KWh)')
ax[0,0].set_ylabel('Probability density')
ax[0,0].legend(loc='upper right')

ax[0,1].set_xlabel('Electricity consumption(KWh)')
ax[0,1].set_ylabel('Probability density')
ax[0,1].legend(loc='upper right')

ax[0,2].set_xlabel('Electricity consumption(KWh)')
ax[0,2].set_ylabel('Probability density')
ax[0,2].legend(loc='upper right')

ax[1,0].set_xlabel('Electricity consumption(KWh)')
ax[1,0].set_ylabel('Probability density')
ax[1,0].legend(loc='upper right')

ax[1,1].set_xlabel('Electricity consumption(KWh)')
ax[1,1].set_ylabel('Probability density')
ax[1,1].legend(loc='upper right')

ax[1,2].set_xlabel('Electricity consumption(KWh)')
ax[1,2].set_ylabel('Probability density')
ax[1,2].legend(loc='upper right')

ax[2,0].set_xlabel('Electricity consumption(KWh)')
ax[2,0].set_ylabel('Probability density')
ax[2,0].legend(loc='upper right')

ax[2,1].set_xlabel('Electricity consumption(KWh)')
ax[2,1].set_ylabel('Probability density')
ax[2,1].legend(loc='upper right')

ax[2,2].set_xlabel('Electricity consumption(KWh)')
ax[2,2].set_ylabel('Probability density')
ax[2,2].legend(loc='upper right')







