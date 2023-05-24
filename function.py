import random
from binance.client import Client

api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
client = Client(api_key, api_secret)

def create_orders(data):
    volume = data['volume']
    number = data['number']
    amount_dif = data['amountDif']
    side = data['side']
    price_min = data['priceMin']
    price_max = data['priceMax']

    orders = []
    for _ in range(number):
        order_volume = volume / number
        order_price = random.uniform(price_min, price_max)
        order_volume += random.uniform(-amount_dif, amount_dif)
        order_volume = round(order_volume, 2)

        order = client.create_order(
            symbol='BTCUSDT',
            side=side,
            type='LIMIT',
            timeInForce='GTC',
            quantity=order_volume,
            price=order_price
        )
        orders.append(order)

    return orders