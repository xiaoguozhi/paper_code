
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker

import os

os.chdir("D:/Rdata/Third_paper/third_paper_data/")
dat_nanjing=pd.read_excel("nanjing_month_week.xlsx",index_col=[0])

month1=dat_nanjing['20140101':'20140131']['E_demand'].sum()
month2=dat_nanjing['20140201':'20140228']['E_demand'].sum()
month3=dat_nanjing['20140301':'20140331']['E_demand'].sum()
month4=dat_nanjing['20140401':'20140430']['E_demand'].sum()
month5=dat_nanjing['20140501':'20140531']['E_demand'].sum()
month6=dat_nanjing['20140601':'20140630']['E_demand'].sum()
month7=dat_nanjing['20140701':'20140731']['E_demand'].sum()
month8=dat_nanjing['20140801':'20140831']['E_demand'].sum()
month9=dat_nanjing['20140901':'20140930']['E_demand'].sum()
month10=dat_nanjing['20141001':'20141031']['E_demand'].sum()
month11=dat_nanjing['20141101':'20141130']['E_demand'].sum()
month12=dat_nanjing['20141201':'20141231']['E_demand'].sum()

y=[month1,month2,month3,month4,month5,month6,month7,month8,month9,month10,month11,month12]

N=len(y)

x=range(N)
#name_list = ('January', 'February', 'March', 'April', 
           # 'May','June','July','August','September',
            #'October','November','December')


name_list = ('Jan', 'Feb', 'Mar', 'Apr', 
            'May','Jun','Jul','Aug','Sep',
            'Oct','Nov','Dec')
            
pos_list = np.arange(len(name_list))
ax = plt.axes()
ax.xaxis.set_major_locator(ticker.FixedLocator((pos_list)))
ax.xaxis.set_major_formatter(ticker.FixedFormatter((name_list)))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.bar(x,y,width=0.7,align='center',color='darkorange',edgecolor='darkorange')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel('Month')
plt.ylabel('Electricity consumption(KWh)')
#plt.xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5])
plt.title('Monthly electricity consumption in Nanjing')
plt.bar







