<h3>Binance Websocket</h2>
<h5>https://binance-docs.github.io/apidocs/spot/en/#websocket-market-streams</h5>
<ul><li>wss://stream.binance.com:9443</li></ul>

<h3>Python-Binance Wrapper</h3>
<ul><li>https://python-binance.readthedocs.io/en/latest/overview.html</li></ul>

<h3>Binance Paper Trading Testnet</h3>
<ul><li>https://testnet.binance.vision/</li></ul>
<ul><li>Had to clone binance.client.py package and create binance.clientPaper.py with test url to use</ul></li>

<h3>Python web-socket client</h5>
<ul><li>https://github.com/websocket-client/websocket-client</li></ul>

<h1>Backend</h1>
<hr>
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

</br>
<h1>Technical Analysis Libraries</h3>
<ul><li>TA-Lib: http://mrjbq7.github.io/ta-lib/</li></ul>
<ul><li>Pandas-TA: https://github.com/twopirllc/pandas-ta</li></ul>
<ul><li>TA: https://github.com/bukosabino/ta</li></ul>

</br>
<h1>Back Testing</h1>
<hr>
<h3>VectorBT</h3>
* https://vectorbt.dev/ - python library for TA and backtesting with speed

<h3>To save data stream set to file</h3>
<ul><li>wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m | tee dataset.text</ul></li>

<h3>Charting</h3>
<h4>Using light weight charts from trading view: https://github.com/tradingview/lightweight-charts</h4>
<ul><li>For dev, sometimes need to <b>Shift+Refresh</b> in chrome to reset browser code</li></ul>

</br>

<h3>Python write api data to csv for in sub for DB</h3>
<ul><li>https://docs.python.org/3/library/csv.html</li></ul>

<h3>To convert Unix timestamp from api data</h3>
<ul><li>https://www.unixtimestamp.com/</li></ul>












