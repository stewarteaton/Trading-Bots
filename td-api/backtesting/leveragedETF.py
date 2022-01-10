import numpy as np
import pandas as pd
from datetime import datetime

import vectorbt as vbt

# start = '201-01-01 UTC'  
# end = '2020-01-01 UTC'
# btc_price = vbt.YFData.download('BTC-USD', start=start, end=end)
tqqq_price = vbt.YFData.download('TQQQ')

print(tqqq_price.get())