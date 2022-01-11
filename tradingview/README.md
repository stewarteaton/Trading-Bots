<h1>Automated Trading Bots</h1>
</br>

<h3>Trading View</h3>
Website where you can apply code to stock/crypto charts in order to perform technical analysis.
Alerts can be configured and sent when programmatic conditions are met.
</br>

<h3>Web Hooks</h3>
Using the alerts from trading view, we can feed the notifications(ex. buy/sell orders) to an API which triggers buys and sells on a crypto/stock exchage.. Hence ("Trading Bots")
</br>

<h3>Benefit of Trading View</h3>
Instead of having to host a server that's constantly pulling stock/crypto chart data for assets on everytime frame and having to constantly run to check if indicators are met, Trading View provides this funtionality for nearly free. There is a huge open source community on Trading View to discuess and share strategy and scripts. Trading Views backtesting function is extremely useful as well. 
</br>

<h1>Heroku: Hosting the App</h1>
To push "tradingview" repo subtree of Trading Bots repo to Heroku: 
    - git subtree push --prefix=tradingview heroku master

Procfile set up  