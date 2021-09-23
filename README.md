<h3>Binance Websocket</h2>
<ul><li>wss://stream.binance.com:9443</li></ul>

<h3>Example trade stream btc/usdt</h3>
<ul><li>wss://stream.binance.com:9443/ws/btcusdt@trade</li></ul>

<h3>Example candlestick data</h3>
<ul><li>wss://stream.binance.com:9443/ws/btcusdt@kline_5m

<h3>Example output: </h3>
<ul><li>{"e":"kline","E":1631636735735,"s":"BTCUSDT","k":{"t":1631636700000,"T":1631636999999,"s":"BTCUSDT","i":"5m","f":1054217725,"L":1054218306,"o":"46686.15000000","c":"46673.53000000","h":"46686.15000000","l":"46668.45000000","v":"12.26168000","n":582,"x":false,"q":"572337.21655380","V":"3.29093000","Q":"153606.31592330","B":"0"}}</ul></li>

<h3>To save data stream set to file</h3>
<ul><li>wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m | tee dataset.text</ul></li>

<h3>Charting</h3>
<h4>Using light weight charts from trading view: https://github.com/tradingview/lightweight-charts</h4>

<h3>API</h3>
<ul><li>https://python-binance.readthedocs.io/en/latest/</li></ul>

<h3>Python write api data to csv for in sub for DB</h3>
<ul><li>https://docs.python.org/3/library/csv.html</li></ul>

<h3>To convert Unix timestamp from api data</h3>
<ul><li>https://www.unixtimestamp.com/</li></ul>

<h3>Technical Analysis Libraries</h3>
<ul><li>TA-Lib: http://mrjbq7.github.io/ta-lib/</li></ul>
