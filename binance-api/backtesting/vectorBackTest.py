import numpy as np
import pandas as pd
from datetime import datetime

import vectorbt as vbt

# Prepare data
# start = '2019-01-01 UTC'  # crypto is in UTC
# end = '2020-01-01 UTC'
# btc_price = vbt.YFData.download('BTC-USD', start=start, end=end)
btc_price = vbt.YFData.download('BTC-USD')


# print(btc_price.get())

closing_prices = btc_price.get('Close')

# Moving Average Strategy
fast_ma = vbt.MA.run(closing_prices, 10, short_name='fast')
slow_ma = vbt.MA.run(closing_prices, 20, short_name='slow')

entries = fast_ma.ma_above(slow_ma, crossover=True)
exits = fast_ma.ma_below(slow_ma, crossover=True)

pf = vbt.Portfolio.from_signals(closing_prices, entries, exits)

print('MA 10,20 cross return:')
print(pf.total_return())
pf.plot().show()


# RSI Strategy
# rsi = vbt.RSI.run(closing_prices)
# entries = rsi.rsi_below(30, crossover=True)
# exits = rsi.rsi_above(70, crossover=True)

# portfolio = vbt.Portfolio.from_signals(closing_prices, entries, exits, init_cash=10000)
# print(portfolio.total_return())
# portfolio.plot().show()

