from kucoin.client import Client
# from kucoin.base_request.base_request import KucoinBaseRestApi
from kucoin.user import UserData
import requests
import json
import config

api_key = config.TEST_KEY
api_secret = config.TEST_SECRET
api_passphrase = config.TEST_PASSPHRASE

# client = Client(api_key, api_secret, api_passphrase)

# or connect to Sandbox
client = Client(api_key, api_secret, api_passphrase, sandbox=True)

# get currencies
currencies = client.get_currencies()
# for coin in currencies:
#     print(coin['currency'])

# response = KucoinBaseRestApi('GET', "/api/v1/accounts/20200326149205" )
# print(response)
response = requests.get("https://openapi-sandbox.kucoin.com/api/v1/accounts/20200326149205")
print(response)

# get market depth
depth = client.get_order_book('KCS-BTC')

# get symbol klines
klines = client.get_kline_data('KCS-BTC')

# get list of markets
markets = client.get_markets()

# place a market buy order
# order = client.create_market_order('NEO', Client.SIDE_BUY, size=20)

# get list of active orders
# orders = client.get_active_orders('KCS-BTC')