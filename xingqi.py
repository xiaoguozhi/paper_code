import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
from sklearn.neighbors import KernelDensity
from scipy.stats import norm
from scipy import stats
import os

os.chdir("D:/Rdata/Third_paper/third_paper_data/")

total_dat=pd.read_excel('nanjing_total_feature.xlsx',index_col=[0])


total_dat_1=total_dat['20140106':'20141228']
xingqi_data=total_dat_1[['E_demand','month']]
xingqi=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(111)
x=range(len(xingqi))
for i in range(1,51):
    ax1.plot(x,xingqi_data[7*i:7*i+7]['E_demand'].values,'r-',linewidth=3,color='m',alpha=0.5)


ax1.plot(x,xingqi_data[0:7]['E_demand'].values,'r-',linewidth=3,color='m',alpha=0.5,label="Electricity consumption")
ax1.axvline(x=0,color='black',linewidth=1,linestyle='dashed')
ax1.axvline(x=1,color='black',linewidth=1,linestyle='dashed')
ax1.axvline(x=2,color='black',linewidth=1,linestyle='dashed')
ax1.axvline(x=3,color='black',linewidth=1,linestyle='dashed')
ax1.axvline(x=4,color='black',linewidth=1,linestyle='dashed')
ax1.axvline(x=5,color='black',linewidth=1,linestyle='dashed')
ax1.axvline(x=6,color='black',linewidth=1,linestyle='dashed',label="Date")

ax1.set_ylim(8000,35000)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xticks(x, xingqi)
plt.margins(0.001)
plt.title("Electricity consumption from the weekly perspective")
plt.xlabel('Date(day)')
plt.ylabel('Electricity consumption(KWh)')
ax1.legend(loc="upper right")


