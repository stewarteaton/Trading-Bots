import backtrader as bt
import vectorbt as vbt
import pandas as pd
import datetime

cerebro = bt.Cerebro()

# Reads the CSV file and adds column headers to it. df in the variable name stands for dataframe
crypt_df = pd.read_csv(
    "./daily.csv",
    header=None,
    names=[
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "quote_asset_vol",
        "num_trades",
        "taker_buy_base_asset",
        "taker_buy_quote_asset",
        "ignore",
    ],
    parse_dates=True,
)

# Divides the timestamp column by 1000 or 1e3 (scientific notation)
convert = lambda x: datetime.datetime.fromtimestamp(x / 1e3)
crypt_df["timestamp"] = crypt_df["timestamp"].apply(convert)

# Sets the timestamp column as the index per row. So each date is the x value
crypt_df.set_index('timestamp', inplace=True)

print(crypt_df.head())

# Loads the data into backtrader via the pandas method .PandasDirectData()
data = bt.feeds.PandasDirectData(dataname=crypt_df)

cerebro.adddata(data)


cerebro.run()
cerebro.plot()

