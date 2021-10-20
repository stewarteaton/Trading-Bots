import numpy
import talib
# read csv into numpy array
from numpy import genfromtxt

my_data = genfromtxt('30minCandle.csv', delimiter=',')
# print(my_data)

# get closing prices for candles from 4th column 
close = my_data[:,4]


# print(close)

# # creates random array
# close = numpy.random.random(100)

# output = talib.SMA(close, timeperiod=10)

rsi = talib.RSI(close, timeperiod=14)
print(rsi)