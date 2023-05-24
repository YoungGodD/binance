from function import *

data = {
    "volume": 10000.0,
    "number": 5,
    "amountDif": 50.0,
    "side": "SELL",
    "priceMin": 200.0,
    "priceMax": 300.0
}

orders = create_orders(data)
for order in orders:
    print(order)