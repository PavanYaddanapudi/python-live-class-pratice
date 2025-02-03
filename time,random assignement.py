import random
import time
def stock_price_manipulator(base,volatiliy,steps):
    price = base
    for _ in range(steps):
        change_percentage = random.uniform(-volatiliy , volatiliy)
        price *=(1+change_percentage)
        yield price
        time.sleep(1)
print(list(stock_price_manipulator(200,0.03,10)))
