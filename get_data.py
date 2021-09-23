import config
import csv
from binance.client import Client

client = Client(config.API_KEY, config.SECRET_KEY)

avg_price = client.get_avg_price(symbol='BNBBTC')

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_30MINUTE)

# Open csv file
csvfile = open('2018-2021_30m.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=' ')


# for candleStick in candles:
#     print(candleStick)

#     candlestick_writer.writerow(candleStick)

klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 Jan, 2018", "23 Sept, 2021")
for candleStick in klines:
    candlestick_writer.writerow(candleStick)

csvfile.close()

# print(len(candles))