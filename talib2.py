#coding:utf-8

import talib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tushare as ts

df = ts.get_hist_data('sh',start='2017-01-01')
df[df['volume'] == 0] 
def myMACD(price, fastperiod=12, slowperiod=26, signalperiod=9):
    ewma12 = pd.ewma(price,span=fastperiod)
    ewma60 = pd.ewma(price,span=slowperiod)
    dif = ewma12-ewma60
    dea = pd.ewma(dif,span=signalperiod)
    bar = (dif-dea) #有些地方的bar = (dif-dea)*2，但是talib中MACD的计算是bar = (dif-dea)*1
    return dif,dea,bar

mydif,mydea,mybar = myMACD(df['close'].values, fastperiod=12, slowperiod=26, signalperiod=9)
fig = plt.figure(figsize=[18,3])

df.index = pd.to_datetime(df.index) # 注意空虚数据转换，不然出错!
plt.plot(df.index,mydif,label='my dif')
plt.plot(df.index,mydea,label='my dea')
plt.plot(df.index,mybar,label='my bar')
plt.legend(loc='best')
plt.show()
