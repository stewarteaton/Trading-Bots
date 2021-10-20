from flask import Flask, render_template, request, flash, redirect
import config
import csv
from binance.client import Client
from binance.enums import *


app = Flask(__name__)
# For sessions converty secret key to bytes
secrety_key_bytes = config.SESSION_KEY.encode('utf-8')
app.secret_key = secrety_key_bytes


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
    except Exception as e:
        flash(e, "error")

    return redirect('/')

@app.route("/sell")
def sell():
    return "<p>sell</p>"

@app.route("/settings")
def settings():
    return "<p>settings</p>"
