import config
import alpaca_trade_api as tradeapi
import psycopg2
import psycopg2.extras

# Connect to local DB
connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Alpaca API
api = tradeapi.REST(config.API_KEY, config.API_SECRET, base_url=config.API_URL)

# List alpaca stocks
assets = api.list_assets()

# Check if new stocks are out
cursor.execute("""
    SELECT symbol, name from stock
""")
rows = cursor.fetchall()
symbols = []
for row in rows:
    symbols.append(row['symbol'])
# print (symbols)
# symbols = [row['symbol'] for row in rows]
 
# If stock from query is not found in DB, add it
# ---------------------------------------------
# for asset in assets:
#     try:
#         if asset.symbol not in symbols and asset.status == 'active' and asset.tradable:
#             print(f"Inserting stock | {asset.symbol} | {asset.name} ")
#     except Exception as e:
#         print(e)
#     cursor.execute("""
#         INSERT INTO stock (name, symbol, exchange, is_etf) 
#         VALUES (%s, %s, %s, %s)
#     """, (asset.name, asset.symbol, asset.exchange, False))

# # Saves data insert, catch exceptions
# connection.commit()
# ----------------------------------------------

cursor.execute("SELECT * FROM stock")

stocks = cursor.fetchall()

for stock in stocks:
    print(stock['name'])