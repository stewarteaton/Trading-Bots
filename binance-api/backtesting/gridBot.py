import numpy as np
import pandas as pd
from datetime import datetime

import vectorbt as vbt

# Prepare data
start = '2020-01-01 UTC'  # crypto is in UTC
end = '2022-12-31 UTC'
btc_price = vbt.YFData.download('BTC-USD', start=start, end=end)

print(btc_price.get())

