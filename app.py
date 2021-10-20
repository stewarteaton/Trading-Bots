from flask import Flask, render_template, request, flash, redirect, jsonify
from flask_cors import CORS
import config
import csv
from binance.client import Client
from binance.enums import *


app = Flask(__name__)
CORS(app)
# For sessions converty secret key to bytes
# secrety_key_bytes = config.SESSION_KEY.encode('utf-8')
app.secret_key = b'alvvjlkjweoiru43lkv'


client = Client(config.API_KEY, config.SECRET_KEY, tld='us')

@app.route("/")
def index():
    title='Asset View'

    account = client.get_account()
    balances = account['balances']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    # print(balances)
    return render_template('index.html', title=title, my_balances=balances, symbols=symbols)

@app.route("/buy", methods=["POST"])
def buy():
    print(request.form)
    try: 
        order = client.create_order(
            symbol=request.form['symbol'],
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=request.form['quantity'],
            )
        flash("successful buy")
    except Exception as e:
        flash(e.message, "error")

    return redirect('/')

@app.route("/sell")
def sell():
    return "<p>sell</p>"

@app.route("/settings")
def settings():
    return "<p>settings</p>"

@app.route("/history")
def history():
    candleSticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "4 Oct, 2021", "21 Oct, 2021")

    processed_candlesticks = []

    for data in candleSticks:
        # create dictionary
        candlestick = {
            # divide by 1000 to convert from ms to s
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4]
        } 

        processed_candlesticks.append(candlestick)

    # return jsonify(candleSticks)
    return jsonify(processed_candlesticks)

