from tda.auth import easy_client
from tda.client import Client
from tda.streaming import StreamClient
import config

import asyncio
import json

client = easy_client(
        api_key=config.API_KEY,
        redirect_uri=config.REDIRECT_URL,
        token_path=config.TOKEN_PATH)
        
stream_client = StreamClient(client, account_id=config.ACCOUNT_ID)

def orderbook_handler(msg):
    print(json.dumps(msg, indent=4))

async def read_stream():
    await stream_client.login()
    await stream_client.quality_of_service(StreamClient.QOSLevel.EXPRESS)

    # Always add handlers before subscribing because many streams start sending
    # data immediately after success, and messages with no handlers are dropped.
    # stream_client.add_nasdaq_book_handler(
    #         lambda msg: print(json.dumps(msg, indent=4)))
    stream_client.add_nasdaq_book_handler(orderbook_handler)
    await stream_client.nasdaq_book_subs(['GOOG'])

    while True:
        await stream_client.handle_message()

asyncio.run(read_stream())