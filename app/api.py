from binance import Client

api_key = '5Q8q62mUz4bT0x9Dgv2PxZGPVtU43QEPKAxLEGc1DTfm8yvpXWVG5sG2gGfpMsoy'
secret_key = '18MFgOKDuZj9KCyaWaXOFSxoyVEuuDIe8HLHwRQhX1LzZysdnSVYScq86bawJbmq'


async def get_crypto_price(crypto):
    client = Client(api_key, secret_key)

    ticker = client.get_symbol_ticker(symbol=f"{crypto}USDT")

    return ticker['price']