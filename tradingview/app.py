from flask import Flask, request
from os import environ as env
# load env variables
from dotenv import load_dotenv
load_dotenv()
import redis
import json
# import config
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
# account = clientPaper.get_account()
# balances = account['balances']
# print(balances)

r = redis.from_url(env["REDIS_URL"])
r = redis.Redis(
    host=env['REDIS_HOST'],
    port=env['REDIS_PORT'], 
    password=env['REDIS_PASSWORD'])

r.set('foo', 'bar')
value = r.get('foo')
print(value)


def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print(f"sending over {order_type} - {side} {quantity} {symbol}")
        order = clientPaper.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        # order = clientReal.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        price = float(order['fills'][0]['price'])
        print( price)
        print(f"{order_type} - {side} {quantity} {symbol} at ${price}")
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False
    
    return True

@app.route('/')
def hello_world(): 
    value = r.get('foo')
    print(value)
    return value

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