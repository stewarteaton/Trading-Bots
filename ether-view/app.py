from flask import Flask, render_template, request, flash, redirect
import config, ccxt, time
from web3 import Web3
import ccxt


app = Flask(__name__)

# Web3 using Infura API 
w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))

def get_eth_price():
    # connect to binance api
    binance = ccxt.binance()
    ether_price = binance.fetch_ticker('ETH/USDC')    

    return ether_price

@app.route("/")
def index():

    eth = w3.eth
    ether_price = get_eth_price()

    latest_blocks = []
    for block_number in range(w3.eth.block_number, w3.eth.block_number-10, -1):
        block = w3.eth.get_block(block_number)
        latest_blocks.append(block)

    latest_transactions = []
    for tx in latest_blocks[-1]['transactions'][-10:]:
        transaction = w3.eth.get_transaction(tx)
        latest_transactions.append(transaction)

    current_time = time.time()

    return render_template('index.html', 
        eth = eth,
        ether_price=ether_price, 
        latest_blocks=latest_blocks, 
        latest_transactions=latest_transactions,
        current_time=current_time,
        miners = config.MINERS)

@app.route("/address")
def address():
    address = request.args.get('address')

    ether_price = get_eth_price()

    try:
        address = w3.toChecksumAddress(address)
    except:
        flash('Invalid address','danger')
        return redirect('/')

    balance = w3.eth.get_balance(address)
    balance = w3.fromWei(balance, 'ether')

    return render_template('address.html', ether_price=ether_price, balance=balance, address=address)

@app.route("/block/<blockNumber>")
def block(blockNumber):
    return render_template('transaction.html', blockNumber=blockNumber)

@app.route("/tx/<hash>")
def transaction(hash):
    transaction = w3.eth.get_transaction(hash)
    return render_template('transaction.html', hash=hash, transaction=transaction)