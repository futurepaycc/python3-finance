import ccxt

huobi  = ccxt.huobi({
    'apiKey': '509c8efe-f199de4e-a77913de-d516f',
    'secret': 'c814f815-a9b1cc19-b3317b61-a78ac'
})

result = huobi.load_markets()
print(result)

result = huobi.fetch_balance()
print(result)

result = huobi.fetch_ohlcv("BTC/CNY")
print(result)