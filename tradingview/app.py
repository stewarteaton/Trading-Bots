from flask import Flask, request, render_template
from os import environ as env
# load env variables
from dotenv import load_dotenv
load_dotenv()
import redis
import json
import datetime
from binance.client import Client
from binance.enums import *

app = Flask(__name__)

clientPaper = Client(env['API_KEY_PAPER'], env['SECRET_KEY_PAPER'], tld='us')
clientPaper.API_URL = 'https://testnet.binance.vision/api'
# clientReal = Client(env['API_KEY'], env['SECRET_KEY'], tld='us')

## Check min quantity required to trade
# info = clientPaper.get_symbol_info('ETHUSDT')
# print(info['filters'][2]['minQty'])
## Get Balances
account = clientPaper.get_account()
balances = account['balances']

## Heroku 
# r = redis.from_url(env["REDIS_URL"])
## Local 
r = redis.Redis(
    host=env['MY_REDIS_HOST'],
    port=env['MY_REDIS_PORT'], 
    password=env['MY_REDIS_PASSWORD'],
    decode_responses=True)

# r.set('foo', 'bar')
# value = r.get('foo')
# print(value)


def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print(f"sending over {order_type} - {side} {quantity} {symbol}")
        order = clientPaper.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        # order = clientReal.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        price = (order['fills'][0]['price'])
        date = str(datetime.datetime.now())
        record = f"{date}: {order_type} - {side} {quantity} {symbol} at {price}"
        r.set(date, record)
        print(record)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False
    
    return True

@app.route('/')
def hello_world(): 
    title = 'View Trading Bot Executions'
    balances = account['balances']
    txList = []
    for key in r.scan_iter():
       print(r.get(key))
       txList.append(r.get(key))
    return render_template('index.html', title=title, my_balances=balances, txs=txList)

@app.route('/webhook', methods=['POST'])
def webhook():
    # convert json to python dictionary    
    data = json.loads(request.data)

    if data["passphrase"] != env['WEBHOOK_PASSPHRASE']:
        return {
            "code": "error",
            "message": "Invalid passphrase"
        }
    
    print(data['ticker'])
    print(data['bar'])

    ticker = data['ticker']
    side = data['strategy']['order_action'].upper() # upper makes all caps
    quantity = data['strategy']['order_contracts']
    # Execute Order
    order_response = order(side, quantity, ticker)
    if order_response:
        print('Order Success')
        return {
            "code": "success",
            "message": "order executed"
        }
    else:
        print("order failed")

    print(order_response)