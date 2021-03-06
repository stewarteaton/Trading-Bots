import config
import csv
from binance.client import Client

client = Client(config.API_KEY, config.SECRET_KEY)

avg_price = client.get_avg_price(symbol='BNBBTC')

# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_30MINUTE)

# For SHORT DATA
# Open csv file
# hourlyCSV = open('hourly.csv', 'w', newline='')
# candlestick_writer = csv.writer(hourlyCSV, delimiter=',')

# for candleStick in candles:
#     print(candleStick)

#     candlestick_writer.writerow(candleStick)

# hourlyCSV.close()


# FOR 3 YEAR DATA
# klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 Jan, 2018", "23 Sept, 2021")
# # Open csv file
# yearlyCSV = open('2018-2021_30m.csv', 'w', newline='')
# candlestick_writer = csv.writer(yearlyCSV, delimiter=',')

# for candleStick in klines:
#     candlestick_writer.writerow(candleStick)

# yearlyCSV.close()

# For Daily
# Open csv file
dailyCSV = open('daily.csv', 'w', newline='')
dailyCandlestick_writer = csv.writer(dailyCSV, delimiter=',')
# Get data
dailyCandlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2021", "23 Sept, 2021")
for candlestick in dailyCandlesticks:
    candlestick[0] = candlestick[0] / 1000 #convert unix time to s
    dailyCandlestick_writer.writerow(candlestick)

dailyCSV.close()

# print(len(candles))