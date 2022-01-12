from flask import Flask, request
import os
import json
# import config
from binance.client import Client
# from binance.clientPaper import ClientPaper
from binance.enums import *


app = Flask(__name__)

clientPaper = Client(os.environ.get('API_KEY_PAPER'), os.environ.get('SECRET_KEY_PAPER'), tld='us')
# clientReal = Client(config.API_KEY, config.SECRET_KEY, tld='us')

# Check min quantity required to trade
# info clientReal.get_symbol_info('ETHUSDT')
# print(info['filters'][2]['minQty'])


def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print(f"sending over {order_type} - {side} {quantity} {symbol}")
        order = clientPaper.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        # order = clientReal.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False
    
    return True

@app.route('/')
def hello_world(): 
    return "Hi !"

@app.route('/webhook', methods=['POST'])
def webhook():
    # convert json to python dictionary    
    data = json.loads(request.data)

    if data["passphrase"] != config.WEBHOOK_PASSPHRASE:
        return {
            "code": "error",
            "message": "Invalid passphrase"
        }
    
    print(data['ticker'])
    print(data['bar'])

    # side = data['strategy']['order_action'].upper() # upper makes all caps


    order_response = order("BUY", .1, "ETHUSDT")
    print(order_response)

    return {
        "code": "success",
        "message": data
    }