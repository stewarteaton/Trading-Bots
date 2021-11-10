import config
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))

print(w3.eth.block_number)

balance = w3.eth.get_balance('0x2f2b44d4A0e843DCe7AcA451C78788eADffE3A4d')

print(balance)

eth_balance = w3.fromWei(balance, 'ether')

print('Eth balance: ', eth_balance)

transaction = w3.eth.get_transaction('0xb797b53c86c29e9aca64ff40cc3c1b69f938694bf045e60363af16a1202024c9')

print(transaction)