import tushare as ts
import matplotlib.pyplot as plt
import matplotlib

result = ts.get_hist_data('sh',start="2017-01-01")
# result = result.reindex(index = result.index[::-1])
result = result.iloc[::-1]
result2 = result[['close','ma5','ma10','ma20']]


result2.plot()
plt.show()