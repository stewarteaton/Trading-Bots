<h2>Binance Websocket</h2>
<ul><li>wss://stream.binance.com:9443</li></ul>
<!-- Example trade stream btc/usdt -->
wss://stream.binance.com:9443/ws/btcusdt@trade
<!-- Example candlestick data -->
wss://stream.binance.com:9443/ws/btcusdt@kline_5m
<!-- Example output:  -->
{"e":"kline","E":1631636735735,"s":"BTCUSDT","k":{"t":1631636700000,"T":1631636999999,"s":"BTCUSDT","i":"5m","f":1054217725,"L":1054218306,"o":"46686.15000000","c":"46673.53000000","h":"46686.15000000","l":"46668.45000000","v":"12.26168000","n":582,"x":false,"q":"572337.21655380","V":"3.29093000","Q":"153606.31592330","B":"0"}}
<!-- To save data stream set to file -->
wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m | tee dataset.text
