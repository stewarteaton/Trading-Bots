import websocket, json, pprint, talib, numpy
from binance.clientPaper import ClientPaper
from binance.enums import *
import config

socket = config.SOCKET

SOCKET = 'wss://stream.binance.com:9443/ws/ethusdt@kline_1m'

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'ethusdt'
TRADE_QUANTITY = 0.001


closes = []
in_position = False

clientPaper = ClientPaper(config.API_KEY_PAPER, config.SECRET_KEY_PAPER, tld='us')

def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print("sending order")
        order = clientPaper.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return True

def on_open(ws):
    print('ws connection opened')
def on_close(ws):
    print('ws connection closed')
def on_message(ws, message):
    global closes, in_position
    
    # print('message received')
    json_message = json.loads(message)
    # pprint.pprint(json_message)

    # get candle data
    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)

        # make sure length number of closing prices is greater than RSI time period
        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("All rsi calculated")
            print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi is {}".format(last_rsi))

            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print("Sell!")
                    #Binance Sell Logic
                    order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position: False
                else:
                    print("Oversold, but already sold")

            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("Overbought, but already bought") 
                else:                
                    print("Buy!")
                    #Binance Buy Logic
                    order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position: False

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()