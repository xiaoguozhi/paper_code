import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
from sklearn.neighbors import KernelDensity
from scipy.stats import norm
from scipy import stats
import os

os.chdir("D:/Rdata/Third_paper/third_paper_data/")

##################################################################
####南京 

dat_density=pd.read_csv('nanjing_quantile_25m.csv',index_col=[0])
dat_real_value=pd.read_excel('nanjing_total.xlsx',index_col=[0])

dat_density=dat_density.T
n_pre=dat_density.shape[1]
n_real_value=dat_real_value[(365-n_pre):365]


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

y_max=np.max([np.max(density1(x)),np.max(density2(x)),
                np.max(density3(x)),np.max(density4(x)),
                np.max(density5(x)),np.max(density6(x)),
                np.max(density7(x)),np.max(density8(x)),
                np.max(density9(x))])
                
                
                
ax[0,0].plot(x, density1(x),linewidth=3,label='Gaussian kernel')
ax[0,0].axvline(x=n_real_value.iloc[0,0],color='r',linewidth=3)
ax[0,0].set_ylim(0,y_max)
ax[0,0].set_title('2014-12-22')

ax[0,1].plot(x, density2(x),linewidth=3,label='Gaussian kernel')
ax[0,1].axvline(x=n_real_value.iloc[1,0],color='r',linewidth=3)
ax[0,1].set_ylim(0,y_max)
ax[0,1].set_title('2014-12-23')

ax[0,2].plot(x, density3(x),linewidth=3,label='Gaussian kernel')
ax[0,2].axvline(x=n_real_value.iloc[2,0],color='r',linewidth=3)
ax[0,2].set_ylim(0,y_max)
ax[0,2].set_title('2014-12-24')

ax[1,0].plot(x, density4(x),linewidth=3,label='Gaussian kernel')
ax[1,0].axvline(x=n_real_value.iloc[3,0],color='r',linewidth=3)
ax[1,0].set_ylim(0,y_max)
ax[1,0].set_title('2014-12-25')

ax[1,1].plot(x, density5(x),linewidth=3,label='Gaussian kernel')
ax[1,1].axvline(x=n_real_value.iloc[4,0],color='r',linewidth=3)
ax[1,1].set_ylim(0,y_max)
ax[1,1].set_title('2014-12-26')

ax[1,2].plot(x, density6(x),linewidth=3,label='Gaussian kernel')
ax[1,2].axvline(x=n_real_value.iloc[5,0],color='r',linewidth=3)
ax[1,2].set_ylim(0,y_max)
ax[1,2].set_title('2014-12-27')

ax[2,0].plot(x, density7(x),linewidth=3,label='Gaussian kernel')
ax[2,0].axvline(x=n_real_value.iloc[6,0],color='r',linewidth=3)
ax[2,0].set_ylim(0,y_max)
ax[2,0].set_title('2014-12-28')

ax[2,1].plot(x, density8(x),linewidth=3,label='Gaussian kernel')
ax[2,1].axvline(x=n_real_value.iloc[7,0],color='r',linewidth=3)
ax[2,1].set_ylim(0,y_max)
ax[2,1].set_title('2014-12-29')

ax[2,2].plot(x, density9(x),linewidth=3,label='Gaussian kernel')
ax[2,2].axvline(x=n_real_value.iloc[8,0],color='r',linewidth=3)
ax[2,2].set_ylim(0,y_max)
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
dat_real_value=pd.read_excel('suzhou_total.xlsx',index_col=[0])
dat_density=dat_density.T
n_pre=dat_density.shape[1]
n_real_value=dat_real_value[(365-n_pre):365]


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
ax[0,0].axvline(x=n_real_value.iloc[0,0],color='r',linewidth=3)
ax[0,0].set_title('2014-12-22')

ax[0,1].plot(x, density2(x),linewidth=3,label='Gaussian kernel')
ax[0,1].axvline(x=n_real_value.iloc[1,0],color='r',linewidth=3)
ax[0,1].set_title('2014-12-23')

ax[0,2].plot(x, density3(x),linewidth=3,label='Gaussian kernel')
ax[0,2].axvline(x=n_real_value.iloc[2,0],color='r',linewidth=3)
ax[0,2].set_title('2014-12-24')

ax[1,0].plot(x, density4(x),linewidth=3,label='Gaussian kernel')
ax[1,0].axvline(x=n_real_value.iloc[3,0],color='r',linewidth=3)
ax[1,0].set_title('2014-12-25')

ax[1,1].plot(x, density5(x),linewidth=3,label='Gaussian kernel')
ax[1,1].axvline(x=n_real_value.iloc[4,0],color='r',linewidth=3)
ax[1,1].set_title('2014-12-26')

ax[1,2].plot(x, density6(x),linewidth=3,label='Gaussian kernel')
ax[1,2].axvline(x=n_real_value.iloc[5,0],color='r',linewidth=3)
ax[1,2].set_title('2014-12-27')

ax[2,0].plot(x, density7(x),linewidth=3,label='Gaussian kernel')
ax[2,0].axvline(x=n_real_value.iloc[6,0],color='r',linewidth=3)
ax[2,0].set_title('2014-12-28')

ax[2,1].plot(x, density8(x),linewidth=3,label='Gaussian kernel')
ax[2,1].axvline(x=n_real_value.iloc[7,0],color='r',linewidth=3)
ax[2,1].set_title('2014-12-29')

ax[2,2].plot(x, density9(x),linewidth=3,label='Gaussian kernel')
ax[2,2].axvline(x=n_real_value.iloc[8,0],color='r',linewidth=3)
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
dat_real_value=pd.read_excel('lianyungang_total.xlsx',index_col=[0])
dat_density=dat_density.T
n_pre=dat_density.shape[1]
n_real_value=dat_real_value[(365-n_pre):365]


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
ax[0,0].axvline(x=n_real_value.iloc[0,0],color='r',linewidth=3)
ax[0,0].set_title('2014-12-22')

ax[0,1].plot(x, density2(x),linewidth=3,label='Gaussian kernel')
ax[0,1].axvline(x=n_real_value.iloc[1,0],color='r',linewidth=3)
ax[0,1].set_title('2014-12-23')

ax[0,2].plot(x, density3(x),linewidth=3,label='Gaussian kernel')
ax[0,2].axvline(x=n_real_value.iloc[2,0],color='r',linewidth=3)
ax[0,2].set_title('2014-12-24')

ax[1,0].plot(x, density4(x),linewidth=3,label='Gaussian kernel')
ax[1,0].axvline(x=n_real_value.iloc[3,0],color='r',linewidth=3)
ax[1,0].set_title('2014-12-25')

ax[1,1].plot(x, density5(x),linewidth=3,label='Gaussian kernel')
ax[1,1].axvline(x=n_real_value.iloc[4,0],color='r',linewidth=3)
ax[1,1].set_title('2014-12-26')

ax[1,2].plot(x, density6(x),linewidth=3,label='Gaussian kernel')
ax[1,2].axvline(x=n_real_value.iloc[5,0],color='r',linewidth=3)
ax[1,2].set_title('2014-12-27')

ax[2,0].plot(x, density7(x),linewidth=3,label='Gaussian kernel')
ax[2,0].axvline(x=n_real_value.iloc[6,0],color='r',linewidth=3)
ax[2,0].set_title('2014-12-28')

ax[2,1].plot(x, density8(x),linewidth=3,label='Gaussian kernel')
ax[2,1].axvline(x=n_real_value.iloc[7,0],color='r',linewidth=3)
ax[2,1].set_title('2014-12-29')

ax[2,2].plot(x, density9(x),linewidth=3,label='Gaussian kernel')
ax[2,2].axvline(x=n_real_value.iloc[8,0],color='r',linewidth=3)
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







