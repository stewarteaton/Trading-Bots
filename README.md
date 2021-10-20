<h3>Binance Websocket</h2>
<h5>https://binance-docs.github.io/apidocs/spot/en/#websocket-market-streams</h5>
<ul><li>wss://stream.binance.com:9443</li></ul>

<h3>Example trade stream btc/usdt</h3>
<ul><li>wss://stream.binance.com:9443/ws/btcusdt@trade</li></ul>

<h3>Example candlestick data</h3>
<ul><li>wss://stream.binance.com:9443/ws/btcusdt@kline_5m</li></ul>

<h3>get_klines response format: </h3>
<ul><li>[
    [
        1499040000000,      # Open time
        "0.01634790",       # Open
        "0.80000000",       # High
        "0.01575800",       # Low
        "0.01577100",       # Close
        "148976.11427815",  # Volume
        1499644799999,      # Close time
        "2434.19055334",    # Quote asset volume
        308,                # Number of trades
        "1756.87402397",    # Taker buy base asset volume
        "28.46694368",      # Taker buy quote asset volume
        "17928899.62484339" # Can be ignored
    ]
]</ul></li>

<h3>To save data stream set to file</h3>
<ul><li>wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m | tee dataset.text</ul></li>

<h3>Charting</h3>
<h4>Using light weight charts from trading view: https://github.com/tradingview/lightweight-charts</h4>
<ul><li>For dev, sometimes need to <b>Shift+Refresh</b> in chrome to reset browser code</li></ul>

<h3>API</h3>
<ul><li>https://python-binance.readthedocs.io/en/latest/</li></ul>

<h3>Python write api data to csv for in sub for DB</h3>
<ul><li>https://docs.python.org/3/library/csv.html</li></ul>

<h3>To convert Unix timestamp from api data</h3>
<ul><li>https://www.unixtimestamp.com/</li></ul>

<h3>Technical Analysis Libraries</h3>
<ul><li>TA-Lib: http://mrjbq7.github.io/ta-lib/</li></ul>


---- BACKEND ----
<h3>Flask</h3>
* https://flask.palletsprojects.com/en/2.0.x/quickstart/#
    Export environment variable in Terminal
        > set FLASK_APP=app
    Run Flask
        > flask run

* Debug Mode - automatically reload on changes
    > set FLASK_ENV=development
    > export FLASK_DEBUG=1


<h3>Jinja HTML Templating</h3>
* https://jinja.palletsprojects.com/en/3.0.x/templates/




