#coding:utf-8

import talib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tushare as ts

# df = pd.read_csv("sh.csv",index_col="date")
df = ts.get_hist_data('sh',start='2014-01-01')
df[df['volume'] == 0] 

dif,dea,bar = talib.MACD(df['close'].values, fastperiod=12, slowperiod=26, signalperiod=9)
df.index = pd.to_datetime(df.index) # 注意数据转换，不然出错!

# fig = plt.figure(figsize=[18,3])
# plt.plot(df.index,dif,label='dif')
# plt.plot(df.index,dea,label='dea')
# plt.plot(df.index,bar,label='bar')
# plt.legend(loc='best')
# plt.show()

for x in range(len(df.index) - 1):
    deaItem = dea.tolist()[x]
    barItem = bar.tolist()[x]

    deaItemPlus = dea.tolist()[x+1]
    barItemPlus = bar.tolist()[x+1]
    #交叉信号
    if(deaItem < barItem) and (deaItemPlus >= barItemPlus):
        print(x)