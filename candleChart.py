#coding:utf-8
import sys
from PyQt5.QtCore import QDateTime,Qt
from PyQt5.QtGui import QColor,QPainter
from PyQt5.QtChart import QBarCategoryAxis,QCandlestickSeries,QChartView,QValueAxis,QCandlestickSet,QChart

from PyQt5.QtWidgets import QApplication,QMainWindow
app = QApplication(sys.argv)

acmeSeries = QCandlestickSeries()
acmeSeries.setName("Acme ltd")
acmeSeries.setIncreasingColor(QColor(Qt.green))
acmeSeries.setDecreasingColor(QColor(Qt.red))

f = open("acme_data.txt")
for line in f.readlines():
    if line.startswith('#'):
        pass
    else:
        timestamp,open,high,low,close = line.strip().split(' ')
        # print((timestamp,open,high,low,close))
        candlestickSet = QCandlestickSet(float(timestamp))
        candlestickSet.setOpen(float(open))
        candlestickSet.setHigh(float(high))
        candlestickSet.setLow(float(low))
        candlestickSet.setClose(float(close))
        acmeSeries.append(candlestickSet)

f.close()

chart1 = QChart()
chart1.addSeries(acmeSeries)
chart1.setTitle("acme Ltd Historical data (july 2015)")
chart1.setAnimationOptions(QChart.SeriesAnimations)
chart1.createDefaultAxes()

axisX = chart1.axes(Qt.Horizontal)[0]
axisY = chart1.axes(Qt.Vertical)[0]

chart1.legend().setVisible(True)
chart1.legend().setAlignment(Qt.AlignBottom)

view  = QChartView(chart1)
view.setRenderHint(QPainter.Antialiasing)



window = QMainWindow()
window.setCentralWidget(view)
window.resize(800,600)
window.show()


sys.exit(app.exec_())